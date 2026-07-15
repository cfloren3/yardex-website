# Yardex Guelph — Website

Static site, no build step. Deploy by dragging this folder to Netlify (or any static host).

## Quote form -> email (IMPORTANT, one-time setup)
The form posts to FormSubmit and emails carter@yardexguelph.ca directly — works on ANY host.
ACTIVATION: the FIRST submission triggers a confirmation email to carter@yardexguelph.ca.
Click the link in that email once; all future submissions arrive automatically.
Do a test submission right after deploy. Visitors are redirected to /thank-you/.

## Deploy (Vercel)
Repo root contains vercel.json (static output from /dist, caching + security headers).
1. Push to GitHub, then vercel.com -> Add New Project -> import the repo -> Deploy (no build settings needed)
2. Project Settings -> Domains -> add yardexguelph.ca and www.yardexguelph.ca
   (set www as primary so it matches all canonical URLs; Vercel shows the exact DNS records)
3. Test the quote form end to end (see activation above)
4. Google Search Console: submit https://www.yardexguelph.ca/sitemap.xml
5. Update the website link on your Google Business Profile

## Before launch
- Replace review placeholders in reviews/index.html with verbatim Google reviews
- Confirm founding year (site says 2020)
- Add the Quality Business Award page URL where marked
- Add a team photo in about/index.html where marked
- Confirm you offer: Aeration & Overseeding, Weed Control (pages exist for both)

## Blog strategy
11 posts are live. Publish ~1/month going forward; each should target one Guelph search
phrase and link to one service page. Seasonal timing matters: publish spring content in
Feb-Mar, fall content in Aug so Google indexes before search volume peaks.

## Editing
Pages are folder/index.html. Colours/fonts: assets/style.css (:root). Photos: assets/img/.
