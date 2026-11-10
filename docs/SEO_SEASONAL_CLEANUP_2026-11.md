# Yardex Guelph — Seasonal Cleanup SEO Expansion (November 2026)

Scope: add Fall Cleanup and Spring Cleanup relevance for Guelph + Puslinch **without**
touching the existing design or the Lawn Care Guelph SEO. Surgical, additive-only change.

Legend: **[VERIFIED]** = checked by tool/test in this pass · **[ASSUMPTION]** = needs owner confirmation ·
**[NOT AVAILABLE]** = could not be measured from this environment.

---

## 1. Summary of existing-SEO protection

- Change is **additive only**: 2 new HTML files + 2 new lines appended to `dist/sitemap.xml`. **[VERIFIED]**
- SHA-256 of all 144 repository files taken before and after: **142 files byte-identical**; the only
  modified existing file is `dist/sitemap.xml` (2 lines appended, 28 original lines unchanged). **[VERIFIED]**
- No change to: homepage, any lawn care / mowing page, `/services/`, `/yard-cleanup-guelph/`,
  `assets/style.css`, `assets/main.js`, `vercel.json` (redirects/headers/routing), `robots.txt`,
  navigation, header, footer, or any existing structured data. **[VERIFIED by hash]**
- Visual regression: 30 existing pages × desktop (1366px) + mobile (390px) = 60 full-page screenshots,
  original commit `69d20cf` vs this branch, served side by side: **60/60 pixel-identical**. **[VERIFIED]**

## 2. Protected URLs (not modified)

Primary lawn care equity: `/` (Lawn Care Guelph), `/services/` (lawn care services Guelph),
`/lawn-mowing-guelph/`, `/lawn-mowing-prices-guelph/`, `/lawn-fertilizer-guelph/`,
`/aeration-overseeding-guelph/`, `/trimming-edging-guelph/`, `/weed-control-guelph/`,
`/mulching-guelph/`, `/vacation-yard-care-guelph/`, `/yard-cleanup-guelph/`.
Also untouched: `/about/`, `/process/`, `/reviews/`, `/faq/`, `/quote/`, `/thank-you/`, `/blog/` + 11 posts, `/404.html`.

## 3. Protected files (not modified — hashes verified identical)

`dist/index.html`, `dist/services/index.html`, `dist/lawn-mowing-guelph/index.html`,
`dist/lawn-mowing-prices-guelph/index.html`, `dist/lawn-fertilizer-guelph/index.html`,
`dist/aeration-overseeding-guelph/index.html`, `dist/yard-cleanup-guelph/index.html`, all other
`dist/**/index.html`, `dist/assets/style.css`, `dist/assets/main.js`, `dist/assets/img/*`,
`dist/robots.txt`, `vercel.json`, `api/reviews.js`, and every root-level (non-`dist`) copy.

Note: Vercel serves **`dist/`** (`outputDirectory: "dist"`). The root-level HTML/CSS copies are stale
and differ from `dist/`; they are not deployed and were left alone. Production deploys `main` @ `69d20cf`,
which matched the live site byte-for-byte at audit time. **[VERIFIED]**

## 4. Existing SEO baseline (recorded before any change)

| Page | Title | H1 | Canonical |
|---|---|---|---|
| `/` | Lawn Care Guelph \| No Contracts \| Yardex — 75+ Five-Star Reviews | Guelph’s highest-rated lawn care. No contracts. No catch. | https://www.yardexguelph.ca/ |
| `/services/` | Lawn Care & Landscaping Services in Guelph \| Yardex | Lawn care & landscaping services in Guelph | …/services/ |
| `/lawn-mowing-guelph/` | Lawn Mowing Guelph \| Weekly Grass Cutting from $27.50 \| Yardex | Weekly lawn mowing in Guelph | …/lawn-mowing-guelph/ |
| `/yard-cleanup-guelph/` | Spring & Fall Yard Cleanup Guelph \| Debris Hauled Away \| Yardex | Spring & fall yard cleanups in Guelph | …/yard-cleanup-guelph/ |

- Homepage structured data: `LocalBusiness` (`@id` `https://www.yardexguelph.ca/#business`, 14 Guelph
  `areaServed` entries, award, sameAs), `WebSite`, `FAQPage`. Unchanged.
