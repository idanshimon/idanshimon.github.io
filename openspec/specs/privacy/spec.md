# privacy

## Purpose
Readers get anonymous, aggregate reading statistics only; this spec allows exactly one analytics tool and keeps the footer statement true on every page.

## Requirements

### Requirement: Only Microsoft Clarity analytics
Pages SHALL load exactly one analytics script, Microsoft Clarity project `zaqs2a633d`, in `<head>`, and SHALL NOT include any other analytics, tracking pixels, advertising scripts or third-party fonts.

#### Scenario: New page
- **WHEN** a page is added, by hand or from a generator template
- **THEN** it includes the Clarity snippet for `zaqs2a633d` and loads no other third-party script, font or image

### Requirement: Footer states analytics truthfully
Footers SHALL NOT claim "No tracking scripts" or "No analytics".

#### Scenario: Footer check
- **WHEN** `grep -rn "No tracking\|No analytics" --include=*.html .` runs
- **THEN** it returns no matches

### Requirement: Admin data stays private
Clarity API tokens, exported statistics and the admin dashboard SHALL NOT be committed to this public repository.

#### Scenario: Commit check
- **WHEN** a commit is prepared
- **THEN** it contains no Clarity token and no exported statistics files
