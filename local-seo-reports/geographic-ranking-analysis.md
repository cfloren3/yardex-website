# Geographic ranking analysis: Guelph and Puslinch

Date: 2026-11-25 · **No grid data**. Local Falcon isn't connected, so no neighbourhood is classified here as top 3, positions 4–10, below 10 or absent. Doing so without scans would be guessing.

What this file provides instead:
1. The scan design.
2. A pre-scan hypothesis map built from proximity.
3. The expansion playbook to apply once real data exists.

## 1. Scan design
- **Guelph:** 9×9 grid, 6 km radius, centred on the GBP pin. Repeat at 10 km for the two core keywords (lawn care, lawn mowing).
- **Puslinch:** the township is large, rural and runs south of Guelph to Hwy 401. A 9×9 grid wastes points on fields and the Puslinch Lake area. Use a **7×7 grid, 8 km radius, centred on Aberfoyle** (Brock Rd / Wellington Rd 46 area), where the homes are concentrated.
- Keep the centre, grid size, radius, time of day and weekday identical on every future scan.

## 2. Hypothesis map (to be replaced by scan data)
Google weighs distance between the searcher and the business heavily, and Yardex is a service-area business with a hidden pin. Birdeye lists 435 Stone Rd W (southwest-central Guelph). **If** the pin is near there:

| Area | Approx. distance from Stone Rd W | Expected starting position | Main competitor pressure (hypothesis) |
|---|---|---|---|
| Old University, Kortright Hills, Hanlon Creek | 0–3 km | Strongest zone | Small mowing crews |
| Westminster Woods, Clairfields, Pine Ridge (south end) | 3–6 km | Mid | A Cut Above (Arkell Rd), Hometurf (Airpark Pl) are closer |
| Downtown, Exhibition Park | 2–4 km | Mid-strong | Manor (Elizabeth St) to the east |
| West Willow Woods | 3–5 km | Mid | West-end crews |
| Grange Hill East, North Guelph | 5–8 km | Weak | Businesses on the north and east sides |
| Aberfoyle / Puslinch | 8–15 km | Weak to absent | Rural and Puslinch-based providers; directories dominate the organic results |

If the pin is somewhere else, for example the owner's home, this table shifts with it. **First task:** confirm the pin location with the owner (GBP → Location).

## 3. Expansion playbook (only legitimate methods)

| Lever | Effect on distant grid points | Notes |
|---|---|---|
| More, steadier reviews | Raises prominence everywhere and stretches the radius where Yardex ranks | The most dependable lever |
| Primary category = Lawn care service | Relevance across the grid | Only if it isn't already set |
| Neighbourhood case studies (a real job, photos, the problem and the fix) on the site | Organic plus relevance; weak direct effect on Maps | One page or blog post per neighbourhood, only for real jobs. No city-swap pages. |
| Local links (news, chamber, partners) | Prominence | See `local-backlink-opportunities.csv` |
| Citations kept consistent | Trust and accuracy | See `citation-audit.csv` |
| GBP service areas | **Doesn't overcome distance**; mainly affects eligibility and display | Add Guelph, Puslinch, Aberfoyle |
| Fake addresses, virtual offices, extra profiles | **Never.** Suspension risk. | Not recommended under any circumstances |

## Realistic expectations
- Expect strong Maps visibility around the pin and diminishing visibility at the edges of the 10 km grid. "70–85% SoLV" across a 10 km grid is unlikely for any single service-area business against long-established competitors. Set targets from the first scan.
- For **Puslinch**, organic pages and directory presence will probably bring more leads than Maps does. Measure quote requests from Puslinch addresses rather than relying only on grid percentages.
