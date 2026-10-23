# Ground Truth (idanshimon.github.io)

Personal engineering blog by Idan Shimon. Notes from shipping production AI tools.

- Live: https://idanshimon.github.io
- Hosting: GitHub Pages from `main` root, `.nojekyll`. Every push to `main` deploys in about a minute.
- Stack: hand-written static HTML with inline CSS, inline SVG and small inline scripts. No build step, no framework, no external JavaScript.
- Shared assets: `assets/favicon.svg`, `assets/fonts.css` with self-hosted fonts (IBM Plex Sans/Mono, Space Grotesk, Playfair Display).
- Layout: one folder per article (`<slug>/index.html`), companions as sibling files.
- Repository is public, owned by the personal account `idanshimon`. Push with the personal account; the corporate account cannot see it.
- License: writing CC-BY 4.0, code snippets MIT.

Capabilities are specified under `specs/`:
- `homepage`: the front page.
- `article-pages`: structure and navigation of every article.
- `content-integrity`: rules every published word and number must follow.
- `publishing`: how a change goes live and how it is verified.
- `privacy`: what the site may and may not collect or reveal.
