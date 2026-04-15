import type { MetadataRoute } from "next";
import { company, getPath, locales, pageOrder } from "@/lib/site";

export default function sitemap(): MetadataRoute.Sitemap {
  const now = new Date();

  return locales.flatMap((locale) =>
    pageOrder
      .filter((pageKey) => pageKey !== "thankYou")
      .map((pageKey) => ({
        url: `${company.url}${getPath(locale, pageKey)}`,
        lastModified: now,
        changeFrequency: pageKey === "home" ? "weekly" : "monthly",
        priority: pageKey === "home" ? 1 : pageKey === "contact" ? 0.9 : 0.8
      }))
  );
}
