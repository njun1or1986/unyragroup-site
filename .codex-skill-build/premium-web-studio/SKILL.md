---
name: premium-web-studio
description: Design and build ultra-premium marketing websites and brand-led web experiences from strategy through deployment. Use when Codex needs to create or improve a website with premium product storytelling, Apple/Tesla-style polish, landing pages, multi-section brand sites, responsive frontend implementation, motion design, performance tuning, accessibility, SEO, launch preparation, or web publication workflows.
---

# Premium Web Studio

## Overview

Design and ship websites that feel high-trust, high-craft, and commercially intentional. Treat Apple and Tesla as reference signals for clarity, spatial discipline, motion restraint, product storytelling, and production quality; do not copy layouts, copywriting, or branded elements directly.

Match the user's language in all user-facing content unless the repo, brief, or brand materials clearly require another language.

## Operating Standard

Aim for work that feels custom, not templated.

Optimize for:

- clear narrative flow before visual flourish
- distinctive art direction before generic SaaS patterns
- fast loading, responsive behavior, and accessibility as part of the premium bar
- conversion clarity without looking salesy or cluttered
- elegant implementation that can survive iteration

Avoid:

- interchangeable hero sections
- default font stacks unless constrained by the existing design system
- purple-on-white "AI product" styling by default
- excessive UI chrome, noisy badges, or dense dashboards unless the brief truly requires them
- copycat reproduction of Apple or Tesla pages

## Workflow

### 1. Frame the website before touching UI

Establish:

- business goal
- target audience
- primary offer or story
- trust signals or proof
- primary call to action
- required pages or sections

If the user does not provide all of this, infer from the repo, existing brand, or market context and state the assumptions after doing the work.

### 2. Choose the right build shape

Use the lightest architecture that fits the outcome:

- Choose a static or mostly-static site when the goal is marketing, storytelling, company presence, waitlists, product launches, or lead generation.
- Choose a framework app when the experience needs authenticated flows, dynamic dashboards, heavy personalization, or frequent client-side state.
- Choose a CMS-backed approach only when non-developers truly need ongoing editing or publishing autonomy.

Favor a simple deployment path. If no platform is specified, default to a modern static/frontend host with previews and easy custom-domain setup.

### 3. Design the narrative spine

Build pages as a sequence of persuasion beats:

1. Immediate value or intrigue
2. Product, service, or brand thesis
3. Depth through features, proof, or experience
4. Objection handling
5. Strong close with a clear CTA

Before implementing, sketch the section order in words. Treat section sequencing as a storytelling system, not a pile of components.

For premium visual direction, read [references/premium-direction.md](references/premium-direction.md).
For ready-made section structures, read [references/page-blueprints.md](references/page-blueprints.md).

### 4. Build an intentional visual system

Define a compact design language before composing pages:

- typography scale
- spacing rhythm
- color system
- surface/material rules
- image and illustration direction
- motion vocabulary
- button, card, and container behavior

Prefer CSS variables or theme tokens so future changes remain easy.

Use expressive, appropriate typography. Default system fonts are acceptable only when they genuinely support the brand or performance goals.

### 5. Implement with premium engineering discipline

Build mobile-first, then refine upward.

Use:

- semantic HTML structure
- accessible focus states and keyboard flows
- fluid spacing and type scales
- image optimization and lazy loading where appropriate
- restrained client-side JavaScript
- smooth but purposeful motion

Keep interactions elegant under slow network and reduced-motion settings.

If working inside an existing codebase or design system, preserve the established patterns and visual language unless the user explicitly asks for a redesign.

### 6. Publish with launch readiness

Before launch, verify:

- responsive behavior across key breakpoints
- performance and Core Web Vitals basics
- metadata, social sharing, and favicon coverage
- accessibility checks for landmarks, labels, contrast, and focus
- analytics, forms, and conversion paths
- domain, DNS, HTTPS, redirects, and preview-production parity

For implementation, QA, SEO, and deployment guidance, read [references/build-and-launch.md](references/build-and-launch.md).

## Design Heuristics

Treat premium design as controlled contrast:

- bold vs quiet
- large-scale simplicity vs small-scale precision
- minimal UI vs rich atmosphere
- restrained palettes vs one intentional accent

Create breathing room. Premium sites often feel expensive because they are willing to leave space around important ideas.

Use motion to reveal hierarchy, not to decorate boredom. Animate entrances, transitions, and parallax only when they strengthen the story and remain smooth on mid-range hardware.

Let typography do real work. If the layout would feel generic without imagery, strengthen type, spacing, and rhythm before adding more components.

## Content and Copy

Write concise, high-confidence copy with a premium tone:

- clear
- specific
- understated
- benefit-led
- free of hype clichés

Avoid filler phrases such as "revolutionary platform," "next-generation solution," or "unlock your potential" unless they are grounded in the brand voice.

## Delivery Pattern

When asked to create a new site or page:

1. Define the narrative and section plan.
2. Define the visual direction and implementation approach.
3. Build the site or page directly.
4. Refine motion, responsiveness, and polish.
5. Check launch readiness and explain assumptions briefly.

When asked to improve an existing site:

1. Identify what currently breaks the premium bar.
2. Preserve what is strong.
3. Upgrade hierarchy, spacing, type, imagery, and motion.
4. Reduce clutter before adding new elements.
5. Leave the codebase cleaner than you found it.

## Reference Map

- Read [references/premium-direction.md](references/premium-direction.md) for visual language, pacing, motion, typography, and premium anti-patterns.
- Read [references/page-blueprints.md](references/page-blueprints.md) for homepage, product page, launch page, and company-site section structures.
- Read [references/build-and-launch.md](references/build-and-launch.md) for delivery flow from discovery through QA, deployment, and post-launch checks.
