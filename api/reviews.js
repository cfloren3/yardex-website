// Live Google review count for Yardex Guelph.
// Requires env vars in Vercel: GOOGLE_PLACES_API_KEY, YARDEX_PLACE_ID
// Returns { count, rating } — cached at the edge for 6 hours.
export default async function handler(req, res) {
  const key = process.env.GOOGLE_PLACES_API_KEY;
  const placeId = process.env.YARDEX_PLACE_ID;
  if (!key || !placeId) {
    res.status(500).json({ error: "not configured" });
    return;
  }
  try {
    const r = await fetch(
      `https://places.googleapis.com/v1/places/${placeId}?fields=rating,userRatingCount`,
      { headers: { "X-Goog-Api-Key": key } }
    );
    if (!r.ok) throw new Error(`places api ${r.status}`);
    const data = await r.json();
    res.setHeader("Cache-Control", "s-maxage=21600, stale-while-revalidate=86400");
    res.status(200).json({ count: data.userRatingCount, rating: data.rating });
  } catch (e) {
    res.status(502).json({ error: "unavailable" });
  }
}
