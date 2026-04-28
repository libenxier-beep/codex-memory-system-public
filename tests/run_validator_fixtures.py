#!/usr/bin/env python3
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURES_ROOT = REPO_ROOT / "tests" / "fixtures"
VALID_ROOT = FIXTURES_ROOT / "valid"
VALIDATOR = REPO_ROOT / "scripts" / "validate_memory.py"
POLICY = REPO_ROOT / "checks" / "policy.json"


def iter_cases():
    for path in sorted(FIXTURES_ROOT.iterdir()):
        if path.is_dir():
            yield path


def overlay_tree(src: Path, dst: Path):
    for path in sorted(src.rglob("*")):
        rel = path.relative_to(src)
        if rel.name == "expect.json":
            continue
        target = dst / rel
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def run_case(case_dir: Path):
    expectation = json.loads((case_dir / "expect.json").read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix=f"{case_dir.name}-") as tmpdir:
        root = Path(tmpdir) / "root"
        shutil.copytree(VALID_ROOT, root)
        if case_dir.name != "valid":
            overlay_tree(case_dir, root)

        result = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                "--root",
                str(root),
                "--policy",
                str(POLICY),
            ],
            capture_output=True,
            text=True,
        )

    ok = result.returncode == expectation["exit_code"]
    missing = [
        needle
        for needle in expectation.get("contains", [])
        if needle not in result.stdout and needle not in result.stderr
    ]
    if not ok or missing:
        print(f"CASE FAILED: {case_dir.name}")
        print(result.stdout)
        print(result.stderr)
        if not ok:
            print(
                f"Expected exit code {expectation['exit_code']}, got {result.returncode}"
            )
        if missing:
            print("Missing expected substrings:")
            for needle in missing:
                print("-", needle)
        return False

    print(f"CASE PASSED: {case_dir.name}")
    return True


def main() -> int:
    all_ok = True
    for case_dir in iter_cases():
        all_ok = run_case(case_dir) and all_ok
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
