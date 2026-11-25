# Yardex Guelph — Service Page Strategy

Rule used for every decision: **one page per distinct search intent, only for services the owner confirmed (2026-11-25)**, preserving every URL that may hold ranking history.

## Final architecture

| Service | Primary keyword | URL | Status | Decision |
|---|---|---|---|---|
| Lawn care (core) | lawn care Guelph | `/` | Protected | Homepage stays the lawn-care page; metadata tightened, supporting copy added |
| Lawn mowing | lawn mowing Guelph | `/lawn-mowing-guelph/` | **Protected — unchanged content** | Only sitewide nav/footer, breadcrumb and sidebar links changed |
| Mowing prices | lawn mowing prices Guelph | `/lawn-mowing-prices-guelph/` | Protected | Update "(2026)" → "(2027)" in Feb **only once 2027 prices are confirmed** |
| Spring cleanup | spring cleanup Guelph | `/services/spring-cleanup/` | Existing (Nov 2026) | Now linked from hub, homepage, yard-cleanup, blog |
| Fall cleanup + leaf removal | fall cleanup Guelph, leaf removal Guelph | `/services/fall-cleanup/` | Existing | **Leaf removal stays here.** The page already has a dedicated H2 ("Leaf removal that actually finishes the job"), and a separate leaf page would split one seasonal intent across two thin pages. Revisit if GSC shows leaf queries ranking poorly. |
| Property / yard cleanup | property cleanup Guelph, yard cleanup Guelph | `/yard-cleanup-guelph/` | Protected | Kept as the generic/combined hub; links out to both seasonal pages so it no longer competes with them |
| Dethatching | dethatching Guelph, power raking | `/dethatching-guelph/` | **New** | Distinct intent (thatch) from aeration (compaction); cross-linked |
| Aeration + overseeding | lawn aeration Guelph, overseeding Guelph | `/aeration-overseeding-guelph/` | Protected | Owns overseeding; links to dethatching and sodding |
| Fertilization | lawn fertilization Guelph | `/lawn-fertilizer-guelph/` | Protected | Title "Fertilizing & Overseeding" kept; overlap with aeration is acceptable (different primary intent) |
| Lawn restoration / renovation | lawn restoration Guelph | — | No new page | Covered by the aeration → dethatching → sodding cluster; a separate "restoration" page would cannibalize all three |
| Sodding | sodding Guelph, sod installation | `/sodding-guelph/` | **New** | |
| Mulching | mulching Guelph | `/mulching-guelph/` | Protected | Links to garden maintenance |
| Garden maintenance | garden maintenance Guelph, garden weeding, groundcover removal, branch removal | `/garden-maintenance-guelph/` | **New** | Uses genuine before/after photos |
| Weed control | weed control Guelph | `/weed-control-guelph/` | Protected | Title shortened; keeps the pesticide-free/lawn intent |
| Hedge trimming | hedge trimming Guelph, bush trimming, shrub pruning | `/hedge-trimming-guelph/` | **New** | `/trimming-edging-guelph/` title changed "Hedges, Walkways & Beds" → "Lawn Edging & Walkways" and links here |
| Lawn edging | lawn edging Guelph | `/trimming-edging-guelph/` | Protected | |
| Vacation lawn care | vacation lawn care Guelph | `/vacation-yard-care-guelph/` | Protected | |
| Puslinch | lawn care Puslinch, Aberfoyle | `/lawn-care-puslinch/` | **New** | Honest "selected services, availability confirmed per address" positioning, per owner |

URL convention: new pages follow the established `/{service}-guelph/` pattern that the ranking pages use, not the newer `/services/{x}/` pattern, so the strongest pages share one structure.

## What every new page contains

Unique title (<580 px) and description · descriptive H1 · intro answering what/why · "The service" checklist · local know-how (Guelph clay, bylaw, timing, Ontario pesticide rules, Puslinch septic/wells) · **pricing factors** (no invented prices) · 5–6 FAQs (visible + schema) · sidebar quote card · related-service cards · blog link · CTA band · Service + BreadcrumbList + FAQPage JSON-LD · OG/Twitter image.

All built from existing components (`hero--sub`, `svc-intro`, `grid-2`, `checklist`, `prose`, `svc-more`, `faq`, `svc-aside`, `svc-related-grid`, `cta-band`, `grid-3`/`card`). No new CSS, fonts or libraries.

## Photography — honest status

| Page | Photos used | Gap |
|---|---|---|
| Garden maintenance | Genuine before/after sets (overgrown bed, deck vines) + mulched beds | — |
| Hedge & shrub trimming | Genuine photos with cedars and shrub borders (not trimming-in-progress) | **Need:** before/after of a hedge trim |
| Sodding | Genuine Yardex lawn photos, captioned as lawns — **not** presented as sod jobs | **Need:** a real sod install (before, during, after) |
| Dethatching | Genuine Yardex lawn photos, captioned neutrally | **Need:** dethatching in progress and the pulled-up thatch pile |
| Puslinch | Genuine large-property photo; location not claimed | **Need:** a Puslinch property (with permission, no house number) |

Replacing these with real project photos is the single best upgrade for the new pages, and the source for GBP posts and case studies.

## Pricing

The owner provided no prices for sodding, dethatching, hedge trimming or garden maintenance, so pages list pricing factors and promise a firm quote. If you're comfortable publishing "from" prices, add them to the "What affects the price" section and as an `Offer` in that page's Service schema.

## Owner follow-ups

1. Confirm which services are offered in Puslinch (the brief's answer was "limited"). Update the Puslinch list if any listed service is **not** available there.
2. You selected "Something else" in the service question without naming it. Tell me and it gets a page or a mention.
3. Supply project photos (table above).
