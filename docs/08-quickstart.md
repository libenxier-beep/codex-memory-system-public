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
- `/tmp/agent-memory/memories/short_term`

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
- Add one session summary in `short_term/session_summaries/`
- Run validator again

## Troubleshooting

- Missing frontmatter: add YAML block between `---` markers
- Invalid scope: use values from `checks/policy.json`
- Secret detection hit: redact before commit
