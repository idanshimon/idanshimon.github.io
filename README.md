# Ground Truth

Personal engineering writing by Idan Shimon. Notes from shipping production AI tools.

**Live site:** https://idanshimon.github.io

## Published articles

| Date | Article | Companions |
|------|---------|------------|
| 2026-06-17 | [I shipped a tool with 34× token reduction. Then the benchmark told me it wasn't enough.](workingset/) | [Dashboard](workingset/dashboard.html), [Glossary](workingset/glossary.html), [Integration guide](workingset/integration-guide.html) |

## Repository structure

```
idanshimon.github.io/
├── index.html              homepage (article listing)
├── workingset/             first launch piece + companions
│   ├── index.html          the main article
│   ├── dashboard.html      interactive 432-trial benchmark dashboard
│   ├── glossary.html       LLM context terminology reference
│   └── integration-guide.html  practical guide for agent developers
├── assets/                 shared resources (currently unused)
├── CHANGELOG.md            published-article history
├── LICENSE                 CC-BY 4.0 for writing, MIT for code snippets
└── .nojekyll               tell GitHub Pages: serve files as-is, no Jekyll
```

Each article folder is self-contained: one `index.html` plus optional companion HTMLs. No build step. No JavaScript dependencies. Everything renders from `file://` or a static webserver.

## How this is published

GitHub Pages from the `main` branch root. Every commit to `main` deploys automatically within ~1 minute. No CI/CD, no SSG, no framework. Just HTML + inline CSS + inline SVG.

## Writing in progress

See [CHANGELOG.md](CHANGELOG.md) for the publication history. Drafts live in private repos until they're ready to ship.

## Related projects

- [workingset](https://github.com/idanshimon/workingset) — the tool the first article is about. Markdown-vault context compactor for AI agents.

## License

- **Writing** (HTML articles, prose): [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) — share and adapt with attribution
- **Code snippets** within articles: MIT, use freely

See [LICENSE](LICENSE) for full text of both.

## Contact

[GitHub](https://github.com/idanshimon) is the only place I publish from. If you've reproduced a benchmark, found a bug in a code snippet, or want to discuss the writing, open an issue on this repo.

## Support the writing

If the work has been useful to you, you can [sponsor my work on GitHub](https://github.com/sponsors/idanshimon). 100% of every contribution goes to me, no platform fees.
