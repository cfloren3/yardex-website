#!/usr/bin/env python3
"""Generate the 2027 service pages from the existing service-page template.

Header, footer, sticky CTA and scripts are copied from dist/mulching-guelph/ (after
apply_2027.py has run), so the new pages use the site's existing components only.
Owner-confirmed services (2026-11-25): sodding, dethatching, hedge & shrub trimming,
garden maintenance; Puslinch served for selected services only. No prices are stated
for these services because none were provided — pricing factors are listed instead.
"""
import html, json, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'dist'))
SITE = 'https://www.yardexguelph.ca'
tpl = open(os.path.join(ROOT, 'mulching-guelph/index.html'), encoding='utf-8').read()
HEADER = tpl[tpl.index('<body>'):tpl.index('<main id="main">')].replace(' aria-current=page', '')
FOOTER = tpl[tpl.index('</main>'):]
HEAD_STATIC = tpl[tpl.index('<link rel="icon"'):tpl.index('<link rel="preload" as="image"')]

def faq_html(faqs):
    return '<div class="faq">' + ''.join(f'<details><summary>{html.escape(q, quote=False)}</summary><p>{a}</p></details>' for q, a in faqs) + '</div>'
def strip_tags(s): return re.sub(r'<[^>]+>', '', s)

def page(d):
    url = SITE + d['path']
    e = lambda s: html.escape(s)
    area = d.get('area', {"@type": "City", "name": "Guelph", "address": {"@type": "PostalAddress", "addressRegion": "ON", "addressCountry": "CA"}})
    service = {"@context": "https://schema.org", "@type": "Service", "@id": url + "#service", "name": d['service'],
               "serviceType": d['service_type'], "description": d['schema_desc'],
               "provider": {"@type": "LocalBusiness", "name": "Yardex Guelph", "url": SITE, "@id": SITE + "/#business"},
               "areaServed": area, "url": url, "image": SITE + d['hero']}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Services", "item": SITE + "/services/"},
        {"@type": "ListItem", "position": 3, "name": d['crumb']}]}
    faqld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in d['faqs']]}
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in (service, crumbs, faqld))
    head = f'''<!DOCTYPE html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(d['title'], quote=False)}</title>
<meta name="description" content="{e(d['desc'])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Yardex Guelph">
<meta property="og:title" content="{e(d['title'])}">
<meta property="og:description" content="{e(d['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{d['og']}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(d['og_alt'])}">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(d['title'])}">
<meta name="twitter:description" content="{e(d['desc'])}">
<meta name="twitter:image" content="{SITE}{d['og']}">
<meta name="twitter:image:alt" content="{e(d['og_alt'])}">
{HEAD_STATIC}<link rel="preload" as="image" href="{d['hero']}" fetchpriority="high">
<noscript><link rel="stylesheet" href="/assets/v2/enhance-r3.css"></noscript>
{ld}</head>
'''
    related = ''.join(f'<a href="{h}"><img src="{img}" alt="" width="560" height="420" loading="lazy" decoding="async"><span>{t}</span></a>' for h, t, img in d['related'])
    aside_links = ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t, _ in d['related'] if h != '/services/') + '<li><a href="/services/">All services</a></li>'
    main = f'''<main id="main"><section class="hero hero--sub" style="--hero-img:url('{d['hero']}')">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span aria-hidden="true">›</span> <a href="/services/">Services</a> <span aria-hidden="true">›</span> <span>{d['crumb']}</span></nav>
    <h1>{d['h1']}</h1>
    <p class="lede">{d['lede']}</p>
    <div class="hero-ctas">
      <a class="btn btn--gold btn--lg" href="/quote/">Get a Free Quote</a>
      <a class="btn btn--ghost btn--lg" href="tel:+15198350774">Call or Text</a>
    </div>
    <p class="hero-proof"><a href="https://www.google.com/maps?q=Yardex+Guelph" rel="noopener">★★★★★&nbsp; 75+ five-star Google reviews</a></p>

  </div>
</section>
<div class="svc-light">

<div class="svc-body"><div class="svc-main">
<section class="section svc-intro"><div class="container">{d['intro']}</div></section>
{d['body']}
<section class="section">
  <div class="container reveal" style="max-width:820px">
    <span class="eyebrow">Common questions</span>
    <h2>{d['faq_h2']}</h2>
    <hr class="rule">
    {faq_html(d['faqs'])}
  </div>
</section>
</div><aside class="svc-aside" aria-label="Get a quote"><div class="svc-aside-card"><p class="svc-aside-title">Get a free quote</p><p>{d.get('aside_area', 'Serving all of Guelph. We reply within 24 hours — usually much faster.')}</p><a class="btn btn--gold" href="/quote/">Request a Quote</a><a class="btn btn--ghost" href="tel:+15198350774">Call or text (519) 835-0774</a><p class="svc-aside-proof">★★★★★ 75+ five-star Google reviews</p><p class="svc-aside-h">Other services</p><ul>{aside_links}</ul></div></aside></div>
</div>

<section class="section section--alt section--tight">
  <div class="container reveal">
    <span class="eyebrow">Keep exploring</span>
    <h2>Related services &amp; reading</h2>
    <hr class="rule">
    <div class="svc-related-grid">{related}</div>
    <p style="margin-top:.6rem"><b>From our blog:</b> <a class="link-arrow" href="{d['blog'][0]}">{d['blog'][1]}</a></p>
  </div>
</section>

<section class="section cta-band on-dark">
  <div class="container reveal">
    <hr class="rule rule--center">
    <h2>{d['cta_h2']}</h2>
    <p>Send your address and we’ll reply with a firm quote within 24 hours.</p>
    <a class="btn btn--gold btn--lg" href="/quote/">Get Your Free Quote</a>
    <p class="cta-reassure">No contracts. No cancellation fees. We reply within 24 hours — usually much faster.</p>
  </div>
</section>
'''
    return head + HEADER.replace(f'<a href="{d["path"]}">', f'<a href="{d["path"]}" aria-current=page>', 1) + main + FOOTER

