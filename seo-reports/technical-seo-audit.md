# Yardex Guelph — Technical SEO Audit (November 2026)

Branch `seo/2027-optimization` · baseline tag `baseline/pre-seo-2027` (`0c99ed8`).
Status: ✅ fixed in repo · 🟡 needs owner/dashboard action · ⚪ verified OK, no change.

## 1. Domain consolidation

| Check | Result | Status |
|---|---|---|
| Preferred host | `https://www.yardexguelph.ca/` (canonicals, sitemap, internal links all use it) | ⚪ |
| `yardexguelph.ca` → www | 308 (Vercel domain redirect) | ⚪ |
| HTTP → HTTPS | 308; HSTS `max-age=63072000; includeSubDomains; preload` | ⚪ |
| `yardexguelph.com` (apex) | Vercel config: 308 → `www.yardexguelph.ca` | ⚪ |
| **`www.yardexguelph.com`** | **Vercel config: attached to the project with no redirect → serves a full duplicate of the site.** Canonicals point to .ca, which limits damage, but it splits link signals (ThreeBestRated links to `.com`). | ✅ repo fix: host-conditional 301 in `vercel.json`. 🟡 Better: set the redirect in Vercel → Domains → `www.yardexguelph.com` → Redirect to `www.yardexguelph.ca` (308). Either works; the dashboard fix applies even if `vercel.json` is edited later. |
| `*.vercel.app` | `X-Robots-Tag: noindex, nofollow` (host-conditional header) | ⚪ |
| `/index.html` | Was HTTP 200 (duplicate of `/`) | ✅ 301 → `/` in `vercel.json` |
| Two-hop redirects | `http://yardexguelph.ca` → https apex → www (2 hops); `/post/...` → add slash → target (2 hops) | ⚪ Acceptable; Google follows up to 10 hops. |

Couldn't be verified live from this sandbox (proxy blocks `.com` and `vercel.app`): check after merging with
```bash
curl -sI https://www.yardexguelph.com/about/ | grep -i -E "^HTTP|^location"
```
Expected: `301` + `location: https://www.yardexguelph.ca/about/`.

## 2. Crawlability and indexing

| Check | Result |
|---|---|
| robots.txt | `Allow: /` + sitemap reference ⚪ |
| Sitemap | Rebuilt from the pages themselves: 35 URLs (30 → 35), only self-canonical, non-noindex pages; `lastmod` reflects real changes. Valid XML. ✅ |
| Noindex | `/thank-you/`, `/404.html` — correct ⚪ |
| Status codes | All 37 HTML files resolve locally; unknown URLs return 404 ⚪ |
| Orphans | Before: `/services/spring-cleanup/` and `/services/fall-cleanup/` had 2 inbound links (each other). After: linked from nav-level hub cards, the homepage, the yard-cleanup page, blog posts and the new pages ✅ |
| Rendering | Fully static; no client-rendered content ⚪ |
| Broken internal links/assets | 0 before, 0 after (automated crawl of every `href`/`src`) ✅ |

## 3. Metadata

- Unique title, description and H1 on every page — 0 duplicates (automated check) ✅
- Homepage title 611 px → **564 px**: `Lawn Care Guelph | No Contracts, 75+ 5-Star Reviews | Yardex` ✅
  - Why not the brief's proposal (`Lawn Care Guelph | 75+ 5-Star Reviews | Yardex`, 436 px)? It drops "No Contracts", the main differentiator in the current title and likely part of its CTR. The chosen title keeps the keyword first, the review proof and the hook, and fits.
- 13 more titles over ~580 px shortened (11 blog/utility, plus weed control and trimming & edging). Title tag, `og:title` and `twitter:title` updated together; **H1s and URLs unchanged** ✅
- Titles left slightly over (590–601 px) **on purpose** — protected ranking pages: `/lawn-mowing-guelph/` (592), `/lawn-mowing-prices-guelph/` (601), `/aeration-overseeding-guelph/` (596), `/blog/how-often-mow-lawn-guelph/` (599). The truncation risk is cosmetic; rewriting a ranking title without GSC CTR data is the bigger risk.
- Canonical, OG and Twitter, `en-CA` and `og:locale en_CA` on all pages, including the 5 new ones ✅
- `"highest-rated"` removed from homepage H1, description and OG/Twitter image alt (unsubstantiated) ✅

## 4. Image SEO and accessibility

