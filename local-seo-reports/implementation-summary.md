# Implementation summary

Date: 2026-11-25 · Branch: `seo/local-maps-2026-11` (pushed, **not merged**). Merging to `main` deploys to production through Vercel.

## 1. What could be accessed
| Integration | Status |
|---|---|
| Local Falcon | **Not connected.** No scans, no historical data, no credits used. |
| Google Business Profile | **Not connected** |
| Google Search Console, GA4 | **Not connected** (and the site has no analytics tag) |
| Google Maps / Places API | **Blocked** by the network policy. The repo's `/api/reviews` has no API key configured. |
| Ahrefs, Semrush, BrightLocal, Keyword Planner | **Not connected.** No search volumes are claimed anywhere. |
| Bing Places, Apple Business Connect | **Not connected** |
| Website repo (GitHub `cfloren3/yardex-website`) | Connected: cloned, edited and pushed to a branch |
| Vercel | Connected (read-only use: project, domains, deployment) |
| Wix | Connected (read-only: found the legacy site still published) |
| Web search | Available (US index, not localized). Used for third-party evidence. |
| Gmail, Google Drive | Connected but **not used**. No outreach or messages were sent. |

As a result, every ranking, SoLV, ARP and competitor metric field is blank and marked **NOT MEASURED**. No numbers were invented.

## 2. Repository changes (this pass)
| File | Change | Why | Risk |
|---|---|---|---|
| `dist/services/index.html` | Spring and Fall cleanup "Learn more" links and ItemList schema now point to `/services/spring-cleanup/` and `/services/fall-cleanup/` instead of `/yard-cleanup-guelph/` | The hub's two seasonal cards pointed to the combined page, so the dedicated pages had almost no internal links. This was flagged as the #1 fix in the Nov 10 report. | Low: href and schema URL only. No title, H1, meta or anchor text changed. |
| `dist/yard-cleanup-guelph/index.html` | Two contextual `link-arrow` links under the Spring and Fall sections | Makes the combined page a hub rather than a competitor for seasonal terms | Low: reuses the existing component |
| `dist/index.html` | Service-area FAQ (visible text and FAQPage schema, kept identical) now includes the Township of Puslinch and Aberfoyle. LocalBusiness `areaServed` gains `Township of Puslinch` (AdministrativeArea) and `Aberfoyle`. | Removes the conflict with the Puslinch cleanup pages; the brief confirms Puslinch is served | Low. Title, H1 and meta unchanged. |
| `dist/sitemap.xml` | lastmod set to 2026-11-25 for the 3 changed URLs | Accurate freshness signal | None |
| `local-seo-reports/` | 15 deliverables (not deployed; outside `dist/`) | Requested | None |

**Validation:**
- All JSON-LD blocks on the changed pages parse.
- The sitemap is valid XML.
- A local server returns 200 for `/`, `/services/`, `/yard-cleanup-guelph/` and both seasonal pages.
- No horizontal overflow at 1366 px or 390 px.
- The new links resolve.

**Not re-run:** the full 60-screenshot pixel comparison from the November pass.

**Rollback:** revert the single commit.

**Deliberately not changed:**
- The "75+ reviews" claim and the 35+ vs 50 lawn count: the true values are unknown, so they need owner input.
- The Maps link: the real profile URL is unknown.
- Analytics: needs an account or ID.
- No dethatching or sod pages: the services aren't confirmed.
- No redesign, nav or title changes.
- The stale root-level HTML copies: not deployed.

## 3. External change manifest (needs your approval; nothing below was done)
| # | Where | Field | Before | After | Risk |
|---|---|---|---|---|---|
| 1 | GBP | Address | *Unknown; Birdeye shows 435 Stone Rd W* | Hidden (service-area only) **if** no staffed location | Short local dip; prevents suspension |
| 2 | GBP | Primary category | *Unknown* | Lawn care service (no change if already set) | Medium |
| 3 | GBP | Secondary categories | *Unknown* | Landscaper, Gardener (+ Property maintenance if offered in picker) | Low |
| 4 | GBP | Description | *Unknown* | Version A in `optimized-business-description.md` | Low |
| 5 | GBP | Services | *Unknown* | ✅ rows in `optimized-service-descriptions.md` | Low |
| 6 | GBP | Service areas | *Unknown* | Guelph, Puslinch, Aberfoyle | Low |
| 7 | GBP | Website URL | *Unknown* | `https://www.yardexguelph.ca/?utm_source=google&utm_medium=organic&utm_campaign=gbp` (**only after analytics is live**) | None |
| 8 | GBP | Quote link | *Unknown* | `https://www.yardexguelph.ca/quote/?utm_source=google&utm_medium=organic&utm_campaign=gbp-quote` | None |
| 9 | GBP | Photos | *Unknown* | Dec 1 batch (`photo-upload-calendar.md`) | None |
| 10 | GBP | Posts | *None known* | Weekly from the CSV, approved in batches | None |
| 11 | Vercel | Env vars | not set | `GOOGLE_PLACES_API_KEY`, `YARDEX_PLACE_ID` | None (Google Cloud billing account needed) |
| 12 | Vercel | Web Analytics | off (no script on site) | Enable, then add the script tag to the pages (repo change) | None; check plan limits |
| 13 | Wix | Legacy site | Published, Premium | Unpublish once confirmed unused | Low |
| 14 | Directories | see `citation-audit.csv` | | | Low |

## 4. Questions only you can answer (they unblock the most work)
1. What is the exact Google review count today, and is there a street address showing on the GBP?
2. Do you offer **dethatching**, **sod installation**, biweekly mowing, groundcover removal? Which shrub-pruning scope?
3. How many weekly lawns: 35+ or 50?
4. Can you connect Local Falcon (and ideally GBP / GSC) to a future session, and what Local Falcon credit budget is OK? The 12-scan baseline is about 900 grid points.
5. Is the Consumer Choice Award (mentioned on the unreleased 2.0 branch) real? If so, send the URL. Otherwise it should be removed from that branch.

## 5. Deliverables index
- `google-business-profile-audit.md`
- `local-falcon-baseline.csv` (scan plan; results blank)
- `google-maps-competitor-analysis.md`
- `keyword-ranking-matrix.csv` (53 keywords, metrics blank)
- `geographic-ranking-analysis.md`
- `recommended-gbp-categories.md`
- `optimized-business-description.md`
- `optimized-service-descriptions.md`
- `review-acquisition-strategy.md`
- `photo-upload-calendar.md`
- `52-week-google-post-calendar.csv`
- `citation-audit.csv`
- `local-backlink-opportunities.csv`
- `90-day-local-seo-roadmap.md`
- `implementation-summary.md`