def grid2(eyebrow, h2, items, after, img, alt, w, h):
    lis = ''.join(f'\n        <li>{i}</li>' for i in items)
    return f'''
<section class="section">
  <div class="container grid-2">
    <div class="reveal">
      <span class="eyebrow">{eyebrow}</span>
      <h2>{h2}</h2>
      <hr class="rule">
      <ul class="checklist">{lis}
      </ul>
      {after}
    </div>
    <div class="reveal"><img src="{img}" alt="{alt}" loading="lazy" width="{w}" height="{h}" style="border-radius:10px" decoding="async"></div>
  </div>
</section>
'''
def prose(eyebrow, h2, first, more, alt=True):
    more_html = f'\n    <details class="svc-more"><summary>Read more</summary>\n    {more}\n    </details>' if more else ''
    return f'''
<section class="section{' section--alt' if alt else ''}">
  <div class="container prose reveal">
    <span class="eyebrow">{eyebrow}</span>
    <h2>{h2}</h2>
    <hr class="rule">
    {first}{more_html}
  </div>
</section>
'''
def plain_list(eyebrow, h2, intro, items, outro=''):
    lis = ''.join(f'\n        <li>{i}</li>' for i in items)
    return f'''
<section class="section">
  <div class="container prose reveal">
    <span class="eyebrow">{eyebrow}</span>
    <h2>{h2}</h2>
    <hr class="rule">
    <p>{intro}</p>
    <ul class="checklist">{lis}
    </ul>
    {outro}
  </div>
</section>
'''

R = {  # related-card images (all existing, genuine Yardex photos)
 'aer': ('/aeration-overseeding-guelph/', 'Aeration &amp; Overseeding', '/assets/img2/curved-shade-stripes-560.webp'),
 'mow': ('/lawn-mowing-guelph/', 'Lawn Mowing', '/assets/img2/treeline-stripes-560.webp'),
 'fert': ('/lawn-fertilizer-guelph/', 'Fertilizing &amp; Overseeding', '/assets/img2/backyard-stripes-pink-flowers-560.webp'),
 'deth': ('/dethatching-guelph/', 'Dethatching', '/assets/img2/backyard-curved-bed-edge-560.webp'),
 'sod': ('/sodding-guelph/', 'Sodding', '/assets/img/green-lawn-street-560.webp'),
 'spring': ('/services/spring-cleanup/', 'Spring Cleanup', '/assets/img/backyard-bed-cleanup.webp'),
 'fall': ('/services/fall-cleanup/', 'Fall Cleanup', '/assets/img2/striped-slope-fall-560.webp'),
 'trim': ('/trimming-edging-guelph/', 'Trimming &amp; Edging', '/assets/img2/sunset-sidewalk-crisp-edges-560.webp'),
 'hedge': ('/hedge-trimming-guelph/', 'Hedge &amp; Shrub Trimming', '/assets/img2/edged-curved-garden-beds-560.webp'),
 'garden': ('/garden-maintenance-guelph/', 'Garden Maintenance', '/assets/img/front-porch-garden-560.webp'),
 'mulch': ('/mulching-guelph/', 'Mulching', '/assets/img/mulched-beds.webp'),
 'weed': ('/weed-control-guelph/', 'Weed Control', '/assets/img/front-porch-garden.webp'),
 'all': ('/services/', 'All services', '/assets/img/lawn-wide-street.jpg'),
}

