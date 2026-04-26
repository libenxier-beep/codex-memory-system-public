# 01 Architecture

## Core idea

Use a layered memory architecture instead of transcript dumping.

- Durable memory is explicit and structured.
- Session context is temporary and isolated.
- Platform behavior is adapted without polluting neutral rules.

## Main components

1. Memory layers
- `core`: neutral durable rules
- `platform`: environment-specific adapter rules
- `learnings`: reusable lessons and recurring failures
- `rollout_summaries`: complete round retrospectives and promotion candidates

2. Runtime sidecar
- `memory-sidecar/evidence`: raw or near-raw execution evidence
- `memory-sidecar/sessions`: session-level compressed runtime state
- `memory-sidecar/indexes`: current/recent lookup entrypoints
- `memory-sidecar/policies`: read, promotion, and retention rules

3. Private personal-memory branch
- `personal_memory/logs/raw_signals.md`: broad private candidate signals
- `personal_memory/logs/growth_log.md`: growth events worth keeping
- `personal_memory/reviews/weekly.md` and `reviews/monthly.md`: periodic refinement
- dimension files: stable private patterns, values, relationship and cognition notes

4. Protocol files
- `memory_index.md`: source-of-truth index
- `memory_schema.md`: entry schema
- `memory_intake_checklist.md`: write gate
- `memory_change_log.md`: structural change audit log

5. Execution skills
- `forge`: source material -> durable upgrades
- `post-collaboration-distillation`: post-task conservative distillation
- `mem-search`: cross-session recall workflow

## Why this architecture

- keeps memory usable under long-running work
- minimizes token waste from replaying full transcripts
- reduces policy drift by separating scope and lifecycle
- keeps handoff, runtime evidence, retrospective memory, and durable memory from collapsing into one bucket
- allows private self-understanding to evolve in parallel without polluting work-facing memory
