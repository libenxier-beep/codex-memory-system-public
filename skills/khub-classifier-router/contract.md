# Contract

This skill converts a standardized intake item into either a machine-readable `route-plan` or a human-review `decision-report`.

## Input Requirements

Expected upstream fields per item:

- `source`
- `timestamp`
- `memo_ref` or stable `source_id`
- `tags`
- `candidate_type`
- `summary`
- `raw_text`
- `notes`

The carrier may be Markdown, but the parsed record must expose the fields above.

## Output A: Route Plan

Use this output only when the item is safe to write into KHub.

```yaml
kind: route-plan
intake_id: MjMxNDQ3MDI2
source: flomo
source_id: MjMxNDQ3MDI2
timestamp: 2026-04-14 12:48
normalized_title: 先写出对的感觉再找对的词
final_type: seed
target_area: 25_Personal_Growth
target_bucket: Seeds
template_id: TP_Seed_认知半成品
operation: create
target_note_title: Seed_先写出对的感觉再找对的词
target_note_path: 20_Areas/25_Personal_Growth/Seeds/Seed_先写出对的感觉再找对的词.md
confidence: 0.88
related_candidates: []
dedupe_basis:
  - source_id
  - title_similarity
review_needed: false
write_blocked: false
```

### Allowed Operations

- `create`
- `append`
- `skip_duplicate`
- `split_new_note`

## Output B: Decision Report

Use this output when the workflow must stop and wait for a decision in the current Codex conversation.

```yaml
kind: decision-report
intake_id: MjMxXXXXXX
status: no_fit
source: flomo
source_id: MjMxXXXXXX
timestamp: 2026-04-14 12:48
raw_link: https://flomoapp.com/...
raw_text: ...
agent_read: This item compares two methods and does not fit an existing KHub template cleanly.
best_candidates:
  - final_type: cognition
    target_area: 25_Personal_Growth
    confidence: 0.44
    why_not: The comparison shape would be flattened.
  - final_type: concept
    target_area: 21_Learning
    confidence: 0.39
    why_not: The note is not a stable atom yet.
why_not_fit:
  - No existing template matches the comparison structure.
missing_template_or_area:
  - template
suggested_next_decisions:
  - user_choose_existing_type
  - create_new_template
  - skip_for_now
write_blocked: true
```

### Decision States

- `create`
- `append`
- `skip_duplicate`
- `split_new_note`
- `no_fit`
- `needs_human_decision`

## Hard Boundary

- `no_fit` and `needs_human_decision` must never be converted into a route plan automatically.
- `write_blocked: true` means downstream execution must stop.
- This skill must never write Obsidian content directly.

## Principle Reference

- Apply the template-density and no-force-fit principles from `../workflow-principles.md`.
- This contract only defines the routing boundary; the workflow-principles file remains the single source of truth for cross-layer classifier behavior.
