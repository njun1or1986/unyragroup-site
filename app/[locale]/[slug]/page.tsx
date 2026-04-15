import type { Metadata } from "next";
import { notFound } from "next/navigation";
import SiteShell from "@/components/site-shell";
import { getDictionary } from "@/lib/dictionaries";
import { buildPageMetadata, buildStructuredData } from "@/lib/seo";
import { innerPageSlugs, isValidLocale, locales, resolveInnerPageKey } from "@/lib/site";

type InnerPageProps = {
  params: Promise<{ locale: string; slug: string }>;
};

export const dynamicParams = false;

export function generateStaticParams() {
  return locales.flatMap((locale) =>
    Object.values(innerPageSlugs[locale]).map((slug) => ({
      locale,
      slug
    }))
  );
}

export async function generateMetadata({
  params
}: InnerPageProps): Promise<Metadata> {
  const { locale, slug } = await params;

  if (!isValidLocale(locale)) {
    notFound();
  }

  const pageKey = resolveInnerPageKey(locale, slug);
  if (!pageKey) {
    notFound();
  }

  return buildPageMetadata(locale, pageKey, getDictionary(locale));
}

export default async function InnerPage({ params }: InnerPageProps) {
  const { locale, slug } = await params;

  if (!isValidLocale(locale)) {
    notFound();
  }

  const pageKey = resolveInnerPageKey(locale, slug);
  if (!pageKey) {
    notFound();
  }

  const dictionary = getDictionary(locale);

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(buildStructuredData(locale, pageKey, dictionary))
        }}
      />
      <SiteShell locale={locale} pageKey={pageKey} dictionary={dictionary} />
    </>
  );
}
