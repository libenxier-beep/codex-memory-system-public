#!/usr/bin/env bash
set -euo pipefail

TARGET_ROOT="${1:-${AGENT_HOME:-$HOME/.agent-memory}}"
MEM_ROOT="$TARGET_ROOT/memories"
SIDECAR_ROOT="$TARGET_ROOT/memory-sidecar"

mkdir -p \
  "$MEM_ROOT/core" \
  "$MEM_ROOT/platform" \
  "$MEM_ROOT/learnings" \
  "$MEM_ROOT/rollout_summaries" \
  "$MEM_ROOT/short_term" \
  "$SIDECAR_ROOT/evidence" \
  "$SIDECAR_ROOT/sessions" \
  "$SIDECAR_ROOT/indexes" \
  "$SIDECAR_ROOT/policies" \
  "$TARGET_ROOT/personal_memory/logs" \
  "$TARGET_ROOT/personal_memory/reviews"

cat > "$MEM_ROOT/README.md" <<'EOM'
# Memories System

Layered long-term memory system.

- core: durable neutral rules
- platform: runtime-specific adapters
- learnings: reusable review output
- rollout_summaries: complete round retrospectives
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
# Short-Term Memory (Legacy)

Retired legacy layer kept only for migration traceability.
EOM

cat > "$SIDECAR_ROOT/README.md" <<'EOM'
# Memory Sidecar

- evidence: raw or near-raw execution traces
- sessions: session-level compressed runtime state
- indexes: lightweight current/recent lookup entrypoints
- policies: read, promotion, and retention rules
EOM

cat > "$SIDECAR_ROOT/policies/read-policy.md" <<'EOM'
# Read Policy

- Do not load the sidecar by default.
- Query indexes first, then sessions, then raw evidence only when needed.
EOM

cat > "$TARGET_ROOT/personal_memory/README.md" <<'EOM'
# Personal Memory

- logs/raw_signals.md: broad private candidate signals
- logs/growth_log.md: confirmed growth events
- reviews/weekly.md and reviews/monthly.md: periodic refinement
EOM

cat > "$TARGET_ROOT/personal_memory/logs/raw_signals.md" <<'EOM'
# Raw Signals

- Broad private candidate signals go here first.
EOM

cat > "$TARGET_ROOT/personal_memory/logs/growth_log.md" <<'EOM'
# Growth Log

- Confirmed private growth events go here.
EOM

cat > "$TARGET_ROOT/personal_memory/reviews/weekly.md" <<'EOM'
# Weekly Review

- Review raw private signals once a week.
EOM

cat > "$TARGET_ROOT/personal_memory/reviews/monthly.md" <<'EOM'
# Monthly Review

- Refine stable private patterns once a month.
EOM

printf 'Bootstrapped memory system at: %s\n' "$TARGET_ROOT"
