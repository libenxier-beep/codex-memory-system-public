# 02 Layer Model

## Layer responsibilities

### core
Use for stable, cross-project, cross-platform behavior.

### platform
Use only when behavior depends on a specific runtime or toolchain.

### learnings
Use for review-derived lessons, recurring failure patterns, and future improvement requests.

### short_term
Use for active task context, candidate memories, and summary-only session outputs.

## Boundary rules

- Never put temporary task state into `core`.
- Never put platform-specific quirks into `core`.
- Never let `short_term` bypass quality gates into `core` directly.
- Route first by scope, then by quality score.

## Source-of-truth rule

- Update `core` first.
- Adapt into `platform` second.
- Keep one canonical rule per behavior.
