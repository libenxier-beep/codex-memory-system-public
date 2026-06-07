#!/usr/bin/env python3
"""Lightweight lint for domain work_context mini wikis."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


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

FRONTMATTER_REQUIRED = [
    "id",
    "title",
    "summary",
    "scope",
    "applies_to",
    "type",
    "stability",
    "status",
    "last_reviewed",
    "retrieval_keys",
]

CARD_REQUIRED = [
    "claim:",
    "mechanism:",
    "use_when:",
    "do_not_use_when:",
    "retrieval_keys:",
    "source_refs:",
    "confidence:",
    "last_reviewed:",
]

DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def extract_frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return text[4:end]


def lint_required_files(root: Path, errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            fail(errors, f"missing required file: {rel}")


def lint_frontmatter(root: Path, errors: list[str]) -> None:
    for md in sorted(root.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        frontmatter = extract_frontmatter(text)
        if frontmatter is None:
            fail(errors, f"{md.name}: missing YAML frontmatter")
            continue
        for field in FRONTMATTER_REQUIRED:
            if not re.search(rf"^{re.escape(field)}\s*:", frontmatter, re.MULTILINE):
                fail(errors, f"{md.name}: frontmatter missing {field}")
        if "retrieval_keys:" in frontmatter and not re.search(
            r"retrieval_keys:\s*\n\s+-\s+\S+", frontmatter
        ):
            fail(errors, f"{md.name}: retrieval_keys must include at least one item")
        if "last_reviewed:" in frontmatter and not DATE_RE.search(frontmatter):
            fail(errors, f"{md.name}: last_reviewed should use YYYY-MM-DD")


def lint_manifest(root: Path, errors: list[str]) -> None:
    manifest = root / "sources" / "manifest.jsonl"
    if not manifest.exists():
        return
    for idx, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            fail(errors, f"sources/manifest.jsonl:{idx}: invalid JSON: {exc.msg}")
            continue
        for field in ["id", "type", "title", "url_or_path", "accessed_at", "quality", "summary", "derived_pages"]:
            if field not in item:
                fail(errors, f"sources/manifest.jsonl:{idx}: missing {field}")
        if item.get("quality") not in {"high", "medium", "low", "reject"}:
            fail(errors, f"sources/manifest.jsonl:{idx}: quality must be high, medium, low, or reject")
        if "accessed_at" in item and not DATE_RE.fullmatch(str(item["accessed_at"])):
            fail(errors, f"sources/manifest.jsonl:{idx}: accessed_at should use YYYY-MM-DD")


def lint_knowledge_cards(root: Path, errors: list[str]) -> None:
    target_pages = [
        "principles.md",
        "patterns.md",
        "architecture.md",
        "micro_tactics.md",
        "casebook.md",
    ]
    found_any = False
    for rel in target_pages:
        path = root / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "claim:" in text:
            found_any = True
            for required in CARD_REQUIRED:
                if required not in text:
                    fail(errors, f"{rel}: knowledge card content includes claim but misses {required}")
    if not found_any:
        fail(errors, "no knowledge card detected in principles, patterns, architecture, micro_tactics, or casebook")


def lint_links(root: Path, errors: list[str]) -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for md in sorted(root.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        for match in link_re.finditer(text):
            target = match.group(1)
            if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                continue
            target_path = (md.parent / target.split("#", 1)[0]).resolve()
            if target_path.suffix and not target_path.exists():
                fail(errors, f"{md.name}: broken relative link {target}")


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
        lint_manifest(root, errors)
        lint_knowledge_cards(root, errors)
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