- Sitemap: 28 URLs, all lastmod 2026-07-15. robots.txt: allow all + sitemap. Unchanged.
- Rendering: static HTML on Vercel CDN, no build step, no client-side rendering.
- Rollback point: commit `69d20cf` (current production). Reverting this branch's single commit restores it exactly.
- **Google Search Console: [NOT AVAILABLE].** No GSC connector is connected to this session, so no
  impressions/clicks/CTR/position baseline was collected. No performance data has been invented.
  Capture it yourself before deploying (see §15).

## 5. Competitor research findings

Method limitation: the search tool used is not Google.ca and is not localized to Guelph, and competitor
sites could not be fetched from this environment (network policy). Findings below come from search
result titles/snippets only. **No rankings, volumes or metrics are claimed.**

Guelph pages surfaced for fall/spring cleanup and leaf removal:
- **A Cut Above Yard Services** — combined page “Yard Cleanup Guelph — Spring & Fall Cleanups, Leaf Removal”.
- **Hayden’s Property Maintenance** — dedicated “Fall Yard Clean Up Guelph” page.
- **PropertyWerks** — fall cleanup scope listed: bed/hedge blowout, hand raking, bagging, final mow, optional aeration/fertilizer.
- **Guelph Home Services** — angle: leaf drop from Guelph’s mature maples and oaks.
- **Guelph Lawn Care** — leaf removal framed around snow-mould prevention.
- **Elite Landscaping, Leaf It Alone** — spring/fall cleanup listed among many services.

Puslinch: **Guelph General Maintenance** and **Cutting Edge Property Services** list Puslinch in a service-area
list; directory listings (HomeStars, BBB) dominate. **No dedicated Puslinch seasonal-cleanup page was found.**

Gaps Yardex can own:
1. Separate, season-specific pages (most competitors use one combined page or a bullet in a service list).
2. Genuinely Puslinch-specific content (County of Wellington waste program, rural lots, woodlot edges).
3. Local practical detail: City of Guelph green-cart rules, loose-leaf collection, wet-lawn timing.
4. Trust signals competitors lack: 75+ reviews, 2024 Quality Business Award, GuelphToday feature.

## 6. Keyword strategy (keyword → URL map, avoids cannibalization)

| Intent | Target URL |
|---|---|
| fall cleanup / fall clean up Guelph + Puslinch, leaf removal Guelph + Puslinch, fall yard/lawn/property cleanup, leaf cleanup, autumn yard cleanup | **`/services/fall-cleanup/`** (new) |
| spring cleanup / spring clean up Guelph + Puslinch, spring yard/lawn/property/garden cleanup | **`/services/spring-cleanup/`** (new) |
| “yard cleanup Guelph” (generic, non-seasonal) | `/yard-cleanup-guelph/` (unchanged; both new pages link to it as “Yard Cleanups in Guelph”) |
| lawn care Guelph / lawn care services / lawn mowing | `/`, `/services/`, `/lawn-mowing-guelph/` — **unchanged** |

Overlap risk with `/yard-cleanup-guelph/` is real but low: 5-word-shingle overlap is 2.6% (fall) and 3.5% (spring)
**[VERIFIED]**; fall vs spring overlap is 4.8%, mostly shared CTA wording. Guelph vs Puslinch sections on each
page share 0% of 5-word sequences (no city-swap duplication). **[VERIFIED]**

## 7. New page URLs

- https://www.yardexguelph.ca/services/fall-cleanup/
- https://www.yardexguelph.ca/services/spring-cleanup/

No equivalent pages existed at these URLs. `/yard-cleanup-guelph/` is the nearest equivalent; it was not
redirected or edited, per the no-redirect / no-edit rules.

## 8. Files created or modified

| File | Change |
|---|---|
| `dist/services/fall-cleanup/index.html` | **created** (~1,450 words main content) |
| `dist/services/spring-cleanup/index.html` | **created** (~1,150 words main content) |
| `dist/sitemap.xml` | **2 lines appended**; existing 28 entries unchanged |
| `docs/SEO_SEASONAL_CLEANUP_2026-11.md` | **created** (this report; not deployed — outside `dist/`) |

The new pages reuse the header, footer, sticky CTA, FAB and scripts copied verbatim from
`/yard-cleanup-guelph/`, and only existing CSS classes (`hero--sub`, `grid-2`, `grid-3`, `card`, `checklist`,
`prose`, `faq`, `cta-band`, …). No new CSS, JS, fonts, images or dependencies.

