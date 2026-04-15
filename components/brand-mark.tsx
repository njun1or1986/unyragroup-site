import Image from "next/image";
import { company } from "@/lib/site";

type BrandMarkProps = {
  compact?: boolean;
  statement?: boolean;
  light?: boolean;
  ambient?: boolean;
  className?: string;
};

export default function BrandMark({
  compact = false,
  statement = false,
  light = false,
  ambient = false,
  className = ""
}: BrandMarkProps) {
  const widthClass = statement
    ? "w-[18rem] sm:w-[23rem] lg:w-[27rem]"
    : compact
      ? "w-[11.25rem] sm:w-[13.4rem]"
      : "w-[13.5rem] sm:w-[16rem]";

  if (ambient) {
    return (
      <span
        aria-hidden="true"
        className={`pointer-events-none absolute select-none ${className}`}
      >
        <Image
          src={company.logoAsset}
          alt=""
          width={1336}
          height={422}
          priority={false}
          className={`h-auto ${widthClass} brand-logo-ambient`}
        />
      </span>
    );
  }

  return (
    <span
      className={`inline-flex items-center rounded-[1.4rem] ${
        light ? "brand-logo-shell-dark" : "brand-logo-shell"
      } ${className}`}
    >
      <Image
        src={company.logoAsset}
        alt={company.name}
        width={1336}
        height={422}
        priority={compact}
        className={`h-auto ${widthClass} ${
          light ? "brand-logo-image-dark" : "brand-logo-image"
        }`}
      />
    </span>
  );
}
