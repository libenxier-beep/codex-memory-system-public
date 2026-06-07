# Agent Learning Loop

The skill should make the agent learn in a way that improves future work, not just this turn's answer.

## Loop

1. Source triage
   - Identify type: article, architecture, quote, case, code, transcript, report, or dataset.
   - Decide whether it is worth durable storage.
   - Record provenance before interpretation.

2. Mechanism extraction
   - Separate claim, evidence, mechanism, example, and style.
   - Prefer causal structure over memorable wording.
   - Mark unverified inference explicitly.

3. Abstraction
   - Convert source-specific lessons into domain-level principles, patterns, architecture, micro tactics, or cases.
   - Keep the original source boundary visible so the abstraction does not overclaim.

4. Future-use encoding
   - Add `use_when`, `do_not_use_when`, `retrieval_keys`, `source_refs`, `confidence`, and `last_reviewed`.
   - Write in language future users and agents will actually search for, including likely user phrases.

5. Retrieval testing
   - Invent one likely future user prompt.
   - Check whether `README.md`, `index.md`, `retrieval.md`, and `rg` would lead to the right page.
   - If not, patch routing before declaring success.

## What The Agent Should Learn

For every durable item, make these future-callable:

- Trigger: what user request should load this domain context?
- Operation: what should the agent do differently because this exists?
- Boundary: when would applying it be harmful?
- Evidence: what source or case supports it?
- Confidence: how strong is the knowledge today?

## Avoid

- "I learned that X is important" without a usable action.
- Only storing memorable quotes.
- Flattening conflicting sources into a false consensus.
- Hiding uncertainty once knowledge is moved into a polished page.
- Adding many keywords that do not match real future tasks.

## Closing Report

After a distillation run, report:

- What changed in the agent's reusable knowledge.
- Which future tasks should benefit.
- Which prompts or keywords will retrieve the knowledge.
- Which claims remain uncertain or need more evidence.
