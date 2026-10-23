## ADDED Requirements

### Requirement: Every published page MUST have a share preview
Every page linked from the homepage SHALL include `og:title`, `og:description`, `og:url`, `og:image` (1200x627, served from this site) and `twitter:card` set to `summary_large_image`. Numbers shown in the image SHALL match the article.

#### Scenario: Link shared on LinkedIn
- **WHEN** an article URL is pasted into a LinkedIn post
- **THEN** the preview shows the article's own image and title, not a blank card

#### Scenario: New article
- **WHEN** a new article is published
- **THEN** it ships with its own `og.png` and preview tags in the same change
