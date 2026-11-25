# Google Maps competitor analysis

Date: 2026-11-25

## Limits on the evidence
No Local Falcon, Maps, Places, Ahrefs or Semrush access was available. Competitor websites and Maps were blocked by the network policy. Everything below comes from **web-search result snippets** (US index, not localized to Guelph). For each item:
- **[E]** = evidence from a named third-party source
- **[H]** = hypothesis

No SoLV, ARP, ranking, review velocity or backlink numbers are claimed for any competitor. Those columns stay empty until a Local Falcon scan runs.

## Competitors in the brief

| Competitor | What was found | Evidence | Threat to Yardex (hypothesis) |
|---|---|---|---|
| Leaf It Alone | **Not found** in any search result | none | Unknown. Confirm the exact GBP name in a Maps scan. |
| A Cut Above Yard Services | BBB entry at **403 Arkell Rd, Guelph** (south end), (519) 731-5274, BBB rating A, not accredited. Has a combined "Yard Cleanup Guelph: Spring & Fall Cleanups, Leaf Removal" page. | [E] BBB snippet; Nov 2026 cleanup report | **High in South Guelph** (Arkell Rd is close to Westminster Woods and Clairfields) for cleanup and leaf-removal terms. |
| Cutting Edge Property Services | HomeStars profile (N1H, west/central Guelph): **1.8/10 from 5 reviews**. Lists Puslinch among its service areas. | [E] HomeStars snippet | Low on reputation; possibly ranks on proximity or longevity. |
| CH Lawn Care | **Not found** | none | Unknown |
| Manor Landscaping & Property Maintenance | 412 Elizabeth St, Guelph (east-central). **4.7★ / 117 reviews** (a directory citing Google). Founded 1986, focus on commercial property maintenance. | [E] ThreeBestRated / directory snippet | **High for "landscaping" and "property maintenance"**: age, review volume and central location. |
| Weed Man (Guelph) | Franchise with a Guelph page. Fertilization, aeration and weed control. | [E] weedman.com | **High for fertilization and aeration.** Franchise authority, but does not mow. |
| Gelderman | Guelph branch (acquired Outdoor Services in 2014); HQ in Waterdown. Landscape maintenance and construction, mostly commercial. | [E] Landscape Ontario / job posts | Medium for "landscaping"; low for residential mowing. |

## Other competitors that came up
| Business | Finding | Evidence |
|---|---|---|
| Hometurf Lawn Care | Airpark Pl, Guelph. Birdeye 4.6★ / 959 reviews; a Google listing cited at 727. | [E] Birdeye / HomeStars snippets |
| Kendall Lawn Care | Family-owned in Guelph since 1966. Weed control, fertilization, aeration. | [E] search snippet |
| PropertyWerks | Guelph pages since 2008; fertilizer and weed control, plus a detailed fall cleanup scope | [E] propertywerks.ca |
| Nutrilawn (Guelph) | Dedicated dethatching service | [E] nutrilawn.com |
| Jamie's Lawn Care | HomeStars 97% / 121 reviews | [E] HomeStars |
| Hayden's Property Maintenance | Dedicated "Fall Yard Clean Up Guelph" page | [E] Nov 2026 report |
| Riverwood Landscape, Maintenance Moose | On ThreeBestRated's Guelph lawn-care list | [E] ThreeBestRated |

## Why competitors may outrank Yardex (evidence vs hypothesis)

| Factor | Yardex | Competitor pattern | Strength of evidence |
|---|---|---|---|
| Review volume | Site claims 75+; not verified (55 and 53 also quoted) | Hometurf about 700–960; Manor 117 | **[E] for competitors, unverified for Yardex.** A large gap against fertilization brands; comparable to small mowing crews. |
| Business age | Founded 2020 | Manor 1986, Kendall 1966, PropertyWerks 2008 | [E]. Age matters through accumulated reviews and links, not directly. |
| Location/proximity | Service-area business; the hidden pin location is unknown; Birdeye shows 435 Stone Rd W (southwest-central) | Arkell Rd (south), Elizabeth St (east), Airpark Pl (south) | [H]. The pin location decides the strong zone. |
| Website relevance | Strong: 30 pages, a dedicated page per service, schema, blog | Mixed; many competitors have one combined page | [E] Yardex likely leads here. |
| Backlinks | Seobility (brief): 7 referring domains | Unknown | [E] for Yardex (not re-verified), unknown for others |
| Primary category | Unknown | Unknown | **Must collect** |
| Fertilizer/aeration specialists | Yardex offers both | Weed Man, Nutrilawn, Hometurf and Kendall specialize | [H] Hard to beat on "fertilization"/"aeration" Maps terms without much higher review velocity. Organic pages are the better battleground. |

## Gap matrix by service (what Yardex needs; competitor data still to collect)

| Service | Yardex website page | GBP service | Likely Maps leaders (hypothesis) | Biggest gap for Yardex |
|---|---|---|---|---|
| Lawn care / mowing | ✅ strong | ? | Small mowing crews plus Manor | Reviews + photo velocity; confirm primary category |
| Spring/fall cleanup, leaf removal | ✅ dedicated pages (now linked from hub) | ? | A Cut Above (south), Manor | Seasonal posts, cleanup-specific reviews, before/after photos |
| Aeration/overseeding | ✅ | ? | Weed Man, Hometurf, Kendall, Nutrilawn | Review volume; specialists dominate |
| Fertilization | ✅ | ? | Same as above | Same; lower priority for Maps |
| Dethatching | ❌ | ? | Nutrilawn | Confirm offered → page + GBP service |
| Sodding | ❌ | ? | Landscapers | Confirm offered → page + project photos |
| Landscaping / property maintenance | Partial (/services/) | ? | Manor, Gelderman, Landscaper-category businesses | Secondary category + project case studies |
| Puslinch (all) | Cleanup pages only | ? | Cutting Edge and others listing Puslinch; directory sites dominate the organic results | Distance from the pin; case studies, local links |

## To finish this analysis (first Local Falcon session)
1. Run the 12 baseline scans in `local-falcon-baseline.csv` (about 900 grid points, so check credit cost first).
2. For each keyword, export the competitor report: SoLV, ARP, review count and rating, and primary category.
3. Fill the empty columns in `keyword-ranking-matrix.csv` and replace every [H] above with data.
