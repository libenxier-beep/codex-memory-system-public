#!/usr/bin/env python3
"""Lint domain work_context mini wikis.

This intentionally stays dependency-free. It implements the JSON Schema subset
used by this skill's schemas, plus cross-file checks that schemas cannot cover.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_FILES = [
    "README.md",
    "index.md",
    "AGENT.md",
    "principles.md",
    "patterns.md",
    "architecture.md",
    "micro_tactics.md",
    "casebook.md",
    "retrieval.md",
    "open_questions.md",
    "log.md",
    "sources/manifest.jsonl",
]

CARD_PAGES = [
    "principles.md",
    "patterns.md",
    "architecture.md",
    "micro_tactics.md",
    "casebook.md",
]

LIST_FIELDS = {"use_when", "do_not_use_when", "retrieval_keys", "source_refs", "derived_pages"}
DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def skill_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_schema(name: str) -> dict[str, Any]:
    path = skill_root() / "schemas" / name
    return json.loads(path.read_text(encoding="utf-8"))


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def extract_frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return text[4:end]


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the small YAML subset used in domain page frontmatter."""
    data: dict[str, Any] = {}
    current_key: str | None = None
    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        list_match = re.match(r"^\s+-\s+(.*)$", raw_line)
        if list_match and current_key:
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(clean_scalar(list_match.group(1)))
            continue
        key_match = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", raw_line)
        if not key_match:
            continue
        key, value = key_match.group(1), key_match.group(2).strip()
        if value:
            data[key] = clean_scalar(value)
            current_key = None
        else:
            data[key] = []
            current_key = key
    return data


