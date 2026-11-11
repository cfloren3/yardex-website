# The Lawn Process: scroll-controlled section

A sticky, full-screen section on the homepage, directly under "From first message to
first cut" (`#process`). Scrolling plays a lawn care visit: cutting (30-inch Toro
TurfMaster), trimming and sidewalk/garden-bed edging (STIHL FS 111 R), blowing every
hard surface (STIHL BR 600), and the finished lawn. It is `<section id="lawn-process">`
in `dist/index.html` plus one stylesheet and one script.

## Files

| Path | What it is |
| --- | --- |
| `tools/difference/section.html` | Source copy of the section markup in `dist/index.html` |
| `dist/assets/difference/difference.css` / `.js` | Styles and the scroll player (no dependencies, scoped to `.ydx`) |
| `dist/assets/difference/d/`, `m/` | Desktop (1280×720, 10 fps) and mobile (540×960 portrait crop, 8 fps) WebP frames |
| `dist/assets/difference/poster-1..5.webp` | Stills for the static (reduced-motion / Save-Data / no-JS) version |
| `tools/difference/source/` | The five source clips (AI-generated with Kling 3.0 from Nano Banana Pro start frames) |
| `tools/difference/frames-from-video.sh` | Rebuilds the frames from 5 clips and prints the `data-*` values |

## Preview locally

```bash
python3 -m http.server 4173 -d dist
```

## Replace the footage (e.g. with real drone video)

```bash
DFPS=10 DQ=48 MQ=50 MCROPS="0.13,0.57,0.5,0.45,0.35" \
  tools/difference/frames-from-video.sh cut.mp4 trim.mp4 edge.mp4 blow.mp4 final.mp4
```

Copy the printed `data-count-d`, `data-count-m` and `data-stages` into the section in
`dist/index.html` (and `section.html`).
`MCROPS` is the horizontal centre of the portrait crop for each clip (0 = left, 1 = right);
pick values that keep the worker in frame on phones.

## Performance notes

- No frames are requested on page load. Loading starts ~1.5 screens before the section,
  coarse-to-fine, so scrubbing works early and sharpens as frames arrive.
- Desktop frames total ~24 MB and mobile ~9 MB, only for visitors who scroll there.
- Measured CLS on the homepage is unchanged (0.033 before and after on desktop).
- Reduced motion or Save-Data shows a static 5-step version with no frame downloads.
