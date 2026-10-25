## Context
The publication is hand-written HTML on GitHub Pages. Brand labels are repeated across pages; the shared icon and homepage raster preview also contain the old identity.

## Goals / Non-Goals
**Goals:** Apply Beyond AI / Architecting the Future consistently and preserve existing links and real interactions.
**Non-Goals:** Redesign articles, alter experiments, rewrite benchmark claims, create a GitHub profile README or rename URLs.

## Decisions
1. Keep the existing green palette and typography; change the shared monogram to BA.
2. Make the approved tagline the homepage headline while keeping the testing-method explanation and real trial panel beside it.
3. Change publication-name labels only. Lowercase technical uses of ground truth and recorded experimental artifacts remain untouched.
4. Keep the existing homepage preview URL, replacing its image with the new brand/tagline and author; other article previews retain their subject-specific artwork.
5. Verify all article/companion URLs and links, preserve inline scripts byte-for-byte, exercise homepage filters and inspect desktop/phone rendering before publication.

## Risks / Trade-offs
- Social platforms may cache old previews: verify the new origin asset and metadata, not third-party cache invalidation.
- Longer branding/headlines can overflow phones: inspect 320px and 390px layouts and readable hit targets.
- Search/replace can change scientific language: match the exact publication label, never lowercase technical prose.

## Open Questions
None in the approved rename scope.
