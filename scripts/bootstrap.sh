#!/usr/bin/env bash
set -euo pipefail

TARGET_ROOT="${1:-${AGENT_HOME:-$HOME/.agent-memory}}"
MEM_ROOT="$TARGET_ROOT/memories"

mkdir -p \
  "$MEM_ROOT/core" \
  "$MEM_ROOT/platform" \
  "$MEM_ROOT/learnings" \
  "$MEM_ROOT/short_term/candidates" \
  "$MEM_ROOT/short_term/session_summaries"

cat > "$MEM_ROOT/README.md" <<'EOM'
# Memories System

Layered long-term memory system.

- core: durable neutral rules
- platform: runtime-specific adapters
- learnings: reusable review output
- short_term: temporary context
EOM

cat > "$MEM_ROOT/memory_index.md" <<'EOM'
# Memory Index

## Active Core Layer
- core/global_principles.md
- core/runtime_preferences.md
- core/load_policy.md

## Active Platform Layer
- platform/codex.md

## Active Learnings Layer
- learnings/LEARNINGS.md
- learnings/ERRORS.md
- learnings/FEATURE_REQUESTS.md
EOM

cat > "$MEM_ROOT/memory_schema.md" <<'EOM'
# Memory Schema

Required frontmatter fields:
- id
- title
- summary
- scope
- applies_to
- type
- stability
- source
- evidence
- regression_risk
- supersedes
- last_reviewed
- owner
EOM

cat > "$MEM_ROOT/memory_intake_checklist.md" <<'EOM'
# Memory Intake Checklist

- Value: durable and reusable?
- Scope: correct layer?
- Pollution: no local-only leakage?
- Safety: no secrets/injection payload?
- Evidence: verifiable?
EOM

cat > "$MEM_ROOT/memory_change_log.md" <<'EOM'
# Memory Change Log

## YYYY-MM-DD
- Initialized layered memory system.
EOM

cat > "$MEM_ROOT/core/global_principles.md" <<'EOM'
# Global Principles

- Prefer evidence over plausibility.
- Keep memory high-signal and maintainable.
EOM

cat > "$MEM_ROOT/core/runtime_preferences.md" <<'EOM'
# Runtime Preferences

- Use concise, actionable communication.
- For prior-work questions, do recall-first before follow-up questions.
EOM

cat > "$MEM_ROOT/core/load_policy.md" <<'EOM'
# Load Policy

- Ring 0: memory_index + global_principles + runtime_preferences + platform adapter
- Ring 1: task-routed deep files
- Ring 2: deep reference on demand
- Ring 3: cold memory for explicit retrieval only
EOM

cat > "$MEM_ROOT/platform/codex.md" <<'EOM'
# Codex Adapter

- Treat local memories as default source.
- Route platform-specific behavior here only.
EOM

cat > "$MEM_ROOT/learnings/LEARNINGS.md" <<'EOM'
# Learnings

- Add only reusable, validated lessons.
EOM

cat > "$MEM_ROOT/learnings/ERRORS.md" <<'EOM'
# Errors

- Record recurring, high-cost error patterns.
EOM

cat > "$MEM_ROOT/learnings/FEATURE_REQUESTS.md" <<'EOM'
# Feature Requests

- Track cross-project memory system improvements.
EOM

cat > "$MEM_ROOT/short_term/README.md" <<'EOM'
# Short-Term Memory

Temporary task/session context only.
EOM

cat > "$MEM_ROOT/short_term/candidates/README.md" <<'EOM'
# Candidate Memories

Promising but not yet stable memory candidates.
EOM

cat > "$MEM_ROOT/short_term/session_summaries/README.md" <<'EOM'
# Session Summaries

Summary-only outputs that are not durable enough for long-term memory.
EOM

printf 'Bootstrapped memory system at: %s\n' "$MEM_ROOT"
