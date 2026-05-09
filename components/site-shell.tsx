import Link from "next/link";
import {
  ArrowRight,
  BriefcaseBusiness,
  Globe2,
  Handshake,
  Leaf,
  Mail,
  MapPin,
  MapPinned,
  Phone,
  Route,
  ShieldCheck,
  Users2
} from "lucide-react";
import BrandMark from "@/components/brand-mark";
import ContactForm from "@/components/contact-form";
import GlobalOperationsMap from "@/components/global-operations-map";
import LanguageSwitcher from "@/components/language-switcher";
import { company, getPath, mainNavKeys, type Dictionary, type Locale, type PageKey } from "@/lib/site";

type SiteShellProps = {
  locale: Locale;
  pageKey: PageKey;
  dictionary: Dictionary;
};

const capabilityIcons = [
  Globe2,
  Route,
  BriefcaseBusiness,
  ShieldCheck,
  Handshake,
  MapPinned
];

const reasonIcons = [ShieldCheck, Globe2, BriefcaseBusiness, Users2, Handshake, Leaf];

export default function SiteShell({
  locale,
  pageKey,
  dictionary
}: SiteShellProps) {
  const contactHref = getPath(locale, "contact");
  const localizedContactItems = getLocalizedContactItems(dictionary);

  return (
    <div className="site-background">
      <a href="#content" className="skip-link">
        {dictionary.labels.skipToContent}
      </a>

      <header className="sticky top-0 z-50 px-4 pt-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl rounded-[1.6rem] border border-[rgba(10,22,34,0.08)] bg-[rgba(255,255,255,0.86)] px-4 py-4 shadow-[0_20px_70px_rgba(10,18,28,0.06)] backdrop-blur-xl sm:px-6">
          <div className="flex flex-col gap-4">
            <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
              <Link href={getPath(locale, "home")} className="shrink-0">
                <BrandMark compact />
              </Link>

              <div className="flex w-full items-center justify-end gap-3 sm:w-auto">
                <div className="hidden sm:block">
                  <LanguageSwitcher
                    locale={locale}
                    pageKey={pageKey}
                    label={dictionary.labels.languageSwitcher}
                  />
                </div>
                <Link href={contactHref} className="button-primary w-full sm:w-auto">
                  {dictionary.labels.primaryCta}
                </Link>
              </div>
            </div>

            <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
              <nav
                aria-label={dictionary.labels.footerNavigation}
                className="flex min-w-0 gap-2 overflow-x-auto pb-1 sm:flex-1"
              >
                {mainNavKeys.map((key) => {
                  const active = key === pageKey;

                  return (
                    <Link
                      key={key}
                      href={getPath(locale, key)}
                      aria-current={active ? "page" : undefined}
                      className={`header-pill ${active ? "header-pill-active" : ""}`}
                    >
                      {dictionary.labels.nav[key]}
                    </Link>
                  );
                })}
              </nav>

              <div className="self-end sm:hidden">
                <LanguageSwitcher
                  locale={locale}
                  pageKey={pageKey}
                  label={dictionary.labels.languageSwitcher}
                />
              </div>
            </div>
          </div>
        </div>
      </header>

      <main id="content" className="pb-36 pt-10 sm:pb-32 sm:pt-12">
        {pageKey === "home" ? (
          <HomeContent locale={locale} dictionary={dictionary} />
        ) : pageKey === "about" ? (
          <AboutContent locale={locale} dictionary={dictionary} />
        ) : pageKey === "markets" ? (
          <MarketsContent locale={locale} dictionary={dictionary} />
        ) : pageKey === "solutions" ? (
          <SolutionsContent locale={locale} dictionary={dictionary} />
        ) : pageKey === "buyers" ? (
          <BuyersContent locale={locale} dictionary={dictionary} />
        ) : pageKey === "producers" ? (
          <ProducersContent locale={locale} dictionary={dictionary} />
        ) : pageKey === "contact" ? (
          <ContactContent locale={locale} dictionary={dictionary} />
        ) : pageKey === "privacy" ? (
          <PrivacyContent locale={locale} dictionary={dictionary} />
        ) : (
          <ThankYouContent locale={locale} dictionary={dictionary} />
        )}
      </main>

      <footer className="px-4 pb-36 sm:px-6 sm:pb-28 lg:px-8">
        <div className="mx-auto max-w-7xl rounded-[2rem] border border-[rgba(10,22,34,0.08)] bg-[rgba(255,255,255,0.9)] p-6 shadow-[0_24px_90px_rgba(10,18,28,0.07)] backdrop-blur-xl sm:p-10">
          <div className="grid gap-10 lg:grid-cols-[minmax(0,1.2fr)_minmax(300px,0.8fr)]">
            <div>
              <BrandMark />
              <p className="mt-6 max-w-2xl text-sm leading-7 text-[var(--muted)] sm:text-base">
                {dictionary.labels.footerSummary}
              </p>
              <div className="mt-6 flex flex-col gap-3 sm:flex-row sm:flex-wrap">
                <Link href={contactHref} className="button-primary">
                  {dictionary.labels.secondaryCta}
                </Link>
                <Link href={getPath(locale, "about")} className="button-secondary">
                  {dictionary.labels.nav.about}
                </Link>
              </div>
            </div>

            <div className="grid gap-8 sm:grid-cols-2">
              <div>
                <h3 className="text-sm font-semibold uppercase tracking-[0.24em] text-[var(--muted)]">
                  {dictionary.labels.footerNavigation}
                </h3>
                <div className="mt-4 grid gap-3">
                  {[...mainNavKeys, "privacy" as const].map((key) => (
                    <Link key={key} href={getPath(locale, key)} className="footer-link">
                      {dictionary.labels.nav[key]}
                    </Link>
                  ))}
                </div>
              </div>

              <div>
                <h3 className="text-sm font-semibold uppercase tracking-[0.24em] text-[var(--muted)]">
                  {dictionary.labels.footerContact}
                </h3>
                <div className="mt-4 grid gap-3 text-sm text-[var(--muted-strong)]">
                  {localizedContactItems.map((item) => (
                    <ContactLine
                      key={item.title}
                      icon={item.icon}
                      label={item.title}
                      value={item.value}
                      href={item.href}
                    />
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </footer>

      <div className="sticky-cta">
        <div className="sticky-cta__inner">
          <span className="hidden text-sm text-white/66 lg:block">{dictionary.labels.tagline}</span>
          <Link href={contactHref} className="button-primary button-primary-inverse">
            {dictionary.labels.stickyCta}
          </Link>
        </div>
      </div>
    </div>
  );
}

function HomeContent({
  locale,
  dictionary
}: {
  locale: Locale;
  dictionary: Dictionary;
}) {
  const hero = dictionary.home.hero;

  return (
    <div className="space-y-20 sm:space-y-24">
      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[minmax(0,1.02fr)_minmax(380px,0.98fr)] lg:items-center">
          <div className="relative isolate space-y-8">
            <div className="inline-flex items-center rounded-full border border-[rgba(10,22,34,0.08)] bg-white/82 px-4 py-2 text-[0.72rem] font-semibold uppercase tracking-[0.24em] text-[var(--muted-strong)] shadow-[0_16px_34px_rgba(10,18,28,0.04)]">
              {hero.experienceLabel}
            </div>
            <div className="space-y-5">
              <p className="eyebrow">{hero.eyebrow}</p>
              <h1 className="font-display max-w-4xl text-[2.45rem] font-semibold leading-[0.94] tracking-[-0.06em] text-[var(--ink)] sm:text-[4.15rem] lg:text-[5.5rem]">
                {hero.title}
              </h1>
              <p className="max-w-2xl text-base leading-8 text-[var(--muted-strong)] sm:text-[1.1rem]">
                {hero.description}
              </p>
              <p className="max-w-2xl text-sm leading-7 text-[var(--muted)]">
                {hero.marketLine}
              </p>
            </div>
            <div className="flex flex-col gap-4 sm:flex-row">
              <Link href={getPath(locale, "contact")} className="button-primary">
                {hero.primaryCta}
              </Link>
              <Link href={getPath(locale, "producers")} className="button-secondary">
                {hero.secondaryCta}
              </Link>
            </div>
            <div className="flex flex-wrap gap-3">
              {hero.highlightPoints.map((item) => (
                <span key={item} className="surface-chip">
                  {item}
                </span>
              ))}
            </div>
          </div>

          <div className="premium-panel-dark relative overflow-hidden rounded-[2.2rem] border border-white/10 p-6 sm:p-10">
            <div className="hero-network" />
            <div className="relative z-10">
              <p className="eyebrow-light">{hero.floatingCardTitle}</p>
              <h2 className="font-display mt-4 text-3xl font-semibold tracking-[-0.04em] text-white sm:text-[2.65rem]">
                {dictionary.labels.tagline}
              </h2>
              <p className="mt-4 max-w-lg text-sm leading-7 text-white/66 sm:text-base">
                {hero.floatingCardDescription}
              </p>

              <div className="mt-10 grid gap-4 sm:grid-cols-2">
                <div className="dark-float-card">
                  <p className="eyebrow-light">{company.experienceBadge}</p>
                  <p className="mt-3 text-xl font-semibold tracking-[-0.03em] text-white">
                    {dictionary.home.hero.experienceLabel}
                  </p>
                </div>
                <div className="dark-float-card dark-float-card-offset">
                  <p className="eyebrow-light">{dictionary.home.network.eyebrow}</p>
                  <p className="mt-3 text-xl font-semibold tracking-[-0.03em] text-white">
                    {dictionary.home.network.cards.map((card) => card.title).join(", ")}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto grid max-w-7xl gap-4 md:grid-cols-2 xl:grid-cols-4">
          {dictionary.home.trustStrip.map((item) => (
            <article key={item.title} className="premium-card h-full">
              <h3 className="font-display mt-4 text-xl font-semibold tracking-[-0.03em] text-[var(--ink)]">
                {item.title}
              </h3>
              <p className="mt-3 text-sm leading-7 text-[var(--muted)]">{item.description}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[minmax(0,1.05fr)_minmax(320px,0.95fr)]">
          <div className="space-y-5">
            <SectionHeading
              eyebrow={dictionary.home.aboutPreview.eyebrow}
              title={dictionary.home.aboutPreview.title}
              description={dictionary.home.aboutPreview.description}
            />
            {dictionary.home.aboutPreview.paragraphs.map((paragraph) => (
              <p key={paragraph} className="text-base leading-8 text-[var(--muted-strong)]">
                {paragraph}
              </p>
            ))}
          </div>
          <div className="editorial-card">
            <p className="text-sm font-semibold uppercase tracking-[0.24em] text-[var(--accent-strong)]">
              {dictionary.home.aboutPreview.eyebrow}
            </p>
            <div className="mt-5 grid gap-4">
              {dictionary.home.aboutPreview.markers.map((marker) => (
                <div key={marker} className="feature-line">
                  <span className="feature-line__dot" />
                  <span>{marker}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <SectionHeading
            eyebrow={dictionary.home.solutions.eyebrow}
            title={dictionary.home.solutions.title}
            description={dictionary.home.solutions.description}
          />
          <div className="mt-10 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {dictionary.home.solutions.items.map((item, index) => {
              const Icon = capabilityIcons[index % capabilityIcons.length];

              return (
                <article key={item.title} className="premium-card">
                  <span className="icon-badge">
                    <Icon className="h-4 w-4" />
                  </span>
                  <h3 className="font-display mt-5 text-[1.28rem] font-semibold tracking-[-0.03em] text-[var(--ink)]">
                    {item.title}
                  </h3>
                  <p className="mt-3 text-sm leading-7 text-[var(--muted)]">{item.description}</p>
                </article>
              );
            })}
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto grid max-w-7xl gap-8 lg:grid-cols-[minmax(0,0.92fr)_minmax(0,1.08fr)]">
          <div className="premium-panel-dark rounded-[2rem] border border-white/10 p-8 sm:p-10">
            <SectionHeading
              eyebrow={dictionary.home.expertise.eyebrow}
              title={dictionary.home.expertise.title}
              description={dictionary.home.expertise.description}
              light
            />
            <div className="mt-8 grid gap-4">
              {dictionary.home.expertise.pillars.map((item) => (
                <article key={item.title} className="dark-list-card">
                  <h3 className="font-display text-xl font-semibold tracking-[-0.03em] text-white">
                    {item.title}
                  </h3>
                  <p className="mt-3 text-sm leading-7 text-white/64">{item.description}</p>
                </article>
              ))}
            </div>
          </div>
          <div className="premium-card flex flex-col justify-between">
            <div>
              <p className="eyebrow">{dictionary.home.expertise.asideTitle}</p>
              <p className="mt-5 text-xl leading-9 text-[var(--muted-strong)] sm:text-2xl">
                {dictionary.home.expertise.asideText}
              </p>
            </div>
            <div className="mt-8 grid gap-3 text-sm text-[var(--muted)]">
              {dictionary.home.network.cards.map((card) => (
                <div key={card.key} className="surface-chip justify-start">
                  {card.title}
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <GlobalOperationsMap
            eyebrow={dictionary.home.network.eyebrow}
            title={dictionary.home.network.title}
            description={dictionary.home.network.description}
            cards={dictionary.home.network.cards}
          />
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <SectionHeading
            eyebrow={dictionary.home.audience.eyebrow}
            title={dictionary.home.audience.title}
            description={dictionary.home.audience.description}
          />
          <div className="mt-10 grid gap-5 lg:grid-cols-2">
            <AudienceCard href={getPath(locale, "buyers")} card={dictionary.home.audience.buyers} />
            <AudienceCard href={getPath(locale, "producers")} card={dictionary.home.audience.producers} />
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <SectionHeading
            eyebrow={dictionary.home.why.eyebrow}
            title={dictionary.home.why.title}
            description={dictionary.home.why.description}
          />
          <div className="mt-10 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {dictionary.home.why.items.map((item, index) => {
              const Icon = reasonIcons[index % reasonIcons.length];

              return (
                <article key={item.title} className="premium-card">
                  <span className="icon-badge">
                    <Icon className="h-4 w-4" />
                  </span>
                  <h3 className="font-display mt-5 text-[1.2rem] font-semibold tracking-[-0.03em] text-[var(--ink)]">
                    {item.title}
                  </h3>
                  <p className="mt-3 text-sm leading-7 text-[var(--muted)]">{item.description}</p>
                </article>
              );
            })}
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl rounded-[2rem] border border-[rgba(10,22,34,0.08)] bg-[linear-gradient(135deg,rgba(9,19,31,1),rgba(17,38,52,0.96))] px-6 py-8 shadow-[0_28px_90px_rgba(9,18,28,0.2)] sm:px-10 sm:py-10 lg:flex lg:items-end lg:justify-between">
          <div className="max-w-3xl">
            <p className="eyebrow-light">{company.experienceBadge}</p>
            <h2 className="font-display mt-4 text-[2.15rem] font-semibold tracking-[-0.04em] text-white sm:text-4xl">
              {dictionary.home.ctaBand.title}
            </h2>
            <p className="mt-4 text-sm leading-7 text-white/66 sm:text-base">
              {dictionary.home.ctaBand.description}
            </p>
          </div>
          <div className="mt-8 flex flex-col gap-4 sm:flex-row lg:mt-0">
            <Link href={getPath(locale, "contact")} className="button-primary button-primary-inverse">
              {dictionary.home.ctaBand.primaryCta}
            </Link>
            <Link href={getPath(locale, "buyers")} className="button-secondary button-secondary-dark">
              {dictionary.home.ctaBand.secondaryCta}
            </Link>
          </div>
        </div>
      </section>

      <LeadSection
        locale={locale}
        source="home"
        dictionary={dictionary}
        intro={dictionary.home.contact}
      />
    </div>
  );
}

function AboutContent({
  locale,
  dictionary
}: {
  locale: Locale;
  dictionary: Dictionary;
}) {
  return (
    <div className="space-y-20 sm:space-y-24">
      <PageHero
        locale={locale}
        pageKey="about"
        dictionary={dictionary}
        eyebrow={dictionary.about.hero.eyebrow}
        title={dictionary.about.hero.title}
        description={dictionary.about.hero.description}
      />

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[minmax(0,1.05fr)_minmax(320px,0.95fr)]">
          <div className="space-y-5">
            <SectionHeading
              eyebrow={dictionary.about.overview.eyebrow}
              title={dictionary.about.overview.title}
              description={dictionary.about.overview.description}
            />
            {dictionary.about.overview.paragraphs.map((paragraph) => (
              <p key={paragraph} className="text-base leading-8 text-[var(--muted-strong)]">
                {paragraph}
              </p>
            ))}
          </div>
          <div className="premium-card">
            <p className="eyebrow">{dictionary.labels.tagline}</p>
            <p className="mt-5 text-xl leading-9 text-[var(--muted-strong)]">
              {dictionary.about.overview.description}
            </p>
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <SectionHeading
            eyebrow={dictionary.about.values.eyebrow}
            title={dictionary.about.values.title}
            description={dictionary.about.values.description}
          />
          <div className="mt-10 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {dictionary.about.values.items.map((item, index) => {
              const Icon = reasonIcons[index % reasonIcons.length];

              return (
                <article key={item.title} className="premium-card">
                  <span className="icon-badge">
                    <Icon className="h-4 w-4" />
                  </span>
                  <h3 className="font-display mt-5 text-[1.2rem] font-semibold tracking-[-0.03em] text-[var(--ink)]">
                    {item.title}
                  </h3>
                  <p className="mt-3 text-sm leading-7 text-[var(--muted)]">{item.description}</p>
                </article>
              );
            })}
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto grid max-w-7xl gap-8 lg:grid-cols-[minmax(0,1.08fr)_minmax(340px,0.92fr)]">
          <div className="premium-panel-dark rounded-[2rem] border border-white/10 p-6 sm:p-10">
            <SectionHeading
              eyebrow={dictionary.about.experience.eyebrow}
              title={dictionary.about.experience.title}
              description={dictionary.about.experience.description}
              light
            />
            <div className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
              {dictionary.about.experience.pillars.map((item) => (
                <article key={item.title} className="dark-list-card">
                  <h3 className="font-display text-xl font-semibold tracking-[-0.03em] text-white">
                    {item.title}
                  </h3>
                  <p className="mt-3 text-sm leading-7 text-white/64">{item.description}</p>
                </article>
              ))}
            </div>
          </div>
          <div className="editorial-card">
            <p className="text-sm font-semibold uppercase tracking-[0.24em] text-[var(--accent-strong)]">
              {company.experienceBadge}
            </p>
            <div className="mt-6 grid gap-4">
              {dictionary.about.experience.timeline.map((item) => (
                <div key={item} className="feature-line">
                  <span className="feature-line__dot" />
                  <span>{item}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl rounded-[2rem] border border-[rgba(10,22,34,0.08)] bg-white/88 p-6 shadow-[0_20px_70px_rgba(10,18,28,0.05)] backdrop-blur-xl sm:p-10">
          <h2 className="font-display text-3xl font-semibold tracking-[-0.04em] text-[var(--ink)] sm:text-4xl">
            {dictionary.about.relationships.title}
          </h2>
          <p className="mt-4 max-w-3xl text-sm leading-7 text-[var(--muted)] sm:text-base">
            {dictionary.about.relationships.description}
          </p>
          <div className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {dictionary.about.relationships.bullets.map((item) => (
              <div key={item} className="surface-chip justify-start rounded-[1rem] px-4 py-4 text-sm normal-case tracking-normal">
                {item}
              </div>
            ))}
          </div>
        </div>
      </section>

      <SimpleCtaBand
        locale={locale}
        buttonLabel={dictionary.labels.secondaryCta}
        title={dictionary.about.ctaBand.title}
        description={dictionary.about.ctaBand.description}
      />
    </div>
  );
}

function MarketsContent({
  locale,
  dictionary
}: {
  locale: Locale;
  dictionary: Dictionary;
}) {
  return (
    <div className="space-y-20 sm:space-y-24">
      <PageHero
        locale={locale}
        pageKey="markets"
        dictionary={dictionary}
        eyebrow={dictionary.markets.hero.eyebrow}
        title={dictionary.markets.hero.title}
        description={dictionary.markets.hero.description}
      />

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <GlobalOperationsMap
            eyebrow={dictionary.markets.map.eyebrow}
            title={dictionary.markets.map.title}
            description={dictionary.markets.map.description}
            cards={dictionary.markets.map.cards}
          />
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <SectionHeading
            eyebrow={dictionary.markets.connectivity.eyebrow}
            title={dictionary.markets.connectivity.title}
            description={dictionary.markets.connectivity.description}
          />
          <div className="mt-10 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {dictionary.markets.connectivity.items.map((item, index) => {
              const Icon = capabilityIcons[index % capabilityIcons.length];

              return (
                <article key={item.title} className="premium-card">
                  <span className="icon-badge">
                    <Icon className="h-4 w-4" />
                  </span>
                  <h3 className="font-display mt-5 text-[1.2rem] font-semibold tracking-[-0.03em] text-[var(--ink)]">
                    {item.title}
                  </h3>
                  <p className="mt-3 text-sm leading-7 text-[var(--muted)]">{item.description}</p>
                </article>
              );
            })}
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl rounded-[2rem] border border-[rgba(10,22,34,0.08)] bg-white/88 p-6 shadow-[0_20px_70px_rgba(10,18,28,0.05)] backdrop-blur-xl sm:p-10">
          <h2 className="font-display text-3xl font-semibold tracking-[-0.04em] text-[var(--ink)] sm:text-4xl">
            {dictionary.markets.opportunity.title}
          </h2>
          <p className="mt-4 max-w-3xl text-sm leading-7 text-[var(--muted)] sm:text-base">
            {dictionary.markets.opportunity.description}
          </p>
          <div className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {dictionary.markets.opportunity.bullets.map((item) => (
              <div key={item} className="surface-chip justify-start rounded-[1rem] px-4 py-4 text-sm normal-case tracking-normal">
                {item}
              </div>
            ))}
          </div>
        </div>
      </section>

      <SimpleCtaBand
        locale={locale}
        buttonLabel={dictionary.labels.secondaryCta}
        title={dictionary.markets.ctaBand.title}
        description={dictionary.markets.ctaBand.description}
      />
    </div>
  );
}

function SolutionsContent({
  locale,
  dictionary
}: {
  locale: Locale;
  dictionary: Dictionary;
}) {
  return (
    <div className="space-y-20 sm:space-y-24">
      <PageHero
        locale={locale}
        pageKey="solutions"
        dictionary={dictionary}
        eyebrow={dictionary.solutions.hero.eyebrow}
        title={dictionary.solutions.hero.title}
        description={dictionary.solutions.hero.description}
      />

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <SectionHeading
            eyebrow={dictionary.solutions.capabilities.eyebrow}
            title={dictionary.solutions.capabilities.title}
            description={dictionary.solutions.capabilities.description}
          />
          <div className="mt-10 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {dictionary.solutions.capabilities.items.map((item, index) => {
              const Icon = capabilityIcons[index % capabilityIcons.length];

              return (
                <article key={item.title} className="premium-card">
                  <span className="icon-badge">
                    <Icon className="h-4 w-4" />
                  </span>
                  <h3 className="font-display mt-5 text-[1.2rem] font-semibold tracking-[-0.03em] text-[var(--ink)]">
                    {item.title}
                  </h3>
                  <p className="mt-3 text-sm leading-7 text-[var(--muted)]">{item.description}</p>
                </article>
              );
            })}
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl rounded-[2rem] border border-[rgba(10,22,34,0.08)] bg-white/88 p-6 shadow-[0_20px_70px_rgba(10,18,28,0.05)] backdrop-blur-xl sm:p-10">
          <SectionHeading
            eyebrow={dictionary.solutions.process.eyebrow}
            title={dictionary.solutions.process.title}
            description={dictionary.solutions.process.description}
          />
          <div className="mt-10 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {dictionary.solutions.process.steps.map((step, index) => (
              <article key={step.title} className="premium-card bg-[rgba(247,243,236,0.75)]">
                <p className="text-[0.72rem] font-semibold uppercase tracking-[0.24em] text-[var(--accent-strong)]">
                  0{index + 1}
                </p>
                <h3 className="font-display mt-5 text-[1.2rem] font-semibold tracking-[-0.03em] text-[var(--ink)]">
                  {step.title}
                </h3>
                <p className="mt-3 text-sm leading-7 text-[var(--muted)]">{step.description}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl rounded-[2rem] border border-white/10 bg-[linear-gradient(135deg,rgba(9,19,31,1),rgba(17,38,52,0.96))] px-6 py-8 shadow-[0_28px_90px_rgba(9,18,28,0.2)] sm:px-10 sm:py-10">
          <h2 className="font-display text-3xl font-semibold tracking-[-0.04em] text-white sm:text-4xl">
            {dictionary.solutions.expertise.title}
          </h2>
          <p className="mt-4 max-w-3xl text-sm leading-7 text-white/66 sm:text-base">
            {dictionary.solutions.expertise.description}
          </p>
          <div className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {dictionary.solutions.expertise.bullets.map((item) => (
              <div key={item} className="surface-chip surface-chip-dark justify-start rounded-[1rem] px-4 py-4 text-sm normal-case tracking-normal">
                {item}
              </div>
            ))}
          </div>
        </div>
      </section>

      <SimpleCtaBand
        locale={locale}
        buttonLabel={dictionary.labels.secondaryCta}
        title={dictionary.solutions.ctaBand.title}
        description={dictionary.solutions.ctaBand.description}
      />
    </div>
  );
}

