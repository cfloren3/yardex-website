# Yardex Guelph — Lighthouse Comparison

Tool: Lighthouse 12.8.2, headless Chromium, default throttling (mobile = simulated slow 4G + 4× CPU; desktop preset). **All numbers are lab data** (one machine, one moment). They are **not** Core Web Vitals field data. Real-user CWV (CrUX / GSC "Core Web Vitals") was **[UNVERIFIED]**: no GSC access, and a small local site may lack CrUX data entirely.

## A. Production baseline (live site, before any change)

Measured against https://www.yardexguelph.ca from this sandbox (through a proxy, which adds latency).

| Page | Device | Perf | A11y | BP | SEO | LCP | CLS | TBT |
|---|---|---|---|---|---|---|---|---|
| / | Mobile | 69 | 93 | 96 | 92 | 8.79 s | 0.000 | 8 ms |
| / | Desktop | 90 | 93 | 96 | 92 | 1.86 s | 0.035 | 0 ms |
| /lawn-mowing-guelph/ | Mobile | 95 | 96 | 96 | 100 | 2.77 s | 0.000 | 0 ms |
| /lawn-mowing-guelph/ | Desktop | 99 | 91 | 96 | 100 | 0.78 s | 0.001 | 0 ms |
| /services/ | Mobile | 93 | 96 | 96 | 92 | 3.03 s | 0.000 | 54 ms |
| /services/ | Desktop | 97 | 92 | 96 | 92 | 1.04 s | 0.002 | 0 ms |
| /services/fall-cleanup/ | Mobile | 93 | 96 | 96 | 100 | 3.02 s | 0.000 | 0 ms |
| /services/fall-cleanup/ | Desktop | 97 | 91 | 96 | 100 | 1.00 s | 0.002 | 0 ms |
| /yard-cleanup-guelph/ | Mobile | 90 | 96 | 96 | 100 | 3.38 s | 0.000 | 74 ms |
| /yard-cleanup-guelph/ | Desktop | 93 | 91 | 96 | 100 | 1.37 s | 0.001 | 6 ms |

## B. Controlled A/B — baseline vs new build, identical conditions

Both builds served from local static servers in the same sandbox, same throttling, back to back. **No compression** (Vercel adds Brotli/gzip), so absolute performance numbers are worse than production. The comparison between columns is what matters. Homepage mobile was run 3× per side to show variance.

| Page | Device | Perf before → after | A11y | BP | SEO | LCP before → after | CLS |
|---|---|---|---|---|---|---|---|
| **/** | **Mobile (run 1/2/3)** | **73 / 73 / 69 → 80 / 84 / 79** | 93 → **96**¹ | 96 → 96² | **92 → 100** | **11.10 / 11.18 / 11.48 s → 5.21 / 4.43 / 5.18 s** | 0 → 0 |
| / | Desktop | 86 → 89 | 93 → 93 | 96 → 96 | **92 → 100** | 2.38 → 1.98 s | 0.035 → 0.033 |
| /services/ | Mobile | 78 → 78 | 96 → 96 | 96 → 96 | **92 → 100** | 6.01 → 6.00 s | 0 → 0 |
| /services/ | Desktop | 95 → 95 | 92 → 92 | 96 → 96 | **92 → 100** | 1.32 → 1.28 s | 0.005 → 0.005 |
| /lawn-mowing-guelph/ | Mobile | 86 → 87 | 96 → 96 | 96 → 96 | 100 → 100 | 4.13 → 3.98 s | 0 → 0 |
| /lawn-mowing-guelph/ | Desktop | 97 → 99 | 91 → 91 | 96 → 96 | 100 → 100 | 1.05 → 0.92 s | 0.002 → 0.004 |
| /yard-cleanup-guelph/ | Mobile | 80 → 75 | 96 → 96 | 96 → 96 | 100 → 100 | 5.26 → 5.63 s | 0 → 0 |
| /yard-cleanup-guelph/ | Desktop | 96 → 96 | 91 → 91 | 96 → 96 | 100 → 100 | 1.21 → 1.21 s | 0.032 → 0.031 |

¹ After the follow-up underline fix on in-text GuelphToday links (re-run: Perf 79, A11y 96, SEO 100, LCP 4.62 s).
² The remaining Best Practices failure in the local runs is `/api/reviews` → 404, because a static server can't run the Vercel function. On the real Vercel preview the endpoint now returns **200** (verified), so production BP should reach 100.

The yard-cleanup mobile dip (80 → 75) is within run-to-run variance: the page's only change is one paragraph of links, and FCP moved 1.73 → 2.57 s, a CPU-timing artefact in the lab.

### New pages (after only)

| Page | Mobile Perf / A11y / BP / SEO / LCP | Desktop Perf / A11y / BP / SEO / LCP |
|---|---|---|
| /sodding-guelph/ | 86 / 96 / 96² / 100 / 4.05 s | 99 / 91 / 96² / 100 / 0.85 s |
| /garden-maintenance-guelph/ | 82 / 96 / 96² / 100 / 4.73 s | 99 / 91 / 96² / 100 / 0.91 s |
| /lawn-care-puslinch/ | 96 / 96 / 96² / 100 / 2.56 s | 100 / 91 / 96² / 100 / 0.74 s |

## What changed the numbers

| Change | Effect |
|---|---|
| Hero slides 2–4 load after the `load` event; WebP; 960 px images on phones; responsive preload | Homepage transfer 2,643 → 2,049 KiB; LCP render delay 10.65 s → 4.76 s (lab, mobile) |
| Descriptive "Learn more" text | Lighthouse SEO `link-text` passes → SEO 92 → 100 on `/` and `/services/` |
| GuelphToday in-text links underlined | `link-in-text-block` passes on `/` → A11y 93 → 96 |
| `/api/reviews` 200 instead of 500 | Removes the console error on every page (BP) — verified on Vercel preview |

## Against the targets

| Target | Status |
|---|---|
| Lighthouse SEO 100 | ✅ every tested page (lab) |
| Mobile perf 90+ | ❌ homepage ~80 in uncompressed lab (production baseline 69). Inner pages 86–96. Remaining blocker: render-blocking Google Fonts and the web-font swap repainting the H1 (LCP element) |
| Desktop perf 95+ | ✅ inner pages 95–100; homepage 89 |
| Accessibility 95+ | ✅ homepage 96, mobile service pages 96. ❌ desktop service pages 91–92: gold-button text contrast and unstyled breadcrumb links (brand styling, owner decision) |
| Best practices 95+ | ✅ 96 (expected 100 on Vercel now the API is fixed) |
| LCP ≤ 2.5 s / CLS ≤ 0.1 / INP ≤ 200 ms | CLS ✅ everywhere. LCP lab mobile ❌ on the homepage. INP can't be measured in the lab (TBT 0–124 ms is the proxy). **Judge LCP and INP on field data** in GSC once available |

## Next performance step (not done — changes first paint)

Self-host Archivo and Fraunces (WOFF2, subset to Latin) with `<link rel="preload" as="font">` and `font-display: swap`. This removes two third-party connections and the render-blocking Google CSS (~1.5 s in the lab). Test that the visual result is identical before shipping.

## How to reproduce

```bash
npx lighthouse@12.8.2 https://www.yardexguelph.ca/ --quiet --output=json --output-path=home-mobile.json
```
Run 3× and use the median; repeat with `--preset=desktop`.
