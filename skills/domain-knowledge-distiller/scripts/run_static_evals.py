#!/usr/bin/env python3
"""Run deterministic checks for domain-knowledge-distiller.

This is not a model-grading harness. It validates the skill's static eval assets:
prompt scenarios are well-formed and every fixture context passes the linter.
"""

from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path


REQUIRED_PROMPT_FIELDS = {"id", "should_trigger", "prompt", "expected_evidence"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def skill_root() -> Path:
    return Path(__file__).resolve().parent.parent


def validate_prompts(errors: list[str]) -> None:
    prompts = skill_root() / "evals" / "prompts.csv"
    with prompts.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fields = set(reader.fieldnames or [])
        missing = REQUIRED_PROMPT_FIELDS - fields
        if missing:
            fail(errors, f"evals/prompts.csv: missing columns {sorted(missing)}")
            return
        seen: set[str] = set()
        for row_num, row in enumerate(reader, start=2):
            scenario_id = (row.get("id") or "").strip()
            if not scenario_id:
                fail(errors, f"evals/prompts.csv:{row_num}: missing id")
            elif scenario_id in seen:
                fail(errors, f"evals/prompts.csv:{row_num}: duplicate id {scenario_id!r}")
            seen.add(scenario_id)
            if (row.get("should_trigger") or "").strip().lower() not in {"true", "false"}:
                fail(errors, f"evals/prompts.csv:{row_num}: should_trigger must be true or false")
            for field in ["prompt", "expected_evidence"]:
                if not (row.get(field) or "").strip():
                    fail(errors, f"evals/prompts.csv:{row_num}: missing {field}")


def validate_fixtures(errors: list[str]) -> None:
    fixtures_dir = skill_root() / "evals" / "fixtures"
    if not fixtures_dir.exists():
        fail(errors, "evals/fixtures: missing directory")
        return
    linter = skill_root() / "scripts" / "lint_domain_context.py"
    fixture_roots = sorted(path for path in fixtures_dir.iterdir() if (path / "README.md").exists())
    if not fixture_roots:
        fail(errors, "evals/fixtures: no fixture contexts with README.md")
        return
    for fixture in fixture_roots:
        result = subprocess.run(
            [sys.executable, str(linter), str(fixture)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if result.returncode != 0:
            fail(errors, f"{fixture.relative_to(skill_root())}: lint failed\n{result.stdout}")


def main() -> int:
    errors: list[str] = []
    validate_prompts(errors)
    validate_fixtures(errors)
    if errors:
        print("static evals failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("static evals passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
