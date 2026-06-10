# Dedupe Policy

## Candidate Search Inputs

- `source_id`
- title similarity
- raw signal overlap
- recent note window
- same-area proximity

## Allowed Outcomes

- `create`: no meaningful existing match
- `append`: same note, same meaning, new supporting detail
- `skip_duplicate`: already covered with no material delta
- `split_new_note`: related but meaningfully different angle

## Append Bias

- Prefer append when the note deepens the same judgment rather than changing topic.
- Prefer split when the new material would damage clarity if forced into the old note.