def validate_schema(value: Any, schema: dict[str, Any], where: str, errors: list[str]) -> None:
    schema_type = schema.get("type")
    if schema_type == "object":
        if not isinstance(value, dict):
            fail(errors, f"{where}: expected object")
            return
        for required in schema.get("required", []):
            if required not in value:
                fail(errors, f"{where}: missing {required}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    fail(errors, f"{where}.{key}: unexpected property")
        for key, subschema in properties.items():
            if key in value:
                validate_schema(value[key], subschema, f"{where}.{key}", errors)
        return

    if schema_type == "array":
        if not isinstance(value, list):
            fail(errors, f"{where}: expected array")
            return
        if len(value) < schema.get("minItems", 0):
            fail(errors, f"{where}: expected at least {schema['minItems']} item(s)")
        item_schema = schema.get("items")
        if item_schema:
            for idx, item in enumerate(value):
                validate_schema(item, item_schema, f"{where}[{idx}]", errors)
        return

    if schema_type == "string":
        if not isinstance(value, str):
            fail(errors, f"{where}: expected string")
            return
        if len(value) < schema.get("minLength", 0):
            fail(errors, f"{where}: expected at least {schema['minLength']} character(s)")
        if "enum" in schema and value not in schema["enum"]:
            fail(errors, f"{where}: {value!r} not in {schema['enum']}")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            fail(errors, f"{where}: {value!r} does not match {schema['pattern']}")


def lint_required_files(root: Path, errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            fail(errors, f"missing required file: {rel}")


def lint_frontmatter(root: Path, errors: list[str]) -> dict[str, str]:
    schema = load_schema("domain-page-frontmatter.schema.json")
    seen_ids: dict[str, str] = {}
    for md in sorted(root.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        frontmatter = extract_frontmatter(text)
        rel = md.relative_to(root).as_posix()
        if frontmatter is None:
            fail(errors, f"{rel}: missing YAML frontmatter")
            continue
        item = parse_simple_yaml(frontmatter)
        validate_schema(item, schema, f"{rel}:frontmatter", errors)
        page_id = item.get("id")
        if isinstance(page_id, str):
            if page_id in seen_ids:
                fail(errors, f"{rel}: duplicate frontmatter id {page_id!r}; first seen in {seen_ids[page_id]}")
            seen_ids[page_id] = rel
        if item.get("retrieval_keys") == []:
            fail(errors, f"{rel}: retrieval_keys must include at least one item")
        if "last_reviewed" in item and not DATE_RE.fullmatch(str(item["last_reviewed"])):
            fail(errors, f"{rel}: last_reviewed should use YYYY-MM-DD")
    return seen_ids


def lint_manifest(root: Path, errors: list[str]) -> set[str]:
    schema = load_schema("source-manifest.schema.json")
    manifest = root / "sources" / "manifest.jsonl"
    source_ids: set[str] = set()
    if not manifest.exists():
        return source_ids
    for idx, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        where = f"sources/manifest.jsonl:{idx}"
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            fail(errors, f"{where}: invalid JSON: {exc.msg}")
            continue
        validate_schema(item, schema, where, errors)
        source_id = item.get("id")
        if isinstance(source_id, str):
            if source_id in source_ids:
                fail(errors, f"{where}: duplicate source id {source_id!r}")
            source_ids.add(source_id)
        for page in item.get("derived_pages", []):
            if not isinstance(page, str):
                continue
            if "://" in page or page.startswith("#"):
                continue
            if not (root / page).exists():
                fail(errors, f"{where}: derived page does not exist: {page}")
    return source_ids


def parse_knowledge_cards(text: str) -> list[dict[str, Any]]:
    lines = text.splitlines()
    cards: list[dict[str, Any]] = []
    i = 0
    while i < len(lines):
        if not re.match(r"^-\s+claim\s*:", lines[i]):
            i += 1
            continue
        card: dict[str, Any] = {}
        current_key: str | None = None
        while i < len(lines):
            line = lines[i]
            if line.startswith("## ") or line.startswith("### "):
                break
            field_match = re.match(r"^-\s+([A-Za-z_]+)\s*:\s*(.*)$", line)
            if field_match:
                key, value = field_match.group(1), field_match.group(2).strip()
                if key in LIST_FIELDS:
                    card[key] = [clean_scalar(value)] if value else []
                else:
                    card[key] = clean_scalar(value)
                current_key = key
                i += 1
                continue
            item_match = re.match(r"^\s+-\s+(.*)$", line)
            if item_match and current_key:
                if not isinstance(card.get(current_key), list):
                    card[current_key] = []
                card[current_key].append(clean_scalar(item_match.group(1)))
            i += 1
        cards.append(card)
    return cards


def collect_source_refs(text: str) -> list[str]:
    refs: list[str] = []
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if not re.match(r"^-\s+source_refs\s*:\s*$", line):
            continue
        cursor = idx + 1
        while cursor < len(lines):
            item_match = re.match(r"^\s+-\s+(.*)$", lines[cursor])
            if not item_match:
                break
            refs.append(clean_scalar(item_match.group(1)))
            cursor += 1
    return refs


def lint_knowledge_cards(root: Path, source_ids: set[str], errors: list[str]) -> None:
    schema = load_schema("knowledge-card.schema.json")
    found_any = False
    for rel in CARD_PAGES:
        path = root / rel
        if not path.exists():
            continue
        for idx, card in enumerate(parse_knowledge_cards(path.read_text(encoding="utf-8")), start=1):
            found_any = True
            validate_schema(card, schema, f"{rel}:card[{idx}]", errors)
            for source_ref in card.get("source_refs", []):
                if source_ref not in source_ids:
                    fail(errors, f"{rel}:card[{idx}]: source_ref not found in manifest: {source_ref}")
    if not found_any:
        fail(errors, "no knowledge card detected in principles, patterns, architecture, micro_tactics, or casebook")


def lint_source_refs(root: Path, source_ids: set[str], errors: list[str]) -> None:
    for md in sorted(root.rglob("*.md")):
        rel = md.relative_to(root).as_posix()
        for source_ref in collect_source_refs(md.read_text(encoding="utf-8")):
            if source_ref not in source_ids:
                fail(errors, f"{rel}: source_ref not found in manifest: {source_ref}")


def lint_links(root: Path, errors: list[str]) -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for md in sorted(root.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        rel = md.relative_to(root).as_posix()
        for match in link_re.finditer(text):
            target = match.group(1)
            if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                continue
            target_path = (md.parent / target.split("#", 1)[0]).resolve()
            if target_path.suffix and not target_path.exists():
                fail(errors, f"{rel}: broken relative link {target}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint a domain work_context mini wiki.")
    parser.add_argument("path", help="Path to work_contexts/<domain_slug>")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    errors: list[str] = []

    if not root.exists():
        fail(errors, f"path does not exist: {root}")
    elif not root.is_dir():
        fail(errors, f"path is not a directory: {root}")
    else:
        lint_required_files(root, errors)
        lint_frontmatter(root, errors)
        source_ids = lint_manifest(root, errors)
        lint_knowledge_cards(root, source_ids, errors)
        lint_source_refs(root, source_ids, errors)
        lint_links(root, errors)

    if errors:
        print("domain context lint failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"domain context lint passed: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
