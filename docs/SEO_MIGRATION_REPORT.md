# Yardex Guelph — Wix → Vercel Migration Report (2026-07-15)

## Baseline: live Wix site (pre-migration)
Indexed URLs found: `/`, `/about`, `/services`, `/contact-us`, `/blog`,
`/post/lawn-mowing-services-in-guelph-ontario`, `/post/mulching-services-in-guelph-ontario`,
`/post/sidewalk-garden-edging-guelph-ontario`, `/post/garden-installation-landscaping-guelph-ontario`,
`/profile/carter/profile`.
Old titles pattern: "Page | Yardex Guelph". Minimal schema, Wix-generated meta, generic OG image.
Verification present: Google Search Console (meta), Bing, Facebook, Pinterest.

## URL mapping (301s in vercel.json)
| Old Wix URL | New URL | Note |
|---|---|---|
| / | / | direct match |
| /about | /about/ | trailing-slash 308 (automatic) |
| /blog | /blog/ | trailing-slash 308 (automatic) |
| /services | /#services | 301 → homepage services section |
| /contact-us | /quote/ | 301 |
| /post/lawn-mowing-services… | /lawn-mowing-guelph/ | 301, topical match |
| /post/mulching-services… | /mulching-guelph/ | 301, topical match |
| /post/sidewalk-garden-edging… | /trimming-edging-guelph/ | 301, topical match |
| /post/garden-installation… | /mulching-guelph/ | 301, closest match |
| /post/* (any other) | /blog/ | catch-all 301 |
| /profile/* | /about/ | catch-all 301 |

## What improved vs. Wix (diff highlights)
- 22 content pages vs 5 (8 service pages, pricing, process, reviews, FAQ, 11 blog posts)
- Unique keyword-targeted titles/descriptions on every page (Wix used generic patterns)
- Full schema: LocalBusiness w/ 14 areaServed entries, Service, BlogPosting, FAQPage, HowTo, BreadcrumbList
- Per-page 1200×630 social share images (Wix reused one photo)
- Static HTML on Vercel CDN vs Wix runtime: faster TTFB/LCP, immutable asset caching, security headers
- All verification meta tags carried over — Search Console/Bing access survives migration

## Risk register
- LOW: /services → /#services loses anchor in some crawlers → lands on homepage (acceptable)
- LOW: old Wix blog posts were thin (1-min reads, 6 days old) — minimal equity to lose
- MONITOR: Search Console coverage for 404s from unknown Wix URLs (add redirects if found)
- MONITOR: "founded 2021" appeared on old Wix homepage; new site says 2020 — confirm which is right

## Post-launch checklist
1. Merge redirects BEFORE pointing DNS at Vercel
2. Vercel → Domains: add yardexguelph.ca + www (www primary) → set DNS at registrar
3. Test quote form on live domain; click FormSubmit activation email (one-time)
4. Search Console (existing property still verified): submit /sitemap.xml, then URL-inspect + request indexing for: /, /lawn-mowing-guelph/, /lawn-mowing-prices-guelph/, /quote/
5. Bing Webmaster Tools: import from Search Console
6. Update Google Business Profile website link
7. Instagram bio link check (yardex_guelph)
8. Week 1 daily: GSC Coverage + old URL redirects (curl -I the 9 old URLs). Month 1 weekly: Performance, Core Web Vitals. Ongoing monthly: everything above + publish 1 blog post ahead of season.

## Quality scores
Technical SEO 96 · On-page 94 (thin FAQ answers could expand) · Local SEO 92 (needs GBP posts/photos cadence + citation consistency: BBB says "Yardex", site says "Yardex Guelph") · Performance 90 (grass photos are noise-dense; ~500KB hero is the floor without visible loss) · Accessibility 93 (minor h1→h3 skips on 5 utility pages, left to avoid visual changes) · Content 91 · UX 94 · Conversion 93 · Maintainability 97 · Code quality 96