## 9. New metadata

| | Fall | Spring |
|---|---|---|
| Title | Fall Cleanup Guelph & Puslinch \| Yardex Guelph (46 chars) | Spring Cleanup Guelph & Puslinch \| Yardex Guelph (48) |
| Description | Professional fall cleanup in Guelph and Puslinch. Leaf removal, yard cleanup and seasonal lawn maintenance. Request a free quote from Yardex Guelph. (148) | Professional spring cleanup services in Guelph and Puslinch. Lawn debris removal, garden bed cleanup and seasonal property maintenance. (135) |
| H1 | Fall Cleanup Services in Guelph & Puslinch | Spring Cleanup Services in Guelph & Puslinch |
| Canonical | self, absolute, trailing slash | self, absolute, trailing slash |
| Robots | index, follow, max-image-preview:large | same |
| OG/Twitter | full set, existing 1200×630 OG image `shaded-front-yard-og.jpg` | `mulched-beds-og.jpg` |

H2s (fall): Our fall cleanup services · Leaf removal that actually finishes the job · Fall cleanup in Guelph ·
Fall cleanup in Puslinch · When to book your fall cleanup · Why choose Yardex Guelph… · Fall cleanup FAQ.
H2s (spring): Our spring cleanup services · Spring cleanup in Guelph · Spring cleanup in Puslinch ·
How spring cleanup works · Why choose Yardex… · Spring cleanup FAQ.

## 10. Structured data (per new page)