- The "10 missing alts" were 10 **empty** alts (2 logo marks, 8 `aria-hidden` work-reel duplicates). Now descriptive. `aria-hidden` kept, so screen-reader output is unchanged ✅
- Logo mark sitewide: `alt="Yardex Guelph logo"` (inside a link that already has an accessible name; kept `aria-hidden`) ✅
- Related-service cards keep `alt=""` deliberately: each card has a visible text label in the same link, so an alt would make screen readers read the name twice. Seobility may still count these on service pages; that's the correct trade-off.
- All new images have `width`/`height` (no CLS), `loading="lazy"` below the fold, and the hero is preloaded ✅
- New responsive assets: `hero` 960 px WebP for phones, slide WebPs, three 560 px card WebPs, three 1200×630 OG images ✅
- In-text GuelphToday links (homepage story, awards card, sitewide footer badge) now underlined (Lighthouse `link-in-text-block`; homepage a11y 93 → 96) ✅

## 5. Structured data

| Page(s) | Types | Change |
|---|---|---|
| `/` | LocalBusiness (`@id …/#business`), WebSite, FAQPage | Description lists all services; `areaServed` + Township of Puslinch; new `hasOfferCatalog` (13 services with URLs); FAQ answer on service area updated **in both visible text and schema** ✅ |
| Service pages | Service, BreadcrumbList, FAQPage | Breadcrumb "Services" item now `/services/` (was `/#services`) ✅ |
| New pages (5) | Service (`provider` → `#business`), BreadcrumbList, FAQPage | New; FAQ schema generated from the same list as the visible FAQ ✅ |
| `/services/` | ItemList, BreadcrumbList, FAQPage | Spring/Fall items point to the dedicated pages; 5 new items ✅ |

Validation: all JSON-LD parses (automated, every page). Visible FAQ ↔ FAQPage schema parity: 0 mismatches (automated). Google Rich Results Test and validator.schema.org **[UNVERIFIED]** — not reachable here; run them on the preview URL.

Deliberately **not** added: `AggregateRating`/`Review` (self-serving review markup isn't eligible and the brief forbids it), street address/geo (no public storefront; ThreeBestRated shows a Stone Rd W address that should not be repeated without owner confirmation), opening hours (not provided), `Offer` prices for new services (no verified prices).

Note: Google shows FAQ rich results only for authoritative government and health sites since 2023. FAQPage markup here is for clarity and AI/answer-engine parsing, not an expected SERP feature.

## 6. Internal linking

- Nav dropdown and footer list all 12 services; footer adds "Lawn Care in Puslinch" ✅
- Homepage: new supporting paragraph with 9 contextual links (mowing, spring, fall, aeration/overseeding, dethatching, fertilizing, sodding, Puslinch) ✅
- "Learn more" ×16 → visually identical but with screen-reader/crawler text ("Learn more about lawn mowing", etc.) ✅
- Clusters implemented: spring cleanup → dethatching, aeration, mulching, garden maintenance · dethatching ↔ aeration, spring cleanup, sodding · aeration → dethatching, sodding · fall cleanup → hedge trimming, garden maintenance, fall aeration · yard cleanup → spring, fall, dethatching, garden maintenance · sodding → mowing, aeration, fertilizer · garden maintenance → weed control, mulching, hedge · trimming & edging → hedge trimming · 4 blog posts → commercial pages · Puslinch → cleanups, mowing, aeration, hedge, garden ✅

## 7. Server and console hygiene

- `/api/reviews` returned 500 on every page view (Places API not configured) → console error on all pages (Lighthouse Best Practices). Now returns 200 with `{count:null}`; `main.js` already ignores nulls ✅. 🟡 To show the live count: add `GOOGLE_PLACES_API_KEY` and `YARDEX_PLACE_ID` in Vercel → Settings → Environment Variables.
- Security headers present (HSTS, nosniff, frame-options, referrer-policy, permissions-policy) ⚪

## 8. Known remaining issues

1. `color-contrast` on `.btn--gold` text in some contexts (Lighthouse a11y) — part of the brand palette; changing it is a visual change and needs owner sign-off.
2. `target-size` on the homepage scroll-cue arrow (small tap target) — visual change; left.
3. Google Fonts CSS is render-blocking (~1.5 s in mobile lab tests). Self-hosting the two fonts with preload would remove a third-party round trip; deferred because font-swap behaviour changes first paint.
4. Large noise-dense lawn photos (300–540 KB JPEG) on the homepage below the fold; WebP versions exist for most and the `<picture>`/`srcset` work could continue.
5. Root-level stale HTML copies in the repo (not deployed) — consider deleting to avoid confusion.
6. "50 weekly lawns" (footer) vs "35+ lawns" (About meta) inconsistency.
