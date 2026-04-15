import type { Metadata } from "next";
import { notFound } from "next/navigation";
import SiteShell from "@/components/site-shell";
import { getDictionary } from "@/lib/dictionaries";
import { buildPageMetadata, buildStructuredData } from "@/lib/seo";
import { isValidLocale, locales } from "@/lib/site";

type LocalePageProps = {
  params: Promise<{ locale: string }>;
};

export function generateStaticParams() {
  return locales.map((locale) => ({ locale }));
}

export async function generateMetadata({
  params
}: LocalePageProps): Promise<Metadata> {
  const { locale } = await params;

  if (!isValidLocale(locale)) {
    notFound();
  }

  return buildPageMetadata(locale, "home", getDictionary(locale));
}

export default async function LocaleHomePage({ params }: LocalePageProps) {
  const { locale } = await params;

  if (!isValidLocale(locale)) {
    notFound();
  }

  const dictionary = getDictionary(locale);

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(buildStructuredData(locale, "home", dictionary))
        }}
      />
      <SiteShell locale={locale} pageKey="home" dictionary={dictionary} />
    </>
  );
}
