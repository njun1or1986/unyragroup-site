export const locales = ["en", "pt", "es"] as const;

export type Locale = (typeof locales)[number];

export const defaultLocale: Locale = "en";

export type PageKey =
  | "home"
  | "about"
  | "markets"
  | "solutions"
  | "buyers"
  | "producers"
  | "contact"
  | "privacy"
  | "thankYou";

export type InnerPageKey = Exclude<PageKey, "home">;

export type MarketKey =
  | "unitedStates"
  | "canada"
  | "brazil"
  | "chile"
  | "argentina"
  | "egypt"
  | "turkey"
  | "europe"
  | "china";

export const pageOrder: PageKey[] = [
  "home",
  "about",
  "markets",
  "solutions",
  "buyers",
  "producers",
  "contact",
  "privacy",
  "thankYou"
];

export const mainNavKeys: PageKey[] = [
  "about",
  "markets",
  "solutions",
  "buyers",
  "producers",
  "contact"
];

export const localeMeta = {
  en: {
    label: "English",
    shortLabel: "EN",
    languageTag: "en-US",
    openGraphLocale: "en_US"
  },
  pt: {
    label: "Português",
    shortLabel: "PT",
    languageTag: "pt-BR",
    openGraphLocale: "pt_BR"
  },
  es: {
    label: "Español",
    shortLabel: "ES",
    languageTag: "es-ES",
    openGraphLocale: "es_ES"
  }
} as const satisfies Record<
  Locale,
  {
    label: string;
    shortLabel: string;
    languageTag: string;
    openGraphLocale: string;
  }
>;

export const innerPageSlugs = {
  en: {
    about: "about",
    markets: "markets-global-network",
    solutions: "solutions",
    buyers: "for-buyers",
    producers: "for-producers-exporters",
    contact: "contact",
    privacy: "privacy-policy",
    thankYou: "thank-you"
  },
  pt: {
    about: "sobre",
    markets: "mercados-rede-global",
    solutions: "solucoes",
    buyers: "para-compradores",
    producers: "para-produtores-exportadores",
    contact: "contato",
    privacy: "politica-de-privacidade",
    thankYou: "obrigado"
  },
  es: {
    about: "nosotros",
    markets: "mercados-red-global",
    solutions: "soluciones",
    buyers: "para-compradores",
    producers: "para-productores-exportadores",
    contact: "contacto",
    privacy: "politica-de-privacidad",
    thankYou: "gracias"
  }
} as const satisfies Record<Locale, Record<InnerPageKey, string>>;

export const marketSequence: MarketKey[] = [
  "unitedStates",
  "canada",
  "brazil",
  "chile",
  "argentina",
  "egypt",
  "turkey",
  "europe",
  "china"
];

export const marketCoordinates: Record<MarketKey, { x: number; y: number }> = {
  unitedStates: { x: 17, y: 33 },
  canada: { x: 17, y: 22 },
  brazil: { x: 31, y: 58 },
  chile: { x: 23, y: 70 },
  argentina: { x: 27, y: 77 },
  egypt: { x: 55, y: 43 },
  turkey: { x: 61, y: 36 },
  europe: { x: 55, y: 25 },
  china: { x: 77, y: 34 }
};

export const company = {
  name: "Unyra Group LLC",
  legalName: "Unyra Group LLC",
  url: "https://unyragroup.com",
  tagline: "Connecting Markets. Building Trust. Delivering Value.",
  experienceBadge: "20+ years",
  description:
    "Unyra Group LLC is a global company specialized in connecting buyers and producer-exporters worldwide, especially in the garlic market and agricultural commodities.",
  longDescription:
    "Unyra Group LLC brings more than 20 years of experience in the garlic market and agricultural commodities, connecting buyers and producer-exporters across international markets with disciplined commercial coordination and long-term relationship focus.",
  markets: [
    "United States",
    "Canada",
    "Brazil",
    "Chile",
    "Argentina",
    "Egypt",
    "Turkey",
    "Europe",
    "China"
  ],
  logoAsset: "/brand/unyra-logo-transparent-clean.png",
  contact: {
    companyEmailLabel: "Email",
    companyEmail: "sales@unyragroup.com",
    salesEmailLabel: "Sales Email",
    salesEmail: "sales@unyragroup.com",
    phoneLabel: "Phone / WhatsApp",
    phoneDisplay: "+1 888 789 843",
    phoneHref: "tel:+1888789843",
    locationLabel: "Business Location",
    location: "Orlando, Florida, 32801, US"
  },
  address: {
    city: "Orlando",
    region: "Florida",
    postalCode: "32801",
    country: "US"
  },
  socialImage: "/opengraph-image",
  iconPath: "/icon.svg"
} as const;

export type CTA = {
  label: string;
  pageKey?: PageKey;
  href?: string;
};

export type SectionIntro = {
  eyebrow: string;
  title: string;
  description: string;
};

export type FeatureCard = {
  title: string;
  description: string;
};

export type StatItem = {
  title: string;
  description: string;
};

export type AudienceCard = {
  eyebrow: string;
  title: string;
  description: string;
  bullets: string[];
  cta: string;
};

export type RegionCard = {
  key: MarketKey;
  title: string;
  description: string;
};

export type FormOption = {
  value: string;
  label: string;
};

