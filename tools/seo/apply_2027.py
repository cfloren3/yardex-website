#!/usr/bin/env python3
"""Yardex Guelph — 2027 SEO pass (repo-level changes to dist/).

Run once from the repo root on a clean checkout of baseline/pre-seo-2027:
    python3 tools/seo/apply_2027.py
Every edit asserts that its anchor text exists, so a changed template fails loudly
instead of being silently skipped.
"""
import glob, json, os, re, html

ROOT = os.path.join(os.path.dirname(__file__), '..', '..', 'dist')
ROOT = os.path.abspath(ROOT)
SITE = 'https://www.yardexguelph.ca'
VH = ('position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;'
      'clip:rect(0,0,0,0);white-space:nowrap;border:0')

def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, s):
    full = os.path.join(ROOT, p); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(s)
def sub1(s, old, new, count=1, path=''):
    n = s.count(old)
    assert n >= 1, f'anchor not found in {path}: {old[:90]!r}'
    if count == 1: assert n == 1, f'anchor not unique ({n}) in {path}: {old[:90]!r}'
    return s.replace(old, new) if count != 1 else s.replace(old, new, 1)

PAGES = sorted(p[len(ROOT)+1:] for p in glob.glob(ROOT + '/**/*.html', recursive=True)
               if '/assets/' not in p)

# ---------------------------------------------------------------- navigation
NAV = [('/lawn-mowing-guelph/', 'Lawn Mowing'),
       ('/lawn-fertilizer-guelph/', 'Fertilizing & Overseeding'),
       ('/aeration-overseeding-guelph/', 'Aeration & Overseeding'),
       ('/dethatching-guelph/', 'Dethatching'),
       ('/sodding-guelph/', 'Sodding'),
       ('/yard-cleanup-guelph/', 'Spring & Fall Cleanup'),
       ('/mulching-guelph/', 'Mulching'),
       ('/garden-maintenance-guelph/', 'Garden Maintenance'),
       ('/weed-control-guelph/', 'Weed Control'),
       ('/trimming-edging-guelph/', 'Trimming & Edging'),
       ('/hedge-trimming-guelph/', 'Hedge & Shrub Trimming'),
       ('/vacation-yard-care-guelph/', 'Vacation Yard Care')]
FOOT_OLD = '<li><a href="/vacation-yard-care-guelph/">Vacation Yard Care</a></li>\n          <li><a href="/lawn-mowing-prices-guelph/">Pricing</a></li>'
FOOT_NEW = ('<li><a href="/vacation-yard-care-guelph/">Vacation Yard Care</a></li>\n'
            '          <li><a href="/dethatching-guelph/">Dethatching</a></li>\n'
            '          <li><a href="/sodding-guelph/">Sodding</a></li>\n'
            '          <li><a href="/hedge-trimming-guelph/">Hedge &amp; Shrub Trimming</a></li>\n'
            '          <li><a href="/garden-maintenance-guelph/">Garden Maintenance</a></li>\n'
            '          <li><a href="/lawn-care-puslinch/">Lawn Care in Puslinch</a></li>\n'
            '          <li><a href="/lawn-mowing-prices-guelph/">Pricing</a></li>')

def nav_html(current_url):
    out = []
    for u, t in NAV:
        cur = ' aria-current=page' if u == current_url else ''
        out.append(f'<a href="{u}"{cur}>{t}</a>')
    return '<div class="dropdown">' + ''.join(out) + '<a class="drop-all" href="/services/">All services →</a></div>'

LEARN = {'/lawn-mowing-guelph/': 'lawn mowing', '/lawn-fertilizer-guelph/': 'fertilizing and overseeding',
         '/aeration-overseeding-guelph/': 'aeration and overseeding', '/yard-cleanup-guelph/': 'spring and fall yard cleanups',
         '/mulching-guelph/': 'mulching', '/weed-control-guelph/': 'weed control', '/trimming-edging-guelph/': 'trimming and edging',
         '/vacation-yard-care-guelph/': 'vacation yard care', '/services/spring-cleanup/': 'spring cleanup',
         '/services/fall-cleanup/': 'fall cleanup and leaf removal', '/dethatching-guelph/': 'dethatching',
         '/sodding-guelph/': 'sodding', '/hedge-trimming-guelph/': 'hedge and shrub trimming',
         '/garden-maintenance-guelph/': 'garden maintenance'}
