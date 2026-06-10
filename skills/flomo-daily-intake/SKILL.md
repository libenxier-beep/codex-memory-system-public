---
name: flomo-daily-intake
description: Use when a task needs raw notes from flomo for a specific day or time range before classification, routing, or writing into Feishu or Obsidian.
---

# Flomo Daily Intake

Read flomo notes for a requested date or range, remove obvious noise, and produce a standardized intake for downstream skills. This skill is an input layer only.

## Use This Skill For

- Reading flomo notes for `today`, `yesterday`, a single date, or a short date range
- Preparing raw flomo material before classification or routing
- Creating a reviewable intake artifact before writing into Feishu or Obsidian

## Do Not Use This Skill For

- Deciding whether a note belongs in Feishu or Obsidian
- Writing final notes into Obsidian
- Writing records into Feishu
- Doing weekly review or long-term distillation

## Workflow

1. Read the requested flomo notes through the available flomo access path.
2. Keep each note's timestamp, raw text, tags, and source link when available.
3. Mark unusable items instead of silently dropping them:
   - blank notes
   - audio placeholders with no usable transcript
   - system or onboarding notes
4. Add a light first-pass label for downstream routing:
   - `project_idea`
   - `concept`
   - `viewpoint`
   - `action_feedback`
   - `journal_fragment`
   - `unknown`
5. Output a standardized Markdown intake that downstream skills can classify, route, and write.

## Output Rules

- Default output format is Markdown.
- Keep original wording in a `raw_text` field; do not over-rewrite at intake stage.
- When source text is missing or ambiguous, say so explicitly in `notes`.
- If nothing usable is found, return an empty intake with the reason instead of inventing content.

See [contract.md](contract.md) for the required input and output structure.
