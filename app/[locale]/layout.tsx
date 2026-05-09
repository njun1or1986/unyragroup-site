import type { Metadata, Viewport } from "next";
import type { ReactNode } from "react";
import { Analytics } from "@vercel/analytics/react";
import { notFound } from "next/navigation";
import "./../globals.css";
import { company, isValidLocale, localeMeta } from "@/lib/site";

type LocaleLayoutProps = {
  children: ReactNode;
  params: Promise<{ locale: string }>;
};

export const metadata: Metadata = {
  metadataBase: new URL(company.url),
  title: company.name,
  description: company.description,
  applicationName: company.name,
  category: "business",
  icons: {
    icon: "/icon.svg",
    shortcut: "/icon.svg",
    apple: "/icon.svg"
  },
  robots: {
    index: true,
    follow: true
  }
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  themeColor: "#08121e"
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
    <html lang={localeMeta[locale].languageTag}>
      <body>
        {children}
        <Analytics />
      </body>
    </html>
  );
}
