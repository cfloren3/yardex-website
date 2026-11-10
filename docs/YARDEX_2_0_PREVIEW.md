# Yardex Guelph 2.0 — refinement of the original site (preview)

Branch: `redesign/yardex-2-0` (preview only — **not deployed to production**).
Approach: the original site, design system and homepage hero are kept; an
enhancement layer adds motion, depth and cleaner presentation.

## What changed

### Files
| File | Change |
|---|---|
| `dist/assets/v2/enhance.css` | **new** — enhancement styles (4.5 KB gzipped) |
| `dist/assets/v2/enhance.js` | **new** — enhancement behaviour (3.4 KB gzipped, no libraries) |
| all 32 `dist/**/*.html` | `<head>`: one `<noscript>` stylesheet link; end of `<body>`: one deferred script tag |
| `dist/index.html` | targeted section additions (below) — **hero markup byte-identical** |
| `dist/about/`, `dist/services/`, `dist/reviews/` | additive credential / recognition blocks |
| `dist/assets/style.css`, `dist/assets/main.js` | **unchanged** |

### Site-wide (all pages, via the enhancement layer)
- Smooth cross-page transitions (View Transitions API; no JS)
- Scroll-progress hairline in brand gold
- Header tucks away while scrolling down, returns on scroll up
- More fluid reveals (longer ease-out, soft blur-to-sharp on desktop), staggered grids
- Section headings (H2) reveal word-by-word; full heading text remains in the DOM and is exposed to screen readers via `aria-label`. H1s are never touched.
- Gold rules draw in; card images reveal with a clip/zoom
- Subtle parallax on the existing photo-backed sections (desktop only)
- Gentle 3D tilt on service/award cards (mouse/trackpad only)
- Smoother buttons, underline-grow links, checklist/pillar micro-interactions
- FAQ accordions open/close smoothly (where supported)
- Review/process carousels: drag-to-scroll on desktop
- Gallery photos open in a lightbox (keyboard accessible)
- Prose pages: larger first paragraph and more breathing room
- **Bug fix (pre-existing):** closing "Get Your Free Quote" buttons were gold text on gold — now legible
- Mobile: floating "Contact Us" pill hidden (it overlapped the hero and duplicated the sticky Free Quote / Call bar)

### Homepage (targeted)
- Counters band: same four animated counters (75 now shows "75+"), each with a gold underline that draws in; new credentials row underneath — Fully insured (commercial general liability), WSIB coverage, 2024 Quality Business Award, 5.0 Google rating — with line icons that draw themselves
- Marquees: "Fully insured & WSIB covered" added
- Our story: animated 3-step timeline (2020 → 2024 → Today) under the existing paragraph
- Awards & press: recognition row (Quality Business Award 2024, Consumer Choice Award 2024, Google 5.0, GuelphToday, BBB profile) above the existing award cards
- Reviews: animated 5.0 rating badge (counts up, stars fill) linking to the Google profile
- Service area: the long neighbourhood sentence is now a short intro + 13 neighbourhood chips + closing sentence (same neighbourhood names)

## SEO preservation (verified against origin/main, all 32 pages)
- Titles, meta descriptions, canonicals, robots, verification tags, Open Graph: **identical**
- JSON-LD structured data: **identical**
- H1s: **identical**; no H2/H3 removed; **no headings added**
- Internal links: none removed, none added; external links: none removed
- Visible copy: identical except the one intentional homepage change (service-area sentence → chips; all neighbourhood names kept)
- `sitemap.xml`, `robots.txt`, `vercel.json`, `/api`: **unchanged**; URLs unchanged
- Rendering: still static HTML; all content is in the HTML before any JS runs

