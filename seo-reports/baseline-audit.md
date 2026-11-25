# Yardex Guelph — SEO Baseline Audit

**Measured:** 2026-11-25 · **Baseline commit:** `0c99ed8` (tag `baseline/pre-seo-2027`) · **Live site = this commit, byte-identical** (MD5 of `/`, `/lawn-mowing-guelph/`, `/services/fall-cleanup/`, `/sitemap.xml` compared live vs repo).

Legend: **[VERIFIED]** measured in this pass · **[UNVERIFIED]** could not be measured from this environment · **[OWNER]** confirmed by the owner on 2026-11-25.

## 1. Architecture

| Item | Finding |
|---|---|
| Framework | Static HTML, no build step (`buildCommand: null`). Vercel serves `dist/`. **[VERIFIED]** |
| Source of truth | `dist/`. Root-level HTML copies are stale and not deployed (documented since July). |
| Rendering | All content is in the server HTML; JS only adds motion, counters and the Lawn Process player. No JS-dependent indexability. **[VERIFIED]** |
| Hosting | Vercel (`server: Vercel`, edge `iad1`). Seobility's "Germany" server location is the CDN edge its crawler hit, not a real hosting issue. |
| Serverless | `api/reviews.js` — Google Places live review count. **Not configured** (no env vars) → returned HTTP 500 on every page view → console error on every page. **[VERIFIED]** |
| Forms | Quote form posts to FormSubmit (`formsubmit.co`) → redirects to `/thank-you/` (noindex). |
| Analytics | **None installed.** No GA4, GTM, Vercel Web Analytics (API: "Web Analytics not found"), Plausible or Meta pixel. **No conversion data exists anywhere.** **[VERIFIED]** |
| Verification tags | Google, Bing, Facebook, Pinterest meta tags present on the homepage. |

## 2. Integrations discovered

| Tool | Status |
|---|---|
| Local Falcon | Installed on the claude.ai account but **connection incomplete** — tools not available. **[UNVERIFIED data]** |
| Google Search Console | No connector. **[UNVERIFIED]** |
| Google Analytics 4 | Not installed on the site; no connector. **[UNVERIFIED]** |
| Google Business Profile | No connector. **[UNVERIFIED]** |
| Ahrefs / Semrush | Not installed. **[UNVERIFIED]** |
| Bing Webmaster Tools | Verification tag present; no connector. **[UNVERIFIED]** |
| Seobility | No API; the scores in the brief are used as reported. |
| Vercel | Connected — used for domain configuration and deployment checks. |
| GitHub | Connected — repo `cfloren3/yardex-website`. |

No rankings, search volumes, impressions or backlink counts in these reports were invented. Where they're missing, they are marked unverified.

## 3. Seobility findings — independently checked

| Seobility finding | Verified? | What we found |
|---|---|---|
| Homepage title 615 px | ✅ | Measured 611 px (Arial 20 px). Fixed → 564 px. |
| 10 images lack alt | ✅ (nuance) | Source HTML has **0** images without an `alt` attribute. The 10 are **empty** `alt=""`: 2 logo marks + 8 duplicated work-reel images inside `aria-hidden` loop items. Accessibility-wise they were already correct (decorative/duplicate). Seobility counts empty alt as missing. Given descriptive alts while keeping `aria-hidden`, so screen readers are unaffected. |
| H1 words not in content | ✅ | H1 "Guelph's highest-rated lawn care…" — "highest-rated" appears nowhere else and is not substantiable. |
| 31 headings / 37 bold | ✅ | 31 headings on the homepage; most are legitimate H3 service and process titles. Not changed for the checker. |
| Repeated anchor text | ✅ | 8× "Learn more" on the homepage and hub (also failed Lighthouse `link-text`). |
| ~30 external links | ✅ (nuance) | Only **7 unique destinations**, all relevant (GBP, Instagram, BBB, QBA award, GuelphToday, ThreeBestRated, a press mention). Kept. |
| 10 backlinks / 7 domains | ❓ | **[UNVERIFIED]** — no backlink tool connected. |
| 1,293 words, 44.8 kB, HTTP 200, canonical, en-CA | ✅ | 1,298 words in `<main>`; HTML 45,841 bytes; all confirmed. |
| No additional structured data | ❌ | Incorrect: the homepage already has LocalBusiness, WebSite and FAQPage JSON-LD; service pages have Service, BreadcrumbList and FAQPage. Seobility likely only checks specific types. |
| Server in Germany | n/a | Vercel CDN edge, see above. |