PAGES = []

# ------------------------------------------------------------------ SODDING
PAGES.append(dict(
 path='/sodding-guelph/', title='Sodding Guelph | Sod Installation & Lawn Replacement | Yardex',
 desc='Residential sod installation in Guelph: old turf removed, soil prepared and levelled, fresh sod laid tight and rolled. Free quotes, no contracts.',
 h1='Sod Installation in Guelph', crumb='Sodding in Guelph', service='Sod installation', service_type='Sodding',
 schema_desc='Residential sod installation and lawn replacement in Guelph, Ontario: turf removal, soil preparation and levelling, sod laying, rolling and aftercare guidance.',
 hero='/assets/img/green-lawn-street.jpg', og='/assets/img/og/green-lawn-street-og.jpg', og_alt='Thick, even front lawn on a Guelph street — Yardex sodding in Guelph',
 lede='A finished lawn in a day, built on the prep work that decides whether new sod actually roots.',
 intro='<p class="svc-intro-lead">When a lawn is too far gone for overseeding — mostly bare, mostly weeds, torn up after construction or a dug-up trench — new sod is the fastest way back to a usable lawn. We remove the old turf, prepare and level the soil, then lay fresh sod tight with staggered seams and roll it so the roots meet the soil.</p><p>Most of the work in a good sod job happens before the first roll goes down. Guelph’s heavy clay packs hard and sheds water, so the ground is loosened and graded to drain away from the house first. Sod laid on compacted, uneven clay roots shallowly and struggles every July.</p>',
 body=grid2('The service', 'From tired turf to a new lawn',
   ['Old grass, weeds and debris stripped and removed', 'Soil loosened, levelled and graded to drain away from the house',
    'Fresh sod laid tight, with staggered seams and no gaps', 'Rolled for firm root-to-soil contact, then watered in',
    'A clear aftercare plan: watering, first mow, first feeding'],
   '<p>Sod makes sense after renovations and new builds, where a lawn has thinned beyond repair, or where you need a usable yard quickly rather than waiting a season for seed to fill in.</p>',
   '/assets/img/estate-lawn.jpg', 'Established green lawn and walkway under mature trees at a Guelph home', 1200, 884)
  + prose('Local know-how', 'Sod or overseeding? How we decide',
   '<p>Sod isn’t always the right answer, and we’ll say so. If your lawn still has a reasonable base of grass, <a href="/aeration-overseeding-guelph/">core aeration and overseeding</a> costs far less and thickens it within a season. Sod earns its price when most of the area is bare soil or weeds, when the grade needs fixing, or when you need the yard usable now.</p>',
   '<p><b>Timing in Guelph.</b> The best windows are spring, once the ground has thawed and dried out (usually May into June), and late summer into early fall, when nights cool down and rain is more reliable. Sod can go down in midsummer, but it needs much more water to survive the heat — and outdoor watering in Guelph follows the City’s Outside Water Use program, so check the current level first (<a href="/blog/guelph-watering-bylaw-explained/">our bylaw explainer</a>).</p>\n    <p><b>Never over old grass.</b> Laying sod on top of an existing lawn leaves a spongy layer of dead turf between the new roots and the soil. The old lawn comes off first, every time.</p>')
  + plain_list('Pricing', 'What affects the price of sodding', 'Every sod job is quoted on your actual property, after we’ve seen it. The main factors:',
   ['Area in square feet', 'Removing and disposing of the old turf', 'How much levelling or grading the soil needs',
    'Access — open front yard versus a backyard behind a narrow gate', 'Slopes and awkward shapes that need more cutting'],
   '<p>You’ll get a firm price before anything is booked. No contracts, no deposit games.</p>')
  + prose('Aftercare', 'The first four weeks', '<ul class="checklist"><li><b>Weeks 1–2:</b> keep the soil under the sod moist, not just the blades. Lift a corner: the soil should be damp.</li><li><b>Weeks 2–3:</b> taper to deeper, less frequent watering as roots take hold. Keep foot traffic light.</li><li><b>First mow:</b> once the sod resists a gentle tug, usually two to three weeks in. We cut at 3 inches, and can add it to your <a href="/lawn-mowing-guelph/">weekly mowing</a>.</li><li><b>First feeding:</b> after it has rooted, a <a href="/lawn-fertilizer-guelph/">balanced fertilizer</a> helps it thicken before its first winter.</li></ul>', ''),
 faq_h2='Sodding questions', faqs=[
  ('When is the best time to lay sod in Guelph?', 'Spring once the ground has dried out, usually May into June, and late summer into early fall. Midsummer installs can work, but they need far more water to survive the heat.'),
  ('Should I sod or overseed?', 'If your lawn still has a reasonable base of grass, aeration and overseeding is cheaper and very effective. Sod makes sense when most of the area is bare or weeds, the grade needs fixing, or you need a usable lawn quickly.'),
  ('How much do I water new sod?', 'Enough to keep the soil underneath moist, not just the grass — usually daily for the first week or two, then tapering to deeper, less frequent watering as it roots. Check the City of Guelph’s current outside water use level before setting timers.'),
  ('When can I walk on new sod?', 'Light foot traffic after about two to three weeks, once it has rooted and resists a gentle tug. Keep heavy use — play, parties, dogs running laps — off it for the first month.'),
  ('Can you lay sod over my existing lawn?', 'No. Sod laid over old grass and weeds sits on a spongy dead layer and roots poorly. The old turf is always removed first.'),
  ('How much does sodding cost?', 'It depends on the area, turf removal, how much levelling the soil needs and access to the yard. We quote each property after seeing it, with a firm price before anything is booked.'),
 ],
 related=[R['aer'], R['mow'], R['fert'], R['deth']], blog=('/blog/fix-patchy-lawn-guelph/', 'How to Fix a Patchy, Thin Lawn in Guelph'),
 cta_h2='Book sod installation in Guelph'))

