import { NextResponse } from "next/server";
import { randomUUID } from "node:crypto";
import { company, locales, pageOrder, type Locale, type PageKey } from "@/lib/site";

type SubmissionPayload = {
  fullName: string;
  company: string;
  email: string;
  phone: string;
  country: string;
  role: string;
  interest: string;
  message: string;
  website?: string;
  locale: Locale;
  source: PageKey;
};

type ValidationErrorCode =
  | "required"
  | "invalid_email"
  | "message_too_short"
  | "invalid_option"
  | "invalid_context";

type DeliveryResult = {
  reference: string;
  provider: "webhook" | "resend" | "console";
  externalId?: string;
};

export const runtime = "nodejs";

const roleValues = new Set(["buyer", "producer-exporter", "distributor", "other"]);
const interestValues = new Set([
  "garlic",
  "agricultural-commodities",
  "strategic-partnership",
  "other"
]);

function clean(value: unknown) {
  return typeof value === "string" ? value.trim() : "";
}

function isValidEmail(value: string) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
}

function createFieldErrors(payload: Record<string, unknown>) {
  const errors: Record<string, ValidationErrorCode> = {};

  const requiredFields = [
    "fullName",
    "company",
    "email",
    "phone",
    "country",
    "role",
    "interest",
    "message"
  ] as const;

  for (const field of requiredFields) {
    if (!clean(payload[field])) {
      errors[field] = "required";
    }
  }

  const email = clean(payload.email);
  if (email && !isValidEmail(email)) {
    errors.email = "invalid_email";
  }

  const message = clean(payload.message);
  if (message && message.length < 20) {
    errors.message = "message_too_short";
  }

  const role = clean(payload.role);
  if (role && !roleValues.has(role)) {
    errors.role = "invalid_option";
  }

  const interest = clean(payload.interest);
  if (interest && !interestValues.has(interest)) {
    errors.interest = "invalid_option";
  }

  const locale = clean(payload.locale);
  if (locale && !locales.includes(locale as Locale)) {
    errors.locale = "invalid_context";
  }

  const source = clean(payload.source);
  if (source && !pageOrder.includes(source as PageKey)) {
    errors.source = "invalid_context";
  }

  return errors;
}

function normalizePayload(raw: Record<string, unknown>): SubmissionPayload {
  return {
    fullName: clean(raw.fullName),
    company: clean(raw.company),
    email: clean(raw.email),
    phone: clean(raw.phone),
    country: clean(raw.country),
    role: clean(raw.role),
    interest: clean(raw.interest),
    message: clean(raw.message),
    website: clean(raw.website),
    locale: clean(raw.locale) as Locale,
    source: clean(raw.source) as PageKey
  };
}

function buildReference() {
  const timestamp = new Date().toISOString().replace(/[-:TZ.]/g, "").slice(0, 12);
  const suffix = randomUUID().replace(/-/g, "").slice(0, 6).toUpperCase();
  return `UNY-${timestamp}-${suffix}`;
}

function buildMessage(submission: SubmissionPayload, reference: string, submittedAt: string) {
  return [
    "Unyra Group LLC website inquiry",
    "",
    `Inquiry Reference: ${reference}`,
    `Submitted: ${submittedAt}`,
    `Locale: ${submission.locale}`,
    `Source page: ${submission.source}`,
    "",
    `Full Name: ${submission.fullName}`,
    `Company: ${submission.company}`,
    `Email: ${submission.email}`,
    `Phone / WhatsApp: ${submission.phone}`,
    `Country: ${submission.country}`,
    `Role: ${submission.role}`,
    `Interest: ${submission.interest}`,
    "",
    "Message:",
    submission.message
  ].join("\n");
}

function buildHtmlMessage(submission: SubmissionPayload, reference: string, submittedAt: string) {
  const escapeHtml = (value: string) =>
    value
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#39;");

  const rows = [
    ["Inquiry Reference", reference],
    ["Submitted", submittedAt],
    ["Locale", submission.locale],
    ["Source page", submission.source],
    ["Full Name", submission.fullName],
    ["Company", submission.company],
    ["Email", submission.email],
    ["Phone / WhatsApp", submission.phone],
    ["Country", submission.country],
    ["Role", submission.role],
    ["Interest", submission.interest]
  ]
    .map(
      ([label, value]) =>
        `<tr><td style="padding:10px 14px;border:1px solid #d7dce4;background:#f7f9fc;font-weight:600;">${escapeHtml(label)}</td><td style="padding:10px 14px;border:1px solid #d7dce4;">${escapeHtml(value)}</td></tr>`
    )
    .join("");

  return `
    <div style="background:#f4f6fa;padding:32px 16px;font-family:Arial,sans-serif;color:#101828;">
      <div style="max-width:720px;margin:0 auto;background:#ffffff;border:1px solid #d7dce4;border-radius:18px;overflow:hidden;">
        <div style="padding:28px 32px;background:#0f2233;color:#ffffff;">
          <p style="margin:0 0 8px;font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:#c2a071;">Unyra Group LLC</p>
          <h1 style="margin:0;font-size:24px;line-height:1.2;">New website inquiry</h1>
          <p style="margin:14px 0 0;font-size:13px;letter-spacing:0.14em;text-transform:uppercase;color:#d8e4f0;">Reference ${escapeHtml(reference)}</p>
        </div>
        <div style="padding:28px 32px;">
          <p style="margin:0 0 18px;font-size:15px;line-height:1.7;">A new qualified inquiry was submitted through the Unyra website.</p>
          <table style="width:100%;border-collapse:collapse;font-size:14px;line-height:1.6;margin:0 0 20px;">
            <tbody>${rows}</tbody>
          </table>
          <div style="padding:18px 20px;border-radius:14px;background:#f7f9fc;border:1px solid #d7dce4;">
            <p style="margin:0 0 10px;font-size:12px;letter-spacing:0.12em;text-transform:uppercase;color:#667085;">Message</p>
            <p style="margin:0;font-size:15px;line-height:1.8;white-space:pre-wrap;">${escapeHtml(submission.message)}</p>
          </div>
        </div>
      </div>
    </div>
  `;
}

