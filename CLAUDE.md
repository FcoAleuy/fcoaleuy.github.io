# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Deployment

- **Live branch**: `gh-pages` — this is the branch GitHub Pages serves. All changes go here.
- **Domain**: franciscoaleuy.ca (set via `/CNAME`)
- No build step. Files are served as-is. Push to `gh-pages` and the site updates immediately.

## Site Structure

Trilingual portfolio with two parallel tracks:

```
/index.html          ← EN landing
/es/index.html       ← ES landing
/fr/index.html       ← FR landing

/it/index.html       ← IT/Operations portfolio (EN)
/es/it/index.html    ← IT portfolio (ES)
/fr/it/index.html    ← IT portfolio (FR)

/music/index.html    ← Music/Arts portfolio (EN)
/es/music/index.html ← Music portfolio (ES)
/fr/music/index.html ← Music portfolio (FR)

/work/{project}/     ← Case study pages (EN) — also under /es/work/ and /fr/work/
/assets/             ← Images, videos, JS bundles, PDF CV
```

## Language Handling

Language preference is stored in `localStorage('fa-lang-v2')` with values `en`, `es`, or `fr`. Each page reads this on load and redirects to the correct language directory. The v2 key replaced `fa-lang` (v1 migration clears stale French preferences).

When editing any content, apply the change to all three language files (`/`, `/es/`, `/fr/`).

## Styling Conventions

All styles are **inline within each HTML file** — there is no shared stylesheet in active use (styles/global.css is a legacy file, not linked from current pages).

Two color schemes:
- **IT portfolio**: dark navy `#071426` background, cyan accent `#38bdf8`
- **Music portfolio**: dark `#0d1117` background, purple accent `#a78bfa` (CSS var `--accent`)

Glassmorphism pattern used throughout:
```css
background: rgba(56,189,248,0.04);
border: 1px solid rgba(56,189,248,0.18);
border-radius: 14px;
backdrop-filter: blur(8px);
```

Language switcher uses the `.lang-pill` class (fixed bottom bar) with `.current` on the active language. Flags are inline SVGs — England (St George's Cross), France (tricolor), Chile (red/white/blue with polygon star).

## JS Components

React islands bundled under `/assets/`:
- `ContributionSlider` / `ContributionSlider_ES.js` / `ContributionSlider_FR.js` — used in work case studies
- `EnterpriseSlider` / `EnterpriseSlider_ES.js` / `EnterpriseSlider_FR.js` — used in work case studies
- `client.DCKK-Ipe.js` — Astro client runtime (do not modify)

The Journey Gallery (on music pages) is a vanilla JS carousel written inline — no external library. It uses `.journey-track`, `.journey-slide`, `.journey-dot`, `.journey-btn` classes and pauses on `mouseenter`.

## Key Assets

- `/assets/odac-logo.png` — Osoyoos & District Arts Council logo (dark text, needs white chip background when placed on dark pages)
- `/assets/CV_Francisco_Aleuy.pdf` — the file exists but is intentionally NOT linked from any page (resume download buttons were removed site-wide; do not re-add them)
- `/assets/yo.jpg` — portrait photo used on landing pages