## 4. Domains and redirects (live tests)

| Request | Result |
|---|---|
| http://yardexguelph.ca | 308 → https://yardexguelph.ca/ → 308 → https://www.yardexguelph.ca/ (2 hops) |
| https://yardexguelph.ca | 308 → https://www.yardexguelph.ca/ |
| http://www.yardexguelph.ca | 308 → https://www.yardexguelph.ca/ |
| /about (no slash) | 308 → /about/ |
| /nope/ | 404 |
| /index.html | **200 (duplicate of /)**, canonical points to / |
| /post/lawn-mowing-services-in-guelph-ontario | 308 → …/ → 308 → /lawn-mowing-guelph/ (2 hops) |
| **www.yardexguelph.com** | **Vercel domain config: no redirect — serves the site directly (duplicate host).** Could not be fetched from this sandbox (proxy blocks .com). Apex yardexguelph.com → 308 → www.yardexguelph.ca. |
| yardex-website.vercel.app | Sends `X-Robots-Tag: noindex` (vercel.json rule). |

## 5. Per-page baseline (all 32 HTML files)

| URL | Status | Indexable | Title (chars) | Desc (chars) | H1 | Headings | Words | Imgs (no alt) | Inbound pages | Ext. links | JSON-LD |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `/about/` | 200 | yes | 59 | 145 | Started at 12 with a rake | 13 | 496 | 7 (0; 2 empty) | 32 | 5 | Organization, BreadcrumbList |
| `/aeration-overseeding-guelph/` | 200 | yes | 65 | 153 | Aeration & overseeding in Guelph | 10 | 808 | 7 (0; 6 empty) | 32 | 5 | Service, BreadcrumbList, FAQPage |
| `/blog/choose-lawn-care-company-guelph/` | 200 | yes | 79 | 144 | How to Choose a Lawn Care Company in Guelph: 7 Questions to Ask | 12 | 356 | 3 (0; 2 empty) | 1 | 5 | BlogPosting, BreadcrumbList |
| `/blog/does-my-guelph-lawn-need-aeration/` | 200 | yes | 76 | 137 | Does Your Guelph Lawn Need Aeration? Three Tests to Find Out | 10 | 286 | 3 (0; 2 empty) | 3 | 5 | BlogPosting, BreadcrumbList |
| `/blog/fall-lawn-care-checklist-guelph/` | 200 | yes | 80 | 132 | Fall Lawn Care in Guelph: The Checklist That Sets Up Next Spring | 10 | 306 | 3 (0; 2 empty) | 4 | 5 | BlogPosting, BreadcrumbList |
| `/blog/fix-patchy-lawn-guelph/` | 200 | yes | 56 | 139 | How to Fix a Patchy, Thin Lawn in Guelph | 10 | 349 | 3 (0; 2 empty) | 4 | 5 | BlogPosting, BreadcrumbList |
| `/blog/guelph-watering-bylaw-explained/` | 200 | yes | 75 | 148 | Guelph’s Outside Water Use Bylaw, Explained for Lawn Owners | 9 | 426 | 3 (0; 2 empty) | 3 | 5 | BlogPosting, BreadcrumbList |
| `/blog/how-often-mow-lawn-guelph/` | 200 | yes | 61 | 143 | How Often Should You Mow Your Lawn in Guelph? | 9 | 294 | 3 (0; 2 empty) | 5 | 5 | BlogPosting, BreadcrumbList |
| `/blog/` | 200 | yes | 47 | 131 | The Yardex lawn care blog | 16 | 402 | 2 (0; 2 empty) | 32 | 5 | BreadcrumbList |
| `/blog/lawn-watering-guide-guelph-summer/` | 200 | yes | 78 | 147 | Watering Your Lawn in a Guelph Summer: Less Often, Much Deeper | 10 | 320 | 3 (0; 2 empty) | 4 | 5 | BlogPosting, BreadcrumbList |
| `/blog/spring-lawn-care-checklist-guelph/` | 200 | yes | 77 | 139 | The Complete Spring Lawn Care Checklist for Guelph Homeowners | 11 | 327 | 3 (0; 2 empty) | 6 | 5 | BlogPosting, BreadcrumbList |
| `/blog/when-to-fertilize-lawn-ontario/` | 200 | yes | 85 | 155 | When to Fertilize Your Lawn in Ontario: A Guelph Homeowner’s Schedule | 10 | 481 | 3 (0; 2 empty) | 6 | 5 | BlogPosting, BreadcrumbList |
| `/blog/when-to-start-mowing-guelph-spring/` | 200 | yes | 68 | 152 | When to Start Mowing Your Lawn in Guelph Each Spring | 9 | 385 | 3 (0; 2 empty) | 3 | 5 | BlogPosting, BreadcrumbList |
| `/blog/why-we-mow-at-3-inches/` | 200 | yes | 56 | 141 | Why We Mow Every Guelph Lawn at 3 Inches | 9 | 389 | 3 (0; 2 empty) | 6 | 5 | BlogPosting, BreadcrumbList |
| `/faq/` | 200 | yes | 71 | 142 | Frequently asked questions | 5 | 495 | 3 (0; 2 empty) | 32 | 5 | FAQPage, BreadcrumbList |
| `/` | 200 | yes | 64 | 155 | Guelph’s highest-rated lawn care. No contracts. No catch. | 31 | 1298 | 35 (0; 10 empty) | 36 | 7 | LocalBusiness, WebSite, FAQPage |
| `/lawn-fertilizer-guelph/` | 200 | yes | 60 | 155 | Lawn fertilizer service in Guelph | 10 | 865 | 7 (0; 6 empty) | 32 | 5 | Service, BreadcrumbList, FAQPage |
| `/lawn-mowing-guelph/` | 200 | yes | 62 | 159 | Weekly lawn mowing in Guelph | 20 | 1029 | 13 (0; 5 empty) | 32 | 5 | Service, FAQPage, BreadcrumbList |
| `/lawn-mowing-prices-guelph/` | 200 | yes | 64 | 155 | Lawn mowing prices in Guelph (2026) | 11 | 700 | 3 (0; 2 empty) | 32 | 5 | FAQPage, BreadcrumbList |
| `/mulching-guelph/` | 200 | yes | 59 | 138 | Mulching in Guelph | 9 | 720 | 7 (0; 6 empty) | 32 | 5 | Service, BreadcrumbList, FAQPage |
| `/process/` | 200 | yes | 46 | 154 | How it works | 17 | 536 | 17 (0; 2 empty) | 32 | 5 | HowTo, BreadcrumbList |
| `/quote/` | 200 | yes | 45 | 142 | Get your free quote | 5 | 106 | 3 (0; 2 empty) | 62 | 5 | — |
| `/reviews/` | 200 | yes | 68 | 136 | 75+ five-star Google reviews | 11 | 296 | 54 (0; 2 empty) | 32 | 5 | BreadcrumbList |
| `/services/fall-cleanup/` | 200 | yes | 46 | 148 | Fall Cleanup Services in Guelph & Puslinch | 16 | 1562 | 9 (0; 7 empty) | 2 | 5 | Service, WebPage, BreadcrumbList, FAQPage |
| `/services/` | 200 | yes | 51 | 171 | Lawn care & landscaping services in Guelph | 17 | 480 | 26 (0; 10 empty) | 32 | 5 | ItemList, BreadcrumbList, FAQPage |
| `/services/spring-cleanup/` | 200 | yes | 48 | 135 | Spring Cleanup Services in Guelph & Puslinch | 15 | 1256 | 9 (0; 7 empty) | 2 | 5 | Service, WebPage, BreadcrumbList, FAQPage |
| `/thank-you/` | 200 | no (noindex) | 32 | 72 | Got it — talk soon. | 4 | 37 | 2 (0; 2 empty) | 0 | 5 | — |
| `/trimming-edging-guelph/` | 200 | yes | 59 | 126 | Trimming & edging in Guelph | 9 | 701 | 8 (0; 6 empty) | 32 | 5 | Service, BreadcrumbList, FAQPage |
| `/vacation-yard-care-guelph/` | 200 | yes | 71 | 147 | Vacation yard care in Guelph | 9 | 741 | 7 (0; 6 empty) | 32 | 5 | Service, BreadcrumbList, FAQPage |
| `/weed-control-guelph/` | 200 | yes | 69 | 164 | Weed control in Guelph | 9 | 744 | 6 (0; 6 empty) | 32 | 5 | Service, BreadcrumbList, FAQPage |
| `/yard-cleanup-guelph/` | 200 | yes | 63 | 140 | Spring & fall yard cleanups in Guelph | 11 | 824 | 9 (0; 6 empty) | 32 | 5 | Service, BreadcrumbList, FAQPage |
| `/404.html` | 200 (served as 404) | no (noindex) | 30 | 61 | 404 — this page got mowed. | 4 | 26 | 2 (0; 2 empty) | 0 | 5 | — |