function BuyersContent({
  locale,
  dictionary
}: {
  locale: Locale;
  dictionary: Dictionary;
}) {
  return (
    <div className="space-y-20 sm:space-y-24">
      <PageHero
        locale={locale}
        pageKey="buyers"
        dictionary={dictionary}
        eyebrow={dictionary.buyers.hero.eyebrow}
        title={dictionary.buyers.hero.title}
        description={dictionary.buyers.hero.description}
      />

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <SectionHeading
            eyebrow={dictionary.buyers.priorities.eyebrow}
            title={dictionary.buyers.priorities.title}
            description={dictionary.buyers.priorities.description}
          />
          <div className="mt-10 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
            {dictionary.buyers.priorities.items.map((item, index) => {
              const Icon = capabilityIcons[index % capabilityIcons.length];

              return (
                <article key={item.title} className="premium-card">
                  <span className="icon-badge">
                    <Icon className="h-4 w-4" />
                  </span>
                  <h3 className="font-display mt-5 text-[1.2rem] font-semibold tracking-[-0.03em] text-[var(--ink)]">
                    {item.title}
                  </h3>
                  <p className="mt-3 text-sm leading-7 text-[var(--muted)]">{item.description}</p>
                </article>
              );
            })}
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl rounded-[2rem] border border-[rgba(10,22,34,0.08)] bg-white/88 p-6 shadow-[0_20px_70px_rgba(10,18,28,0.05)] backdrop-blur-xl sm:p-10">
          <SectionHeading
            eyebrow={dictionary.buyers.approach.eyebrow}
            title={dictionary.buyers.approach.title}
            description={dictionary.buyers.approach.description}
          />
          <div className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {dictionary.buyers.approach.bullets.map((item) => (
              <div key={item} className="surface-chip justify-start rounded-[1rem] px-4 py-4 text-sm normal-case tracking-normal">
                {item}
              </div>
            ))}
          </div>
        </div>
      </section>

      <LeadSection
        locale={locale}
        source="buyers"
        dictionary={dictionary}
        intro={{
          eyebrow: dictionary.form.badge,
          title: dictionary.buyers.formPanel.title,
          description: dictionary.buyers.formPanel.description
        }}
      />
    </div>
  );
}

