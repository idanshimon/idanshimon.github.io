## Decisions
- Single static `index.html`, inline CSS/SVG/JS, matching the rest of the site.
- Trial panel uses the recorded workingset counts: 432 trials = 351 correct, 77 "not in context", 4 trap failures (checked against the run files). Animation starts when visible, falls back after 1.5 s, and respects reduced motion.
- Thumbnails are hand-drawn SVG per article, not stock images.
- Filters hide cards with a class; all links stay in the HTML so the page works without JavaScript.
- Layout: 3-column grid at desktop, 2 at tablet, 1 on phones; grid items use `min-width:0` to avoid overflow.

## Verification done
- Rendered with Chrome DevTools at 1280 px and 390 px (mobile emulation): document width equals viewport, no element past the right edge.
- Image review over several rounds; final pass reported no visual bugs.
