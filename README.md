# Unyra Group LLC Website

Premium multilingual corporate website for `UnyraGroup.com`, built with Next.js App Router, TypeScript, and Tailwind CSS.

## Project Admin

Operational and restore documentation is now organized in:

- `UNYRA-WEBSITE-START-HERE.md`
- `project-admin/README.md`
- `project-admin/DEPLOYMENT-AND-DOMAINS.md`
- `project-admin/RESTORE-AND-CHECKPOINTS.md`

## Current Production

- Canonical domain: `https://www.unyragroup.com`
- Non-www domain: `https://unyragroup.com` redirects to the canonical `www` domain
- Vercel production project: `unyragroup-site`

## Stack

- Next.js 16 App Router
- TypeScript
- Tailwind CSS
- Locale-based routing with centralized dictionaries
- Server-backed lead form with placeholder delivery modes for Resend or webhook integrations

## Local Development

1. Install dependencies:

```bash
npm install
```

2. Copy environment variables:

```bash
cp .env.example .env.local
```

3. Start the development server:

```bash
npm run dev
```

4. Build for production:

```bash
npm run build
```

## Locale Routes

- English: `/en`
- Portuguese: `/pt`
- Spanish: `/es`

Inner pages are localized by slug and generated statically for all locales.

## Where to Edit Content

- Company details and launch placeholders: `lib/site.ts`
- English copy: `messages/en.ts`
- Portuguese copy: `messages/pt.ts`
- Spanish copy: `messages/es.ts`
- Shared metadata and structured data helpers: `lib/seo.ts`
- Form delivery logic: `app/api/contact/route.ts`

## Contact Form Delivery

The form supports three modes:

- `CONTACT_PROVIDER=console`
  Best for local development. Submissions are logged on the server.
- `CONTACT_PROVIDER=resend`
  Uses the Resend REST API via `RESEND_API_KEY`, `CONTACT_FORM_FROM`, and `CONTACT_FORM_TO`.
- `CONTACT_PROVIDER=webhook`
  Posts the submission payload to `CONTACT_FORM_WEBHOOK_URL`.

If `CONTACT_PROVIDER` is not set, the route automatically falls back to:

1. `webhook` when `CONTACT_FORM_WEBHOOK_URL` is defined
2. `resend` when `RESEND_API_KEY` is defined
3. `console` otherwise

Recommended setup for Unyra:

- `CONTACT_FORM_TO=sales@unyragroup.com`
- `CONTACT_FORM_FROM=website@unyragroup.com`
- Leave `CONTACT_PROVIDER` unset so the route automatically switches to Resend when `RESEND_API_KEY` is present
- Verify the `unyragroup.com` sender in Resend before going live

## SEO and Structured Data

The site includes:

- Localized metadata for every page and locale
- Open Graph and Twitter image routes
- Canonical and hreflang alternates
- `robots.txt`
- `sitemap.xml`
- JSON-LD for Organization, WebSite, ContactPage, WebPage, and BreadcrumbList

## Replace Before Launch

Update these placeholders before publishing:

- `.env.local`
  Configure Resend or webhook delivery for the contact form
- `lib/site.ts`
  Confirm the production domain if it changes from `https://www.unyragroup.com`
- `app/api/contact/route.ts`
  Extend delivery logic only if you want an additional provider beyond Resend or webhook
- `messages/*.ts`
  Review the privacy policy text and any market messaging you want to refine before launch

## Deployment

This project is structured for Vercel deployment out of the box.

Recommended deployment flow:

1. Push the repository to GitHub
2. Import the project into Vercel
3. Add the environment variables from `.env.example`
4. Deploy
5. Test the contact form delivery and final legal copy before pointing the domain live
