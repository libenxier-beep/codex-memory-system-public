#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml


FRONTMATTER_DELIM = "---\n"


def extract_frontmatter(text: str):
    if not text.startswith(FRONTMATTER_DELIM):
        return None
    end = text.find(f"\n{FRONTMATTER_DELIM}", len(FRONTMATTER_DELIM))
    if end == -1:
        return None
    return text[len(FRONTMATTER_DELIM):end]


def parse_frontmatter(text: str):
    block = extract_frontmatter(text)
    if block is None:
        return None, "missing"
    try:
        data = yaml.safe_load(block) or {}
    except (yaml.YAMLError, ValueError) as exc:
        return None, f"invalid YAML frontmatter ({exc.__class__.__name__})"
    if not isinstance(data, dict):
        return None, "frontmatter must be a YAML mapping"
    return data, None


def expect_str(data: dict, key: str):
    value = data.get(key)
    if value is None:
        return None, f"missing {key} value"
    if not isinstance(value, str):
        return None, f"{key} must be a string"
    return value.strip(), None


def expect_date_string(data: dict, key: str):
    value = data.get(key)
    if value is None:
        return None, f"missing {key} value"
    if isinstance(value, dt.date):
        return value.isoformat(), None
    if not isinstance(value, str):
        return None, f"{key} must be an ISO date string"
    return value.strip(), None


def expect_string_list(data: dict, key: str):
    value = data.get(key)
    if value is None:
        return None, f"missing {key} value"
    if not isinstance(value, list):
        return None, f"{key} must be a list"
    bad = [item for item in value if not isinstance(item, str)]
    if bad:
        return None, f"{key} must contain strings only"
    return [item.strip() for item in value], None


def is_valid_iso_date(value: str) -> bool:
    try:
        dt.date.fromisoformat(value)
        return True
    except ValueError:
        return False


def validate_memory_index(root: Path, errors: list[str]):
    index_path = root / "memories" / "memory_index.md"
    if not index_path.exists():
        errors.append("missing expected file: memories/memory_index.md")
        return

    lines = index_path.read_text(encoding="utf-8").splitlines()
    bullet_re = re.compile(r"^-\s+`?([^`]+?)`?\s*$")
    for lineno, line in enumerate(lines, start=1):
        m = bullet_re.match(line.strip())
        if not m:
            continue
        rel = m.group(1)
        if not rel or rel.endswith(":"):
            continue
        target = root / "memories" / rel
        if not target.exists():
            errors.append(
                f"memories/memory_index.md:{lineno}: referenced target missing: {rel}"
            )


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
    allowed_statuses = set(policy["allowed_statuses"])
    secret_patterns = [re.compile(p) for p in policy["secret_patterns"]]
    field_schemas = {
        "id": "string",
        "title": "string",
        "summary": "string",
        "layer": "string",
        "scope": "string",
        "applies_to": "string",
        "type": "string",
        "stability": "string",
        "source": "list",
        "evidence": "list",
        "regression_risk": "string",
        "supersedes": "list",
        "owner": "string",
        "status": "string",
    }

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

    validate_memory_index(root, errors)

    seen_ids = {}
    durable_entries = []

    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")

        # global hygiene checks
        if has_hidden_control_chars(text):
            errors.append(f"{rel}: contains hidden control characters")
        for pat in secret_patterns:
            if pat.search(text):
                errors.append(f"{rel}: possible secret matched pattern {pat.pattern}")

        fm, fm_error = parse_frontmatter(text)
        if fm is not None:
            item_id = fm.get("id")
            if item_id:
                if item_id in seen_ids:
                    errors.append(
                        f"{rel}: duplicate id '{item_id}' already used by {seen_ids[item_id]}"
                    )
                else:
                    seen_ids[item_id] = str(rel)

        # only validate durable entry frontmatter for non-README files in work-memory durable layers
        if path.name.lower() == "readme.md":
            continue
        if len(rel.parts) < 3:
            continue
        if rel.parts[0] != "memories":
            continue
        if rel.parts[1] not in {"core", "platform", "learnings"}:
            continue

        if fm is None:
            if fm_error == "missing":
                errors.append(f"{rel}: missing YAML frontmatter")
            else:
                errors.append(f"{rel}: {fm_error}")
            continue

        missing = sorted(required - set(fm.keys()))
        if missing:
            errors.append(f"{rel}: missing required keys: {', '.join(missing)}")

        for field, expected in field_schemas.items():
            if field not in fm:
                continue
            value = fm[field]
            if expected == "string" and not isinstance(value, str):
                errors.append(f"{rel}: {field} must be a string")
            if expected == "list" and not isinstance(value, list):
                errors.append(f"{rel}: {field} must be a list")

        layer, err = expect_str(fm, "layer")
        if err:
            errors.append(f"{rel}: {err}")
            layer = None
        elif layer not in allowed_layers:
            errors.append(f"{rel}: invalid layer '{layer}'")
        elif layer != rel.parts[1]:
            errors.append(f"{rel}: layer '{layer}' does not match directory '{rel.parts[1]}'")

        scope, err = expect_str(fm, "scope")
        if err:
            errors.append(f"{rel}: {err}")
        elif scope not in allowed_scopes:
            errors.append(f"{rel}: invalid scope '{scope}'")

        status, err = expect_str(fm, "status")
        if err:
            errors.append(f"{rel}: {err}")
        elif status not in allowed_statuses:
            errors.append(f"{rel}: invalid status '{status}'")

        last_reviewed, err = expect_date_string(fm, "last_reviewed")
        if err:
            errors.append(f"{rel}: {err}")
        elif not is_valid_iso_date(last_reviewed):
            errors.append(f"{rel}: invalid last_reviewed '{last_reviewed}'")

        supersedes, err = expect_string_list(fm, "supersedes")
        if err:
            errors.append(f"{rel}: {err}")
            supersedes = []
        item_id = fm.get("id")
        if item_id and item_id in supersedes:
            errors.append(f"{rel}: supersedes cannot reference self id '{item_id}'")
        durable_entries.append((rel, supersedes))

    for rel, supersedes in durable_entries:
        for target_id in supersedes:
            if target_id not in seen_ids:
                errors.append(f"{rel}: supersedes missing id '{target_id}'")

    if errors:
        print("VALIDATION FAILED")
        for e in errors:
            print("-", e)
        return 1

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
