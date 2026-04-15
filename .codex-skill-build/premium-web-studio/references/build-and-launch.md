# Build and Launch

## Discovery to Delivery

Treat website delivery as a product-quality pipeline, not just page assembly.

Recommended order:

1. Clarify business goal, audience, offer, proof, and CTA.
2. Define page list and section order.
3. Define visual direction and component system.
4. Choose stack and hosting path.
5. Implement core layout and responsive system.
6. Add imagery, motion, and polish.
7. Run QA for accessibility, performance, and SEO basics.
8. Prepare deployment, domain, analytics, and handoff.

## Stack Selection

Default to the simplest option that supports the experience:

- Plain HTML/CSS/JS for focused landing pages or microsites
- Next.js, Astro, Remix, or similar for scalable marketing sites and hybrid experiences
- CMS integration only when content-editing needs justify the complexity

Prefer:

- server rendering or static generation for public marketing pages
- minimal client bundles
- predictable asset pipelines

## Implementation Rules

- Build mobile-first.
- Use semantic landmarks and heading order.
- Keep typography and spacing tokenized.
- Keep sections modular, but do not let component reuse flatten the art direction.
- Use `srcset`, modern formats, and compression for imagery.
- Avoid autoplay-heavy or unoptimized background video unless it is mission-critical to the concept.
- Keep animation cheap enough for mid-range devices.

## Premium QA Checklist

### Visual QA

- Check hero impact on desktop and mobile.
- Check line breaks in large headlines.
- Check spacing rhythm between sections.
- Check buttons, cards, and surfaces for consistency.
- Check dark/light transitions and edge cases.

### Responsive QA

- Test small phone, standard phone, tablet, laptop, and large desktop ranges.
- Ensure no horizontal overflow.
- Ensure motion and sticky elements do not degrade on touch devices.
- Ensure layouts do not rely on hover-only affordances.

### Accessibility QA

- Verify keyboard navigation.
- Verify visible focus states.
- Verify alt text for meaningful images.
- Verify contrast on all major surfaces.
- Verify form labels, errors, and status messages.
- Respect `prefers-reduced-motion`.

### Performance QA

- Compress and resize media.
- Avoid large render-blocking bundles.
- Defer non-critical scripts.
- Audit obvious LCP risks in hero media and fonts.
- Keep above-the-fold rendering simple and fast.

### SEO and Metadata QA

- Set title and meta description per page.
- Add Open Graph and Twitter/X sharing basics.
- Add canonical URLs when needed.
- Use meaningful heading structure.
- Ensure sitemap/robots behavior matches the deployment model.

## Deployment Guidance

If no platform is specified, prefer a host with:

- preview deployments
- fast static/frontend delivery
- easy environment management
- straightforward custom domain support
- simple rollback

Common good fits:

- Vercel for Next.js and fast preview-heavy workflows
- Netlify for static/front-end projects and simple forms
- Cloudflare Pages for globally distributed static or edge-focused delivery
- GitHub Pages for very simple static sites when requirements are minimal

## Domain and Launch Tasks

Before launch, verify:

- production environment variables
- analytics or tag manager placement
- form destination and success/error states
- custom domain connection
- DNS records
- HTTPS certificate status
- redirect rules
- favicon and social preview assets

## Post-Launch Checks

- Open the live site on desktop and mobile.
- Confirm the primary CTA path works end to end.
- Confirm no placeholder copy or dev artifacts remain.
- Confirm 404 handling and key redirects.
- Confirm analytics events or page views are firing if configured.

## Handoff Standard

When handing off, summarize:

- what was built
- assumptions made
- where key styling tokens or components live
- how to update content
- how to deploy or publish future changes
