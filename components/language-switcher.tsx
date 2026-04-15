import Link from "next/link";
import { getPath, localeMeta, locales, type Locale, type PageKey } from "@/lib/site";

type LanguageSwitcherProps = {
  locale: Locale;
  pageKey: PageKey;
  label: string;
  light?: boolean;
};

export default function LanguageSwitcher({
  locale,
  pageKey,
  label,
  light = false
}: LanguageSwitcherProps) {
  return (
    <nav
      aria-label={label}
      className={`inline-flex items-center gap-1 rounded-full border p-1 ${
        light
          ? "border-white/14 bg-white/[0.06]"
          : "border-[rgba(10,22,34,0.09)] bg-white/85 shadow-[0_16px_32px_rgba(10,18,28,0.04)]"
      }`}
    >
      {locales.map((entry) => {
        const active = entry === locale;

        return (
          <Link
            key={entry}
            href={getPath(entry, pageKey)}
            aria-current={active ? "page" : undefined}
            className={`rounded-full px-3.5 py-2.5 text-[0.7rem] font-semibold uppercase tracking-[0.2em] ${
              active
                ? light
                  ? "bg-[var(--accent)] text-[var(--ink)]"
                  : "bg-[var(--ink)] text-white"
                : light
                  ? "text-white/66 hover:text-white"
                  : "text-[var(--muted)] hover:text-[var(--ink)]"
            }`}
          >
            {localeMeta[entry].shortLabel}
          </Link>
        );
      })}
    </nav>
  );
}