def learn_more(href):
    return f'<a class="link-arrow" href="{href}">Learn more<span style="{VH}"> about {LEARN[href]}</span></a>'

def url_of(path):
    if path == 'index.html': return '/'
    if path.endswith('/index.html'): return '/' + path[:-len('index.html')]
    return '/' + path

# ------------------------------------------------------------- titles (<580px)
TITLES = {
 'index.html': 'Lawn Care Guelph | No Contracts, 75+ 5-Star Reviews | Yardex',
 'blog/when-to-fertilize-lawn-ontario/index.html': 'When to Fertilize Your Lawn in Ontario: Guelph Schedule | Yardex',
 'blog/choose-lawn-care-company-guelph/index.html': 'How to Choose a Lawn Care Company in Guelph | Yardex',
 'blog/lawn-watering-guide-guelph-summer/index.html': 'Summer Lawn Watering in Guelph: Less Often, Deeper | Yardex',
 'blog/spring-lawn-care-checklist-guelph/index.html': 'Spring Lawn Care Checklist for Guelph Homeowners | Yardex',
 'blog/fall-lawn-care-checklist-guelph/index.html': 'Fall Lawn Care Checklist for Guelph Lawns | Yardex',
 'blog/does-my-guelph-lawn-need-aeration/index.html': 'Does Your Guelph Lawn Need Aeration? 3 Tests | Yardex',
 'blog/guelph-watering-bylaw-explained/index.html': 'Guelph Outside Water Use Bylaw, Explained | Yardex',
 'blog/when-to-start-mowing-guelph-spring/index.html': 'When to Start Mowing in Guelph Each Spring | Yardex',
 'weed-control-guelph/index.html': 'Weed Control Guelph | Bed Weeding & Lawn Care | Yardex',
 'faq/index.html': 'Lawn Care FAQ Guelph | Pricing & Scheduling | Yardex',
 'vacation-yard-care-guelph/index.html': 'Vacation Yard Care Guelph | Mowing While You Travel | Yardex',
 'reviews/index.html': 'Yardex Guelph Reviews | 75+ Five-Star Google Reviews',
 'trimming-edging-guelph/index.html': 'Trimming & Edging Guelph | Lawn Edging & Walkways | Yardex',
}
def set_title(s, new, path):
    old = re.search(r'<title>(.*?)</title>', s).group(1)
    old_esc = old
    s = s.replace(f'<title>{old}</title>', f'<title>{html.escape(new, quote=False)}</title>')
    for prop in ('property="og:title"', 'name="twitter:title"'):
        s = re.sub(rf'(<meta {prop} content=")[^"]*(">)', lambda m: m.group(1) + html.escape(new) + m.group(2), s)
    return s

# ====================================================================== SITEWIDE
for path in PAGES:
    s = rd(path); u = url_of(path)
    # 1. logo marks: descriptive alt (still aria-hidden, link already has a name)
    s = s.replace('<img src="/assets/img/logo-mark.png" alt=""', '<img src="/assets/img/logo-mark.png" alt="Yardex Guelph logo"')
    # 2. nav dropdown
    s = re.sub(r'<div class="dropdown">.*?</div>', lambda m: nav_html(u), s, count=1)
    # 3. footer services list
    if FOOT_OLD in s: s = s.replace(FOOT_OLD, FOOT_NEW)
    # 4. breadcrumbs point at the /services/ hub, not the homepage anchor
    s = s.replace('<a href="/#services">Services</a>', '<a href="/services/">Services</a>')
    s = s.replace('"item": "https://www.yardexguelph.ca/#services"', '"item": "https://www.yardexguelph.ca/services/"')
    # 5. descriptive (screen-reader) text on repeated "Learn more" links
    s = re.sub(r'<a class="link-arrow" href="([^"]+)">Learn more</a>', lambda m: learn_more(m.group(1)), s)
    # 6. titles over 580px
    if path in TITLES: s = set_title(s, TITLES[path], path)
    # 7. conversion-event shim (no-op until an analytics tool is installed)
    if '</body>' in s and 'track-r1.js' not in s:
        s = s.replace('</body>', '<script src="/assets/v2/track-r1.js" defer></script>\n</body>', 1)
    wr(path, s)

