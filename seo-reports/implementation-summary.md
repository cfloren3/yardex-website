# Yardex Guelph — SEO Implementation Summary (2026-11-25)

**Branch:** `seo/2027-optimization` · **Baseline:** tag `baseline/pre-seo-2027` = `0c99ed8` = current production.
**Deployed to production?** **No.** The branch has a Vercel *preview* deployment only (READY). Production changes only when the branch is merged into `main`.

## 1. Before / after measurements

| Metric | Before | After | How measured |
|---|---|---|---|
| Homepage title width | 611 px | **564 px** | Canvas, Arial 20 px |
| Titles over ~600 px (site) | 13 | **0** (4 protected pages at 592–601 px left on purpose) | same |
| Images without alt / empty alt on homepage | 0 / **10** | 0 / **0** | Rendered DOM (Playwright) |
| Duplicate titles / descriptions / H1s | 0 / 0 / 0 | 0 / 0 / 0 | Crawl of all pages |
| Broken internal links / assets | 0 | 0 | Crawl |
| Indexable URLs in sitemap | 30 | **35** | sitemap.xml |
| Inbound internal links to spring/fall cleanup pages | 2 pages | **37 pages** | Crawl |
| Service pages | 11 | **16** (+ Puslinch location page) | — |
| Lighthouse SEO, `/` and `/services/` | 92 | **100** | Lab, A/B |
| Homepage mobile LCP (lab, uncompressed A/B, 3 runs) | 11.10–11.48 s | **4.43–5.21 s** | Lab |
| Homepage mobile performance (A/B, 3 runs) | 69–73 | **79–84** | Lab |
| Homepage transfer size (mobile) | 2,643 KiB | **2,049 KiB** | Lab |
| Homepage accessibility | 93 | **96** | Lab |
| Console errors per page (`/api/reviews` 500) | 1 on every page | **0** on Vercel (endpoint returns 200, verified on preview) | Vercel fetch |
| Organic rankings, Maps rankings, SoLV, clicks, CTR, leads | **[UNVERIFIED]** | **[UNVERIFIED]** | No GSC / Local Falcon / GA4 access |

Rankings are not claimed to have improved. Measure after Google recrawls (2–8 weeks), against a GSC baseline exported **before** merging.

## 2. Changes

### Homepage (`dist/index.html`)
- Title → `Lawn Care Guelph | No Contracts, 75+ 5-Star Reviews | Yardex`. Kept "No Contracts" (the existing differentiator) rather than the brief's shorter version.
- Description → the brief's proposed text (153 chars). OG/Twitter updated.
- H1 `Guelph's highest-rated lawn care. No contracts. No catch.` → **`Five-star Guelph lawn care. No contracts. No catch.`** Same styling, same three-line layout. "Highest-rated" couldn't be substantiated (ThreeBestRated ranks Yardex #2); "five-star" is backed by the 5.0 rating.
- New supporting paragraph under "Full-service residential lawn care" with 9 contextual service links and the Puslinch mention.
- FAQ "What areas do you serve?" (visible + schema): adds selected services in parts of Puslinch.
- LocalBusiness schema: broader description, Puslinch in `areaServed`, `hasOfferCatalog` (13 services).
- Hero performance: WebP, phone-sized slide images, slides 2–4 loaded after page load (slideshow timing unchanged).
- Work-reel duplicate images and logo marks given alts (still `aria-hidden`).
- GuelphToday in-text link underlined (accessibility).

### Sitewide (all 32 existing HTML files)
- Nav dropdown: + Dethatching, Sodding, Garden Maintenance, Hedge & Shrub Trimming.
- Footer services: + the same four + Lawn Care in Puslinch.
- Breadcrumbs (visible + schema) "Services" → `/services/` (was `/#services`).
- "Learn more" links get visually hidden context ("…about lawn mowing").
- Logo alt; footer GuelphToday link underlined; conversion-event script added.
- 13 over-long titles shortened (title + og:title + twitter:title only; H1s and URLs untouched).

### Existing pages with content-level edits
| Page | Edit |
|---|---|
| `/services/` | Spring/Fall cards and ItemList point to the dedicated pages; 4 new cards; Puslinch line; ItemList +5 |
| `/yard-cleanup-guelph/` | Links to spring, fall, dethatching and garden maintenance pages; sidebar |
| `/trimming-edging-guelph/` | Title "Hedges, Walkways & Beds" → "Lawn Edging & Walkways"; "hedge and shrub trimming" now links to the new page |
| `/weed-control-guelph/` | Title shortened |
| `/services/spring-cleanup/`, `/services/fall-cleanup/` | "Related services" link block before the CTA |
| Aeration, fertilizer, mowing, mulching, weed, trimming, vacation | Sidebar "Other services" gains relevant new pages |
| 4 blog posts | "Related services" links at the end of the article |
| 7 blog posts + FAQ, reviews, vacation | Title shortened only |

### New pages (5)
`/sodding-guelph/` · `/dethatching-guelph/` · `/hedge-trimming-guelph/` · `/garden-maintenance-guelph/` · `/lawn-care-puslinch/` — built from the existing service-page template. Each has unique metadata, Service + BreadcrumbList + FAQPage schema, pricing **factors** (no invented prices), FAQs, related services and a CTA. See `service-page-strategy.md`.