function resolveReplyTo(submission: SubmissionPayload) {
  return submission.email;
}

function resolveFromAddress(configuredFrom: string, configuredTo: string) {
  const normalizedFrom = configuredFrom.trim().toLowerCase();
  const normalizedTo = configuredTo.trim().toLowerCase();
  const fallbackDomain =
    configuredTo.split("@")[1] || configuredFrom.split("@")[1] || company.contact.companyEmail.split("@")[1];
  const fallbackAddress = `website@${fallbackDomain}`;
  const safeAddress =
    !configuredFrom || normalizedFrom === normalizedTo ? fallbackAddress : configuredFrom.trim();

  if (safeAddress.includes("<")) {
    return safeAddress;
  }

  return `${company.name} Website <${safeAddress}>`;
}

async function deliverSubmission(submission: SubmissionPayload) {
  const provider =
    process.env.CONTACT_PROVIDER ??
    (process.env.CONTACT_FORM_WEBHOOK_URL
      ? "webhook"
      : process.env.RESEND_API_KEY
        ? "resend"
        : "console");

  const reference = buildReference();
  const submittedAt = new Date().toISOString();
  const subject = `${process.env.CONTACT_SUBJECT_PREFIX ?? "[Unyra Inquiry]"} ${reference} | ${submission.company} - ${submission.fullName}`;
  const text = buildMessage(submission, reference, submittedAt);
  const html = buildHtmlMessage(submission, reference, submittedAt);

  if (provider === "webhook") {
    const webhookUrl = process.env.CONTACT_FORM_WEBHOOK_URL;

    if (!webhookUrl) {
      throw new Error("CONTACT_FORM_WEBHOOK_URL is not configured.");
    }

    const response = await fetch(webhookUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        subject,
        reference,
        company: company.name,
        submission
      })
    });

    if (!response.ok) {
      throw new Error(`Webhook delivery failed with status ${response.status}.`);
    }

    return {
      reference,
      provider: "webhook"
    } satisfies DeliveryResult;
  }

  if (provider === "resend") {
    const resendApiKey = process.env.RESEND_API_KEY;
    const to = process.env.CONTACT_FORM_TO;
    const from = process.env.CONTACT_FORM_FROM;

    if (!resendApiKey || !to || !from) {
      throw new Error(
        "RESEND_API_KEY, CONTACT_FORM_TO, and CONTACT_FORM_FROM must be configured."
      );
    }

    const resolvedFrom = resolveFromAddress(from, to);
    const replyTo = resolveReplyTo(submission);

    const response = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${resendApiKey}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        from: resolvedFrom,
        to: [to],
        reply_to: replyTo,
        subject,
        text,
        html,
        tags: [
          { name: "source", value: submission.source },
          { name: "locale", value: submission.locale }
        ]
      })
    });

    const responseText = await response.text();

    if (!response.ok) {
      throw new Error(
        `Resend delivery failed with status ${response.status}. Response: ${responseText}`
      );
    }

    const resendResponse = JSON.parse(responseText) as { id?: string };

    console.info("[unyra-contact-resend]", {
      reference,
      to,
      from: resolvedFrom,
      replyTo,
      subject,
      submission: {
        locale: submission.locale,
        source: submission.source,
        company: submission.company,
        email: submission.email
      },
      resend: responseText
    });

    return {
      reference,
      provider: "resend",
      externalId: resendResponse.id
    } satisfies DeliveryResult;
  }

  console.info("[unyra-contact-placeholder]", {
    reference,
    subject,
    text,
    submission
  });

  return {
    reference,
    provider: "console"
  } satisfies DeliveryResult;
}

export async function POST(request: Request) {
  let payload: Record<string, unknown>;

  try {
    payload = (await request.json()) as Record<string, unknown>;
  } catch {
    return NextResponse.json(
      { ok: false, code: "invalid_payload", message: "Invalid payload." },
      { status: 400 }
    );
  }

  if (clean(payload.website)) {
    return NextResponse.json({ ok: true });
  }

  const errors = createFieldErrors(payload);
  if (Object.keys(errors).length > 0) {
    return NextResponse.json(
      { ok: false, code: "validation_failed", message: "Validation failed.", errors },
      { status: 400 }
    );
  }

  const submission = normalizePayload(payload);

  try {
    const delivery = await deliverSubmission(submission);

    return NextResponse.json({ ok: true, reference: delivery.reference });
  } catch (error) {
    console.error("[unyra-contact-error]", error);

    return NextResponse.json(
      {
        ok: false,
        code: "delivery_failed",
        message: "The inquiry could not be delivered."
      },
      { status: 500 }
    );
  }
}