# =================================================================== HOMEPAGE
p = 'index.html'; s = rd(p)
NEW_DESC = 'Trusted lawn care in Guelph with 75+ five-star reviews. Weekly mowing from $27.50, seasonal cleanups and lawn treatments. No contracts. Get a free quote.'
OLD_DESC = "Guelph's highest-rated lawn care. Weekly mowing from $27.50, fertilizer and cleanups with no contracts and no cancellation fees. Free quotes, fast replies."
s = sub1(s, f'name="description" content="{OLD_DESC}"', f'name="description" content="{NEW_DESC}"', path=p)
s = sub1(s, f'property="og:description" content="{OLD_DESC}"', f'property="og:description" content="{NEW_DESC}"', path=p)
s = sub1(s, f'name="twitter:description" content="{OLD_DESC}"', f'name="twitter:description" content="{NEW_DESC}"', path=p)
s = s.replace('content="Guelph’s highest-rated lawn care. No contracts. No catch. — Yardex lawn care in Guelph, Ontario"',
              'content="Striped front lawn cared for by Yardex lawn care in Guelph, Ontario"')
s = sub1(s, '<h1>Guelph’s highest-rated lawn care. No contracts. No catch.</h1>',
         '<h1>Five-star Guelph lawn care. No contracts. No catch.</h1>', path=p)
# hero performance: responsive WebP preload, slides 2-4 load after the page's load event
s = sub1(s, '<link rel="preload" as="image" href="/assets/img/hero-striped-front-lawn.jpg" fetchpriority="high">',
 '<link rel="preload" as="image" href="/assets/img/hero-striped-front-lawn-960.webp" media="(max-width: 640px)" fetchpriority="high">\n'
 '<link rel="preload" as="image" href="/assets/img/hero-striped-front-lawn.webp" media="(min-width: 641px)" fetchpriority="high">\n'
 '<style>.hero-slides .slide:first-child{background-image:url(/assets/img/hero-striped-front-lawn.webp)!important}'
 '@media (max-width:640px){.hero-slides .slide:first-child{background-image:url(/assets/img/hero-striped-front-lawn-960.webp)!important}}</style>', path=p)
s = sub1(s, '''    <div class="slide" style="background-image:url('/assets/img/backyard-striped-wide.jpg')"></div>
    <div class="slide" style="background-image:url('/assets/img/front-lawn-curb.jpg')"></div>
    <div class="slide" style="background-image:url('/assets/img/lawn-wide-street.jpg')"></div>''',
'''    <div class="slide" data-bg="/assets/img/backyard-striped-wide.webp" data-bg-sm="/assets/img/backyard-striped-wide-720.webp"></div>
    <div class="slide" data-bg="/assets/img/front-lawn-curb.webp" data-bg-sm="/assets/img/front-lawn-curb-960.webp"></div>
    <div class="slide" data-bg="/assets/img/lawn-wide-street.jpg" data-bg-sm="/assets/img/lawn-wide-street-960.webp"></div>
    <script>addEventListener('load',function(){var sm=matchMedia('(max-width:640px)').matches;document.querySelectorAll('.hero-slides [data-bg]').forEach(function(d){d.style.backgroundImage='url('+(sm?d.dataset.bgSm:d.dataset.bg)+')'})})</script>''', path=p)
# supporting copy under the services heading (keyword + contextual links)
s = sub1(s, '''      <h2>Full-service residential lawn care</h2>
      <hr class="rule">
    </div>''', '''      <h2>Full-service residential lawn care</h2>
      <hr class="rule">
      <p style="max-width:68ch">Yardex Guelph provides professional lawn care and residential property maintenance throughout Guelph, with selected services in parts of <a href="/lawn-care-puslinch/">Puslinch</a>. From <a href="/lawn-mowing-guelph/">weekly lawn mowing</a> and <a href="/services/spring-cleanup/">spring</a> and <a href="/services/fall-cleanup/">fall cleanups</a> to <a href="/aeration-overseeding-guelph/">aeration and overseeding</a>, <a href="/dethatching-guelph/">dethatching</a>, <a href="/lawn-fertilizer-guelph/">fertilizing</a> and <a href="/sodding-guelph/">sodding</a>, one local crew looks after it, with flexible scheduling and no contracts.</p>
    </div>''', path=p)
