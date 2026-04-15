import type { RegionCard } from "@/lib/site";
import { marketCoordinates, marketSequence } from "@/lib/site";

type GlobalOperationsMapProps = {
  eyebrow: string;
  title: string;
  description: string;
  cards: RegionCard[];
};

const routes = [
  "M 17 22 C 20 25, 18 29, 17 33",
  "M 17 33 C 24 38, 28 47, 31 58",
  "M 31 58 C 28 63, 25 69, 23 75",
  "M 23 75 C 24 77, 25 79, 27 82",
  "M 17 33 C 31 31, 44 28, 55 25",
  "M 55 25 C 59 28, 60 32, 61 36",
  "M 55 25 C 61 24, 68 25, 77 34",
  "M 61 36 C 60 39, 58 41, 55 43",
  "M 31 58 C 39 54, 46 50, 55 43"
];

export default function GlobalOperationsMap({
  eyebrow,
  title,
  description,
  cards
}: GlobalOperationsMapProps) {
  return (
    <section className="premium-panel-dark overflow-hidden rounded-[2rem] border border-white/10 p-6 sm:p-8 lg:p-10">
      <div className="max-w-3xl">
        <p className="eyebrow-light">{eyebrow}</p>
        <h3 className="font-display mt-4 text-[2.1rem] font-semibold tracking-[-0.04em] text-white sm:text-4xl">
          {title}
        </h3>
        <p className="mt-4 max-w-2xl text-sm leading-7 text-white/66 sm:text-base">
          {description}
        </p>
      </div>

      <div className="mt-8 grid gap-8 lg:grid-cols-[minmax(0,1.15fr)_minmax(320px,0.85fr)] lg:items-start">
        <div className="map-stage min-h-[24rem] rounded-[1.75rem] border border-white/8 px-4 py-6 sm:min-h-[29rem] sm:px-6">
          <svg
            viewBox="0 0 100 100"
            className="absolute inset-0 h-full w-full"
            preserveAspectRatio="none"
            aria-hidden="true"
          >
            <defs>
              <linearGradient id="unyra-trade-route" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stopColor="#D4B082" />
                <stop offset="52%" stopColor="#F7E6C9" />
                <stop offset="100%" stopColor="#799D8B" />
              </linearGradient>
            </defs>

            <g opacity="0.18" fill="#f8f3ea">
              <path d="M5 37 C 7 26, 15 20, 25 20 C 29 20, 34 22, 38 25 C 41 27, 46 28, 50 26 C 53 24, 57 22, 63 22 C 71 22, 78 25, 84 31 C 88 35, 89 41, 84 44 C 80 47, 74 47, 68 46 C 62 46, 58 48, 53 50 C 46 52, 37 50, 31 46 C 24 42, 13 43, 9 44 C 6 45, 4 42, 5 37 Z" />
              <path d="M21 58 C 24 57, 29 60, 32 64 C 34 68, 33 74, 31 79 C 29 84, 28 90, 25 92 C 21 95, 16 91, 16 85 C 16 79, 17 73, 18 68 C 19 63, 19 59, 21 58 Z" />
              <path d="M58 30 C 62 28, 68 28, 74 31 C 80 35, 84 40, 84 46 C 84 50, 81 54, 76 56 C 72 57, 68 57, 63 56 C 59 55, 57 50, 56 45 C 55 39, 55 33, 58 30 Z" />
            </g>

            {routes.map((path, index) => (
              <path
                key={path}
                d={path}
                className={index % 2 === 0 ? "route-dash" : "route-dash-slow"}
                stroke="url(#unyra-trade-route)"
                strokeWidth={index === 8 ? 0.6 : 0.45}
                strokeLinecap="round"
                strokeDasharray={index === 8 ? "1.8 1.8" : "1.25 1.55"}
                fill="none"
              />
            ))}
          </svg>

          {marketSequence.map((key) => {
            const point = marketCoordinates[key];
            const label = cards.find((card) => card.key === key)?.title ?? key;

            return (
              <div
                key={key}
                className="map-node"
                style={{ left: `${point.x}%`, top: `${point.y}%` }}
              >
                <span className="map-node__ping" />
                <span className="map-node__dot" />
                <span className="map-node__label">{label}</span>
              </div>
            );
          })}
        </div>

        <div className="grid gap-3">
          {cards.map((card) => (
            <article
              key={card.key}
              className="rounded-[1.35rem] border border-white/8 bg-white/[0.05] p-4 backdrop-blur-xl transition-transform duration-300 hover:-translate-y-1 hover:border-[rgba(212,176,130,0.28)]"
            >
              <h4 className="font-display text-lg font-semibold tracking-[-0.03em] text-white">
                {card.title}
              </h4>
              <p className="mt-2 text-sm leading-7 text-white/64">
                {card.description}
              </p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}
