# publishing

## Purpose
How a change goes from a local edit to the live site, and how we confirm it actually went live.

## Requirements

### Requirement: Changes MUST be reviewed locally before pushing
Every change SHALL be previewed locally, and redesigns SHALL be prepared in a separate copy so the live version stays intact until approved.

#### Scenario: Redesign
- **WHEN** a page is redesigned
- **THEN** the owner approves the local version before it is pushed

### Requirement: Publishing MUST use the personal account and be verified live
Pushes SHALL authenticate as `idanshimon`, the active account SHALL be restored afterwards, and each changed page SHALL be fetched from the live site to confirm the new content.

#### Scenario: Push
- **WHEN** a change is pushed to `main`
- **THEN** the live pages return 200 and contain the new text within a few minutes