# work-reel loop duplicates (aria-hidden): give them the same alt as the visible originals
for src, alt in [('lawn-striped-06-400', 'Freshly mowed and striped backyard lawn in Guelph'),
                 ('lawn-wide-street-400', 'Wide freshly cut front lawn on a Guelph street'),
                 ('lawn-striped-10-400', 'Freshly striped lawn at a Guelph home'),
                 ('estate-lawn-400', 'Large green residential lawn in Guelph')]:
    s = s.replace(f'<img src="/assets/img2/reel/{src}.webp" alt=""', f'<img src="/assets/img2/reel/{src}.webp" alt="{alt}"')
# service area: Guelph + selected services in Puslinch (owner-confirmed, limited)
OLD_AREA = 'All residential Guelph, Ontario. If you’re in the city, you’re on our map.'
NEW_AREA = 'All residential Guelph, Ontario, plus selected services in parts of Puslinch Township. If you’re in the city, you’re on our map; in Puslinch, send your address and we’ll confirm availability.'
assert s.count(OLD_AREA) == 2, 'homepage FAQ area answer should appear twice (visible + schema)'
s = s.replace(OLD_AREA, NEW_AREA)
s = sub1(s, '{"@type": "Place", "name": "Hanlon Creek, Guelph, ON"}]',
 '{"@type": "Place", "name": "Hanlon Creek, Guelph, ON"}, {"@type": "AdministrativeArea", "name": "Township of Puslinch, Wellington County, ON"}]', path=p)
s = sub1(s, '"description": "Residential lawn care in Guelph, Ontario: weekly mowing, fertilizer, cleanups, trimming and edging. No contracts, no cancellation fees."',
 '"description": "Residential lawn care and property maintenance in Guelph, Ontario: weekly mowing, fertilizing, aeration and overseeding, dethatching, sodding, spring and fall cleanups, mulching, garden maintenance, hedge trimming, trimming and edging. No contracts, no cancellation fees."', path=p)
CATALOG = [('Lawn Mowing', '/lawn-mowing-guelph/'), ('Fertilizing & Overseeding', '/lawn-fertilizer-guelph/'),
           ('Aeration & Overseeding', '/aeration-overseeding-guelph/'), ('Dethatching', '/dethatching-guelph/'),
           ('Sodding', '/sodding-guelph/'), ('Spring Cleanup', '/services/spring-cleanup/'),
           ('Fall Cleanup & Leaf Removal', '/services/fall-cleanup/'), ('Mulching', '/mulching-guelph/'),
           ('Garden Maintenance', '/garden-maintenance-guelph/'), ('Weed Control', '/weed-control-guelph/'),
           ('Trimming & Edging', '/trimming-edging-guelph/'), ('Hedge & Shrub Trimming', '/hedge-trimming-guelph/'),
           ('Vacation Yard Care', '/vacation-yard-care-guelph/')]
catalog = {"@type": "OfferCatalog", "name": "Residential lawn care and property maintenance services",
           "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": SITE + u}} for n, u in CATALOG]}
s = sub1(s, '"award": "2024 Quality Business Award — Best Lawn Care Services in Guelph"}',
         '"award": "2024 Quality Business Award — Best Lawn Care Services in Guelph", "hasOfferCatalog": ' + json.dumps(catalog, ensure_ascii=False) + '}', path=p)
# a11y: in-paragraph GuelphToday link distinguishable without colour (link-in-text-block)
s = sub1(s, 'featured in <a href="https://www.guelphtoday.com/local-news/fourteen-year-old-launches-local-landscaping-company-6451456" rel="noopener">GuelphToday</a> and recognized',
 'featured in <a href="https://www.guelphtoday.com/local-news/fourteen-year-old-launches-local-landscaping-company-6451456" rel="noopener" style="text-decoration:underline;text-underline-offset:2px">GuelphToday</a> and recognized', path=p)
wr(p, s)

