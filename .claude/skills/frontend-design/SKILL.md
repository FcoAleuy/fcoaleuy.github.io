---
description: >
  Live frontend editing with browser preview for franciscoaleuy.ca.
  Use this skill whenever the user wants to see, edit, or improve any
  page of the site visually — from their phone or any device.
  Invoked with /frontend-design.
---

# /frontend-design — Live Visual Editor

## What this skill does

1. Serves the site locally with Python's HTTP server
2. Opens the target page in a Playwright Chromium browser
3. Takes a screenshot and sends it to the user
4. Applies edits (HTML/CSS) and screenshots again to show the result
5. Repeats until the user is happy
6. Commits and pushes to `gh-pages` (live site)

## How to run it

When the user invokes `/frontend-design [page]`, follow these steps:

### Step 1 — Identify the target page

If the user specifies a page (e.g. "música", "IT", "landing"), resolve it:

| User says | Files to edit |
|---|---|
| landing / inicio / accueil | `/index.html`, `/es/index.html`, `/fr/index.html` |
| música / music / musique | `/music/index.html`, `/es/music/index.html`, `/fr/music/index.html` |
| IT / ops / tech | `/it/index.html`, `/es/it/index.html`, `/fr/it/index.html` |

Default to the landing page if nothing is specified.

### Step 2 — Start the server and capture a screenshot

```bash
# Kill any existing server on the port first
kill $(lsof -t -i:8090) 2>/dev/null; true
# Start server in background
python3 -m http.server 8090 --directory /home/user/fcoaleuy.github.io &>/tmp/fe-srv.log &
sleep 1
```

Then use Playwright (Node.js) to screenshot:

```js
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const browser = await chromium.launch();
  // Desktop viewport
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 2 });
  await page.goto('http://localhost:8090/PATH/', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1200);
  await page.screenshot({ path: '/tmp/fe-before.png' });
  // Mobile viewport
  const mob = await browser.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3 });
  await mob.goto('http://localhost:8090/PATH/', { waitUntil: 'networkidle' });
  await mob.waitForTimeout(1200);
  await mob.screenshot({ path: '/tmp/fe-before-mobile.png' });
  await browser.close();
})();
```

Send both screenshots to the user with `SendUserFile`.

### Step 3 — Edit

Use the `Edit` tool to make changes to the HTML/CSS files.
**Always edit all three language versions** (EN + ES + FR) unless told otherwise.

### Step 4 — Screenshot after

Same Playwright script, save to `/tmp/fe-after.png` and `/tmp/fe-after-mobile.png`.
Send both to the user.

### Step 5 — Commit and push to gh-pages

Only when the user approves:

```bash
git add <changed files>
git commit -m "brief description of change"
git push origin gh-pages
```

## Site structure reminders

- All styles are **inline** inside each HTML file — no shared stylesheet.
- IT palette: dark navy `#071426`, cyan accent `#38bdf8`
- Music palette: dark `#0d1117`, purple accent `#a78bfa`
- Language switcher stored in `localStorage('fa-lang')` with values `en`, `es`, `fr`
- Live branch: `gh-pages` → franciscoaleuy.ca

## Port management

Always use port **8090** for this skill. Kill it before starting:
```bash
kill $(lsof -t -i:8090) 2>/dev/null; true
```
Kill it after screenshotting:
```bash
kill $(lsof -t -i:8090) 2>/dev/null; true
```
