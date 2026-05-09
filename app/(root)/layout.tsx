import type { Metadata, Viewport } from "next";
import type { ReactNode } from "react";
import "./../globals.css";
import { company, defaultLocale, localeMeta } from "@/lib/site";

export const metadata: Metadata = {
  metadataBase: new URL(company.url)
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  themeColor: "#08121e"
};

export default function RedirectRootLayout({
  children
}: Readonly<{
  children: ReactNode;
}>) {
  return (
    <html lang={localeMeta[defaultLocale].languageTag}>
      <body>{children}</body>
    </html>
  );
}
