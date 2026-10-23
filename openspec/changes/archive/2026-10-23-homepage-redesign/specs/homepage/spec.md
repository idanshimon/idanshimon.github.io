## ADDED Requirements

### Requirement: Homepage MUST state the blog's method up front
The homepage SHALL open with the blog's testing method and an example drawn from published data.

#### Scenario: First screen
- **WHEN** a reader opens the homepage
- **THEN** the first screen shows the headline, the method and the trial panel

### Requirement: Articles MUST be filterable by topic
The homepage SHALL offer topic filters, and with JavaScript disabled all articles SHALL remain visible.

#### Scenario: Filter
- **WHEN** a reader selects a topic
- **THEN** only that topic's articles are shown and the count on the button matches