export type Dictionary = {
  locale: Locale;
  metadata: Record<
    PageKey,
    {
      title: string;
      description: string;
    }
  >;
  labels: {
    siteTitle: string;
    skipToContent: string;
    home: string;
    backToHome: string;
    breadcrumbSeparator: string;
    languageSwitcher: string;
    nav: Record<PageKey, string>;
    primaryCta: string;
    secondaryCta: string;
    stickyCta: string;
    tagline: string;
    footerSummary: string;
    footerContact: string;
    footerNavigation: string;
    footerLaunchNote: string;
    privacyNote: string;
    thankYouButton: string;
  };
  form: {
    badge: string;
    title: string;
    description: string;
    submit: string;
    sending: string;
    success: string;
    error: string;
    redirecting: string;
    privacyNote: string;
    honeypot: string;
    labels: {
      fullName: string;
      company: string;
      email: string;
      phone: string;
      country: string;
      role: string;
      interest: string;
      message: string;
    };
    placeholders: {
      fullName: string;
      company: string;
      email: string;
      phone: string;
      country: string;
      message: string;
    };
    roleOptions: FormOption[];
    interestOptions: FormOption[];
    validation: {
      required: string;
      email: string;
      messageLength: string;
    };
  };
  home: {
    hero: {
      eyebrow: string;
      title: string;
      description: string;
      experienceLabel: string;
      marketLine: string;
      primaryCta: string;
      secondaryCta: string;
      floatingCardTitle: string;
      floatingCardDescription: string;
      highlightPoints: string[];
    };
    trustStrip: StatItem[];
    aboutPreview: SectionIntro & {
      paragraphs: string[];
      markers: string[];
    };
    solutions: SectionIntro & {
      items: FeatureCard[];
    };
    expertise: SectionIntro & {
      pillars: FeatureCard[];
      asideTitle: string;
      asideText: string;
    };
    network: SectionIntro & {
      cards: RegionCard[];
    };
    audience: SectionIntro & {
      buyers: AudienceCard;
      producers: AudienceCard;
    };
    why: SectionIntro & {
      items: FeatureCard[];
    };
    ctaBand: {
      title: string;
      description: string;
      primaryCta: string;
      secondaryCta: string;
    };
    contact: SectionIntro & {
      bullets: string[];
    };
  };
  about: {
    hero: {
      eyebrow: string;
      title: string;
      description: string;
    };
    overview: SectionIntro & {
      paragraphs: string[];
    };
    values: SectionIntro & {
      items: FeatureCard[];
    };
    experience: SectionIntro & {
      pillars: FeatureCard[];
      timeline: string[];
    };
    relationships: {
      title: string;
      description: string;
      bullets: string[];
    };
    ctaBand: {
      title: string;
      description: string;
    };
  };
  markets: {
    hero: {
      eyebrow: string;
      title: string;
      description: string;
    };
    map: SectionIntro & {
      cards: RegionCard[];
    };
    connectivity: SectionIntro & {
      items: FeatureCard[];
    };
    opportunity: {
      title: string;
      description: string;
      bullets: string[];
    };
    ctaBand: {
      title: string;
      description: string;
    };
  };
  solutions: {
    hero: {
      eyebrow: string;
      title: string;
      description: string;
    };
    capabilities: SectionIntro & {
      items: FeatureCard[];
    };
    process: SectionIntro & {
      steps: FeatureCard[];
    };
    expertise: {
      title: string;
      description: string;
      bullets: string[];
    };
    ctaBand: {
      title: string;
      description: string;
    };
  };
  buyers: {
    hero: {
      eyebrow: string;
      title: string;
      description: string;
    };
    priorities: SectionIntro & {
      items: FeatureCard[];
    };
    approach: SectionIntro & {
      bullets: string[];
    };
    formPanel: {
      title: string;
      description: string;
    };
  };
  producers: {
    hero: {
      eyebrow: string;
      title: string;
      description: string;
    };
    priorities: SectionIntro & {
      items: FeatureCard[];
    };
    approach: SectionIntro & {
      bullets: string[];
    };
    formPanel: {
      title: string;
      description: string;
    };
  };
  contact: {
    hero: {
      eyebrow: string;
      title: string;
      description: string;
    };
    contactCards: FeatureCard[];
    response: {
      title: string;
      description: string;
      bullets: string[];
    };
  };
  privacy: {
    hero: {
      eyebrow: string;
      title: string;
      description: string;
    };
    sections: Array<{
      title: string;
      paragraphs: string[];
    }>;
  };
  thankYou: {
    eyebrow: string;
    title: string;
    description: string;
    primaryCta: string;
    secondaryCta: string;
  };
};

export function isValidLocale(value: string): value is Locale {
  return locales.includes(value as Locale);
}

export function getPath(locale: Locale, pageKey: PageKey): string {
  if (pageKey === "home") {
    return `/${locale}`;
  }

  return `/${locale}/${innerPageSlugs[locale][pageKey]}`;
}

export function resolveInnerPageKey(
  locale: Locale,
  slug: string
): InnerPageKey | null {
  const entry = Object.entries(innerPageSlugs[locale]).find(
    ([, value]) => value === slug
  );

  return (entry?.[0] as InnerPageKey | undefined) ?? null;
}

export function getAlternateLinks(pageKey: PageKey): Record<string, string> {
  const links = Object.fromEntries(
    locales.map((locale) => [localeMeta[locale].languageTag, `${company.url}${getPath(locale, pageKey)}`])
  );

  return {
    ...links,
    "x-default": `${company.url}${getPath(defaultLocale, pageKey)}`
  };
}

export function joinUrl(path: string) {
  return `${company.url}${path}`;
}
