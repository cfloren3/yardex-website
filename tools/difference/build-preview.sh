#!/usr/bin/env bash
# Builds a local, noindexed preview of the homepage with "The Yardex Difference"
# inserted after the "How it works" section. Does NOT modify dist/index.html.
#   tools/difference/build-preview.sh && python3 -m http.server 4173 -d tools/difference/.preview
set -euo pipefail
cd "$(dirname "$0")/../.."
OUT=tools/difference/.preview
rm -rf "$OUT" && cp -r dist "$OUT"
python3 - "$OUT/index.html" tools/difference/section.html <<'PY'
import sys
page, section = sys.argv[1], open(sys.argv[2]).read()
html = open(page).read()
anchor = 'Swipe or use the arrows to move through the steps.</p>\n  </div>\n</section>\n'
assert html.count(anchor) == 1, "insertion point not found"
html = html.replace(anchor, anchor + "\n" + section + "\n")
html = html.replace('<link rel="stylesheet" href="/assets/style.css">',
  '<link rel="stylesheet" href="/assets/style.css">\n<link rel="stylesheet" href="/assets/difference/difference.css">\n<meta name="robots" content="noindex, nofollow">')
html = html.replace('<script src="/assets/main.js" defer></script>',
  '<script src="/assets/main.js" defer></script>\n<script src="/assets/difference/difference.js" defer></script>')
open(page, "w").write(html)
PY
echo "preview built in $OUT"
