# Yardex Guelph — Technical SEO Implementation Audit (July 2026)

## Executive summary
Audited against the full 23-phase technical SEO specification. The overwhelming majority
was already implemented during the migration and architecture projects (July 2026).
This pass verified live behavior and closed the three remaining gaps.

## Verified live (no action needed)
- Domain consolidation: yardexguelph.com (www + apex) 308→ https://www.yardexguelph.ca (verified by live fetch)
- Canonicals: self-referencing absolute .ca URLs, consistent trailing slash, all 28 pages
- robots.txt: allow all + canonical sitemap reference
- sitemap.xml: 28 canonical URLs, lastmod, no redirects/noindex/params
- Old-URL redirects: all 9 Wix-era URLs 301 to closest equivalents (tested live)
- Service architecture: /services/ hub + 9 dedicated pages, crawlable HTML anchors
- Metadata: unique titles/descriptions/OG/Twitter + per-page share images on every page
- Schema: LocalBusiness (areaServed, award, sameAs), Service, BreadcrumbList, FAQPage
  (per-page unique), BlogPosting, ItemList — validated; no self-serving review markup
- Internal links: hub↔services↔blog mesh, breadcrumbs, footer; zero noncanonical refs
- Facts consistent site-wide: 55 reviews, 5-person crew, 50 lawns, est. 2020, $27.50

## Implemented this pass
1. X-Robots-Tag noindex for *.vercel.app hosts (host-conditional header in vercel.json)
   — prevents the Vercel alias domains from being indexed as duplicates
2. "Grass cutting" / "lawn maintenance" synonym coverage on /lawn-mowing-guelph/
   (genuine FAQ, visible + schema in sync) — per spec, synonyms on the authoritative
   page rather than duplicate pages

## Keyword → URL map (primary targets)
lawn care Guelph → / | lawn care services Guelph → /services/ | lawn mowing / grass
cutting / weekly mowing → /lawn-mowing-guelph/ | fertilization → /lawn-fertilizer-guelph/
| aeration + overseeding → /aeration-overseeding-guelph/ | spring/fall/yard cleanup →
/yard-cleanup-guelph/ | mulching → /mulching-guelph/ | weed control →
/weed-control-guelph/ | trimming/edging → /trimming-edging-guelph/ | prices →
/lawn-mowing-prices-guelph/ | vacation → /vacation-yard-care-guelph/

## Not created (requires owner confirmation these services are offered)
/lawn-dethatching-guelph/, /lawn-levelling-guelph/, /garden-bed-installation-guelph/,
standalone /garden-maintenance-guelph/. Creating pages for unoffered services would be
deceptive; confirm and they can be added to the established template in one pass.

## External actions (owner-only, priority order)
1. GSC: verify DOMAIN property for yardexguelph.ca (DNS TXT via Vercel DNS panel);
   also verify yardexguelph.com the same way
2. GSC: submit sitemap; remove any legacy Wix/.com sitemap submissions
3. GSC → URL Inspection → Request indexing: / , /services/ , /lawn-mowing-guelph/ ,
   /lawn-fertilizer-guelph/ , /aeration-overseeding-guelph/ , /yard-cleanup-guelph/ ,
   /lawn-mowing-prices-guelph/ (one pass; do not resubmit unchanged URLs)
4. GSC Change of Address: only applicable FROM the .com property TO .ca if the .com
   was ever indexed as its own site; verify both properties first, redirects (done) are
   the prerequisite
5. Bing Webmaster Tools: import from GSC; submit same sitemap
6. GBP: website field → https://www.yardexguelph.ca/ ; confirm name "Yardex Guelph",
   phone (519) 835-0774, service area Guelph, hours accurate; add quote link
   https://www.yardexguelph.ca/quote/
7. Citations (exact NAP "Yardex Guelph" everywhere): GuelphToday directory, BBB name
   correction, YellowPages.ca, Yelp, Nextdoor, Apple Business Connect, Bing Places;
   ask GuelphToday to update article link to the .ca if it points elsewhere

## Content roadmap (next 12, ranked)
1. Lawn aeration cost in Guelph (commercial, links aeration)
2. Best grass seed for Guelph lawns (Aug, pre-overseeding)
3. Aeration vs dethatching in Ontario (comparison intent)
4. What's included in professional lawn mowing (commercial-support)
5. Lawn care calendar for Guelph/Ontario (evergreen hub, heavy internal links)
6. Common lawn diseases in Ontario (June seasonal)
7. Crabgrass vs quackgrass ID guide (spring)
8. How to repair a thin lawn after summer drought (Sept)
9. Mulch calculator / how much mulch do I need (tool-style, links mulching)
10. First/last mow dates in Guelph (seasonal FAQ traffic)
11. Lawn watering after fertilizer: exact schedule (links fertilizer)
12. Snow mold recovery in spring (Apr)

## Validation (this pass)
Crawl 28 pages / 37 assets: 0 errors · JSON-LD: all valid · redirects: live-tested ·
.com: live-verified 308 → .ca · no internal noncanonical links · build: static, n/a
