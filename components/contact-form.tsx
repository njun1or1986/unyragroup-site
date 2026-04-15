"use client";

import { startTransition, useMemo, useState, type ChangeEvent, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { getPath, type Dictionary, type Locale, type PageKey } from "@/lib/site";

type ContactFormProps = {
  locale: Locale;
  source: PageKey;
  copy: Dictionary["form"];
};

type FormValues = {
  fullName: string;
  company: string;
  email: string;
  phone: string;
  country: string;
  role: string;
  interest: string;
  message: string;
  website: string;
};

type FormErrors = Partial<Record<keyof Omit<FormValues, "website">, string>>;

const initialValues: FormValues = {
  fullName: "",
  company: "",
  email: "",
  phone: "",
  country: "",
  role: "",
  interest: "",
  message: "",
  website: ""
};

function isValidEmail(value: string) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
}

export default function ContactForm({
  locale,
  source,
  copy
}: ContactFormProps) {
  const router = useRouter();
  const [values, setValues] = useState<FormValues>(initialValues);
  const [errors, setErrors] = useState<FormErrors>({});
  const [status, setStatus] = useState<"idle" | "sending" | "success" | "error">(
    "idle"
  );

  const messageLength = values.message.trim().length;

  const fields = useMemo(
    () => [
      { key: "fullName", type: "text", autoComplete: "name" },
      { key: "company", type: "text", autoComplete: "organization" },
      { key: "email", type: "email", autoComplete: "email" },
      { key: "phone", type: "tel", autoComplete: "tel" },
      { key: "country", type: "text", autoComplete: "country-name" }
    ] as const,
    []
  );

  function validate(nextValues: FormValues) {
    const nextErrors: FormErrors = {};
    const requiredFields: Array<keyof Omit<FormValues, "website">> = [
      "fullName",
      "company",
      "email",
      "phone",
      "country",
      "role",
      "interest",
      "message"
    ];

    for (const field of requiredFields) {
      if (!nextValues[field].trim()) {
        nextErrors[field] = copy.validation.required;
      }
    }

    if (nextValues.email.trim() && !isValidEmail(nextValues.email.trim())) {
      nextErrors.email = copy.validation.email;
    }

    if (nextValues.message.trim() && nextValues.message.trim().length < 20) {
      nextErrors.message = copy.validation.messageLength;
    }

    return nextErrors;
  }

  function handleChange(
    event: ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
  ) {
    const { name, value } = event.target;

    setValues((current) => ({ ...current, [name]: value }));
    setErrors((current) => ({ ...current, [name]: undefined }));
    setStatus("idle");
  }

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const nextErrors = validate(values);
    if (Object.keys(nextErrors).length > 0) {
      setErrors(nextErrors);
      setStatus("error");
      return;
    }

    setStatus("sending");

    try {
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          ...values,
          locale,
          source
        })
      });

      if (!response.ok) {
        throw new Error("Contact submission failed");
      }

      setStatus("success");
      setValues(initialValues);
      setErrors({});

      window.setTimeout(() => {
        startTransition(() => {
          router.push(getPath(locale, "thankYou"));
        });
      }, 900);
    } catch {
      setStatus("error");
    }
  }

  const statusMessage =
    status === "success"
      ? `${copy.success} ${copy.redirecting}`
      : status === "error"
        ? copy.error
        : "";

  return (
    <form className="grid gap-5" onSubmit={handleSubmit} noValidate>
      <div className="grid gap-5 md:grid-cols-2">
        {fields.map((field) => {
          const label = copy.labels[field.key];
          const placeholder = copy.placeholders[field.key];
          const error = errors[field.key];

          return (
            <label key={field.key} className="grid gap-2 text-sm font-medium text-white/82">
              <span>{label}</span>
              <input
                type={field.type}
                name={field.key}
                value={values[field.key]}
                onChange={handleChange}
                placeholder={placeholder}
                autoComplete={field.autoComplete}
                aria-invalid={Boolean(error)}
                aria-describedby={error ? `${field.key}-error` : undefined}
                className={`form-field ${error ? "form-field-error" : ""}`}
              />
              {error ? (
                <span id={`${field.key}-error`} className="form-error">
                  {error}
                </span>
              ) : null}
            </label>
          );
        })}
      </div>

      <div className="grid gap-5 md:grid-cols-2">
        <label className="grid gap-2 text-sm font-medium text-white/82">
          <span>{copy.labels.role}</span>
          <select
            name="role"
            value={values.role}
            onChange={handleChange}
            aria-invalid={Boolean(errors.role)}
            aria-describedby={errors.role ? "role-error" : undefined}
            className={`form-field ${errors.role ? "form-field-error" : ""}`}
          >
            <option value="">{copy.labels.role}</option>
            {copy.roleOptions.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
          {errors.role ? (
            <span id="role-error" className="form-error">
              {errors.role}
            </span>
          ) : null}
        </label>

        <label className="grid gap-2 text-sm font-medium text-white/82">
          <span>{copy.labels.interest}</span>
          <select
            name="interest"
            value={values.interest}
            onChange={handleChange}
            aria-invalid={Boolean(errors.interest)}
            aria-describedby={errors.interest ? "interest-error" : undefined}
            className={`form-field ${errors.interest ? "form-field-error" : ""}`}
          >
            <option value="">{copy.labels.interest}</option>
            {copy.interestOptions.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
          {errors.interest ? (
            <span id="interest-error" className="form-error">
              {errors.interest}
            </span>
          ) : null}
        </label>
      </div>

      <label className="grid gap-2 text-sm font-medium text-white/82">
        <span>{copy.labels.message}</span>
        <textarea
          name="message"
          value={values.message}
          onChange={handleChange}
          placeholder={copy.placeholders.message}
          aria-invalid={Boolean(errors.message)}
          aria-describedby={errors.message ? "message-error" : "message-hint"}
          className={`form-field min-h-40 resize-y ${errors.message ? "form-field-error" : ""}`}
        />
        <span id="message-hint" className="text-xs text-white/45">
          {messageLength}/20+
        </span>
        {errors.message ? (
          <span id="message-error" className="form-error">
            {errors.message}
          </span>
        ) : null}
      </label>

      <label className="sr-only" htmlFor="website">
        {copy.honeypot}
      </label>
      <input
        id="website"
        name="website"
        type="text"
        value={values.website}
        onChange={handleChange}
        tabIndex={-1}
        autoComplete="off"
        className="hidden"
      />

      <div className="mt-2 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <p className="max-w-xl text-sm leading-7 text-white/56">{copy.privacyNote}</p>
        <button
          type="submit"
          disabled={status === "sending"}
          className="inline-flex min-h-12 w-full items-center justify-center rounded-full bg-[var(--accent)] px-7 text-[0.74rem] font-semibold uppercase tracking-[0.22em] text-[var(--ink)] shadow-[0_18px_36px_rgba(194,160,113,0.24)] hover:-translate-y-0.5 disabled:cursor-not-allowed disabled:opacity-70 sm:w-auto"
        >
          {status === "sending" ? copy.sending : copy.submit}
        </button>
      </div>

      <div className="min-h-6" aria-live="polite">
        {statusMessage ? <p className="text-sm text-white/82">{statusMessage}</p> : null}
      </div>
    </form>
  );
}
