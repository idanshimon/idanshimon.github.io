# Changelog

Publication history for Ground Truth (idanshimon.github.io). Newest first.

## 2026-06-27

### Published

- **[groundedwork: retrieval that knows when it doesn't know](groundedwork/)** — launch piece for my open-source tool (github.com/idanshimon/groundedwork): a tiny, dependency-free BM25 retrieval layer with a relevance floor that abstains instead of hallucinating, in Python and TypeScript. A measured 99.2% token reduction, opt-in hybrid embeddings that double paraphrase recall, and a live in-browser demo running the real engine. MIT.

## 2026-06-18

### Published

- **[ContextForge: how to give a coding agent a codebase without drowning it in tokens](contextforge/)** — a companion to the workingset study, about a different engineer's open-source SDK (github.com/Betanu701/ContextForge) optimized for code rather than markdown. Written from a read of the actual source and a local run of the 115-test suite. Covers the SQLite knowledge tree, the BM25 per-query working set, the code-generation path that compacts each finished file to its signatures (verified: a 202-token file body to 77 tokens), the KV-cache permanent-context layer with the honest self-hosting caveat, and the real 15-turn benchmark (ContextForge vs Azure AI Foundry Agent: 13.4× fewer tokens, 8× faster, 75.0% vs 64.7% quality, including the 5 of 15 turns the Foundry Agent won). Cross-linked both ways with the workingset article.

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
