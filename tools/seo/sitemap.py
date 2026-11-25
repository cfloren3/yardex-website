#!/usr/bin/env python3
"""Rebuild dist/sitemap.xml: every indexable page (canonical == own URL, no noindex).
lastmod = today for pages changed since baseline/pre-seo-2027, else the previous value."""
import glob, os, re, subprocess, datetime
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'dist'))
SITE = 'https://www.yardexguelph.ca'
old = dict(re.findall(r'<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>', open(ROOT + '/sitemap.xml').read()))
changed = set(subprocess.run(['git', 'diff', '--name-only', 'baseline/pre-seo-2027', '--', 'dist'], capture_output=True, text=True, cwd=os.path.dirname(ROOT)).stdout.split())
changed |= set(subprocess.run(['git', 'ls-files', '--others', '--exclude-standard', 'dist'], capture_output=True, text=True, cwd=os.path.dirname(ROOT)).stdout.split())
today = datetime.date.today().isoformat()
urls = []
for f in sorted(glob.glob(ROOT + '/**/index.html', recursive=True)):
    s = open(f, encoding='utf-8').read()
    rel = f[len(ROOT):].replace('index.html', '')
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', s)
    if 'noindex' in (re.search(r'<meta name="robots" content="([^"]+)"', s) or [None, ''])[1] if re.search(r'<meta name="robots"', s) else False: continue
    if not canon or canon.group(1) != SITE + rel: continue
    lm = today if ('dist' + rel + 'index.html') in changed else old.get(SITE + rel, today)
    urls.append((SITE + rel, lm))
urls.sort(key=lambda x: (x[0] != SITE + '/', x[0]))
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
      ''.join(f'  <url><loc>{u}</loc><lastmod>{l}</lastmod></url>\n' for u, l in urls) + '</urlset>\n'
open(ROOT + '/sitemap.xml', 'w').write(xml); print(len(urls), 'urls')
