# Review acquisition strategy

Date: 2026-11-25

## 1. Current position (verify first)
| Metric | Value | Status |
|---|---|---|
| Google review count | Site says "75+". The July 2026 repo audit says 55. Third-party page says 53. Birdeye shows about 38 (5.0). | **NOT VERIFIED.** The owner must read the true count from GBP. |
| Average rating | Site and Birdeye say 5.0 | Not verified on Google |
| Recency, monthly velocity, seasonality, per-service coverage, owner response rate | Unknown | Needs a GBP review export. Note the date and service for each review. |
| Competitor review growth | Hometurf about 700–960, Manor 117 (point-in-time snippets) | No velocity data. Track monthly once Local Falcon or Places is connected. |

**Fix the claim first.** If the Google count is under 75, change the site's "75+" (in 90+ places, including the homepage title) to the true figure, rounded down. Then set `GOOGLE_PLACES_API_KEY` and `YARDEX_PLACE_ID` in Vercel so `/api/reviews` returns the live count. That needs the owner: it's a Google Cloud key with billing.

## 2. Target for 2027
The brief's stretch target is 150–175 Google reviews by November 2027. Here is the arithmetic, with stated assumptions:

| Input | Assumption, to replace with real numbers |
|---|---|
| Recurring mowing clients | about 50 (site footer) |
| One-off cleanup, aeration and mulch clients in 2027 | about 80–120 |
| Customers asked | 100% of completed jobs, not only happy ones |
| Share who leave a review when asked well | 25–40% (varies widely) |
| **Expected new reviews in 2027** | **about 35–65** |

- If the true count today is about 55: about **90–120** by November 2027 is realistic. 150–175 would need roughly 2–3× the customer base, or unusually high response.
- If it's about 75: about **110–140**.

**Recommended target:** the current count plus 50, at 4.8★ or higher. Revisit in July with real velocity data. More than the total, the goal is **steady recency**: at least 1 new review per week from April to November, every review answered within 48 hours.

## 3. Workflow (semi-automated, no new paid tools required)
Trigger: a job marked complete (an invoice sent from Wix Invoices, which the site already has installed, or the end of a client's **first** mowing week, then once per season).

1. **Same day, around 2 hours after the job:** send an SMS from the business phone (template S1).
2. **3 days later, if no review:** email (template E1). One reminder only.
3. **Recurring clients:** ask once after their 3rd cut, and once after a seasonal job (cleanup or aeration), so reviews mention different services.
4. **Everyone** gets the same ask. Never filter by satisfaction or send unhappy customers to a private form first ("review gating" breaks Google's policy).
5. **Track it** in a sheet: date asked, channel, service, review received (y/n), and response posted (y/n).
6. **Reply to every review** within 48 hours: thank them, name the service performed, sign as Carter. Reply to negative reviews calmly, offer a fix, and take it offline.

Short review link: GBP → "Ask for reviews" → copy the `g.page/r/...` link. Use it in every template and on invoices.

Possible automation later (needs approval): a Wix Automations trigger on "invoice paid" that sends E1 automatically. Gmail is connected to this session, but **no messages were sent** and none will be without your go-ahead.

## 4. Templates (natural; no keywords, no incentives, no star requests)

**S1 (SMS, same day)**
> Hi [First name], it's Carter from Yardex. Thanks for having us out today for your [service]. If you have a minute, would you leave an honest Google review? It really helps a small local business: [link]. And if anything wasn't right, just reply here and I'll fix it.

**E1 (email, 3 days later)**
> Subject: How did your [service] turn out?
>
> Hi [First name],
>
> Thanks again for choosing Yardex for your [service] on [day]. If you have a moment, an honest Google review would mean a lot to our team. Mentioning what we did and how it turned out helps your neighbours know what to expect.
>
> [link]
>
> If something wasn't up to standard, reply to this email and I'll make it right.
>
> Carter Florence, Yardex Guelph · (519) 835-0774

**Recurring client, end of season**
> Hi [First name], we've loved looking after your lawn this season. If you haven't already, would you share an honest review of how the weekly service has been? [link]. Either way, thanks for sticking with us.

**Review reply examples**
- Positive: "Thanks, [Name]! Glad the fall cleanup left the beds ready for winter. See you for the spring cleanup. – Carter"
- Negative: "[Name], I'm sorry the edging along your walkway wasn't right. I'll call you today to set up a revisit at no charge. – Carter"

## 5. Never
Buying reviews, writing reviews for customers, discounts or draws in exchange for reviews, asking only happy customers, asking for 5 stars, giving customers keyword scripts, reviews from staff or family, or asking for several reviews from one household.
