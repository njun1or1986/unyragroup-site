import type { ReactNode } from "react";
import { notFound } from "next/navigation";
import { isValidLocale, localeMeta } from "@/lib/site";

type LocaleLayoutProps = {
  children: ReactNode;
  params: Promise<{ locale: string }>;
};

export default async function LocaleLayout({
  children,
  params
}: LocaleLayoutProps) {
  const { locale } = await params;

  if (!isValidLocale(locale)) {
    notFound();
  }

  return (
    <>
      <script
        dangerouslySetInnerHTML={{
          __html: `document.documentElement.lang=${JSON.stringify(localeMeta[locale].languageTag)};`
        }}
      />
      {children}
    </>
  );
}
