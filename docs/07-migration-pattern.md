# 07 Minimal-Delta Migration Pattern

## Objective

Migrate from flat legacy memory files to layered architecture with minimal disruption.

## Migration steps

1. Inventory existing files by function
2. Define layered target mapping
3. Detect duplicates by behavior, not filename
4. Detect conflicts by trigger and scope
5. Keep stronger source as single truth
6. Apply minimal edits first
7. Log structural changes

## Conflict policy

For each conflict:

- Option A: keep local version
- Option B: replace with incoming version
- Option C: layered merge (preferred if minimal and safe)

## Do not do

- do not create parallel systems for same behavior
- do not migrate low-value complexity
- do not overwrite existing working rules blindly
