# 02 Layer Model

## Layer responsibilities

### core
Use for stable, cross-project, cross-platform behavior.

### platform
Use only when behavior depends on a specific runtime or toolchain.

### learnings
Use for review-derived lessons, recurring failure patterns, and future improvement requests.

### rollout_summaries
Use for complete round retrospectives, evidence-backed context, and promotion candidates that still need a higher-confidence durable judgment.

### memory-sidecar
Use for runtime-only materials: raw evidence, session-level compressed state, and lightweight current/recent indexes.

### personal_memory
Use for private long-term understanding: growth signals, self-observation, values, relationship patterns, and stable personal tendencies that should not default into work memory.

## Boundary rules

- `layer` answers where the item is stored. `scope` answers how broadly it applies. Do not collapse these into one field.
- Never put temporary task state into `core`.
- Never put platform-specific quirks into `core`.
- Never let runtime sidecar materials bypass retrospective review into `core` directly.
- Keep handoff artifacts in the project workspace, not in memory layers.
- Keep private growth and life materials out of work memory by default; route them into `personal_memory` instead.
- Route first by scope, then by quality score.

## Source-of-truth rule

- Update `core` first.
- Adapt into `platform` second.
- Keep one canonical rule per behavior.
