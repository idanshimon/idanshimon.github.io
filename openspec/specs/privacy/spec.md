# privacy

## Purpose
The site promises readers it does not track them; this spec keeps that promise true on every page.

## Requirements

### Requirement: The site MUST NOT track readers
Pages SHALL NOT include analytics, tracking pixels, third-party scripts or third-party fonts, because the footer states "No analytics. No trackers."

#### Scenario: New page
- **WHEN** a page is added
- **THEN** it loads no script, font or image from a third-party domain other than plain links
