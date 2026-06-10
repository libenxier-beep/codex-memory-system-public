# Contract

This skill standardizes flomo notes into a Markdown intake artifact for downstream skills.

## Inputs

Supported input scopes:

- single date: `YYYY-MM-DD`
- date range: `YYYY-MM-DD` to `YYYY-MM-DD`
- relative windows: `today`, `yesterday`, `last 7 days`

Optional constraints:

- include tags
- exclude tags
- include or exclude blank/audio-placeholder notes

## Output

Default carrier: Markdown document.

Suggested document shape:

```markdown
# Flomo Intake - 2026-04-09

## Summary

- source: flomo
- requested_scope: 2026-04-09
- total_items: 4
- usable_items: 3
- flagged_items: 1

## Items

### 1. 23:26
- source: flomo
- timestamp: 2026-04-09 23:26
- memo_ref: https://flomoapp.com/...
- tags: []
- status: usable
- candidate_type: concept
- summary: 自传播产品需要让用户的使用直接创造传播素材。
- raw_text: ...
- notes:

### 2. 10:10
- source: flomo
- timestamp: 2026-04-09 10:10
- memo_ref:
- tags: []
- status: blank_or_audio_placeholder
- candidate_type: unknown
- summary: 无可用正文
- raw_text: 00:00
- notes: 页面仅显示音频占位，无正文可提炼。
```

## Required Fields Per Item

- `source`: fixed as `flomo`
- `timestamp`
- `memo_ref`: source URL or stable identifier when available
- `tags`
- `status`
- `candidate_type`
- `summary`
- `raw_text`
- `notes`

## Status Enum

- `usable`
- `blank_or_audio_placeholder`
- `system_note`
- `unreadable`

## Candidate Type Enum

- `project_idea`
- `concept`
- `viewpoint`
- `action_feedback`
- `journal_fragment`
- `unknown`

## Boundary

This skill ends after producing the intake artifact.

Downstream skills are responsible for:

- classification beyond first-pass labeling
- deciding destination system
- applying Obsidian or Feishu templates
- writing final outputs