function ProducersContent({
  locale,
  dictionary
}: {
  locale: Locale;
  dictionary: Dictionary;
}) {
  return (
    <div className="space-y-20 sm:space-y-24">
      <PageHero
        locale={locale}
        pageKey="producers"
        dictionary={dictionary}
        eyebrow={dictionary.producers.hero.eyebrow}
        title={dictionary.producers.hero.title}
        description={dictionary.producers.hero.description}
      />

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <SectionHeading
            eyebrow={dictionary.producers.priorities.eyebrow}
            title={dictionary.producers.priorities.title}
            description={dictionary.producers.priorities.description}
          />
          <div className="mt-10 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
            {dictionary.producers.priorities.items.map((item, index) => {
              const Icon = capabilityIcons[index % capabilityIcons.length];

              return (
                <article key={item.title} className="premium-card">
                  <span className="icon-badge">
                    <Icon className="h-4 w-4" />
                  </span>
                  <h3 className="font-display mt-5 text-[1.2rem] font-semibold tracking-[-0.03em] text-[var(--ink)]">
                    {item.title}
                  </h3>
                  <p className="mt-3 text-sm leading-7 text-[var(--muted)]">{item.description}</p>
                </article>
              );
            })}
          </div>
        </div>
      </section>

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl rounded-[2rem] border border-[rgba(10,22,34,0.08)] bg-white/88 p-6 shadow-[0_20px_70px_rgba(10,18,28,0.05)] backdrop-blur-xl sm:p-10">
          <SectionHeading
            eyebrow={dictionary.producers.approach.eyebrow}
            title={dictionary.producers.approach.title}
            description={dictionary.producers.approach.description}
          />
          <div className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {dictionary.producers.approach.bullets.map((item) => (
              <div key={item} className="surface-chip justify-start rounded-[1rem] px-4 py-4 text-sm normal-case tracking-normal">
                {item}
              </div>
            ))}
          </div>
        </div>
      </section>

      <LeadSection
        locale={locale}
        source="producers"
        dictionary={dictionary}
        intro={{
          eyebrow: dictionary.form.badge,
          title: dictionary.producers.formPanel.title,
          description: dictionary.producers.formPanel.description
        }}
      />
    </div>
  );
}

