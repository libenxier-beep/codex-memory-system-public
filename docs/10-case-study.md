# 10 Case Study

## Goal

Show one sanitized end-to-end chain:

`raw evidence -> session -> rollout summary -> candidate -> memory-commit -> final memory layer`

## Scenario

A completed collaboration round produced three different signals:

1. a reusable work-memory routing rule
2. a reusable process lesson
3. a private growth signal that should not be mixed into work memory

## Stage 1: Raw evidence

Raw evidence belongs in `memory-sidecar/` when it is still close to the original round and mainly useful for backtracking.

Example:

```md
source: conversation
type: evidence

- User says router-first should be a weak default, not a hard prerequisite.
- User says they only want reject-only authority during commit.
- User notes a private growth signal that should stay out of work memory.
```

## Stage 2: Session compression

Session compression keeps the current round readable without promoting everything.

Example:

```md
## 2026-04-28

- memory workflow refined
- router-first kept as weak default
- commit-stage authority simplified to reject-only
- one private signal should route to personal memory
```

## Stage 3: Rollout retrospective

The rollout summary becomes the round-level narrative and the first place to explain why a candidate might be promotable later.

Example:

```md
## Outcome

- work-memory routing became more explicit
- the commit stage stayed thin
- private growth material stayed separate from work memory
```

## Stage 4: Candidate list

Distillation turns the retrospective into a canonical candidate list.

Example:

```yaml
- candidate_id: C1
  summary: Prefer router-first as a weak narrowing pass for core reads.
  recommended_destination: work_memory
  draft_write: memories/core/runtime_preferences.md

- candidate_id: C2
  summary: Keep commit-stage skills thin and downstream-only.
  recommended_destination: learnings
  draft_write: memories/learnings/LEARNINGS.md

- candidate_id: C3
  summary: A private growth signal is worth keeping, but not in work memory.
  recommended_destination: personal_memory
  draft_write: personal_memory/logs/raw_signals.md
```

## Stage 5: Reject-only feedback

The user does not need to route everything by hand.

Example:

```yaml
reject:
  - C2
```

## Stage 6: `memory-commit`

`memory-commit` takes the accepted candidates and writes the minimum necessary updates.

Result:

- `C1` -> work memory
- `C2` -> rejected
- `C3` -> personal memory

## Final landing

- `C1` -> `memories/core/runtime_preferences.md`
- `C2` -> nowhere in this run
- `C3` -> `personal_memory/logs/raw_signals.md`

## Why this matters

- Raw evidence stays queryable without becoming durable memory too early.
- Rollout retrospectives preserve round context.
- Distillation separates judgment from execution.
- Reject-only review keeps user overhead low.
- Private material can be retained without polluting work memory.
