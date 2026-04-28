# 08 Quickstart (15 Minutes)

## Goal

Get a runnable memory mechanism quickly: bootstrap + validate + CI.

## Prerequisites

- bash
- python3
- git

## Step 1: Bootstrap a layered memory root

```bash
bash scripts/bootstrap.sh /tmp/agent-memory
```

Expected result:

- `/tmp/agent-memory/memories/core`
- `/tmp/agent-memory/memories/platform`
- `/tmp/agent-memory/memories/learnings`
- `/tmp/agent-memory/memories/rollout_summaries`
- `/tmp/agent-memory/memory-sidecar/evidence`
- `/tmp/agent-memory/memory-sidecar/sessions`
- `/tmp/agent-memory/memory-sidecar/indexes`

## Step 2: Validate bundled examples

```bash
python3 scripts/validate_memory.py --root examples/sanitized-memory --policy checks/policy.json
```

Expected output: `VALIDATION PASSED`

You can also validate the scaffold you just generated:

```bash
python3 scripts/validate_memory.py --root /tmp/agent-memory --policy checks/policy.json
```

Expected result:

- durable files under `memories/core`, `memories/platform`, and `memories/learnings` pass frontmatter checks
- directory layout under `memories/` and `memory-sidecar/` matches the target-root contract
- index targets, durable `id` uniqueness, durable `status`, `last_reviewed`, and `supersedes` all pass validator checks

## Step 3: Run validator regression fixtures

```bash
python3 tests/run_validator_fixtures.py
```

Expected result:

- the `valid` fixture passes
- negative fixtures fail for the intended reason only
- CI can catch validator regressions before a policy change lands

## Step 4: Wire into your own repo

1. Copy `scripts/bootstrap.sh`, `scripts/validate_memory.py`, and `checks/policy.json`.
2. Add your own memory root path.
3. Add the GitHub workflow from `.github/workflows/validate-memory.yml`.

## Step 5: First practical usage

- Create one durable rule in `memories/core/` with frontmatter
- Add one runtime session note in `memory-sidecar/sessions/`
- For a real project, keep the current-round handoff in `PROJECT_ROOT/docs/progress.md`
- If you need private self-understanding, add `personal_memory/logs/raw_signals.md` and `personal_memory/logs/growth_log.md` as a separate branch
- Run validator again

## Troubleshooting

- Missing frontmatter: add YAML block between `---` markers
- Invalid layer or scope: use values from `checks/policy.json`
- Invalid status or date: use the allowed enums and ISO date format enforced by `checks/policy.json`
- Broken `supersedes`: reference an existing memory `id`, not a file path
- Secret detection hit: redact before commit
