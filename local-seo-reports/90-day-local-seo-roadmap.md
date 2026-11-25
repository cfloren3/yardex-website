# 90-day local SEO roadmap (Dec 1, 2026 to Feb 28, 2027)

Winter is the best time for structural changes. Demand is low, so rankings can settle before the April peak.

## Ranked recommendations

Scoring:
- **Impact:** H/M/L
- **Evidence:** E (verified fact) / I (industry consensus) / H (hypothesis)
- **Cost:** $ = free, $$ = small spend
- **Difficulty:** 1–3
- **Ranking risk:** Low/Med/High
- **Horizon:** when results should show

| # | Action | Impact | Evidence | Cost | Diff. | Risk | Horizon | Who |
|---|---|---|---|---|---|---|---|---|
| 1 | **Check the GBP address.** Birdeye shows 435 Stone Rd W. Hide the address if Yardex has no staffed location there. | H (protects everything) | E (Birdeye) / H (GBP) | $ | 1 | Low (short dip) vs High if suspended | Immediate | Owner |
| 2 | **Install analytics** (Vercel Web Analytics, or GA4 with the quote-form submit as a conversion). Without it, UTMs and GBP leads can't be measured. | H | E (no tags on any page) | $–$$ | 1 | None | Immediate | Owner enables; repo snippet after |
| 3 | **Get the true review count; fix "75+" sitewide if wrong**; set the Places key for `/api/reviews` | H (trust, compliance) | E (55/53/38/75 conflict) | $ | 1 | None | Immediate | Owner + repo |
| 4 | **Run the Local Falcon baseline** (12 scans in `local-falcon-baseline.csv`); export 6 months of GBP Insights and 3 months of GSC | H (needed for every target) | n/a | $$ (credits) | 1 | None | Week 1 | Owner/connect tool |
| 5 | **Primary category = Lawn care service** (only if it isn't already); add secondaries | H | I | $ | 1 | Med | 2–6 weeks | Owner (approval) |
| 6 | **Start the review workflow** (templates ready). Ask the 2026 fall-cleanup clients now, while the job is fresh. | H | I | $ | 2 | None | Ongoing | Owner |
| 7 | **GBP services and description** (files ready); link services to pages | M | I | $ | 1 | Low | 2–8 weeks | Owner (approval) |
| 8 | **Replace the Maps search link** with the real profile URL in the footer and schema (`sameAs`, `hasMap`) | M | E | $ | 1 | Low | 2–6 weeks | Owner sends URL → repo |
| 9 | **Fix citations:** Apple, Bing, Facebook (missing), HomeStars, GuelphToday directory, BBB name | M | I | $ | 2 | Low | 1–3 months | Owner |
| 10 | **Fix existing mention links:** GuelphToday article, QBA, BBB, guelphhomeservices | M | E | $ | 1 | None | 1–3 months | Owner (outreach) |
| 11 | **Confirm dethatching and sodding.** If offered, build 2 pages in the existing template and add GBP services before March. | M | E (page gap) | $ | 2 | Low | 2–4 months | Owner confirm → repo |
| 12 | **Consolidate business facts:** lawn count (35+ vs 50); remove the unverifiable Consumer Choice claim from the 2.0 branch | M | E | $ | 1 | None | Immediate | Owner + repo |
| 13 | **Decide on the legacy Wix site** (published on Premium) | L–M | E | saves $ | 1 | Low | 1–2 months | Owner |
| 14 | **Photo uploads** per `photo-upload-calendar.md` | M (conversion) | I | $ | 1 | None | Ongoing | Owner |
| 15 | **Weekly GBP posts** per the CSV (approve in batches of 4) | L–M | I | $ | 1 | None | Ongoing | Owner |
| 16 | **Puslinch:** one genuine Aberfoyle/Puslinch project case study in spring; Puslinch community link | M (for Puslinch) | H | $ | 2 | None | 3–6 months | Owner + repo |
| 17 | **Chamber membership / sponsorship** | L–M | I | $$ | 1 | None | 3–12 months | Owner (budget) |

## Week by week

**Weeks 1–2 (Dec 1–14)**
- Item 1: address check
- Items 2–3: analytics, review count
- Item 4: baselines
- Merge the repo branch `seo/local-maps-2026-11` once reviewed
- Upload 5 existing project photos plus the cover photo

**Weeks 3–4 (Dec 15–28)**
- Item 5: categories (single change, then a 4-week hold on other GBP structure edits)
- Item 7: services and description
- Item 6: send review asks to fall clients

**Weeks 5–8 (Dec 29–Jan 25)**
- Re-scan 4 core keywords (monthly cadence)
- Items 8–10: profile URL, citations, existing links
- Item 12: fact consolidation
- Item 11: confirm services

**Weeks 9–13 (Jan 26–Feb 28)**
- Switch to biweekly scans from February
- Spring-cleanup posts start (CSV)
- Build dethatching/sod pages if confirmed
- Re-check spring pages are indexed in GSC
- Prepare the spring photo shoot list

## Monitoring cadence (Local Falcon, identical settings every time)
| Months | Frequency | Keywords |
|---|---|---|
| Dec–Jan | Monthly | lawn care, lawn mowing, spring cleanup, fall cleanup (Guelph); lawn care Puslinch |
| Feb–Mar | Biweekly | Above plus dethatching, aeration, spring yard cleanup |
| Apr–Oct | Weekly (priority 4), monthly (rest) | Seasonal focus rotates |
| Nov | Biweekly | fall cleanup, leaf removal, lawn care |

Each report compares SoLV, ARP, ATRP and top-3 coverage against the previous scan, and logs what changed in that window: GBP edits, reviews gained, links earned, site deploys. Read that log as **correlation, not proof**.

## Targets (provisional until the baseline exists)
The brief's stretch goals (core SoLV 70–85%, ARP below 3, 150–175 reviews, 40–60 referring domains) are kept as **stretch** figures. Set the committed targets after the first scan at "baseline + X". A realistic review target is the current count + 50 (see `review-acquisition-strategy.md`). Track **qualified quote requests by service and area** as the main business metric. That needs item 2.