# --------------------------------------------------------------- DETHATCHING
PAGES.append(dict(
 path='/dethatching-guelph/', title='Dethatching Guelph | Lawn Power Raking | Yardex',
 desc='Lawn dethatching and power raking in Guelph. We remove the matted thatch layer so water, air and seed reach the soil, then pair it with overseeding.',
 h1='Lawn Dethatching in Guelph', crumb='Dethatching in Guelph', service='Lawn dethatching', service_type='Dethatching',
 schema_desc='Mechanical lawn dethatching and power raking for residential lawns in Guelph, Ontario, with optional overseeding and aeration.',
 hero='/assets/img2/backyard-curved-bed-edge.jpg', og='/assets/img/og/backyard-curved-bed-edge-og.jpg', og_alt='Backyard lawn with a curved shrub border — Yardex lawn dethatching in Guelph',
 lede='Clear the matted layer choking your lawn so water, air and seed can reach the soil.',
 intro='<p class="svc-intro-lead">Thatch is the layer of dead stems, runners and roots that builds up between the green grass and the soil. A thin layer is normal and even protective. Once it gets thicker than about half an inch, it starts working against you: rain and fertilizer sit on top instead of soaking in, roots grow up into the thatch instead of down into the soil, and the lawn turns spongy and stressed in summer heat.</p><p>Dethatching — also called power raking — uses a machine to pull that layer out of the lawn. We check the thatch depth before quoting, so you only pay for it if your lawn actually needs it.</p>',
 body=grid2('The service', 'Dethatching, done for the right reasons',
   ['Thatch depth checked first — we’ll tell you if you don’t need it', 'Mechanical dethatching across the whole lawn',
    'Pulled-up thatch and debris raked up and cleared off the lawn', 'Optional <a href="/aeration-overseeding-guelph/">overseeding</a> straight after, while the soil is exposed',
    'Advice on follow-up feeding and watering'],
   '<p>A lawn looks thin and scratched-up for a week or two after dethatching. That’s expected: the dead layer is gone and the soil is open for new growth, which is why overseeding at the same time pays off.</p>',
   '/assets/img/lawn-summer-front.jpg', 'Green front lawn beside a curved curb on a Guelph street', 900, 1200)
  + prose('Local know-how', 'Dethatching vs aeration: which does your lawn need?',
   '<p>They solve different problems. Thatch is a problem <em>on top of</em> the soil; compaction is a problem <em>in</em> it. Much of Guelph sits on heavy clay, and many lawns here need <a href="/aeration-overseeding-guelph/">core aeration</a> more than dethatching. A quick test tells you which: cut a small wedge out of the lawn and look at the side. A spongy brown layer over half an inch thick means thatch; hard, dense soil that a screwdriver struggles to enter means compaction.</p>',
   '<p><b>Timing in Guelph.</b> Dethatch when the grass is actively growing so it can recover: late April through May once the lawn has greened up and the soil is firm, or late August into September. Avoid early spring when the ground is soggy — machines tear wet turf — and avoid midsummer heat, when the lawn is already stressed.</p>\n    <p><b>Not the same as a spring cleanup.</b> A <a href="/services/spring-cleanup/">spring cleanup</a> rakes leaves, sticks and winter debris off the surface. Dethatching goes deeper, into the layer at the base of the grass. Many lawns only need the cleanup.</p>')
  + plain_list('Pricing', 'What affects the price of dethatching', 'Dethatching is quoted per property. The main factors:',
   ['Lawn area', 'How heavy the thatch layer is and how much material comes out', 'Whether overseeding or aeration is added in the same visit', 'Access, slopes and obstacles'], ''),
 faq_h2='Dethatching questions', faqs=[
  ('How do I know if my lawn needs dethatching?', 'Push a trowel into the turf and look at the side of the cut. If the spongy brown layer between the green blades and the soil is more than about half an inch thick, it’s worth removing. Less than that is normal.'),
  ('When is the best time to dethatch in Guelph?', 'Late April through May once the lawn has greened up and the soil is firm, or late August into September. Avoid soggy early-spring ground and midsummer heat.'),
  ('Will my lawn look worse right after?', 'For a week or two, yes — it can look thin and scratched. That’s the dead layer gone and the soil open for new growth. Overseeding at the same time helps it fill back in quickly.'),
  ('Is power raking the same as dethatching?', 'The terms are often used for the same job: a machine with rotating tines or blades pulls thatch out of the lawn. What matters is matching the depth to the layer your lawn actually has.'),
  ('Should I dethatch every year?', 'Usually not. Most lawns need it every few years at most. Mowing at the right height, core aeration and not over-fertilizing keep thatch from building back up.'),
  ('Should I dethatch or aerate?', 'Dethatching removes a thick layer on top of the soil; aeration relieves compacted soil underneath. On Guelph clay, aeration is often the bigger need. We’ll check your lawn and recommend one, both, or neither.'),
 ],
 related=[R['aer'], R['spring'], R['fert'], R['sod']], blog=('/blog/does-my-guelph-lawn-need-aeration/', 'Does Your Guelph Lawn Need Aeration? Three Tests to Find Out'),
 cta_h2='Book lawn dethatching in Guelph'))

