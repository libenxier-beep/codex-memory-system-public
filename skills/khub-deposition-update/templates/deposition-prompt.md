# Deposition Prompt Template

Use this template when converting a valid `route-plan` into a note payload and final execution outcome.

## Goal

- accept a `route-plan`
- produce a structured `note-payload`
- render final Obsidian Markdown
- perform create or append safely
- return one `execution-report`

## Rules

- do not reclassify note type or area
- do not guess missing route fields
- if `write_blocked: true`, stop immediately
- if append placement is unclear, return `conflict`
- preserve source trace in all writes
- apply `../workflow-principles.md` for fidelity, empty-section, raw-material, and reporting rules

## Inputs

- route-plan
- original intake item
- matching template
- existing note content when appending

## Output Shape

- `templates/note-payload.schema.yaml`
- `templates/execution-report.schema.yaml`
