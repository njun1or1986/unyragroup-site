export default function TradeImpactVisual() {
  return (
    <div className="relative min-h-[30rem] overflow-hidden rounded-[2.5rem] border border-white/10 bg-[radial-gradient(circle_at_top_left,rgba(198,165,124,0.14),transparent_20%),radial-gradient(circle_at_88%_18%,rgba(109,143,137,0.16),transparent_22%),linear-gradient(180deg,rgba(18,24,32,0.98),rgba(10,13,18,1))] shadow-[0_34px_110px_rgba(7,10,14,0.34)] sm:min-h-[34rem]">
      <div
        className="pointer-events-none absolute inset-0 bg-[linear-gradient(90deg,rgba(255,255,255,0.04)_1px,transparent_1px),linear-gradient(rgba(255,255,255,0.04)_1px,transparent_1px)] [background-size:78px_78px] opacity-20"
        aria-hidden="true"
      />
      <div className="pointer-events-none absolute -left-16 top-16 h-40 w-40 rounded-full border border-white/10 bg-white/5 blur-[2px]" />
      <div className="pointer-events-none absolute bottom-10 right-8 h-56 w-56 rounded-full border border-[rgba(198,165,124,0.2)] bg-[rgba(198,165,124,0.05)]" />

      <svg viewBox="0 0 1200 760" className="absolute inset-0 h-full w-full" aria-hidden="true" role="presentation">
        <defs>
          <linearGradient id="ship-body" x1="194" y1="525" x2="936" y2="525" gradientUnits="userSpaceOnUse">
            <stop stopColor="#173245" />
            <stop offset="1" stopColor="#0F1C27" />
          </linearGradient>
          <linearGradient id="container-stack" x1="0" y1="0" x2="1" y2="1">
            <stop stopColor="#C6A57C" />
            <stop offset="1" stopColor="#6D8F89" />
          </linearGradient>
          <linearGradient id="sky-glow" x1="286" y1="54" x2="984" y2="206" gradientUnits="userSpaceOnUse">
            <stop stopColor="#C6A57C" stopOpacity="0.44" />
            <stop offset="1" stopColor="#6D8F89" stopOpacity="0.08" />
          </linearGradient>
        </defs>

        <ellipse cx="702" cy="666" rx="390" ry="34" fill="#1D2430" />
        <path d="M116 546h968" stroke="#243041" strokeWidth="2" />
        <path d="M194 506H932l-48 104H256l-62-56Z" fill="url(#ship-body)" />
        <path d="M256 610h628l-20 18H272Z" fill="#213142" />
        <path d="M302 470h438v40H302Z" fill="#11212D" />
        <path d="M430 410h108v60H430Z" fill="#223646" />
        <path d="M558 410h106v60H558Z" fill="#263B4D" />

        <g opacity="0.95">
          {[
            [326, 360, 90, 52],
            [422, 360, 90, 52],
            [518, 360, 90, 52],
            [614, 360, 90, 52],
            [710, 360, 90, 52],
            [374, 304, 90, 52],
            [470, 304, 90, 52],
            [566, 304, 90, 52],
            [662, 304, 90, 52]
          ].map(([x, y, width, height], index) => (
            <rect
              key={`${x}-${y}`}
              x={x}
              y={y}
              width={width}
              height={height}
              rx="8"
              fill={index % 3 === 0 ? "#C6A57C" : index % 3 === 1 ? "#6D8F89" : "#1C3342"}
              stroke="rgba(255,255,255,0.1)"
            />
          ))}
        </g>

        <g opacity="0.7">
          <path d="M154 238h104" stroke="#31485A" strokeWidth="8" strokeLinecap="round" />
          <path d="M206 238v292" stroke="#31485A" strokeWidth="8" strokeLinecap="round" />
          <path d="M206 248l168-98" stroke="#31485A" strokeWidth="8" strokeLinecap="round" />
          <path d="M898 214h104" stroke="#31485A" strokeWidth="8" strokeLinecap="round" />
          <path d="M950 214v268" stroke="#31485A" strokeWidth="8" strokeLinecap="round" />
          <path d="M950 222l136-82" stroke="#31485A" strokeWidth="8" strokeLinecap="round" />
        </g>

        <path
          className="route-dash"
          d="M136 198C246 118 382 114 516 154C650 194 794 180 934 140C1002 120 1064 122 1122 152"
          stroke="url(#container-stack)"
          strokeWidth="4"
          fill="none"
          strokeLinecap="round"
          strokeDasharray="10 12"
        />
        <path
          className="route-dash-slow"
          d="M198 254C304 236 424 250 548 286C672 320 794 318 926 290"
          stroke="url(#container-stack)"
          strokeWidth="3"
          fill="none"
          strokeLinecap="round"
          strokeDasharray="8 11"
        />

        <circle cx="140" cy="196" r="7" fill="#FFF5E5" />
        <circle cx="516" cy="154" r="7" fill="#FFF5E5" />
        <circle cx="934" cy="140" r="7" fill="#FFF5E5" />
        <circle cx="1096" cy="150" r="7" fill="#FFF5E5" />

        <ellipse cx="716" cy="130" rx="268" ry="104" fill="url(#sky-glow)" />
      </svg>
    </div>
  );
}
