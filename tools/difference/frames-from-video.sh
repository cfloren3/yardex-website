#!/usr/bin/env bash
# Turns the five stage clips (cut, trim, edge, blow, final) into the WebP frame
# sequences used by the scroll section, and prints the data-* values to paste
# into section.html.
#   tools/difference/frames-from-video.sh cut.mp4 trim.mp4 edge.mp4 blow.mp4 final.mp4
# Env: FADE (crossfade seconds, default 0.5), DFPS (desktop fps, 12), MFPS (mobile fps, 8),
#      MCROP_X (mobile crop centre as a fraction of width, default 0.5)
set -euo pipefail
[ $# -eq 5 ] || { echo "need 5 clips"; exit 1; }
cd "$(dirname "$0")/../.."
OUT=dist/assets/difference
FADE=${FADE:-0.5}; DFPS=${DFPS:-12}; MFPS=${MFPS:-8}; MCROP_X=${MCROP_X:-0.5}
TMP=$(mktemp -d)

# 1. normalise clips and join with short crossfades
durs=(); i=0
for c in "$@"; do
  ffmpeg -loglevel error -y -i "$c" -an -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24,format=yuv420p" -c:v libx264 -crf 14 "$TMP/c$i.mp4"
  durs+=("$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$TMP/c$i.mp4")"); i=$((i+1))
done
read -r FILTER BOUNDS <<<"$(python3 - "$FADE" "${durs[@]}" <<'PY'
import sys
fade=float(sys.argv[1]); d=[float(x) for x in sys.argv[2:]]
f=[]; prev="[0:v]"; bounds=[0]
for i in range(1,len(d)):
    o = sum(d[:i]) - fade*i
    lab = f"[x{i}]"
    f.append(f"{prev}[{i}:v]xfade=transition=fade:duration={fade}:offset={o:.3f}{lab}")
    prev = lab; bounds.append(round(o + fade/2, 2))
total = sum(d) - fade*(len(d)-1); bounds.append(round(total, 2))
print(";".join(f) + f";{prev}null[out]", ",".join(str(b) for b in bounds))
PY
)"
ffmpeg -loglevel error -y -i "$TMP/c0.mp4" -i "$TMP/c1.mp4" -i "$TMP/c2.mp4" -i "$TMP/c3.mp4" -i "$TMP/c4.mp4" \
  -filter_complex "$FILTER" -map "[out]" -c:v libx264 -crf 14 "$TMP/all.mp4"

# 2. frame sequences
rm -rf "$OUT/d" "$OUT/m"; mkdir -p "$OUT/d" "$OUT/m"
ffmpeg -loglevel error -y -i "$TMP/all.mp4" -vf "fps=$DFPS,scale=1280:720" -c:v libwebp -quality ${DQ:-62} -start_number 0 "$OUT/d/%04d.webp"
# mobile: optional per-clip crop centres (MCROPS="x1,x2,x3,x4,x5"), joined with the same crossfades
IFS=, read -r -a MC <<<"${MCROPS:-$MCROP_X,$MCROP_X,$MCROP_X,$MCROP_X,$MCROP_X}"
for k in 0 1 2 3 4; do ffmpeg -loglevel error -y -i "$TMP/c$k.mp4" -vf "crop=608:1080:(iw-608)*${MC[$k]}:0" -c:v libx264 -crf 14 "$TMP/m$k.mp4"; done
ffmpeg -loglevel error -y -i "$TMP/m0.mp4" -i "$TMP/m1.mp4" -i "$TMP/m2.mp4" -i "$TMP/m3.mp4" -i "$TMP/m4.mp4" \
  -filter_complex "$FILTER" -map "[out]" -c:v libx264 -crf 14 "$TMP/mall.mp4"
ffmpeg -loglevel error -y -i "$TMP/mall.mp4" -vf "fps=$MFPS,scale=540:960" -c:v libwebp -quality ${MQ:-60} -start_number 0 "$OUT/m/%04d.webp"

# 3. one poster per stage (stage midpoints)
python3 - "$BOUNDS" <<'PY' > "$TMP/mids"
import sys
b=[float(x) for x in sys.argv[1].split(",")]
print(" ".join(f"{(b[i]+b[i+1])/2:.2f}" for i in range(len(b)-1)))
PY
n=1; for t in $(cat "$TMP/mids"); do
  ffmpeg -loglevel error -y -ss "$t" -i "$TMP/all.mp4" -frames:v 1 -vf scale=960:540 -c:v libwebp -quality 72 "$OUT/poster-$n.webp"; n=$((n+1))
done
echo "data-count-d=\"$(ls "$OUT/d" | wc -l)\" data-count-m=\"$(ls "$OUT/m" | wc -l)\" data-stages=\"$BOUNDS\""
du -sh "$OUT/d" "$OUT/m"
rm -rf "$TMP"
