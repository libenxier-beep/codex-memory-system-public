---
name: khub-deposition-update
description: Use when a validated KHub route-plan must be turned into Obsidian note creation or append operations while preserving source trace, stop rules, and write guards.
---

# KHub Deposition Update

## Overview

This skill is the KHub execution layer.
It accepts only validated downstream routing decisions and turns them into safe Obsidian note changes through `obsidian-markdown` and `obsidian-cli`.
Follow the formal workflow principles in `../workflow-principles.md`.

## Use This Skill For

- Creating a new KHub note from a valid route plan
- Appending new supporting material to an existing KHub note
- Producing a structured execution report after note creation or update
- Enforcing write guards before any Obsidian mutation happens

## Do Not Use This Skill For

- Reclassifying note type or area
- Guessing templates or note paths
- Writing blocked items into KHub anyway
- Turning `decision-report` into a note automatically

## Inputs

- A valid `route-plan`
- The original intake item for traceability
- The selected KHub template
- Existing note content when `operation=append`

## Outputs

- New or updated Obsidian note content
- `execution-report`

## Output Discipline

- This skill must not produce a new classification.
- It must either produce a note payload plus an execution result, or stop with `blocked` or `conflict`.
- When blocked, it must not call write operations.

## Workflow

1. Load and validate the route plan.
2. Enforce write guard rules.
3. Load the template and source trace fields.
4. Map intake content into note sections.
5. Render final Obsidian Markdown.
6. Execute vault operations through `obsidian-cli`.
7. Return an `execution-report`.

## Stop Rules

- If `write_blocked: true`, stop immediately.
- If `status` is `no_fit` or `needs_human_decision`, stop immediately.
- If `template_id`, `target_note_path`, or `final_type` is missing, stop immediately.
- If append placement is unsafe or unclear, return `conflict` instead of forcing a write.

## Module Map

- `route-loader`
- `route-guard`
- `template-loader`
- `source-trace-builder`
- `content-mapper`
- `create-builder`
- `append-strategy`
- `markdown-renderer`
- `vault-writer`
- `conflict-handler`
- `execution-reporter`

## Working Pattern

For each accepted route plan:

1. verify the route is executable
2. load the matching template
3. map intake content into template slots
4. prepare a note payload
5. render Obsidian Markdown
6. perform create or append through `obsidian-cli`
7. return an `execution-report`

See `contract.md` for the execution contract, `references/` for update policies, and `../workflow-principles.md` for the formal workflow principles.
