# Rename verification

Baseline: 01a5230. No article paths, existing href/src destinations, executable inline scripts or JSON evidence are changed. Exact old/new link and script sequences were compared for all 15 existing HTML pages.

## Executed before publication

- Four static brand regression tests passed: homepage identity/metadata, current labels, BA monogram and social-image source.
- All 15 existing HTML routes returned the new publication metadata locally.
- Chromium exercised the trial replay and topic filters at 1280, 390 and 320px; no new script errors or horizontal page overflow.
- The existing real widget still reaches 432 trials and four trap cells. No recorded data was changed.
- Article-to-home return navigation was clicked in the actual rendered page; the homepage remains readable with JavaScript disabled.
- Desktop and 320px homepage screenshots and the actual new 1200x627 social image were visually inspected: name, tagline and monogram readable, no clipping or overlap.

## Existing defect, not repaired by this rename

A featured article remains visible when selecting decision or GitHub filters: decision displays 2 despite a label of 1; GitHub displays 3 despite a label of 2. This was reproduced on both unchanged baseline HTML and the rebranded HTML. The rename preserves the scripts and does not claim the count-integrity requirement passes. Fix separately rather than hide it behind branding verification.

## Release gates

OpenSpec strict validation and diff hygiene are required before publication. Origin metadata, favicon, image bytes and desktop/phone screenshots must be independently rechecked after Pages deploys. A local pass does not prove a hosted release or refresh a third-party social cache.

## Verified live

PR #1 merged as 834208f87832deaa769a8c343d07fedba69aaec4; Pages run 40150170437 completed successfully and the exact revision reports built with no build error. All 15 existing HTML origin routes returned Beyond AI metadata. Chromium repeated desktop/390/320px journeys, counter/filter baseline checks, article return navigation and no-JS reading against https://idanshimon.github.io/. The actual live 390px screenshot was visually inspected. Favicon and homepage PNG bytes independently match the source artifacts.

The known pre-existing filter/count defect remains explicitly excluded from passing claims. No article routes or evidence were changed. Canonical site-branding was synchronized using the normal OpenSpec archive after live verification.