- `Service` (`@id` …#service): name, serviceType, description, `provider` → `{"@id": "https://www.yardexguelph.ca/#business"}`
  (references the existing homepage entity; no business data duplicated or changed), `areaServed` = City of Guelph +
  `AdministrativeArea` Township of Puslinch (County of Wellington), `hasOfferCatalog` of included tasks.
- `WebPage` (`@id` …#webpage) linked to the Service and Breadcrumb.
- `BreadcrumbList`: Home › Services › Fall/Spring Cleanup (all items have URLs).
- `FAQPage`: generated from the same Q/A list as the visible FAQ — schema and on-page text match exactly. **[VERIFIED]**
- Not added (deliberately): prices, ratings/AggregateRating, address, geo, hours.
- Validation: all 8 blocks parse as valid JSON; types/properties are standard Schema.org. **[VERIFIED]**
  Google Rich Results Test was **[NOT AVAILABLE]** from this environment — run it after deploy.
  Note that Google currently shows FAQ rich results only for authoritative government/health sites, so
  the FAQPage markup is for clarity, not an expected SERP feature.

## 11. Sitemap changes

```
+  <url><loc>https://www.yardexguelph.ca/services/fall-cleanup/</loc><lastmod>2026-11-10</lastmod></url>
+  <url><loc>https://www.yardexguelph.ca/services/spring-cleanup/</loc><lastmod>2026-11-10</lastmod></url>
```
Valid XML, 30 URLs. Sitemaps help discovery but don’t guarantee indexing.

## 12. Build and validation results

- Build: the site is static (`buildCommand: null`), so there is no build step to run. Pages are served as-is from `dist/`.
- Local server (python http.server on `dist/`): `/`, `/services/`, both new pages, `/yard-cleanup-guelph/`,
  `/lawn-mowing-guelph/`, `/sitemap.xml`, `/robots.txt` → HTTP 200. **[VERIFIED]**
- New pages: 1 H1 each, logical H2/H3 order, 19/20 internal links all resolving (0 broken), all images exist with alt text,
  no horizontal overflow at 360px. **[VERIFIED]**
- `vercel.json` has `trailingSlash: true`; new URLs use trailing slashes and won’t trigger redirects. **[VERIFIED by config]**
- Live HTTP 200 / indexing on production: **[NOT AVAILABLE]** — not deployed yet (see §15).

## 13. Screenshot comparison

60 full-page screenshots of every existing page (desktop 1366px + mobile 390px), original `69d20cf` vs this branch:
**60/60 pixel-identical**. **[VERIFIED]** A first pass showed 5 differences; a control run proved these were
lazy-image timing noise (two runs of the *same* unchanged files also differed). After forcing all images to
decode before capture, the comparison was clean.

## 14. Changes deliberately avoided (document-only — need approval)

Highest impact first:

1. **Link the new pages from `/services/`** — the hub already has separate “Spring Cleanup” and “Fall Cleanup” cards
   whose “Learn more” both point to `/yard-cleanup-guelph/` (and the ItemList schema does the same). Pointing them to
   `/services/spring-cleanup/` and `/services/fall-cleanup/` is the single strongest discoverability fix. Without links
   from existing pages, the new pages are reachable only via the sitemap and each other, which **will slow indexing
   and limit ranking**.
2. **Add two contextual links on `/yard-cleanup-guelph/`** under the existing Spring and Fall sections
   (e.g. “More on spring cleanup →”, “Fall cleanup & leaf removal →”). This makes the combined page a hub instead of a competitor.
   → Items 1–2 are prepared as `docs/PROPOSED_internal-links_NOT_APPLIED.patch` (only `href`/schema URL changes
   plus two `link-arrow` paragraphs that reuse the existing component; it doesn't change any title, H1, meta or existing anchor text).
   Apply after approval with `git apply docs/PROPOSED_internal-links_NOT_APPLIED.patch`.
3. **Nav dropdown / footer**: optionally split “Spring & Fall Cleanup” into two entries. Sitewide change, so not done.
4. **Puslinch in the service area**: the homepage FAQ says “All residential Guelph… If you’re in the city, you’re on our map”,
   and the `LocalBusiness` `areaServed` lists only Guelph neighbourhoods. The new pages say Yardex serves Puslinch, which
   **conflicts** with that. Owner decision: confirm Puslinch is served, then update the FAQ answer and add Puslinch to
   `areaServed` (protected homepage → needs approval).
5. **Google Business Profile** (owner-only; do not change the primary category): add Puslinch to service areas if served;
   add “Fall cleanup”, “Spring cleanup” and “Leaf removal” as services; post seasonal GBP updates in Sept–Oct and Mar–Apr
   with links to the new URLs; ask cleanup clients to mention the service in reviews.
6. Data inconsistencies noticed (not changed): footer says “50 weekly lawns”, `/about/` says “35+ lawns”, and the July audit says “55 reviews”
   while the site says “75+”. Pick one figure for each.
7. Dethatching / power raking: not offered on the site (July audit flagged it as unconfirmed), so it was **not** advertised.
   If you offer it, add it to the spring page.

**[ASSUMPTIONS] to confirm:** Puslinch is served (taken from the brief); haul-away is available in Puslinch;
the cleanup crew is the same team that mows (the site says the team is five people); the timing guidance
(late Oct–Nov fall, ~mid-April spring) matches the existing `/yard-cleanup-guelph/` copy.

## 15. Recommended next steps

1. **Before deploying:** export a 3-month GSC baseline (Performance → Queries filtered on: lawn care guelph, lawn mowing guelph,
   guelph lawn care, fall cleanup, spring cleanup, leaf removal, puslinch; plus Pages: `/`, `/lawn-mowing-guelph/`,
   `/services/`, `/yard-cleanup-guelph/`), recording impressions, clicks, CTR and average position.
2. Merge `seo/seasonal-cleanup-pages` → `main` (Vercel auto-deploys). Then `curl -I` both URLs (expect 200) and run the Rich Results Test.
3. GSC → URL Inspection → Request indexing for both new URLs; resubmit the sitemap.
4. Approve items 1–2 in §14 (internal links from `/services/` and `/yard-cleanup-guelph/`) — strongly recommended.
5. Publish the spring page refresh/promo in **Feb–Mar** and the fall in **Aug–Sep**, ahead of demand, in line with the existing blog strategy.

### Monitoring plan

| Cadence | What | Alert threshold |
|---|---|---|
| Weekly (first 6 weeks) | GSC position + clicks for lawn care guelph / lawn mowing guelph / guelph lawn care and their landing pages | Avg. position drop > 2 sustained for 2+ weeks |
| Weekly | GSC indexing status of both new URLs | Not indexed after 3 weeks → add the §14 links |
| Monthly | Queries containing fall cleanup / spring cleanup / leaf removal / puslinch: impressions, clicks, landing page | Wrong landing page (e.g. `/yard-cleanup-guelph/` ranking for “spring cleanup”) → add links/consolidate |
| Seasonal | Quote-form submissions mentioning cleanup (FormSubmit emails) | Compare with prior season |

Ranking changes have many causes (algorithm updates, seasonality, competitors). A movement after deploy isn’t
automatically caused by this change — compare against the baseline and same period last year.
