# Source Trace Policy

Every write should remain traceable back to the intake item.

## Trace Elements

- `source`
- `source_id`
- `memo_ref`
- `timestamp`
- collapsible raw-material section with the original source text

## Update Rule

When appending to an existing note:

- keep the old trace
- add the new trace
- do not replace old provenance with new provenance

## Fidelity Rule

- Source trace is not enough by itself; the note should also retain the original material at high fidelity.
- New notes should preserve the source text in full or near-full form inside a collapsible section.
- If the source contains obvious long-term noise, only that portion may be removed.
