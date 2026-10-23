# article-pages

## Purpose
Every article page shares the same basic structure and navigation.

## Requirements

### Requirement: Articles MUST be self-contained folders
Each article SHALL live in its own folder with `index.html`, and its charts, data and companions SHALL live in the same folder or in `assets/`.

#### Scenario: Open from disk
- **WHEN** an article is opened from `file://`
- **THEN** it renders without a network request to a third-party script

### Requirement: Articles MUST link back home
Every article and companion page SHALL link back to the homepage, and the article SHALL include the sponsor note in its footer.

#### Scenario: Reader arrives from a shared link
- **WHEN** a reader opens an article directly
- **THEN** a visible link returns to the homepage

### Requirement: Charts MUST be verified before publishing
Every chart and table SHALL be checked at 1280 px and 390 px for clipped or overlapping labels, and reviewed visually.

#### Scenario: Label longer than its box
- **WHEN** an edited label no longer fits its diagram
- **THEN** the diagram is redrawn, not patched, before publishing
