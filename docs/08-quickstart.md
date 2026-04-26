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

## Step 3: Wire into your own repo

1. Copy `scripts/bootstrap.sh`, `scripts/validate_memory.py`, and `checks/policy.json`.
2. Add your own memory root path.
3. Add the GitHub workflow from `.github/workflows/validate-memory.yml`.

## Step 4: First practical usage

- Create one durable rule in `core/` with frontmatter
- Add one runtime session note in `memory-sidecar/sessions/`
- For a real project, keep the current-round handoff in `PROJECT_ROOT/docs/progress.md`
- If you need private self-understanding, add `personal_memory/logs/raw_signals.md` and `personal_memory/logs/growth_log.md` as a separate branch
- Run validator again

## Troubleshooting

- Missing frontmatter: add YAML block between `---` markers
- Invalid scope: use values from `checks/policy.json`
- Secret detection hit: redact before commit
