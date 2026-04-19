# 03 Memory Lifecycle

## Lifecycle loop

1. Observe interaction outcome
2. Extract candidate insights
3. Classify scope and stability
4. Compare against existing memory
5. Decide `add | merge | upgrade | split | discard`
6. Route to target layer
7. Log structural changes
8. Revalidate over time

## Deduplication decisions

- `revalidate`: same rule, no meaningful delta
- `merge`: same scope, clearer wording or boundary
- `upgrade`: strictly better rule replaces weaker one
- `split`: superficially similar but scope differs
- `discard`: low-signal, local-only, unstable, or risky

## Retirement decisions

- downgrade `core -> platform` when it stops being neutral
- downgrade `core/platform -> short_term` when it becomes temporary
- mark `superseded` instead of deleting when replaced