Notes: "Inbound pages" counts how many pages link to the URL. Site-wide nav and footer give most pages 32. The two seasonal cleanup pages had **2 inbound pages** — only each other plus the sitemap. They were near-orphans.

## 6. Keyword cannibalization and duplication (baseline)

- `/yard-cleanup-guelph/` (combined spring and fall) vs `/services/spring-cleanup/` and `/services/fall-cleanup/`: overlapping intent, and the hub's Spring and Fall cards both linked to `/yard-cleanup-guelph/`, so Google had no signal that the specific pages are preferred.
- `/lawn-fertilizer-guelph/` ("Fertilizing & Overseeding") vs `/aeration-overseeding-guelph/`: both mention overseeding. Acceptable: different primary intents (fertilizer vs aeration), and both are protected ranking URLs.
- `/trimming-edging-guelph/` title included "Hedges", competing with the planned hedge-trimming page.
- No duplicate titles, descriptions or H1s across the site. **[VERIFIED]**

## 7. Business-claim verification

| Claim | Status |
|---|---|
| 75+ five-star Google reviews | **[OWNER]** confirmed accurate. Public third-party counts are lower (Birdeye 38; ThreeBestRated text "over 25") — these lag Google. |
| "Guelph's highest-rated lawn care" | **Not substantiable.** ThreeBestRated ranks Yardex #2 (Hometurf #1, same 4.9 score). Removed from H1, description and OG alt text. |
| Top 3 lawn care in Guelph (ThreeBest Rated) | **[VERIFIED]** — listed #2 of 3 on threebestrated.ca/lawn-care-services-in-guelph-on. |
| 2024 Quality Business Award | Shown on ThreeBestRated. The QBA page itself could not be fetched (DNS blocked here). **[Partially verified]** |
| GuelphToday feature | Article URL returned 403 to our fetcher. **[UNVERIFIED here]** — previously verified in July. |
| Weekly mowing from $27.50 | Consistent site-wide; ThreeBestRated also lists "$27.50 per cut". |
| Insurance and WSIB | Owner-confirmed in the November preview review; keep certificates on file. |
| Puslinch service area | **[OWNER]** served on a limited basis — site now says "selected services in parts of Puslinch". |
| Sodding, dethatching, hedge and shrub trimming, garden maintenance | **[OWNER]** confirmed offered (2026-11-25). |
| Footer "50 weekly lawns" vs About "35+ lawns" | **Inconsistent** — flagged, not changed (owner to pick). |

## 8. Lighthouse baseline (production, this sandbox, Lighthouse 12.8.2)

See `lighthouse-comparison.md`. Headline: homepage **mobile performance 69, LCP 8.8 s** (lab). LCP element is the hero H1 text; 93% of LCP is render delay, caused by four hero slideshow images (~1.4 MB JPEG) downloading at once and delaying the web-font swap.
