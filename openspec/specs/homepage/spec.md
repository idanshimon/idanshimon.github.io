# homepage

## Purpose
The front page introduces the blog and lists every published article.

## Requirements

### Requirement: Every published article MUST be listed
The homepage SHALL list each article folder that is published, newest first, with title, date, topic, reading time and a link that resolves.

#### Scenario: New article added
- **WHEN** a new `<slug>/index.html` is published
- **THEN** the homepage links to it and the link returns the article

### Requirement: Homepage numbers MUST be real
Every number shown on the homepage SHALL come from a published article or its recorded data.

#### Scenario: Trial widget
- **WHEN** the homepage shows a count of trials
- **THEN** the count and the colored cells match the cited benchmark's recorded results

### Requirement: Homepage MUST work without JavaScript and on phones
Article links and text SHALL be readable without JavaScript, and nothing SHALL overflow the screen width at 390 px.

#### Scenario: Phone width
- **WHEN** the page is rendered at 390 px with mobile emulation
- **THEN** document width equals viewport width and no text is cut off
