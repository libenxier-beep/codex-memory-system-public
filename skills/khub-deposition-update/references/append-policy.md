# Append Policy

## Default Behavior

- Prefer incremental updates over overwrite.
- Keep the original note's judgment intact.
- Append only when the new material deepens the same note rather than creating a new one.

## Good Append Cases

- new supporting example
- new evidence for the same lens
- clarified wording that still belongs to the same note

## Bad Append Cases

- topic drift
- new note type hidden inside the old note
- a change that would make the old title misleading

Return `conflict` when append safety is unclear.
