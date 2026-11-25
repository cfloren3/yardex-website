# Yardex Guelph — 12-Month Content Calendar (Dec 2026 – Nov 2027)

**Existing content audit (11 posts):** all Guelph-specific, 290–480 words, published 2026-07-15. Topics: choosing a company, aeration tests, fall checklist, patchy lawn, watering bylaw, mowing frequency, summer watering, spring checklist, fertilizer timing, first mow, 3-inch mowing. **Overlaps to avoid:** "Ontario mowing frequency" = existing `/blog/how-often-mow-lawn-guelph/` → **update it, don't write a new post**. "Fertilization timing" = `/blog/when-to-fertilize-lawn-ontario/` → update. Posts are short; expanding the best three with original photos and Yardex experience beats adding thin new posts.

**Publishing rule:** publish 6–10 weeks **before** the season's search peak. Every post links to one commercial page (listed) and gets one GBP post.

**Verification rule:** each post that states a municipal rule, schedule or price must cite the source and date checked (City of Guelph, County of Wellington, OMAFRA/University of Guelph turf resources). Prices must be Yardex's own, confirmed by the owner. No AI-generic filler: every post needs at least one thing only Yardex knows (a job photo, a measurement, a mistake seen on Guelph lawns).

| Publish | Title (working) | Type | Target query | Links to | Original input needed | Verify |
|---|---|---|---|---|---|---|
| Dec 2026 | **Update:** How Often Should You Mow in Guelph? | Refresh | Ontario mowing frequency | /lawn-mowing-guelph/ | Your actual cut-frequency data by month | — |
| Jan 2027 | What Lawn Care Costs in Guelph in 2027 | New | lawn care cost Guelph | /lawn-mowing-prices-guelph/ | **Confirmed 2027 prices** and real price ranges by lot size | Prices (owner) |
| Feb 2027 | Spring Cleanup in Guelph: When to Book and What's Included | New | spring cleanup timing | /services/spring-cleanup/ | Photos from 2026 cleanups; typical first dates | — |
| Feb 2027 | **Update:** Ontario Spring Lawn Care Checklist | Refresh | spring lawn care checklist Ontario | /services/spring-cleanup/, /dethatching-guelph/ | Add dethatch/aerate decision step | — |
| Mar 2027 | Dethatching vs Aeration: Which Does Your Guelph Lawn Need? | New | dethatching vs aeration | /dethatching-guelph/, /aeration-overseeding-guelph/ | Photo of a thatch wedge vs a compacted core from a real lawn | Horticulture (U of G turf, OMAFRA) |
| Apr 2027 | How Much Does Sod Installation Cost in Guelph? | New | sod installation cost | /sodding-guelph/ | Real quote ranges per sq ft (owner) | Prices (owner) |
| Apr 2027 | Sod vs Overseeding: Which Fixes Your Lawn? | New | sod vs overseeding | /sodding-guelph/, /aeration-overseeding-guelph/ | Before/after of one of each | — |
| May 2027 | How Much Mulch Do You Need (and What It Costs in Guelph) | New | mulch installation cost | /mulching-guelph/ | Yard-to-sq-ft table; real job examples | Prices (owner) |
| Jun 2027 | Restoring an Overgrown Backyard: A Real Guelph Example | Case study | restore overgrown backyard | /garden-maintenance-guelph/ | The deck-vines / overgrown-bed job written up | Customer permission |
| Jul 2027 | **Update:** Guelph Outside Water Use Bylaw (2027 levels) | Refresh | Guelph watering bylaw | /lawn-mowing-guelph/ | — | City of Guelph current program |
| Aug 2027 | When to Overseed and Fertilize in Guelph (Fall Is Best) | New/merge | overseeding timing Ontario | /aeration-overseeding-guelph/, /lawn-fertilizer-guelph/ | Fall job photos | U of G / OMAFRA |
| Aug 2027 | Lawn Care for Larger Puslinch Properties | New | lawn care Puslinch | /lawn-care-puslinch/ | **Only after** confirming Puslinch services; a real Puslinch job | County of Wellington waste info |
| Sep 2027 | What a Fall Cleanup Costs in Guelph (2027) | New | fall cleanup cost | /services/fall-cleanup/ | Real price ranges | Prices (owner) |
| Oct 2027 | City Leaf Collection vs Professional Leaf Removal in Guelph | New | Guelph leaf collection | /services/fall-cleanup/ | — | **City of Guelph yard-waste schedule for 2027** |
| Oct 2027 | When to Do the Final Mow Before Winter in Guelph | New | last mow of the season | /lawn-mowing-guelph/ | Your 2026 final-cut dates | — |
| Nov 2027 | Hedge Trimming Calendar for Guelph: What to Cut When | New | when to trim cedar hedges | /hedge-trimming-guelph/ | Before/after hedge photos | Nesting guidance (Environment and Climate Change Canada) |

## Case study template (copy for each project)

```
Title: [Service] in [Neighbourhood], Guelph — [one-line result]
URL: /projects/[service]-[neighbourhood]-[month-year]/   (or a section on the service page until there are 5+)

Location: [Neighbourhood or street area only — never a house number]
Property: [front / back / both, approx. size, notable features: slope, clay, trees]
Starting condition: [what we found — 2–3 sentences + BEFORE photo]
Customer's goal: [in their words, with permission]
Work performed: [checklist of what was actually done, equipment used, time on site]
Challenges: [e.g. wet spring, buried edging, goutweed runners — and how we handled them]
Result: [AFTER photo(s) from the same angle; follow-up photo after 2–6 weeks if possible]
Related services: [links]
Quote CTA: "Have a yard like this? Send your address for a free quote."
Consent: [customer approved photos and text on YYYY-MM-DD]
```
Schema: `Article` with `about` → the service's `Service` `@id`, and `ImageObject` for each before/after.

## Neighbourhood content (geographic expansion)

The brief lists Westminster Woods, South Guelph, Kortright Hills, Pine Ridge, Clairfields, Exhibition Park, Old University, Grange Hill East, West Willow Woods, Puslinch and Aberfoyle. **No neighbourhood pages were created** — there are no genuine completed-project write-ups per neighbourhood yet, and near-identical city-swap pages are doorway pages. Instead:
1. Write case studies (above) as jobs happen, naming the neighbourhood.
2. Once a neighbourhood has 3+ real case studies with photos, consider a neighbourhood hub that links them, with genuinely local detail.
3. Neighbourhoods stay in the homepage `LocalBusiness` `areaServed` schema (unchanged).
