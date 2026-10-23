# content-integrity

## Purpose
The blog's value is that its claims can be checked.

## Requirements

### Requirement: Claims MUST match recorded evidence
Every measured number SHALL match the recorded data it cites, and figures that compare different things (file size versus billed tokens) SHALL be labeled as such.

#### Scenario: Headline ratio
- **WHEN** an article states a reduction
- **THEN** it states what was measured (file, billed input, latency) and does not imply a different one

### Requirement: Claims about other people's tools MUST be checked against their source
Statements about another project's behavior SHALL be verified in its code, tests or official documentation, and credited with the exact repository link.

#### Scenario: Upstream SDK description
- **WHEN** an article describes how another tool works
- **THEN** the description matches its current source and the link points to its real repository

### Requirement: Published text MUST NOT contain drafts or internal references
Published pages SHALL NOT contain notes to the author, customer names, internal model names, internal tooling incidents or private paths.

#### Scenario: Pre-publish sweep
- **WHEN** a page is about to be published
- **THEN** a text sweep finds no draft notes, customer names or internal identifiers

### Requirement: Corrections MUST be visible
When published facts change, the article SHALL be updated and the change recorded in `CHANGELOG.md`.

#### Scenario: Benchmark number corrected
- **WHEN** a number in a live article is found wrong
- **THEN** the article is fixed and the changelog says what changed
