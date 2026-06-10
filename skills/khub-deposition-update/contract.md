# Contract

This skill turns a safe `route-plan` into note creation or note update actions.

## Accepted Input

The input must contain:

- a `route-plan`
- the original intake content or a traceable excerpt
- a valid `template_id`
- a valid `target_note_path`
- a valid `final_type`

## Refused Input

The skill must refuse execution when:

- `write_blocked: true`
- `kind` is not `route-plan`
- `status` is `no_fit`
- `status` is `needs_human_decision`
- `template_id` is missing
- `target_note_path` is missing
- `final_type` is missing

## Output: Execution Report

```yaml
kind: execution-report
intake_id: MjMxNDQ3MDI2
operation: create
result: added
target_note_path: 20_Areas/25_Personal_Growth/Seeds/Seed_先写出对的感觉再找对的词.md
template_id: TP_Seed_认知半成品
source_trace:
  source: flomo
  source_id: MjMxNDQ3MDI2
  memo_ref: https://flomoapp.com/...
write_attempted: true
notes:
  - note created successfully
fidelity_metrics:
  raw_chars: 120
  retained_chars: 103
  retention_ratio_estimate: 0.86
  ai_added_chars_estimate: 12
  ai_added_ratio_estimate: 0.10
```

### Result Enum

- `added`
- `updated`
- `skipped`
- `blocked`
- `conflict`

## Intermediate Output: Note Payload

Before calling `obsidian-markdown` or `obsidian-cli`, the deposition layer should normalize a note payload shaped like:

```yaml
kind: note-payload
intake_id: MjMxNDQ3MDI2
operation: create
final_type: seed
template_id: TP_Seed_认知半成品
target_note_title: Seed_先写出对的感觉再找对的词
target_note_path: 20_Areas/25_Personal_Growth/Seeds/Seed_先写出对的感觉再找对的词.md
frontmatter:
  created: 2026-04-14 12:48
  type: seed
  status: 🌱
  tags: []
  source: flomo
  source_id: MjMxNDQ3MDI2
  memo_ref: https://flomoapp.com/...
sections:
  raw_signal: 先写出对的感觉再找对的词，不要一开始就卡在命名上。
  current_read: 这是一个关于先保留表达感受、后补命名的种子想法。
  why_keep:
    - 对表达与产出的顺序有长期价值
  open_questions:
    - 这条判断在哪些场景不成立
  growth_path:
    - 可能长成 viewpoint 或 cognition
  ai_notes:
    - 保留原句
    - 轻度推断
```

The exact section keys may differ by template, but the payload must remain structured until render time.

## Append Policy

- Prefer appending to a traceable update section or a section defined by the template.
- Preserve original judgment.
- Preserve source trace.
- Record the append reason rather than silently merging text.

## Hard Boundary

- This skill must not change `final_type`, `target_area`, or `template_id`.
- This skill must not recover from a blocked route by guessing a fallback.

## Principle Reference

- Apply the deposition, fidelity, and reporting principles from `../workflow-principles.md`.
- This contract keeps the execution boundary and report shape; the workflow-principles file remains the single source of truth for cross-layer fidelity behavior.
