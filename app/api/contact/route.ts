import { NextResponse } from "next/server";
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
  const errors: Record<string, string> = {};

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
      errors[field] = "Required";
    }
  }

  const email = clean(payload.email);
  if (email && !isValidEmail(email)) {
    errors.email = "Invalid email";
  }

  const message = clean(payload.message);
  if (message && message.length < 20) {
    errors.message = "Message is too short";
  }

  const role = clean(payload.role);
  if (role && !roleValues.has(role)) {
    errors.role = "Invalid role";
  }

  const interest = clean(payload.interest);
  if (interest && !interestValues.has(interest)) {
    errors.interest = "Invalid interest";
  }

  const locale = clean(payload.locale);
  if (locale && !locales.includes(locale as Locale)) {
    errors.locale = "Invalid locale";
  }

  const source = clean(payload.source);
  if (source && !pageOrder.includes(source as PageKey)) {
    errors.source = "Invalid source";
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

function buildMessage(submission: SubmissionPayload) {
  return [
    "Unyra Group LLC website inquiry",
    "",
    `Submitted: ${new Date().toISOString()}`,
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

async function deliverSubmission(submission: SubmissionPayload) {
  const provider =
    process.env.CONTACT_PROVIDER ??
    (process.env.CONTACT_FORM_WEBHOOK_URL
      ? "webhook"
      : process.env.RESEND_API_KEY
        ? "resend"
        : "console");

  const subject = `${process.env.CONTACT_SUBJECT_PREFIX ?? "[Unyra Inquiry]"} ${submission.company} - ${submission.fullName}`;
  const text = buildMessage(submission);

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
        company: company.name,
        submission
      })
    });

    if (!response.ok) {
      throw new Error(`Webhook delivery failed with status ${response.status}.`);
    }

    return;
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

    const response = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${resendApiKey}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        from,
        to,
        reply_to: submission.email,
        subject,
        text
      })
    });

    if (!response.ok) {
      throw new Error(`Resend delivery failed with status ${response.status}.`);
    }

    return;
  }

  console.info("[unyra-contact-placeholder]", {
    subject,
    text,
    submission
  });
}

export async function POST(request: Request) {
  let payload: Record<string, unknown>;

  try {
    payload = (await request.json()) as Record<string, unknown>;
  } catch {
    return NextResponse.json(
      { ok: false, message: "Invalid payload." },
      { status: 400 }
    );
  }

  if (clean(payload.website)) {
    return NextResponse.json({ ok: true });
  }

  const errors = createFieldErrors(payload);
  if (Object.keys(errors).length > 0) {
    return NextResponse.json(
      { ok: false, message: "Validation failed.", errors },
      { status: 400 }
    );
  }

  const submission = normalizePayload(payload);

  try {
    await deliverSubmission(submission);

    return NextResponse.json({ ok: true });
  } catch (error) {
    console.error("[unyra-contact-error]", error);

    return NextResponse.json(
      {
        ok: false,
        message: "The inquiry could not be delivered."
      },
      { status: 500 }
    );
  }
}
