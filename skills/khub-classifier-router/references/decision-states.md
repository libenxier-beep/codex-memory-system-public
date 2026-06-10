# Decision States

## Write-Allowed States

- `create`
- `append`
- `skip_duplicate`
- `split_new_note`

## Write-Blocked States

- `no_fit`
- `needs_human_decision`

## Rule

Only write-allowed states may produce a downstream `route-plan`.
Write-blocked states must produce a `decision-report` instead.
