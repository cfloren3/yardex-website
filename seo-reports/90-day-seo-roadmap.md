# Yardex Guelph — 90-Day SEO Roadmap (Dec 2026 – Feb 2027)

Goal: be fully indexed, measured and review-ready **before** spring cleanup searches start (~March). Targets are goals, not guarantees.

## Week 0 — Review and launch (owner + dev)

| # | Task | Owner | Done when |
|---|---|---|---|
| 1 | Review the Vercel **preview** of branch `seo/2027-optimization` (desktop + phone): homepage, /services/, the 5 new pages | Owner | Approved |
| 2 | Confirm: Puslinch service list, "Something else" service, founding year, 35 vs 50 lawns, 2027 prices | Owner | Answers in hand |
| 3 | **Before merging:** export a GSC baseline (Performance → last 3 and 12 months → Queries and Pages CSV; Pages for `/`, `/lawn-mowing-guelph/`, `/services/`, `/yard-cleanup-guelph/`) | Owner | CSVs saved |
| 4 | Merge to `main` (Vercel deploys production) | Owner | Live |
| 5 | Post-deploy checks: `curl -sI https://www.yardexguelph.com/` → 301 to .ca; `/index.html` → 301; 5 new URLs → 200; Rich Results Test on `/` and `/sodding-guelph/` | Dev | All pass |
| 6 | Vercel → Domains → set `www.yardexguelph.com` → redirect to `www.yardexguelph.ca` (belt-and-braces with the vercel.json rule) | Owner | Done |
| 7 | GSC: submit sitemap; URL Inspection → Request indexing for the 5 new URLs + `/` + `/services/` | Owner | Requested |
| 8 | Bing Webmaster Tools: import from GSC, submit sitemap | Owner | Done |

## Weeks 1–2 — Measurement foundations

| # | Task | Why |
|---|---|---|
| 9 | **Install analytics.** Option A: Vercel Web Analytics (cookieless, toggle in dashboard + add `<script defer src="/_vercel/insights/script.js"></script>`; custom events need Vercel Pro). Option B: GA4 with a consent-friendly config (privacy notice; IP not stored by GA4). `assets/v2/track-r1.js` already sends `phone_click`, `text_click`, `email_click`, `quote_button_click`, `quote_form_submit` and `generate_lead` (thank-you page) to whichever is installed. | Today there is **zero** conversion data |
| 10 | GA4 only: mark `generate_lead` as a key event; link GA4 ↔ GSC | Lead attribution by landing page |
| 11 | Add the UTM'd website and quote links to GBP (GBP plan §1) | Separate GBP from organic |
| 12 | **Finish connecting Local Falcon** to Claude and run the core 9×9 / 6 km scan (lawn care, lawn mowing) + Puslinch 7×7 / 10 km. Check credits first. | Maps baseline (ARP/ATRP/SoLV) |
| 13 | Connect GSC (e.g. via the Windsor.ai connector) and Semrush or Ahrefs | Fill the "unverified" columns |
| 14 | Add `GOOGLE_PLACES_API_KEY` + `YARDEX_PLACE_ID` to Vercel env vars | Live review count |

## Weeks 2–6 — Local authority

| # | Task |
|---|---|
| 15 | GBP audit + description + 13 services (GBP plan §1–3) |
| 16 | Citations: ThreeBestRated URL fix, BBB name fix, Bing Places, Apple Business Connect, YellowPages, HomeStars (free) |
| 17 | GuelphToday: link-update request + follow-up pitch |
| 18 | Start the review workflow; target 4–8 genuine reviews/month from spring |
| 19 | Photograph every sod, dethatch and hedge job from the first one (before/during/after) |

## Weeks 4–10 — Content (see content calendar)

| # | Task |
|---|---|
| 20 | Dec: refresh "How often to mow" with real data |
| 21 | Jan: "Lawn care costs in Guelph 2027" — after prices are confirmed |
| 22 | Feb: spring cleanup booking post + refreshed spring checklist; GBP posts start weekly |
| 23 | Update `/lawn-mowing-prices-guelph/` title year "(2026)" → "(2027)" when 2027 prices are final |
| 24 | First case study (deck vines / overgrown bed) using the template |

## Weeks 8–12 — Measure and adjust

| Check | Threshold → action |
|---|---|
| GSC: `/`, `/lawn-mowing-guelph/` position for lawn care / lawn mowing Guelph | Drop > 2 positions sustained 2+ weeks vs baseline → review title change (homepage title is the main ranking-page change); revert via `git revert` if correlated |
| GSC indexing of 5 new pages | Not indexed after 3 weeks → re-request; check for "Crawled – not indexed" (thin-content signal → add photos/case study) |
| GSC: queries landing on the wrong page (e.g. spring cleanup → `/yard-cleanup-guelph/`) | Strengthen internal links/anchors to the intended page |
| Local Falcon: SoLV and top-3 coverage for lawn care | Compare monthly; Maps moves mostly on GBP and reviews, not the site |
| Lighthouse (production, mobile) on `/` | LCP lab > 4 s → next step: self-host fonts |
| Leads (once analytics is live) | Quote submissions per landing page, by month |

## Not before spring

- New neighbourhood pages (need real case studies first).
- Removing or redirecting any existing URL.
- Changing the GBP primary category.
