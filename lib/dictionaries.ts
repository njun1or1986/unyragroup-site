import type { Dictionary, Locale } from "@/lib/site";
import en from "@/messages/en";
import es from "@/messages/es";
import pt from "@/messages/pt";

export const dictionaries = {
  en,
  pt,
  es
} as const satisfies Record<Locale, Dictionary>;

export function getDictionary(locale: Locale) {
  return dictionaries[locale];
}