function ContactContent({
  locale,
  dictionary
}: {
  locale: Locale;
  dictionary: Dictionary;
}) {
  const localizedContactItems = getLocalizedContactItems(dictionary);

  return (
    <div className="space-y-20 sm:space-y-24">
      <PageHero
        locale={locale}
        pageKey="contact"
        dictionary={dictionary}
        eyebrow={dictionary.contact.hero.eyebrow}
        title={dictionary.contact.hero.title}
        description={dictionary.contact.hero.description}
      />

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto grid max-w-7xl gap-4 md:grid-cols-2 xl:grid-cols-4">
          {localizedContactItems.map((item) => (
            <article key={item.title} className="premium-card">
              <span className="icon-badge">
                <item.icon className="h-4 w-4" />
              </span>
              <h3 className="font-display mt-5 text-[1.2rem] font-semibold tracking-[-0.03em] text-[var(--ink)]">
                {item.title}
              </h3>
              {item.href ? (
                <a
                  href={item.href}
                  className="mt-3 inline-flex text-sm leading-7 text-[var(--muted)] underline decoration-[rgba(10,22,34,0.18)] underline-offset-4 transition-colors hover:text-[var(--ink)]"
                >
                  {item.value}
                </a>
              ) : (
                <p className="mt-3 text-sm leading-7 text-[var(--muted)]">{item.value}</p>
              )}
            </article>
          ))}
        </div>
      </section>

      <LeadSection
        locale={locale}
        source="contact"
        dictionary={dictionary}
        intro={{
          eyebrow: dictionary.form.badge,
          title: dictionary.form.title,
          description: dictionary.form.description
        }}
      />

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl rounded-[2rem] border border-[rgba(10,22,34,0.08)] bg-white/88 p-6 shadow-[0_20px_70px_rgba(10,18,28,0.05)] backdrop-blur-xl sm:p-10">
          <h2 className="font-display text-3xl font-semibold tracking-[-0.04em] text-[var(--ink)] sm:text-4xl">
            {dictionary.contact.response.title}
          </h2>
          <p className="mt-4 max-w-3xl text-sm leading-7 text-[var(--muted)] sm:text-base">
            {dictionary.contact.response.description}
          </p>
          <div className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
            {dictionary.contact.response.bullets.map((item) => (
              <div key={item} className="surface-chip justify-start rounded-[1rem] px-4 py-4 text-sm normal-case tracking-normal">
                {item}
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}

function PrivacyContent({
  locale,
  dictionary
}: {
  locale: Locale;
  dictionary: Dictionary;
}) {
  return (
    <div className="space-y-20 sm:space-y-24">
      <PageHero
        locale={locale}
        pageKey="privacy"
        dictionary={dictionary}
        eyebrow={dictionary.privacy.hero.eyebrow}
        title={dictionary.privacy.hero.title}
        description={dictionary.privacy.hero.description}
      />

      <section className="px-4 sm:px-6 lg:px-8">
        <div className="mx-auto grid max-w-5xl gap-5">
          {dictionary.privacy.sections.map((section) => (
            <article key={section.title} className="premium-card">
              <h2 className="font-display text-2xl font-semibold tracking-[-0.03em] text-[var(--ink)]">
                {section.title}
              </h2>
              <div className="mt-4 grid gap-4">
                {section.paragraphs.map((paragraph) => (
                  <p key={paragraph} className="text-sm leading-7 text-[var(--muted)] sm:text-base">
                    {paragraph}
                  </p>
                ))}
              </div>
            </article>
          ))}
        </div>
      </section>

      <SimpleCtaBand
        locale={locale}
        buttonLabel={dictionary.labels.backToHome}
        href={getPath(locale, "home")}
        title={dictionary.labels.privacyNote}
        description={dictionary.labels.footerLaunchNote}
      />
    </div>
  );
}

function ThankYouContent({
  locale,
  dictionary
}: {
  locale: Locale;
  dictionary: Dictionary;
}) {
  return (
    <section className="px-4 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-4xl rounded-[2rem] border border-[rgba(10,22,34,0.08)] bg-white/9 p-2 shadow-[0_20px_70px_rgba(10,18,28,0.06)]">
        <div className="premium-panel-dark rounded-[1.8rem] p-7 text-center sm:p-14">
          <p className="eyebrow-light">{dictionary.thankYou.eyebrow}</p>
          <h1 className="font-display mt-5 text-[2.4rem] font-semibold tracking-[-0.05em] text-white sm:text-[3.5rem]">
            {dictionary.thankYou.title}
          </h1>
          <p className="mx-auto mt-5 max-w-2xl text-sm leading-7 text-white/66 sm:text-base">
            {dictionary.thankYou.description}
          </p>
          <div className="mt-10 flex flex-col justify-center gap-4 sm:flex-row">
            <Link href={getPath(locale, "home")} className="button-primary button-primary-inverse">
              {dictionary.thankYou.primaryCta}
            </Link>
            <Link href={getPath(locale, "contact")} className="button-secondary button-secondary-dark">
              {dictionary.thankYou.secondaryCta}
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}

function LeadSection({
  locale,
  source,
  dictionary,
  intro
}: {
  locale: Locale;
  source: PageKey;
  dictionary: Dictionary;
  intro: {
    eyebrow: string;
    title: string;
    description: string;
    bullets?: string[];
  };
}) {
  return (
    <section className="px-4 sm:px-6 lg:px-8">
      <div className="mx-auto grid max-w-7xl gap-8 lg:grid-cols-[minmax(0,0.88fr)_minmax(0,1.12fr)]">
        <div className="premium-card h-full">
          <SectionHeading
            eyebrow={intro.eyebrow}
            title={intro.title}
            description={intro.description}
          />
          <div className="mt-8 grid gap-4">
            {(intro.bullets ?? dictionary.home.contact.bullets).map((item) => (
              <div key={item} className="feature-line">
                <span className="feature-line__dot" />
                <span>{item}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="premium-panel-dark rounded-[2rem] border border-white/10 p-6 sm:p-10">
          <ContactForm locale={locale} source={source} copy={dictionary.form} />
        </div>
      </div>
    </section>
  );
}

function PageHero({
  locale,
  pageKey,
  dictionary,
  eyebrow,
  title,
  description
}: {
  locale: Locale;
  pageKey: PageKey;
  dictionary: Dictionary;
  eyebrow: string;
  title: string;
  description: string;
}) {
  return (
    <section className="px-4 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl rounded-[2.2rem] border border-[rgba(10,22,34,0.08)] bg-[linear-gradient(135deg,rgba(255,255,255,0.96),rgba(244,238,230,0.92))] px-6 py-8 shadow-[0_24px_80px_rgba(10,18,28,0.06)] sm:px-10 sm:py-10 lg:flex lg:items-end lg:justify-between">
        <div className="max-w-4xl">
          <Breadcrumbs locale={locale} pageKey={pageKey} dictionary={dictionary} />
          <p className="eyebrow mt-6">{eyebrow}</p>
          <h1 className="font-display mt-5 text-[2.35rem] font-semibold leading-[0.96] tracking-[-0.06em] text-[var(--ink)] sm:text-[4rem] lg:text-[4.7rem]">
            {title}
          </h1>
          <p className="mt-5 max-w-3xl text-base leading-8 text-[var(--muted-strong)] sm:text-[1.08rem]">
            {description}
          </p>
        </div>

        <div className="mt-8 grid gap-4 lg:mt-0 lg:max-w-sm">
          <div className="surface-chip justify-start rounded-[1rem] px-4 py-4 text-sm normal-case tracking-normal">
            {dictionary.home.hero.experienceLabel}
          </div>
          <div className="surface-chip justify-start rounded-[1rem] px-4 py-4 text-sm normal-case tracking-normal">
            {dictionary.labels.tagline}
          </div>
        </div>
      </div>
    </section>
  );
}

function SectionHeading({
  eyebrow,
  title,
  description,
  light = false
}: {
  eyebrow: string;
  title: string;
  description: string;
  light?: boolean;
}) {
  return (
    <div className="max-w-3xl">
      <p className={light ? "eyebrow-light" : "eyebrow"}>{eyebrow}</p>
      <h2
        className={`font-display mt-4 text-3xl font-semibold tracking-[-0.04em] sm:text-4xl ${
          light ? "text-white" : "text-[var(--ink)]"
        }`}
      >
        {title}
      </h2>
      <p
        className={`mt-4 text-sm leading-7 sm:text-base ${
          light ? "text-white/66" : "text-[var(--muted)]"
        }`}
      >
        {description}
      </p>
    </div>
  );
}

function AudienceCard({
  href,
  card
}: {
  href: string;
  card: Dictionary["home"]["audience"]["buyers"];
}) {
  return (
    <article className="premium-card">
      <p className="eyebrow">{card.eyebrow}</p>
      <h3 className="font-display mt-5 text-2xl font-semibold tracking-[-0.04em] text-[var(--ink)]">
        {card.title}
      </h3>
      <p className="mt-4 text-sm leading-7 text-[var(--muted)] sm:text-base">
        {card.description}
      </p>
      <div className="mt-6 grid gap-3">
        {card.bullets.map((item) => (
          <div key={item} className="feature-line">
            <span className="feature-line__dot" />
            <span>{item}</span>
          </div>
        ))}
      </div>
      <Link href={href} className="button-secondary mt-8 inline-flex">
        {card.cta}
      </Link>
    </article>
  );
}

function Breadcrumbs({
  locale,
  pageKey,
  dictionary
}: {
  locale: Locale;
  pageKey: PageKey;
  dictionary: Dictionary;
}) {
  if (pageKey === "home") {
    return null;
  }

  return (
    <nav
      aria-label={dictionary.labels.breadcrumbSeparator}
      className="flex flex-wrap items-center gap-2 text-sm text-[var(--muted)]"
    >
      <Link href={getPath(locale, "home")} className="hover:text-[var(--ink)]">
        {dictionary.labels.home}
      </Link>
      <span>/</span>
      <span className="text-[var(--muted-strong)]">{dictionary.labels.nav[pageKey]}</span>
    </nav>
  );
}

function SimpleCtaBand({
  locale,
  buttonLabel,
  href,
  title,
  description
}: {
  locale: Locale;
  buttonLabel: string;
  href?: string;
  title: string;
  description: string;
}) {
  return (
    <section className="px-4 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl rounded-[2rem] border border-white/10 bg-[linear-gradient(135deg,rgba(9,19,31,1),rgba(17,38,52,0.96))] px-6 py-8 shadow-[0_28px_90px_rgba(9,18,28,0.2)] sm:px-10 sm:py-10 lg:flex lg:items-end lg:justify-between">
        <div className="max-w-3xl">
          <p className="eyebrow-light">{company.experienceBadge}</p>
          <h2 className="font-display mt-4 text-3xl font-semibold tracking-[-0.04em] text-white sm:text-4xl">
            {title}
          </h2>
          <p className="mt-4 text-sm leading-7 text-white/66 sm:text-base">{description}</p>
        </div>
        <div className="mt-8 lg:mt-0">
          <Link href={href ?? getPath(locale, "contact")} className="button-primary button-primary-inverse">
            {buttonLabel}
          </Link>
        </div>
      </div>
    </section>
  );
}

type LocalizedContactItem = {
  title: string;
  value: string;
  href?: string;
  icon: typeof Mail;
};

function ContactLine({
  icon: Icon,
  label,
  value,
  href
}: {
  icon: typeof Mail;
  label: string;
  value: string;
  href?: string;
}) {
  return (
    <div className="flex items-start gap-3">
      <span className="mt-1 inline-flex h-8 w-8 items-center justify-center rounded-full bg-[rgba(10,22,34,0.06)] text-[var(--ink)]">
        <Icon className="h-4 w-4" />
      </span>
      <div>
        <p className="text-[0.7rem] font-semibold uppercase tracking-[0.2em] text-[var(--muted)]">
          {label}
        </p>
        {href ? (
          <a
            href={href}
            className="mt-1 inline-flex text-sm leading-6 text-[var(--muted-strong)] underline decoration-[rgba(10,22,34,0.16)] underline-offset-4 transition-colors hover:text-[var(--ink)]"
          >
            {value}
          </a>
        ) : (
          <p className="mt-1 text-sm leading-6 text-[var(--muted-strong)]">{value}</p>
        )}
      </div>
    </div>
  );
}

function getLocalizedContactItems(dictionary: Dictionary) {
  return [
    {
      title: dictionary.contact.contactCards[0]?.title ?? company.contact.companyEmailLabel,
      value: company.contact.companyEmail,
      href: `mailto:${company.contact.companyEmail}`,
      icon: Mail
    },
    {
      title: dictionary.contact.contactCards[1]?.title ?? company.contact.phoneLabel,
      value: company.contact.phoneDisplay,
      href: company.contact.phoneHref,
      icon: Phone
    },
    {
      title: dictionary.contact.contactCards[2]?.title ?? company.contact.locationLabel,
      value: company.contact.location,
      icon: MapPin
    }
  ] satisfies LocalizedContactItem[];
}