# ------------------------------------------------------------ HEDGE TRIMMING
PAGES.append(dict(
 path='/hedge-trimming-guelph/', title='Hedge Trimming Guelph | Shrub & Bush Pruning | Yardex',
 desc='Hedge and shrub trimming in Guelph: cedar hedges shaped, bushes cut back from windows and walkways, clippings cleaned up. Free quotes, no contracts.',
 h1='Hedge &amp; Shrub Trimming in Guelph', crumb='Hedge &amp; Shrub Trimming', service='Hedge and shrub trimming', service_type='Hedge trimming',
 schema_desc='Residential hedge trimming, shrub and bush pruning in Guelph, Ontario, including cedar and privacy hedges, with cleanup of clippings.',
 hero='/assets/img2/edged-curved-garden-beds.jpg', og='/assets/img/og/edged-curved-garden-beds-og.jpg', og_alt='Row of cedars beside a curved garden bed — Yardex hedge trimming in Guelph',
 lede='Cedar hedges, privacy rows and foundation shrubs, shaped cleanly and kept healthy.',
 intro='<p class="svc-intro-lead">Hedges and shrubs frame a property — until they start swallowing the front window, crowding the walkway and going bare at the bottom. We shape cedar and privacy hedges, cut back overgrown shrubs and bushes, and clean up every clipping before we leave.</p><p>Every weekly mow already includes trimming around obstacles and edging along walkways (<a href="/trimming-edging-guelph/">trimming &amp; edging</a>). This service is for the hedges and shrubs themselves, as a one-time trim or part of your seasonal maintenance.</p>',
 body=grid2('The service', 'Hedges and shrubs, shaped properly',
   ['Cedar and privacy hedges trimmed straight, square or rounded to your preference', 'Shrubs and bushes cut back from windows, siding, walkways and driveways',
    'Hedges shaped slightly wider at the base so light reaches the bottom', 'Clippings raked and blown off lawns, beds and hard surfaces',
    'One-time trims, or scheduled with your mowing and cleanups'],
   '<p>A hedge cut narrower at the top than the bottom stays green to the ground. Cut the other way, the lower branches lose their light and go thin and bare over a few seasons.</p>',
   '/assets/img2/backyard-curved-bed-edge.jpg', 'Backyard shrub border and curved garden bed beside a striped lawn', 1600, 1200)
  + prose('Local know-how', 'When to trim what in Guelph',
   '<p>Timing matters more than most people think. <b>Spring-flowering shrubs</b> such as lilac and forsythia set next year’s buds soon after they bloom, so they’re trimmed right after flowering — cut them in fall and you cut off next spring’s flowers. <b>Cedar and other evergreen hedges</b> are best trimmed from late spring into summer, once the new growth has come in, with an optional lighter trim later in summer to keep a formal hedge sharp.</p>',
   '<p><b>Don’t cut cedars into bare wood.</b> Cedars rarely regrow from old brown wood, so trimming past the green layer can leave holes that never fill. With an overgrown hedge we take it back gradually and tell you honestly how far it can go.</p>\n    <p><b>Nesting season.</b> Many birds nest in hedges in spring and early summer, and active nests of migratory birds are protected under federal law. We check hedges before trimming during nesting season and leave a section with an active nest until later.</p>\n    <p><b>Late fall.</b> Heavy pruning just before winter leaves fresh cuts exposed to the cold. Light tidying is fine; major shaping waits for the growing season.</p>')
  + plain_list('Pricing', 'What affects the price of hedge trimming', 'Hedge and shrub trimming is quoted per property. The main factors:',
   ['Length and height of the hedges', 'How overgrown they are since the last trim', 'Number and size of shrubs', 'Ladders or access needed for tall or hard-to-reach sides'], ''),
 faq_h2='Hedge trimming questions', faqs=[
  ('How often should a cedar hedge be trimmed?', 'Once a year keeps most hedges in shape, usually late spring into summer. Twice a year — late spring and again later in summer — keeps a formal hedge sharp.'),
  ('Can you cut back a badly overgrown hedge?', 'Usually, in stages. We can take a lot off the sides and top, but cedars don’t regrow from bare brown wood, so cutting past the green layer can leave permanent holes. We’ll tell you how far it can safely go.'),
  ('When should flowering shrubs be trimmed?', 'Spring bloomers like lilac and forsythia are trimmed right after they flower. Trimming them in fall removes next spring’s flower buds.'),
  ('What about bird nests in my hedge?', 'Active nests of migratory birds are protected under federal law. During nesting season we check before trimming and leave any section with an active nest until the young have left.'),
  ('Do you clean up the clippings?', 'Yes. Clippings are raked and blown off your lawn, beds, driveway and walkways before we leave.'),
  ('Is this the same as trimming and edging?', 'No. Trimming and edging — around obstacles, along walkways and bed edges — is part of every weekly mow. Hedge and shrub trimming is the hedges and shrubs themselves.'),
 ],
 related=[R['trim'], R['garden'], R['mulch'], R['fall']], blog=('/blog/fall-lawn-care-checklist-guelph/', 'Fall Lawn Care in Guelph: The Checklist That Sets Up Next Spring'),
 cta_h2='Book hedge trimming in Guelph'))

