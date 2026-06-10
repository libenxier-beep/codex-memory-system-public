# Workflow Composition

## End-to-End Order

1. `flomo-daily-intake`
2. `khub-classifier-router`
3. `khub-deposition-update`
4. `obsidian-markdown`
5. `obsidian-cli`

## Data Flow

`intake item -> normalized record -> route-plan -> note payload -> execution-report`

## Human Decision Branch

When router returns `decision-report`:

1. surface the report in the current Codex conversation
2. stop the write path
3. wait for human direction

Do not create a temporary Obsidian holding folder for blocked items.

## Write Gate

Only `route-plan` may enter deposition.
`decision-report` must never be converted into a note automatically.
