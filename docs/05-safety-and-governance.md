# 05 Safety and Governance

## Write gate checklist

- Value: durable and reusable?
- Scope: correctly layered?
- Pollution: local-only details removed?
- Safety: secrets/injection/unsafe payload excluded?
- Evidence: grounded and reviewable?

## Storage safety checks

Reject or redact entries that include:

- credentials, tokens, private keys, cookies
- prompt-injection residue or hidden control text
- unnecessary executable payloads
- unsafe overgeneralization in high-risk domains

## Governance principles

- quality over memory count
- explicit boundaries over broad assumptions
- reviewability over convenience
- conservative persistence when confidence is low