# ---------------------------------------------------------- GARDEN MAINTENANCE
ba = '''
<section class="section section--alt">
  <div class="container reveal">
    <span class="eyebrow">Before &amp; after</span>
    <h2>Real garden resets by our crew</h2>
    <hr class="rule">
    <div class="grid-2">
      <div><img src="/assets/img2/ba-overgrown-bed-before.webp" alt="Before: garden bed overgrown with spreading groundcover and weeds" width="640" height="640" loading="lazy" decoding="async" style="border-radius:10px"><p><b>Before:</b> a bed lost to spreading groundcover.</p></div>
      <div><img src="/assets/img2/ba-overgrown-bed-after.webp" alt="After: the same bed cleared to bare soil, with the removed growth bagged" width="640" height="640" loading="lazy" decoding="async" style="border-radius:10px"><p><b>After:</b> roots and runners dug out, ready for planting or mulch.</p></div>
      <div><img src="/assets/img2/ba-deck-vines-before.webp" alt="Before: vines overgrowing a backyard deck and privacy fence" width="640" height="640" loading="lazy" decoding="async" style="border-radius:10px"><p><b>Before:</b> vines climbing the deck and fence.</p></div>
      <div><img src="/assets/img2/ba-deck-vines-after.webp" alt="After: deck and privacy fence cleared of vines" width="640" height="640" loading="lazy" decoding="async" style="border-radius:10px"><p><b>After:</b> deck and fence cleared.</p></div>
    </div>
  </div>
</section>
'''
PAGES.append(dict(
 path='/garden-maintenance-guelph/', title='Garden Maintenance Guelph | Bed Weeding & Cleanups | Yardex',
 desc='Garden maintenance in Guelph: bed weeding, groundcover and vine removal, fallen branch cleanup and tidy edges — all season or as a one-time reset.',
 h1='Garden Maintenance in Guelph', crumb='Garden Maintenance in Guelph', service='Garden maintenance', service_type='Garden maintenance',
 schema_desc='Residential garden bed maintenance in Guelph, Ontario: weeding, groundcover and vine removal, fallen branch cleanup, bed edging and mulch top-ups.',
 hero='/assets/img/front-porch-garden.jpg', og='/assets/img/og/front-porch-garden-og.jpg', og_alt='Weeded, freshly mulched front garden — Yardex garden maintenance in Guelph',
 lede='Weeded, edged and tidy garden beds — kept that way all season, or reset in one visit.',
 intro='<p class="svc-intro-lead">Garden beds are where a property slips first. A few weeks of rain and sun, and weeds are seeding, groundcover is creeping into the lawn, and fallen branches are piling up behind the shrubs. We keep beds clean on a schedule that suits your garden, or reset an overgrown yard in one visit.</p><p>It’s the same local crew that mows Guelph lawns every week, so beds, edges and lawn are looked after together — one quote, one invoice, no contract.</p>',
 body=grid2('The service', 'What garden maintenance covers',
   ['Bed weeding and cultivating, roots and all', 'Overgrown groundcover and climbing vines removed', 'Fallen branches and yard debris cleared',
    'Bed edges re-cut so lawn and garden stay separate', '<a href="/mulching-guelph/">Mulch</a> top-ups where beds need it',
    'Recurring visits through the season, or a one-time reset'],
   '<p>Regular visits are what keep beds easy. A bed weeded every few weeks takes minutes; a bed left for a summer takes an afternoon and a lot more of the budget.</p>',
   '/assets/img/garden-bed-mulch.jpg', 'Freshly mulched garden beds in a Guelph backyard', 1200, 900)
  + ba
  + prose('Local know-how', 'Why garden beds get away from you', '<p>The weeds you can see are only half of it. Goutweed (bishop’s weed), creeping bellflower and similar aggressive plants spread through underground runners, so pulling the tops just resets the clock. We dig out roots and runners, and we’re upfront that a heavily infested bed usually needs follow-up visits to catch regrowth.</p>',
   '<p>Ontario restricts cosmetic pesticides, so bed weeding here is hands-on work. That suits a maintenance schedule: small, frequent visits beat one big fight in August. For the lawn side of weeds — thickening turf so weeds can’t establish — see <a href="/weed-control-guelph/">weed control</a>.</p>\n    <p><b>Branches and limbs.</b> We clear fallen branches and limbs that can be handled safely from the ground. Anything large, or still attached high in a tree, is a job for a certified arborist — we’ll tell you when that’s the case.</p>', alt=False)
  + plain_list('Pricing', 'What affects the price of garden maintenance', 'Garden maintenance is quoted per property. The main factors:',
   ['Number and size of beds', 'How overgrown they are at the first visit', 'Visit frequency — recurring visits cost less per visit than a one-time reset', 'Mulch, if you want beds topped up'], ''),
 faq_h2='Garden maintenance questions', faqs=[
  ('How often should garden beds be maintained?', 'Through the growing season, every two to four weeks keeps most beds clean with little effort. Beds left longer need a bigger reset visit.'),
  ('Can you remove groundcover like goutweed?', 'Yes. Aggressive groundcovers spread through underground runners, so we dig out the roots, not just the tops. Heavily infested beds usually need follow-up visits to catch regrowth, and we’ll be upfront about that.'),
  ('Do you remove fallen branches?', 'Yes — fallen branches and limbs that can be handled safely from the ground. Large limbs, or anything still attached high in a tree, needs a certified arborist.'),
  ('Is garden maintenance the same as weed control?', 'They overlap. Weed control covers lawn and beds using pesticide-free methods. Garden maintenance is the broader upkeep of your beds: weeding, groundcover and vine removal, debris, edges and mulch.'),
  ('Can I book a one-time cleanup instead of a schedule?', 'Yes. A one-time reset is common before a sale, an event, or the start of the season. No contract either way.'),
 ],
 related=[R['weed'], R['mulch'], R['hedge'], R['spring']], blog=('/blog/spring-lawn-care-checklist-guelph/', 'The Complete Spring Lawn Care Checklist for Guelph Homeowners'),
 cta_h2='Book garden maintenance in Guelph'))