### Technical
- `vercel.json`: 301 `www.yardexguelph.com/*` → `www.yardexguelph.ca/*` (that host was serving a duplicate site); 301 `/index.html` → `/`.
- `api/reviews.js`: returns 200 `{count:null}` when not configured (was 500 → console error on every page).
- `dist/sitemap.xml`: regenerated (35 URLs).
- `dist/assets/v2/track-r1.js` (new): sends `phone_click`, `text_click`, `email_click`, `quote_button_click`, `quote_form_submit` and `generate_lead` (once per session on `/thank-you/`) to GA4, GTM or Vercel Analytics **if installed**; otherwise does nothing. No personal data.
- New images: 5 responsive WebPs, 3 card WebPs, 3 OG images. **No existing `/assets/` file was modified** (they're cached as immutable for a year).
- `tools/seo/*.py`: the scripts that made these edits (re-runnable from the baseline).

## 3. Files

71 files: 35 modified (32 HTML + `sitemap.xml`, `vercel.json`, `api/reviews.js`), 36 added (5 pages, 12 assets, 3 scripts, `.gitignore` line, reports). Full list: `git diff --stat baseline/pre-seo-2027 seo/2027-optimization`.

## 4. Testing performed

| Test | Result |
|---|---|
| Build | Static site, no build step; Vercel preview build **READY** |
| Link crawl (every `href`/`src`, all 37 pages) | 0 broken |
| JSON-LD parse (all pages) | 0 invalid |
| Visible FAQ ↔ FAQPage schema parity | 0 mismatches |
| Duplicate titles/descriptions/H1s; one H1 per page | Pass |
| Quote form (FormSubmit **intercepted**, no email sent) | Posts all 12 fields; double-submit blocked by the existing "Sending…" state; `quote_form_submit` fires once |
| Thank-you lead event | Fires once; not on reload |
| Phone click event | Fires |
| Hero slideshow | All 4 slides get images after load |
| Mobile menu (390 px) | Opens, 21 links visible |
| Horizontal overflow at 390 px | None on any page |
| JS errors | None (only the local `/api/reviews` 404, which can't run on a static server) |
| Screenshots, 31 baseline pages × desktop 1366 + mobile 390, before vs after | Differences limited to: homepage H1 text and new paragraph, longer nav/footer lists (+114 px desktop footer), `/services/` new cards, cross-link blocks, two underlined links. Header/hero region identical apart from image-decode noise. See `seo-reports/screenshots/` |
| Lighthouse before/after | See `lighthouse-comparison.md` |
| Unsupported claims | No "highest-rated"/"highest rated" anywhere; no prices on new pages |
| Ranking URLs removed or redirected | None. All 31 baseline pages still return 200 locally with the same canonical (plus 404.html) |

## 5. Assumptions and owner confirmations used

- Owner confirmed (2026-11-25): sodding, dethatching, hedge & shrub trimming, garden maintenance are offered; Puslinch served **on a limited basis**; 75+ reviews accurate.
- Assumed: weekly mowing "from $27.50" is still right for 2027 (unchanged copy).
- Hedge page: clippings "raked and blown off" (consistent with the existing blowdown process). Haul-away for hedge/garden work is **not** claimed.
- Puslinch page lists services "most often requested" and says availability is confirmed per address.

## 6. Ranking risks

| Change | Risk | Mitigation |
|---|---|---|
| Homepage title, description, H1 | **Medium** — the main ranking page for "lawn care Guelph" | Keyword stays first in the title; "Guelph lawn care" now in the H1; compare GSC weekly for 6 weeks; revert just these lines if position drops > 2 for 2+ weeks |
| Trimming & edging title (drops "Hedges") | Low–medium | Hedge intent moves to a dedicated page that it links to |
| 13 shortened titles | Low | Keywords kept; Google often rewrites long titles anyway |
| Nav/footer growth | Low | More internal links to new pages slightly dilutes links to old ones; core pages still get every sitewide link |
| New pages without project photos | Low (thin-content perception) | Add real sod, dethatch and hedge photos (strategy doc) |

## 7. External actions required (not done — need the owner)

1. Review the preview; confirm the open questions (Puslinch service list, "Something else" service, founding year, 35 vs 50 lawns).
2. Export the GSC baseline, **then** merge.
3. Vercel → Domains → `www.yardexguelph.com` → redirect to `www.yardexguelph.ca`.
4. Install analytics (Vercel Web Analytics or GA4); add Places API env vars if you want the live review count.
5. GSC: submit sitemap, request indexing for the 5 new URLs. Bing Webmaster import.
6. Finish connecting Local Falcon; connect GSC and Semrush/Ahrefs for real ranking data.
7. GBP updates, citations and outreach (see the GBP and backlink plans). Nothing was sent or submitted.

## 8. Rollback

Before merge: delete or ignore the branch — production is untouched.

After merge:
```bash
git revert -m 1 <merge-commit-sha>
git push origin main
```
Or in Vercel → Deployments → the previous production deployment → **Promote to Production** (instant).

Partial rollback of the homepage title/H1 only: restore `dist/index.html` lines from tag `baseline/pre-seo-2027` and re-apply the rest with `tools/seo/apply_2027.py`.
