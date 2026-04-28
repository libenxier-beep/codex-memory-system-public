# 09 Execution Skills

## Purpose

This repository separates memory architecture from execution skills, but two skills are central to making the architecture usable in real work:

- `post-collaboration-distillation`
- `memory-commit`

They form the default post-task memory-maintenance chain.

## Default chain

1. Primary work finishes
2. `post-collaboration-distillation` reviews the completed round
3. A candidate list is produced
4. User feedback rejects or accepts candidates
5. `memory-commit` writes only the approved results to the correct layer

## `post-collaboration-distillation`

Use this skill when the main need is to decide what, if anything, was worth remembering after a completed task or high-signal collaboration round.

It should:

- summarize what completed work actually mattered
- reject low-signal or local-only noise
- compare candidate insights against existing memory
- decide whether candidates belong in sidecar, rollout retrospectives, work memory, personal memory, or nowhere
- produce a structured Distillation Report

It should not:

- replace the primary task
- invent durable conclusions from weak evidence
- skip deduplication or scope checks

## `memory-commit`

Use this skill only after a completed distillation pass already produced a canonical candidate list.

It should:

- normalize reject-only user feedback
- treat non-rejected candidates as accepted
- route accepted items to `rollout_summaries/`, work memory, or `personal_memory/`
- write the minimum necessary updates
- produce a Commit Report

It should not:

- re-distill raw chat from scratch
- re-score or re-rank the candidate set
- bypass the existing truth sources for routing

## Relationship between the two

- `post-collaboration-distillation` answers: what is worth keeping?
- `memory-commit` answers: where should the accepted items land, and what files change?

Keeping them separate reduces accidental over-persistence and makes user review cheaper.

## Adjacent skill: `forge`

`forge` is still useful, but it is not part of the default post-task memory-maintenance chain.

Use it when the primary job is to learn directly from an external article, note, framework, or workflow and convert that source into durable upgrades.

## Related templates

- `templates/distillation-report-template.md`
- `templates/commit-report-template.md`
