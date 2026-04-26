# 06 Operations and Audit

## Operational routines

- run post-task distillation only for meaningful sessions
- prefer summary-only output when signal is weak
- keep session history and durable memory separate
- keep the rolling long-task handoff in a project-local `docs/progress.md` by default so a fresh session can resume from one stable visible artifact
- split a separate `docs/next_steps.md` only when the next-action queue becomes noisy enough that it harms scan speed in `docs/progress.md`
- keep runtime evidence in `memory-sidecar/` and complete round retrospectives in `rollout_summaries/`

## Audit artifacts

- change log for structural updates
- rollout/session summaries for evidence trail
- schema/checklist files as policy contracts

## Recommended metrics

1. classification accuracy (correct layer)
2. deduplication quality (reduced near-duplicates)
3. pollution rate (invalid durable writes)
4. retrieval usefulness (evidence quality in recall)
