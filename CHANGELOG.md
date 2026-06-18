# Changelog

Publication history for Ground Truth (idanshimon.github.io). Newest first.

## 2026-06-17

### Published

- **[I shipped a tool with 34× token reduction. Then the benchmark told me it wasn't enough.](workingset/)** — workingset launch article. A multi-run behavioral study of seven frontier models on a 1,681-token brief. Three of them passed the first run; one of those three only passes two times in three. Covers the architecture, the benchmark methodology, the abstention-probability finding, the verbatim trap-question evidence, the cost savings ($4,759 per 1,000 agent loads at public list prices), and a practical adoption guide.
  - Companion: [Interactive benchmark dashboard](workingset/dashboard.html) — all 432 trials, the per-model stability heatmap, latency profile, and cost table with $/1K and $/1M projections.
  - Companion: [LLM context glossary](workingset/glossary.html) — terminology reference for readers new to context engineering.
  - Companion: [Integration guide](workingset/integration-guide.html) — practical playbook for developers building agents with custom contexts.

### Infrastructure

- Repository created at https://github.com/idanshimon/idanshimon.github.io
- GitHub Pages enabled from `main` branch root
- License: CC-BY 4.0 for writing, MIT for code snippets
- No analytics, no trackers, no JavaScript dependencies

## How releases work

Each article ships in its own folder (e.g., `workingset/`) so URLs stay clean and content can be linked permanently. The folder's `index.html` is the article; sibling HTMLs are companions (dashboards, glossaries, guides).

Once published, an article's URL is treated as permanent. Substantive corrections are noted inline in the article (with a date). Stylistic or typographic fixes are made without note.
