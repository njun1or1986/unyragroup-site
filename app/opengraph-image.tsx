import { ImageResponse } from "next/og";

export const alt = "Unyra Group LLC";
export const size = {
  width: 1200,
  height: 630
};
export const contentType = "image/png";

export default function OpenGraphImage() {
  return new ImageResponse(
    (
      <div
        style={{
          display: "flex",
          height: "100%",
          width: "100%",
          background:
            "radial-gradient(circle at 20% 10%, rgba(210,172,119,0.22), transparent 28%), radial-gradient(circle at 82% 80%, rgba(92,129,123,0.16), transparent 24%), linear-gradient(135deg, #08121E 0%, #102436 55%, #0A1624 100%)",
          color: "white",
          padding: 56,
          position: "relative",
          fontFamily: "Arial"
        }}
      >
        <div
          style={{
            position: "absolute",
            inset: 28,
            borderRadius: 36,
            border: "1px solid rgba(255,255,255,0.12)"
          }}
        />
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
            width: "100%",
            height: "100%"
          }}
        >
          <div style={{ display: "flex", alignItems: "center", gap: 20 }}>
            <div
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                width: 92,
                height: 92,
                borderRadius: 28,
                background:
                  "linear-gradient(180deg, rgba(255,255,255,0.14), rgba(255,255,255,0.05))",
                border: "1px solid rgba(255,255,255,0.16)",
                color: "#F4E7D0",
                fontSize: 32,
                fontWeight: 700,
                letterSpacing: "0.28em"
              }}
            >
              UG
            </div>
            <div style={{ display: "flex", flexDirection: "column" }}>
              <div
                style={{
                  fontSize: 18,
                  letterSpacing: "0.34em",
                  textTransform: "uppercase",
                  color: "rgba(255,255,255,0.65)"
                }}
              >
                Connecting Markets. Building Trust. Delivering Value.
              </div>
              <div
                style={{
                  marginTop: 12,
                  fontSize: 34,
                  fontWeight: 700,
                  letterSpacing: "-0.06em"
                }}
              >
                Unyra Group LLC
              </div>
            </div>
          </div>

          <div style={{ display: "flex", flexDirection: "column", gap: 18, maxWidth: 900 }}>
            <div
              style={{
                fontSize: 24,
                textTransform: "uppercase",
                letterSpacing: "0.18em",
                color: "#D7B282"
              }}
            >
              20+ years in the garlic market and agricultural commodities
            </div>
            <div
              style={{
                fontSize: 62,
                fontWeight: 700,
                lineHeight: 1.02,
                letterSpacing: "-0.07em"
              }}
            >
              Global trading connections for buyers and producer-exporters.
            </div>
            <div
              style={{
                fontSize: 26,
                color: "rgba(255,255,255,0.76)",
                lineHeight: 1.4
              }}
            >
              United States, Canada, Brazil, Chile, Argentina, Egypt, Turkey, Europe, China.
            </div>
          </div>
        </div>
      </div>
    ),
    size
  );
}