## Validation
- Interaction test (Playwright): counters, rating counter, lightbox (open / arrow keys / Esc), FAQ, timeline, header tuck/return, mobile menu — all pass; **0 JS errors**
- Reduced motion: 0 hidden elements, no heading splitting, no parallax
- No horizontal overflow on any tested page (desktop 1440px, iPhone 13)
- Homepage, mobile emulation, throttled (1.6 Mbps, 4× CPU), local server (uncompressed):
  production LCP ≈ 0.95–0.98 s, CLS 0.078 · preview LCP ≈ 1.0–1.05 s, CLS 0.078
  (difference is within run-to-run variance; on Vercel the new files are compressed to ~8 KB)
- Trade-off: on very slow connections the enhancement styles can arrive a few seconds after first paint; until then the page shows the original styling.

## Needs owner confirmation before going live
1. **Consumer Choice Award 2024** — listed on your LinkedIn; no official winners listing was found. Confirm year and exact designation.
2. **Insurance & WSIB** — confirmed by you; keep a certificate on file. No coverage limits are stated.
3. ThreeBestRated — Yardex is not on their current Guelph list, so it is not shown.
4. BBB — shown as "registered business profile" (BBB lists Yardex as Not Rated / not accredited).
5. Inconsistent figures already on the site: About meta description says "35+ lawns", elsewhere "50"; carterflorence.com schema says founded 2022-03, Yardex says 2020.
6. Not done: before/after comparisons (no genuine paired photos exist), team photo (none available), "Publicus" reference (not received).

## To publish (only after approval)
Merge `redesign/yardex-2-0` into `main`. Rollback = revert that merge.

## Maintenance note
`vercel.json` caches everything under `/assets/` for one year (`immutable`). Never edit
`enhance.css` / `enhance.js` in place after launch — save changes under a new name
(e.g. `/assets/v2.1/enhance.css`) and update the references, or returning visitors will
keep the old version.

## Round 2 changes (owner feedback)
- **More photography:** 10 new owner-supplied lawn photos (`/assets/img2/`) added to the homepage
  gallery strip (mixed with the originals), Reviews gallery, About, Services and Lawn Mowing pages.
- **Before & after:** new homepage section with the three genuine before/after cleanup photos
  (deck vines, garden bed, rock garden); tap any photo to view it full-size.
- **Lawns in motion:** two short silent clips of fresh mowing stripes (≈460 KB each, H.264). They
  download only when scrolled near, play only while on screen, pause off-screen, and never
  autoplay for reduced-motion users (controls are shown instead). Also on the Lawn Mowing page.
- **Photo band:** full-bleed parallax photo with the line "You can tell which yards on the street
  are ours." (from the About page); image loads only when scrolled near.
- **Texture:** fine film grain + soft diagonal mowing-stripe bands on the green sections.
- **Services:** no longer boxed cards — a flowing, staggered two-column photo layout with numbered
  services (same names, descriptions, links; also applies to /services/).
- **Contact button:** bottom-right on every page, goes straight to the quote form
  (`/quote/#quote-form`); hidden while the form is on screen; on phones it appears after the
  first scroll so it never covers the hero text.
- **Removed:** the homepage "Proudly serving all of Guelph" neighbourhood section (owner request).

### SEO impact of round 2 (verified against origin/main)
- Titles, meta descriptions, canonicals, robots, structured data, H1s, URLs, internal links,
  sitemap: unchanged.
- Homepage: H2 "Proudly serving all of Guelph" and its paragraph removed (requested); H2
  "Real cleanups, start to finish" added.
- ⚠️ The removed section was the only on-page mention of the 13 Guelph neighbourhoods. They remain
  in the homepage `LocalBusiness` structured data (`areaServed`), which is unchanged. If local
  neighbourhood searches dip, consider restoring a one-line mention (e.g. in the footer).

### Performance (homepage, emulated phone, throttled, local uncompressed server)
- Production: LCP ≈ 0.95 s, CLS 0.078, initial transfer ≈ 2.5 MB
- Preview:    LCP ≈ 1.0–1.1 s, CLS 0.078, initial transfer ≈ 2.35 MB (lower — new media is deferred)
