# Fit Check Policy

Return `no_fit` when any of these is true:

- no valid `final_type`
- no valid template for the chosen type
- no valid target area or bucket
- the note would obviously pollute the current taxonomy
- the note shape requires a new template, not a forced fallback

Return `needs_human_decision` when any of these is true:

- two or more candidate types are too close
- area choice is ambiguous
- append vs create is ambiguous
- the template is usable only through distortion
- the note is semantically close to a heavier type, but source density is too low to decide whether to downgrade safely

When either state is returned:

- create a `decision-report`
- set `write_blocked: true`
- stop before downstream deposition

## Principle Reference

- Apply the template-density principles from `../workflow-principles.md` during fit checks.
- This file defines when to stop; the workflow-principles file defines the durable preference order behind those checks.
