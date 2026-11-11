# The Yardex Difference: scroll-controlled process section

A sticky, full-screen section that plays the lawn care process (cut, trim, edge,
blow, finished lawn) as the visitor scrolls. **It is not live yet.** `dist/index.html`
is unchanged; only new, unreferenced files exist under `dist/assets/difference/`.

## Files

| Path | What it is |
| --- | --- |
| `tools/difference/section.html` | The section markup to insert into the homepage |
| `dist/assets/difference/difference.css` / `.js` | Styles and the scroll player (no dependencies, scoped to `.ydx`) |
| `dist/assets/difference/d/`, `m/` | Desktop (1280×720, 10 fps) and mobile (540×960 portrait crop, 8 fps) WebP frames |
| `dist/assets/difference/poster-1..5.webp` | Stills for the static (reduced-motion / Save-Data / no-JS) version |
| `tools/difference/source/` | The five source clips (AI-generated with Kling 3.0 from Nano Banana Pro start frames) |
| `tools/difference/frames-from-video.sh` | Rebuilds the frames from 5 clips and prints the `data-*` values |
| `tools/difference/build-preview.sh` | Builds a noindexed local preview in `tools/difference/.preview/` |

## Preview locally

```bash
tools/difference/build-preview.sh
python3 -m http.server 4173 -d tools/difference/.preview
```

## Replace the footage (e.g. with real drone video)

```bash
DFPS=10 DQ=48 MQ=50 MCROPS="0.13,0.57,0.5,0.45,0.35" \
  tools/difference/frames-from-video.sh cut.mp4 trim.mp4 edge.mp4 blow.mp4 final.mp4
```

Copy the printed `data-count-d`, `data-count-m` and `data-stages` into `section.html`.
`MCROPS` is the horizontal centre of the portrait crop for each clip (0 = left, 1 = right);
pick values that keep the worker in frame on phones.

## Go live (only with the owner's approval)

1. Paste `section.html` into `dist/index.html` directly after the "How it works"
   (`#process`) section.
2. Add `<link rel="stylesheet" href="/assets/difference/difference.css">` after `style.css`
   and `<script src="/assets/difference/difference.js" defer></script>` after `main.js`.
3. Do **not** copy the preview's `noindex` meta tag.

Nothing else changes: no URLs, titles, meta tags, schema, canonical tags or existing
headings. The section adds one H2 ("The Yardex Difference").

## Performance notes

- No frames are requested on page load. Loading starts ~1.5 screens before the section,
  coarse-to-fine, so scrubbing works early and sharpens as frames arrive.
- Desktop frames total ~24 MB and mobile ~9 MB, only for visitors who scroll there.
- Measured CLS on the homepage is unchanged (0.033 before and after on desktop).
- Reduced motion or Save-Data shows a static 5-step version with no frame downloads.
