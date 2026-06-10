---
name: khub-classifier-router
description: Use when Flomo or other intake material needs KHub-specific classification, area routing, template selection, and write gating before any Obsidian note is created or updated.
---

# KHub Classifier Router

## Overview

This skill is the KHub decision layer between raw intake and Obsidian note writing.
It decides what a note is, where it belongs, whether it can be safely written, and when the workflow must stop for human review.
Follow the formal workflow principles in `../workflow-principles.md`.

## Use This Skill For

- Converting intake items into KHub note types such as `seed`, `cognition`, `concept`, `viewpoint`, `playbook`, or `prediction`
- Routing an item into a valid KHub area and bucket
- Selecting the matching KHub template
- Choosing between `create`, `append`, `skip_duplicate`, `split_new_note`, `no_fit`, and `needs_human_decision`
- Blocking unsafe writes before anything reaches Obsidian
- Matching template weight to source-material density so short notes are not forced into heavy templates

## Do Not Use This Skill For

- Reading Flomo directly
- Rendering final Obsidian Markdown
- Creating or updating notes in Obsidian
- Silently forcing unmatched content into an existing template or folder

## Inputs

- A standardized intake artifact such as the output of `flomo-daily-intake`
- Current KHub taxonomy and folder layout
- Current KHub template map
- Existing-note candidates from vault search when dedupe or append is needed

## Outputs

- `route-plan` for safe downstream execution
- `decision-report` for blocked or uncertain cases in the current Codex conversation

## Output Discipline

- Return `route-plan` only when the item is safe to write.
- Return `decision-report` when a human decision is still needed.
- Do not return both for the same intake item.
- For `no_fit` and `needs_human_decision`, always set `write_blocked: true`.

## Workflow

1. Parse intake items into normalized records.
2. Classify the final KHub note type.
3. Route the item into a valid KHub area and bucket.
4. Select the template that matches the final type.
5. Search for duplicate or append candidates.
6. Run fit checks, template-density checks, and write gating.
7. Output either a `route-plan` or a `decision-report`.

## Stop Rules

- If no valid KHub type can be chosen, output `no_fit`.
- If type, template, or target area cannot be matched safely, output `no_fit`.
- If multiple candidates remain too close to call, output `needs_human_decision`.
- When output is not safe for writing, set `write_blocked: true`.
- Never create or update Obsidian notes from this skill.

## Module Map

- `intake-parser`
- `signal-normalizer`
- `type-classifier`
- `area-router`
- `template-selector`
- `candidate-search-adapter`
- `dedupe-resolver`
- `fit-checker`
- `decision-gate`
- `route-serializer`

## Working Pattern

For each intake item:

1. extract the raw signal without rewriting the conclusion
2. choose the smallest stable KHub note type
3. choose a valid area and bucket
4. pick the mapped template
5. search for duplicate or append candidates
6. decide whether the template weight matches the source density
7. decide whether writing is allowed
8. emit either a `route-plan` or a `decision-report`

See `contract.md` for the I/O shape, `references/` for routing rules, and `../workflow-principles.md` for the formal workflow principles.
