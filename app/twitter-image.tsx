import { ImageResponse } from "next/og";

export const alt = "Unyra Group LLC";
export const size = {
  width: 1200,
  height: 600
};
export const contentType = "image/png";

export default function TwitterImage() {
  return new ImageResponse(
    (
      <div
        style={{
          display: "flex",
          height: "100%",
          width: "100%",
          background:
            "radial-gradient(circle at 18% 12%, rgba(210,172,119,0.22), transparent 26%), linear-gradient(135deg, #08121E 0%, #102436 58%, #0A1624 100%)",
          color: "white",
          padding: 52,
          position: "relative",
          fontFamily: "Arial"
        }}
      >
        <div
          style={{
            position: "absolute",
            inset: 28,
            borderRadius: 32,
            border: "1px solid rgba(255,255,255,0.12)"
          }}
        />
        <div style={{ display: "flex", flexDirection: "column", gap: 28, justifyContent: "center" }}>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              width: 88,
              height: 88,
              borderRadius: 26,
              background:
                "linear-gradient(180deg, rgba(255,255,255,0.14), rgba(255,255,255,0.05))",
              border: "1px solid rgba(255,255,255,0.16)",
              color: "#F4E7D0",
              fontSize: 30,
              fontWeight: 700,
              letterSpacing: "0.28em"
            }}
          >
            UG
          </div>
          <div
            style={{
              fontSize: 22,
              textTransform: "uppercase",
              letterSpacing: "0.2em",
              color: "#D7B282"
            }}
          >
            Connecting Markets. Building Trust. Delivering Value.
          </div>
          <div
            style={{
              maxWidth: 980,
              fontSize: 58,
              fontWeight: 700,
              lineHeight: 1.04,
              letterSpacing: "-0.07em"
            }}
          >
            Unyra Group LLC connects buyers and producer-exporters worldwide.
          </div>
        </div>
      </div>
    ),
    size
  );
}
