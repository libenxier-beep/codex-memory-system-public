# 03 Memory Lifecycle

## Lifecycle loop

1. Capture runtime evidence
2. Compress one bounded session
3. Write a complete rollout retrospective
4. Extract candidate insights
5. Classify scope and stability
6. Compare against existing memory
7. Decide `add | merge | upgrade | split | discard`
8. Route to target layer
9. Log structural changes
10. Revalidate over time

## Layered promotion flow

- `memory-sidecar/evidence` -> raw or near-raw traces
- `memory-sidecar/sessions` -> compressed runtime context
- `memories/rollout_summaries` -> full retrospective plus promotion candidates
- durable memory layers -> stable promoted outputs

## Deduplication decisions

- `revalidate`: same rule, no meaningful delta
- `merge`: same scope, clearer wording or boundary
- `upgrade`: strictly better rule replaces weaker one
- `split`: superficially similar but scope differs
- `discard`: low-signal, local-only, unstable, or risky

## Retirement decisions

- downgrade `core -> platform` when it stops being neutral
- move durable conclusions back to the runtime sidecar when they prove temporary or too local
- mark `superseded` instead of deleting when replaced
