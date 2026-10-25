# site-branding Specification

## Purpose
Keep the approved Beyond AI / Architecting the Future publication identity consistent across the homepage, navigation, metadata and shared assets while preserving published URLs, evidence and real interactions.
## Requirements
### Requirement: Approved publication identity
Publication branding MUST use Beyond AI, and the homepage MUST visibly pair it with the tagline Architecting the Future.

#### Scenario: Homepage arrival
- **WHEN** a visitor opens the homepage
- **THEN** Beyond AI identifies the publication and Architecting the Future appears as its headline
- **AND** the testing method and real example remain present

### Requirement: Consistent navigation and metadata
Existing publication-name labels MUST use Beyond AI in page navigation, footers, title suffixes and current repository documentation; browser metadata MUST identify the current publication.

#### Scenario: Direct article arrival
- **WHEN** an existing article or companion is opened directly
- **THEN** any publication-branded return label uses Beyond AI and preserves its destination
- **AND** old publication-name title suffixes are replaced

### Requirement: Current branding assets
The shared favicon MUST use BA rather than GT, and the homepage sharing image MUST show the approved name and tagline without introducing numerical or adoption claims.

#### Scenario: A homepage link is shared
- **WHEN** the homepage metadata and referenced preview image are retrieved from the origin
- **THEN** both carry the Beyond AI identity and the image contains Architecting the Future
- **AND** existing asset URLs remain stable

### Requirement: Non-destructive rename
The rename MUST preserve published page paths, existing link destinations, article subjects, recorded evidence and executable inline scripts; technical ground-truth terminology MUST NOT be rewritten as publication branding.

#### Scenario: Existing reader follows a saved URL
- **WHEN** a reader opens a previously published article or companion URL
- **THEN** the page remains available with the same evidence and links
- **AND** its real interactions continue to operate