# ============================================================ SERVICES HUB
p = 'services/index.html'; s = rd(p)
s = sub1(s, '''          <h3>Spring Cleanup</h3>
          <p>Winter debris cleared, beds refreshed, season-opening first cut.</p>
          <div class="svc-actions">
            <a class="btn btn--gold btn--sm" href="/quote/">Book Now</a>
            ''' + learn_more('/yard-cleanup-guelph/'), '''          <h3>Spring Cleanup</h3>
          <p>Winter debris cleared, beds refreshed, season-opening first cut.</p>
          <div class="svc-actions">
            <a class="btn btn--gold btn--sm" href="/quote/">Book Now</a>
            ''' + learn_more('/services/spring-cleanup/'), path=p)
s = sub1(s, '''          <h3>Fall Cleanup</h3>
          <p>Full leaf cleanup, final cut, and the lawn put to bed properly.</p>
          <div class="svc-actions">
            <a class="btn btn--gold btn--sm" href="/quote/">Book Now</a>
            ''' + learn_more('/yard-cleanup-guelph/'), '''          <h3>Fall Cleanup</h3>
          <p>Full leaf cleanup, final cut, and the lawn put to bed properly.</p>
          <div class="svc-actions">
            <a class="btn btn--gold btn--sm" href="/quote/">Book Now</a>
            ''' + learn_more('/services/fall-cleanup/'), path=p)
s = s.replace('"name": "Spring Cleanup", "url": "https://www.yardexguelph.ca/yard-cleanup-guelph/"', '"name": "Spring Cleanup", "url": "https://www.yardexguelph.ca/services/spring-cleanup/"')
s = s.replace('"name": "Fall Cleanup", "url": "https://www.yardexguelph.ca/yard-cleanup-guelph/"', '"name": "Fall Cleanup", "url": "https://www.yardexguelph.ca/services/fall-cleanup/"')
s = sub1(s, '{"@type": "ListItem", "position": 9, "name": "Vacation Yard Care", "url": "https://www.yardexguelph.ca/vacation-yard-care-guelph/"}]',
 '{"@type": "ListItem", "position": 9, "name": "Vacation Yard Care", "url": "https://www.yardexguelph.ca/vacation-yard-care-guelph/"}, '
 '{"@type": "ListItem", "position": 10, "name": "Dethatching", "url": "https://www.yardexguelph.ca/dethatching-guelph/"}, '
 '{"@type": "ListItem", "position": 11, "name": "Sodding", "url": "https://www.yardexguelph.ca/sodding-guelph/"}, '
 '{"@type": "ListItem", "position": 12, "name": "Hedge & Shrub Trimming", "url": "https://www.yardexguelph.ca/hedge-trimming-guelph/"}, '
 '{"@type": "ListItem", "position": 13, "name": "Garden Maintenance", "url": "https://www.yardexguelph.ca/garden-maintenance-guelph/"}, '
 '{"@type": "ListItem", "position": 14, "name": "Lawn Care in Puslinch", "url": "https://www.yardexguelph.ca/lawn-care-puslinch/"}]', path=p)
def card(img, srcset, alt, w, h, tag, title, text, href):
    return f'''      <div class="svc reveal">
        <img class="svc-photo" src="{img}" srcset="{srcset}" sizes="(max-width: 560px) 100vw, (max-width: 900px) 50vw, 33vw" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async">
        <div class="svc-body">
          <span class="svc-tag">{tag}</span>
          <h3>{title}</h3>
          <p>{text}</p>
          <div class="svc-actions">
            <a class="btn btn--gold btn--sm" href="/quote/">Book Now</a>
            {learn_more(href)}
          </div>
        </div>
      </div>
'''
NEW_CARDS = (card('/assets/img2/backyard-curved-bed-edge.jpg', '/assets/img2/backyard-curved-bed-edge-560.webp 560w, /assets/img2/backyard-curved-bed-edge.jpg 1600w', 'Backyard lawn with a curved, edged shrub border in Guelph', 1600, 1200, 'Spring or early fall', 'Dethatching', 'The matted layer pulled out so water, air and seed reach the soil.', '/dethatching-guelph/')
           + card('/assets/img/green-lawn-street.jpg', '/assets/img/green-lawn-street-560.webp 560w, /assets/img/green-lawn-street.jpg 1200w', 'Thick, even front lawn on a Guelph street', 1200, 900, 'Lawn replacement', 'Sodding', 'Old turf out, soil prepared, new sod laid and rolled.', '/sodding-guelph/')
           + card('/assets/img2/edged-curved-garden-beds.jpg', '/assets/img2/edged-curved-garden-beds-560.webp 560w, /assets/img2/edged-curved-garden-beds.jpg 765w', 'Row of cedars beside a freshly edged, curved garden bed', 765, 1020, 'Hedges &amp; shrubs', 'Hedge &amp; Shrub Trimming', 'Cedar hedges and shrubs shaped cleanly and kept healthy.', '/hedge-trimming-guelph/')
           + card('/assets/img/front-porch-garden.jpg', '/assets/img/front-porch-garden-560.webp 560w, /assets/img/front-porch-garden.jpg 1200w', 'Weeded, freshly mulched front garden bed at a Guelph home', 1200, 900, 'Beds &amp; gardens', 'Garden Maintenance', 'Weeding, groundcover removal and tidy beds, all season.', '/garden-maintenance-guelph/'))
