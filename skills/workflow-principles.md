# Flomo To Knowledge-Base Workflow Principles

These principles are shared by the Flomo intake, classifier/router, and deposition/update skills.

## Core Rules

- Treat Flomo as an intake source, not as a general long-term memory system.
- Preserve source trace for every processed memo: keep `source_id` when available, keep a stable memo reference when available, and keep enough raw context for later audit.
- Deduplicate before writing. Exact `source_id` matches block duplicate note creation unless the user explicitly asks for a repair or merge.
- Route before writing. Classification, area routing, template selection, dedupe, and fit checks must happen before any Obsidian mutation.
- Do not force weak material into heavy templates. Match template density to source-material density; short fragments can stay as seeds or be skipped with a decision report.
- Stop with a human-readable decision report when type, area, template, duplicate target, or append placement is unclear.
- Keep source wording available, but do not turn raw Flomo text into a broad durable-memory dump.
- Prefer one clear write over several speculative writes.

## Write Gates

Writing is allowed only when all of these are true:

- A valid final type is selected.
- A target area and note path are selected.
- The selected template fits the source density.
- Duplicate and append candidates have been checked.
- `write_blocked` is false.
- The operation is either `create` or `append`; blocked decisions such as `no_fit`, `needs_human_decision`, and `skip_duplicate` must not mutate the vault.

## Reporting

- Report skipped duplicates separately from newly created or appended notes.
- Keep blocked items visible with the reason they were blocked.
- Include enough execution detail for the user to verify what changed without rereading all raw memos.
