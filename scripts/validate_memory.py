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
    parser = argparse.ArgumentParser(description="Validate layered memory markdown files")
    parser.add_argument("--root", default="examples/sanitized-memory", help="memory root path")
    parser.add_argument("--policy", default="checks/policy.json", help="policy json")
    args = parser.parse_args()

    root = Path(args.root)
    policy = json.loads(Path(args.policy).read_text(encoding="utf-8"))
    required = set(policy["required_frontmatter_fields"])
    allowed_scopes = set(policy["allowed_scopes"])
    secret_patterns = [re.compile(p) for p in policy["secret_patterns"]]

    errors = []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")

        # global hygiene checks
        if has_hidden_control_chars(text):
            errors.append(f"{rel}: contains hidden control characters")
        for pat in secret_patterns:
            if pat.search(text):
                errors.append(f"{rel}: possible secret matched pattern {pat.pattern}")

        # only validate durable entry frontmatter for non-README files in key layers
        if path.name.lower() == "readme.md":
            continue
        if rel.parts[0] not in {"core", "platform", "learnings", "short_term", "memory-sidecar"}:
            continue

        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue

        missing = sorted(required - fm)
        if missing:
            errors.append(f"{rel}: missing required keys: {', '.join(missing)}")

        # scope value check (lightweight regex parse)
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
