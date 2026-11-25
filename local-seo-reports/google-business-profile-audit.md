# Google Business Profile audit: Yardex Guelph

Date: 2026-11-25 · Status: **partial**. There is no access to the Google Business Profile in this session.

## What could and could not be audited

| Source | Available? | What it gave |
|---|---|---|
| Google Business Profile (API or manager access) | **No** | Nothing. No categories, services, hours, photos, posts, insights or reviews were read. |
| Google Places API | **No** | `/api/reviews` exists in the repo but returns `{"error":"not configured"}`: `GOOGLE_PLACES_API_KEY` and `YARDEX_PLACE_ID` are not set in Vercel. |
| Google Maps (browser) | **No** | The network policy blocks google.com/maps. |
| Local Falcon, BrightLocal | **No** | Not connected. |
| Website (yardexguelph.ca) | Yes | Full crawl of 30 pages, plus the repo. |
| Web search (US index, not localized) | Yes | Snippets about third-party listings. |

Every GBP field below is therefore marked **NOT VERIFIED** unless it can be inferred from a third-party source. Nothing here is invented. The checklist at the end is what the owner, or a future session with GBP access, needs to fill in.

## Findings, ranked by risk and impact

### 1. Possible address problem (highest risk) [HYPOTHESIS, verify first]
- Birdeye's profile for "Yardex Guelph" lists **435 Stone Rd W, Guelph**, which is the Stone Road Mall address. Birdeye profiles usually sync from the GBP.
- The website and schema present Yardex as a **service-area business with no street address** (`addressLocality: Guelph` only).
- If the GBP shows a street address where Yardex has no staffed location open to customers during stated hours, Google treats it as ineligible. That is a common cause of suspension for home-service businesses.
- **Action (owner, before any other GBP edit):** open the GBP → Business information → Location.
  - If an address is shown and customers can't visit it, **clear the business address and keep only service areas**.
  - If 435 Stone Rd W is a genuine staffed location, record why. Then make the website consistent with it.
- Expect a short ranking dip in some grid areas after removing an address. A suspension costs far more.

### 2. No link from the website to the actual profile [VERIFIED]
- 88 links and the `sameAs` in the LocalBusiness schema point to `https://www.google.com/maps?q=Yardex+Guelph`. That is a **search**, not the profile, so it can show competitors and gives Google no explicit entity link.
- **Action:** the owner sends the profile's share link (`maps.app.goo.gl/...`) or CID URL. Then swap it into the footer, `/reviews/` and `sameAs`, and add a `hasMap` property. This is a one-line repo change per template and is ready to do once the URL is supplied.

### 3. Review count is unverified and published inconsistently [VERIFIED inconsistency]
- The site says "75+ five-star Google reviews" in 90+ places, and the homepage title includes "75+ Five-Star Reviews".
- The July 2026 technical audit in this repo recorded **55**. A third-party comparison page (guelphhomeservices.ca) quotes **53**. Birdeye shows about **38 at 5.0**, which may cover only part of the total.
- If the real Google count is below 75, the site is overstating it. That is a trust and consumer-protection risk, not only an SEO one.
- **Action:** owner reads the live count from GBP. Update the site to the true figure, rounded down, and set the Places API key so `/api/reviews` keeps it current automatically.

### 4. Business facts that conflict [VERIFIED]
| Fact | Where | Value |
|---|---|---|
| Weekly lawns | footer (32 pages), homepage | 50 |
| Weekly lawns | `/about/` (3 places) | 35+ |
| Service area | homepage FAQ (before this pass) | "All residential Guelph" only |
| Service area | `/services/fall-cleanup/`, `/services/spring-cleanup/` | Guelph **and Puslinch** |

The homepage FAQ and LocalBusiness `areaServed` now include Puslinch (this pass). The brief confirms Puslinch is served. Owner still needs to pick the true lawn count.

### 5. Analytics: none installed [VERIFIED]
No GA4, GTM, Vercel Analytics or other tag on any of the 30 pages. GBP-referred traffic and quote conversions **cannot currently be measured**, so UTM links on the GBP would be collected by nothing. See `implementation-summary.md`.

### 6. Legacy Wix site still published [VERIFIED via Wix API]
`yardexguelph.wixsite.com/yardex-guelph` is published on a Premium plan. If it still has crawlable content, it's a second website for the same business. Confirm the GBP website field is the `.ca` and not the Wix URL. Then consider unpublishing (owner decision).

## Field-by-field checklist (owner or a future session with GBP access)

| Field | Current | Recommended | Ranking factor? |
|---|---|---|---|
| Business name | NOT VERIFIED | "Yardex Guelph" exactly as signage, invoices and site show it. **No keywords added.** | Yes (but keyword-stuffing risks suspension) |
| Primary category | NOT VERIFIED | Lawn care service (see `recommended-gbp-categories.md`) | **Yes, strongest controllable factor** |
| Secondary categories | NOT VERIFIED | See categories file | Yes |
| Description | NOT VERIFIED | `optimized-business-description.md` | Weak/indirect; helps conversion |
| Services | NOT VERIFIED | `optimized-service-descriptions.md` | Indirect (relevance + conversion) |
| Service areas | NOT VERIFIED | Guelph; Puslinch; Aberfoyle (max 20). Doesn't override distance. | Minimal direct effect |
| Address | **Possible issue (Finding 1)** | Hidden, if no staffed storefront | Eligibility |
| Hours | NOT VERIFIED | Real response hours. Add seasonal (winter) hours if they change. | Open-at-search-time is a minor factor |
| Phone | Site: (519) 835-0774 | Match exactly | Consistency |
| Website | NOT VERIFIED | `https://www.yardexguelph.ca/?utm_source=google&utm_medium=organic&utm_campaign=gbp` (once analytics exists) | Indirect |
| Appointment/quote link | NOT VERIFIED | `https://www.yardexguelph.ca/quote/?utm_source=google&utm_medium=organic&utm_campaign=gbp-quote` | Conversion |
| Social links | NOT VERIFIED | Instagram yardex_guelph; add Facebook when created | None |
| Attributes | NOT VERIFIED | Online estimates; only true identity attributes | None/conversion |
| Photos/videos | NOT VERIFIED | `photo-upload-calendar.md` | Indirect (engagement) |
| Posts | NOT VERIFIED | `52-week-google-post-calendar.csv` | Indirect |
| Reviews: count, rating, velocity, response rate | NOT VERIFIED | `review-acquisition-strategy.md` | **Yes (prominence)** |
| Duplicates | NOT VERIFIED | Search Maps for "Yardex" and the phone number; merge or remove any duplicate | Yes |
| Verification status | NOT VERIFIED | Must be verified | Eligibility |
| Insights (searches, calls, website clicks) | NOT VERIFIED | Export 6 months before making changes, as the baseline | n/a |

## How this compares to competitors
A field-by-field comparison needs GBP data for both sides, so it isn't possible this session. Competitor evidence that could be gathered is in `google-maps-competitor-analysis.md`.
