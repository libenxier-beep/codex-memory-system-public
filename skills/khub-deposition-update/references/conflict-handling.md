# Conflict Handling

Return `conflict` instead of forcing a write when:

- the target note exists but the append location is not clear
- the route title and the existing note title disagree materially
- the template shape does not match the existing note shape
- the target path already exists with incompatible content

Conflicts should be reported back to the current Codex conversation with enough detail for a human decision.
