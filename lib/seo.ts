import type { Metadata } from "next";
import { company, getAlternateLinks, getPath, localeMeta, type Dictionary, type Locale, type PageKey } from "@/lib/site";

const baseKeywords = [
  "garlic market",
  "garlic trade",
  "agricultural commodities",
  "international sourcing",
  "global trading",
  "producer-exporter connections",
  "buyers and suppliers in global markets",
  "business partnerships in agricultural trade"
];

export function buildPageMetadata(
  locale: Locale,
  pageKey: PageKey,
  dictionary: Dictionary
): Metadata {
  const page = dictionary.metadata[pageKey];
  const canonical = getPath(locale, pageKey);
  const alternates = getAlternateLinks(pageKey);

  return {
    title: page.title,
    description: page.description,
    alternates: {
      canonical,
      languages: alternates
    },
    keywords: baseKeywords,
    openGraph: {
      type: "website",
      url: canonical,
      title: page.title,
      description: page.description,
      locale: localeMeta[locale].openGraphLocale,
      alternateLocale: Object.values(localeMeta)
        .filter((entry) => entry.openGraphLocale !== localeMeta[locale].openGraphLocale)
        .map((entry) => entry.openGraphLocale),
      images: [
        {
          url: company.socialImage,
          width: 1200,
          height: 630,
          alt: page.title
        }
      ]
    },
    twitter: {
      card: "summary_large_image",
      title: page.title,
      description: page.description,
      images: ["/twitter-image"]
    },
    robots:
      pageKey === "thankYou"
        ? {
            index: false,
            follow: false
          }
        : {
            index: true,
            follow: true
          }
  };
}

export function buildStructuredData(
  locale: Locale,
  pageKey: PageKey,
  dictionary: Dictionary
) {
  const url = `${company.url}${getPath(locale, pageKey)}`;
  const page = dictionary.metadata[pageKey];
  const result: Array<Record<string, unknown>> = [];

  result.push({
    "@context": "https://schema.org",
    "@type": "Organization",
    name: company.name,
    legalName: company.legalName,
    url: company.url,
    description: company.description,
    slogan: dictionary.labels.tagline,
    logo: `${company.url}${company.logoAsset}`,
    email: company.contact.companyEmail,
    telephone: company.contact.phoneDisplay,
    address: {
      "@type": "PostalAddress",
      addressLocality: company.address.city,
      addressRegion: company.address.region,
      postalCode: company.address.postalCode,
      addressCountry: company.address.country
    },
    contactPoint: {
      "@type": "ContactPoint",
      contactType: "sales",
      email: company.contact.companyEmail,
      telephone: company.contact.phoneDisplay
    }
  });

  if (pageKey === "home") {
    result.push({
      "@context": "https://schema.org",
      "@type": "WebSite",
      name: company.name,
      url: company.url,
      description: company.description,
      inLanguage: localeMeta[locale].languageTag
    });
  }

  result.push({
    "@context": "https://schema.org",
    "@type": pageKey === "contact" ? "ContactPage" : "WebPage",
    name: page.title,
    description: page.description,
    url,
    inLanguage: localeMeta[locale].languageTag,
    isPartOf: {
      "@type": "WebSite",
      name: company.name,
      url: company.url
    }
  });

  if (pageKey !== "home") {
    result.push({
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      itemListElement: [
        {
          "@type": "ListItem",
          position: 1,
          name: dictionary.labels.home,
          item: `${company.url}${getPath(locale, "home")}`
        },
        {
          "@type": "ListItem",
          position: 2,
          name: dictionary.labels.nav[pageKey],
          item: url
        }
      ]
    });
  }

  return result;
}