VAC_END = '''          <h3>Vacation Yard Care</h3>
          <p>Mowing and watering kept up while you travel — no favours to ask.</p>
          <div class="svc-actions">
            <a class="btn btn--gold btn--sm" href="/quote/">Book Now</a>
            ''' + learn_more('/vacation-yard-care-guelph/') + '''
          </div>
        </div>
      </div>
'''
s = sub1(s, VAC_END, VAC_END + NEW_CARDS, path=p)
s = sub1(s, '''    <div class="svc-cta reveal">
      <a class="btn btn--gold btn--lg" href="/lawn-mowing-prices-guelph/">See Pricing</a>''',
'''    <p class="reveal" style="margin-top:1.4rem">Outside the city? We offer selected services in parts of Puslinch Township. <a class="link-arrow" href="/lawn-care-puslinch/">Lawn care in Puslinch</a></p>
    <div class="svc-cta reveal">
      <a class="btn btn--gold btn--lg" href="/lawn-mowing-prices-guelph/">See Pricing</a>''', path=p)
wr(p, s)

# ======================================================= CONTEXTUAL LINKS
def para(*links):
    return '<p>' + ' &nbsp;·&nbsp; '.join(f'<a class="link-arrow" href="{h}">{t}</a>' for h, t in links) + '</p>'
EDITS = [
 ('yard-cleanup-guelph/index.html', '<p>Book early — spring slots in Guelph fill fast once the snow is gone.</p>',
  '<p>Book early — spring slots in Guelph fill fast once the snow is gone.</p>\n      ' + para(('/services/spring-cleanup/', 'Spring cleanup in Guelph &amp; Puslinch'), ('/dethatching-guelph/', 'Dethatching'))),
 ('yard-cleanup-guelph/index.html', '<p>A proper fall cleanup prevents snow mould and matted dead patches in April. Your spring self will thank you.</p>',
  '<p>A proper fall cleanup prevents snow mould and matted dead patches in April. Your spring self will thank you.</p>\n      ' + para(('/services/fall-cleanup/', 'Fall cleanup &amp; leaf removal in Guelph &amp; Puslinch'), ('/garden-maintenance-guelph/', 'Garden maintenance'))),
 ('trimming-edging-guelph/index.html', 'We also handle standalone work: hedge and shrub trimming,',
  'We also handle standalone work: <a href="/hedge-trimming-guelph/">hedge and shrub trimming</a>,'),
]
for path, old, new in EDITS:
    s = rd(path); s = sub1(s, old, new, path=path); wr(path, s)

# "Other services" sidebar lists on service pages: add the most related new pages
ASIDE = {
 'aeration-overseeding-guelph/index.html': [('/dethatching-guelph/', 'Dethatching'), ('/sodding-guelph/', 'Sodding')],
 'lawn-fertilizer-guelph/index.html': [('/aeration-overseeding-guelph/', 'Aeration &amp; Overseeding'), ('/sodding-guelph/', 'Sodding')],
 'lawn-mowing-guelph/index.html': [('/sodding-guelph/', 'Sodding'), ('/hedge-trimming-guelph/', 'Hedge &amp; Shrub Trimming')],
 'mulching-guelph/index.html': [('/garden-maintenance-guelph/', 'Garden Maintenance')],
 'weed-control-guelph/index.html': [('/garden-maintenance-guelph/', 'Garden Maintenance')],
 'trimming-edging-guelph/index.html': [('/hedge-trimming-guelph/', 'Hedge &amp; Shrub Trimming')],
 'yard-cleanup-guelph/index.html': [('/services/spring-cleanup/', 'Spring Cleanup'), ('/services/fall-cleanup/', 'Fall Cleanup')],
 'vacation-yard-care-guelph/index.html': [('/garden-maintenance-guelph/', 'Garden Maintenance')],
}
for path, links in ASIDE.items():
    s = rd(path)
    m = re.search(r'<p class="svc-aside-h">Other services</p><ul>', s); assert m, path
    ins = ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in links)
    s = s[:m.end()] + ins + s[m.end():]; wr(path, s)

