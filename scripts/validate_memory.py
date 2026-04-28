#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    block = text[4:end].strip().splitlines()
    keys = []
    for line in block:
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" in line and not line.startswith(" "):
            keys.append(line.split(":", 1)[0].strip())
    return set(keys)


def has_hidden_control_chars(text: str) -> bool:
    for ch in text:
        code = ord(ch)
        if code in (9, 10, 13):
            continue
        if code < 32:
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate layered memory target root")
    parser.add_argument("--root", default="examples/sanitized-memory", help="target root path")
    parser.add_argument("--policy", default="checks/policy.json", help="policy json")
    args = parser.parse_args()

    root = Path(args.root)
    policy = json.loads(Path(args.policy).read_text(encoding="utf-8"))
    required = set(policy["required_frontmatter_fields"])
    allowed_layers = set(policy["allowed_layers"])
    allowed_scopes = set(policy["allowed_scopes"])
    secret_patterns = [re.compile(p) for p in policy["secret_patterns"]]

    errors = []
    expected_dirs = [
        "memories/core",
        "memories/platform",
        "memories/learnings",
        "memories/rollout_summaries",
        "memory-sidecar/evidence",
        "memory-sidecar/sessions",
        "memory-sidecar/indexes",
        "memory-sidecar/policies",
    ]
    for rel in expected_dirs:
        if not (root / rel).exists():
            errors.append(f"missing expected directory: {rel}")

    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")

        # global hygiene checks
        if has_hidden_control_chars(text):
            errors.append(f"{rel}: contains hidden control characters")
        for pat in secret_patterns:
            if pat.search(text):
                errors.append(f"{rel}: possible secret matched pattern {pat.pattern}")

        # only validate durable entry frontmatter for non-README files in work-memory durable layers
        if path.name.lower() == "readme.md":
            continue
        if len(rel.parts) < 3:
            continue
        if rel.parts[0] != "memories":
            continue
        if rel.parts[1] not in {"core", "platform", "learnings"}:
            continue

        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue

        missing = sorted(required - fm)
        if missing:
            errors.append(f"{rel}: missing required keys: {', '.join(missing)}")

        # layer value check
        m = re.search(r"^layer:\s*([^\n]+)$", text, flags=re.MULTILINE)
        if not m:
            errors.append(f"{rel}: missing layer value")
        else:
            layer = m.group(1).strip()
            if layer not in allowed_layers:
                errors.append(f"{rel}: invalid layer '{layer}'")
            if layer != rel.parts[1]:
                errors.append(f"{rel}: layer '{layer}' does not match directory '{rel.parts[1]}'")

        # scope value check
        m = re.search(r"^scope:\s*([^\n]+)$", text, flags=re.MULTILINE)
        if not m:
            errors.append(f"{rel}: missing scope value")
        else:
            scope = m.group(1).strip()
            if scope not in allowed_scopes:
                errors.append(f"{rel}: invalid scope '{scope}'")

    if errors:
        print("VALIDATION FAILED")
        for e in errors:
            print("-", e)
        return 1

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