# ------------------------------------------------------------------ PUSLINCH
PAGES.append(dict(
 path='/lawn-care-puslinch/', title='Lawn Care Puslinch | Mowing & Yard Services | Yardex Guelph',
 desc='Selected lawn care and yard services in parts of Puslinch Township from Yardex Guelph. Send your address and we’ll confirm availability within 24 hours.',
 h1='Lawn Care in Puslinch', crumb='Lawn Care in Puslinch', service='Residential lawn care', service_type='Lawn care',
 schema_desc='Selected residential lawn care and yard services for properties in parts of the Township of Puslinch, Wellington County, Ontario. Availability is confirmed per address.',
 area={"@type": "AdministrativeArea", "name": "Township of Puslinch", "containedInPlace": {"@type": "AdministrativeArea", "name": "Wellington County, Ontario"}},
 aside_area='Selected services in parts of Puslinch. Send your address and we’ll confirm availability within 24 hours.',
 hero='/assets/img2/estate-hillside-stripes.jpg', og='/assets/img/og/estate-hillside-stripes-og.jpg', og_alt='Large sloped lawn mowed in stripes — Yardex lawn care for Puslinch properties',
 lede='Selected Yardex services for homes in parts of Puslinch Township, from the crew that cares for Guelph lawns every week.',
 intro='<p class="svc-intro-lead">Yardex is based in Guelph, and we serve parts of the Township of Puslinch for selected services. Because availability depends on where your property is and what you need, every Puslinch request starts with your address — we’ll confirm within 24 hours whether we can help, and send a firm quote if we can.</p><p>Same terms as in the city: no contracts, no cancellation fees, and the same local crew from one visit to the next.</p>',
 body=plain_list('Services', 'What Puslinch homeowners ask us for', 'These are the services most often requested by Puslinch homeowners. Not every service is available at every address, so we confirm it with your quote.',
   ['<a href="/services/spring-cleanup/">Spring cleanup</a> — winter debris, beds and the first cut', '<a href="/services/fall-cleanup/">Fall cleanup and leaf removal</a> — leaves, final cut, haul-away',
    '<a href="/lawn-mowing-guelph/">Lawn mowing</a> — weekly or bi-weekly where it fits our routes', '<a href="/aeration-overseeding-guelph/">Aeration and overseeding</a>',
    '<a href="/hedge-trimming-guelph/">Hedge and shrub trimming</a>', '<a href="/garden-maintenance-guelph/">Garden maintenance</a>'], '')
  + prose('Local know-how', 'Puslinch properties are different',
   '<p>Just south of Guelph, Puslinch Township takes in Aberfoyle, Morriston, Arkell and the homes around Puslinch Lake. Lots are typically bigger than in the city, many back onto woodlots or hedgerows, and long driveways and open lawns mean more leaves in fall and more mowing in June. We quote each property on its actual size and layout rather than a city-lot price.</p>',
   '<p><b>Septic beds and wells.</b> Many Puslinch homes are on private septic systems and wells. Heavy equipment and core aeration stay off septic leaching beds, and we’ll ask where yours is before the first visit. If you’re on a well, watering advice is about what your well can supply rather than a municipal schedule.</p>\n    <p><b>Yard waste.</b> Waste collection in Puslinch is run by the County of Wellington, not the City of Guelph, and curbside yard-waste pickup doesn’t reach every rural address — so for cleanups, taking the material with us is often the simplest option.</p>\n    <p><b>Travel and routes.</b> Recurring services like weekly mowing depend on how a property fits our routes, which is the main reason availability varies across the township.</p>')
  + '''
<section class="section">
  <div class="container reveal">
    <span class="eyebrow">How it works</span>
    <h2>Getting a quote in Puslinch</h2>
    <hr class="rule">
    <div class="grid-3">
      <div class="card"><h3>1. Send your address</h3><p>Use the <a href="/quote/">quote form</a> or call or text (519) 835-0774, and tell us what you need.</p></div>
      <div class="card"><h3>2. We confirm availability</h3><p>Within 24 hours, we’ll tell you which services we can offer at your address.</p></div>
      <div class="card"><h3>3. Firm quote, no contract</h3><p>You get a price for your actual property. Book once, or keep us on through the season.</p></div>
    </div>
  </div>
</section>
''',
 faq_h2='Puslinch questions', faqs=[
  ('Do you serve all of Puslinch?', 'Not every address or every service. We serve parts of Puslinch Township for selected services. Send your address and what you need, and we’ll confirm within 24 hours.'),
  ('Is pricing the same as in Guelph?', 'Every property is quoted individually. Larger lots and travel are reflected in the quote, and you’ll have a firm price before anything is booked.'),
  ('Can you mow my lawn every week in Puslinch?', 'Where a property fits our routes, yes. Recurring mowing is the service most affected by location, so it’s confirmed with your quote.'),
  ('I have a septic system. Is that a problem?', 'No — just let us know where the septic bed is. Heavy equipment and core aeration stay off it.'),
  ('Do I need to sign a contract?', 'No. Like everywhere we work, there are no contracts and no cancellation fees.'),
 ],
 related=[R['spring'], R['fall'], R['mow'], R['aer']], blog=('/blog/fall-lawn-care-checklist-guelph/', 'Fall Lawn Care in Guelph: The Checklist That Sets Up Next Spring'),
 cta_h2='Lawn care in Puslinch, confirmed for your address'))

for d in PAGES:
    out = os.path.join(ROOT, d['path'].strip('/'), 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(page(d))
    print('wrote', d['path'])