# seasonal cleanup pages -> restoration / garden clusters
def add_before_cta(path, links):
    s = rd(path)
    anchor = '<section class="section cta-band on-dark">'
    assert s.count(anchor) == 1, path
    block = ('<section class="section section--alt section--tight">\n  <div class="container reveal">\n'
             '    <span class="eyebrow">Keep exploring</span>\n    <h2>Related services</h2>\n    <hr class="rule">\n'
             '    ' + para(*links) + '\n  </div>\n</section>\n\n')
    s = s.replace(anchor, block + anchor); wr(path, s)
add_before_cta('services/spring-cleanup/index.html', [('/dethatching-guelph/', 'Dethatching'), ('/aeration-overseeding-guelph/', 'Aeration &amp; overseeding'), ('/mulching-guelph/', 'Mulching'), ('/garden-maintenance-guelph/', 'Garden maintenance'), ('/lawn-care-puslinch/', 'Lawn care in Puslinch')])
add_before_cta('services/fall-cleanup/index.html', [('/hedge-trimming-guelph/', 'Hedge &amp; shrub trimming'), ('/garden-maintenance-guelph/', 'Garden maintenance'), ('/aeration-overseeding-guelph/', 'Fall aeration &amp; overseeding'), ('/lawn-care-puslinch/', 'Lawn care in Puslinch')])

# blog posts -> commercial pages
BLOG_LINKS = {
 'blog/spring-lawn-care-checklist-guelph/index.html': [('/services/spring-cleanup/', 'Spring cleanup in Guelph'), ('/dethatching-guelph/', 'Lawn dethatching')],
 'blog/fall-lawn-care-checklist-guelph/index.html': [('/services/fall-cleanup/', 'Fall cleanup &amp; leaf removal'), ('/aeration-overseeding-guelph/', 'Fall aeration &amp; overseeding')],
 'blog/fix-patchy-lawn-guelph/index.html': [('/aeration-overseeding-guelph/', 'Aeration &amp; overseeding'), ('/sodding-guelph/', 'Sod installation')],
 'blog/does-my-guelph-lawn-need-aeration/index.html': [('/aeration-overseeding-guelph/', 'Core aeration in Guelph'), ('/dethatching-guelph/', 'Dethatching')],
}
for path, links in BLOG_LINKS.items():
    s = rd(path)
    m = list(re.finditer(r'</article>', s))
    assert len(m) == 1, f'{path}: expected one </article>'
    s = s[:m[0].start()] + '<p><b>Related services:</b> ' + ' &nbsp;·&nbsp; '.join(f'<a class="link-arrow" href="{h}">{t}</a>' for h, t in links) + '</p>\n' + s[m[0].start():]
    wr(path, s)

print('sitewide + existing-page edits done')

# a11y follow-up (link-in-text-block): underline the remaining in-text GuelphToday links
import glob as _g
_U = 'https://www.guelphtoday.com/local-news/fourteen-year-old-launches-local-landscaping-company-6451456'
_ST = ' style="text-decoration:underline;text-underline-offset:2px"'
for _f in _g.glob(ROOT + '/**/*.html', recursive=True):
    _s = open(_f, encoding='utf-8').read(); _o = _s
    _s = _s.replace(f'<span>As featured in <a href="{_U}" rel="noopener">GuelphToday', f'<span>As featured in <a href="{_U}" rel="noopener"{_ST}>GuelphToday')
    _s = _s.replace(f'one lawn at a time. <a href="{_U}" rel="noopener">Read the article', f'one lawn at a time. <a href="{_U}" rel="noopener"{_ST}>Read the article')
    if _s != _o: open(_f, 'w', encoding='utf-8').write(_s)
