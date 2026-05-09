# UNYRA OPS SYSTEM AGENT RULES

This repository is the internal operating system for UNYRA GROUP LLC.

These instructions are strict. Follow them exactly.

## 1. Brand Control

- Always preserve the approved UNYRA visual identity.
- Primary brand color: dark navy `#08121E`.
- Secondary navy support: `#102436`.
- Gold accent: `#C2A071`.
- Strong gold accent: `#9D7646`.
- Neutral support colors: ivory `#F7F3EC`, canvas `#F3EEE6`, muted gray-blue `#5B6672`, muted dark `#2A3742`.
- Design language must stay premium, minimalist, corporate, global-trade focused, and founder-ready.
- Do not introduce playful colors, loud gradients, cartoon styling, or consumer-startup aesthetics.
- Keep layouts clean, balanced, and executive-facing.
- Use logo files from `00_brand/01_assets/01_logos/`.
- Use approved signature layouts from `00_brand/01_assets/04_signatures/`.
- Use approved logo compositions and seals from `00_brand/01_assets/05_approved-compositions/`.
- When an approved design already exists, reuse it exactly instead of redesigning it.
- Do not alter spacing, proportion, hierarchy, or composition of approved brand assets unless explicitly authorized.

## 2. Founder-Friendly Structure

- Keep folder names numbered and stable.
- Keep file names explicit and scannable.
- Do not create deep folder trees unless the folder has a real operating purpose.
- Put master templates in `01_templates/`.
- Put live deal work in `02_crm/04_deals/active/` and `03_operations/`.
- Put live shipment work in `03_operations/03_shipments/active/`.
- Put compliance working files in `04_compliance/`.
- Put reference procedures in `05_sops/`.
- Put founder rollups and trackers in `06_dashboard/`.
- Move completed or inactive material to `07_archive/`.

## 3. Naming Conventions

- Master templates must end with `-MASTER`.
- Working copies must never use the `-MASTER` suffix.
- Use Title-Case with hyphens for template file names.
- Use ISO dates in filenames when a document is transaction-specific: `YYYY-MM-DD`.
- Use version suffixes for working copies: `v01`, `v02`, `v03`.
- Deal folders should use this pattern:
  `DEAL-YYYY-###_Customer_Product`
- Shipment folders should use this pattern:
  `SHIP-YYYY-###_Origin-to-Destination`
- CRM entity files should use these prefixes when practical:
  `LEAD`, `CUSTOMER`, `SUPPLIER`, `DEAL`, `SHIPMENT`, `TASK`
- External communication files or folders should use `COMM` when practical.

Examples:

- `Purchase-Order-MASTER.md`
- `2026-04-19_Atlantic-Foods_Purchase-Order_v01.md`
- `DEAL-2026-014_FreshHarvest_Garlic`
- `SHIP-2026-009_China-to-USA`

## 4. Template Protection Rules

- Never overwrite a master template.
- Never edit a file in `01_templates/` to reflect a live transaction.
- Before starting live work, duplicate the master template into the correct live folder.
- Keep master templates clean, generic, and reusable.
- If a template improves, update the master only after confirming the change is broadly reusable.
- If a working copy needs deal-specific content, save it outside `01_templates/`.

## 5. Working Copy Rules

- Purchasing working copies belong in `03_operations/01_purchasing/` or a live deal folder.
- Logistics working copies belong in `03_operations/02_logistics/` or a live shipment folder.
- Compliance working copies belong in the matching compliance folder under `04_compliance/`.
- Legal working copies tied to a live commercial transaction belong in the relevant deal folder.
- Dashboards should summarize status, not replace source records.
- Use the daily founder dashboard for current control and a weekly executive operating review for posture, direction, and next-week priorities.
- Use a strategic initiative tracker for founder priorities that span multiple weeks or require coordinated follow-through across functions.
- Use an executive KPI scorecard when the founder needs one normalized view of business quality across the whole operating system.
- Use an executive risk register when the founder needs one ranked cross-functional view of active exposures, mitigation ownership, and escalation timing.
- Use a cash forecast and exposure outlook when the founder needs a forward-looking view of expected collections, release-dependent cash, and downside timing risk.
- Use a portfolio concentration review when the founder needs one strategic view of customer, supplier, product, region, or cash dependency concentration.
- Use a supplier capacity and backup sourcing review when the founder needs one strategic view of supplier resilience, surge readiness, and fallback coverage on critical programs.
- Use a quarterly operating plan when the founder needs one 90-day commitment layer that turns strategy into targets, owners, trade-offs, and execution priorities.
- Use a revenue forecast and commitments review when the founder needs one disciplined view of committed revenue, weighted pipeline, slippage risk, and commercial forecast quality.
- Use a capital allocation and release priority review when the founder needs one cross-functional view of where scarce cash, supplier capacity, and release approvals should be deployed first and where lower-confidence matters should wait.
- Use an executive scenario and contingency review when the founder needs one trigger-based view of what should happen in the first 48 hours of a critical downside scenario.
- Use an executive assumption and dependency review when the founder needs one explicit view of the assumptions, timing dependencies, proof dates, and fallback paths behind a forecast or operating plan.
- Use an executive plan variance and recovery review when the founder needs one explicit view of where the quarter is drifting from plan and what recovery actions should pull it back.
- Use an executive owner accountability and follow-through review when the founder needs one explicit view of whether named owners are actually closing the commitments already assigned to them.
- Use a funding and payables release review when the founder needs one explicit view of outgoing cash commitments, supplier deposits, freight funding, and payment-release discipline before cash leaves the business.
- Use a claims, credits, and recovery review when the founder needs one explicit view of customer remedy, supplier recovery, commercial credits, and margin leakage on live issue cases.
- Use a CAPA and preventive action review when the founder needs one explicit view of root-cause quality, corrective-action closure, preventive-action verification, and recurrence prevention on active issue cases.
- Use an executive exceptions and override review when the founder needs one explicit view of stacked pricing, release, compliance, claims, or CAPA exceptions before they normalize into default behavior.
- Use a founder control routing matrix when the founder or team needs one explicit answer on which review layer should own a cross-functional issue before time is lost in the wrong dashboard.
- If a trust-linked founder override exists, route it through synchronization, control-integrity confirmation, and then the live functional gate instead of jumping straight from founder intent to execution.
- Use a trust-override executable check control board when the founder needs one explicit view of active executable checks, same-day cutoffs, blocked movement, evidence state, and archive readiness.
- Use an executive control integrity and decision readiness review when the founder needs one explicit answer on whether linked dashboards and source records are current enough to trust before making a call.
- Use an operating system adoption and readiness board when the founder needs one explicit view of whether the UNYRA system is truly being adopted, used correctly, and sustained in real operating behavior.
- When creating a working copy, keep the master untouched and rename the new file immediately.

## 6. Premium Layout Rules

- Keep document layouts clean and executive-friendly.
- Use short headers, clear sections, and restrained tables.
- Prefer whitespace, alignment, and hierarchy over decorative styling.
- Use dark navy for headings and separators.
- Use gold only as an accent for emphasis, status markers, or signature lines.
- Avoid cluttered tables, oversized logos, and inconsistent capitalization.
- Every document should feel suitable for international buyers, suppliers, customs, and internal leadership review.
- For visual document builds and previews, follow `00_brand/02_guidelines/UNYRA-Premium-Document-Standard.md`.
- Reuse the shared styles in `00_brand/03_exports/01_visual-standard/` before creating one-off document layouts.
- When a new Markdown document is created or materially changed, refresh its branded HTML companion and the relevant `OPEN-HERE.html` navigation layer.
- Keep `index.html`, `START-HERE.html`, and folder-level visual entrypoints founder-friendly, premium, and easier to scan than the raw source tree.
- Customer- and supplier-facing communication must read like a disciplined institution, not an improvised small-business email.
- Use `01_templates/11_external-communications/Official-Document-Transmittal-MASTER.md` for controlled outbound document packets.
- Use `01_templates/11_external-communications/Institutional-Trade-Correspondence-MASTER.md` for formal external correspondence.
- Use `01_templates/11_external-communications/Counterparty-Document-Packet-Index-MASTER.md` when multiple external documents are released together.
- Complete `01_templates/11_external-communications/External-Communication-Release-Checklist-MASTER.md` before sending formal counterparty communication externally.
- Use `01_templates/11_external-communications/Counterparty-Communication-Control-Register-MASTER.md` or `06_dashboard/36_external-communications/` when multiple formal counterparty communications are active and reply deadlines or escalation timing matter.
- Use `00_brand/02_guidelines/UNYRA-Institutional-Communication-Style-Guide.md` and `01_templates/11_external-communications/Counterparty-Message-Framework-MASTER.md` to keep external language formal, precise, and institution-grade.
- Use `01_templates/11_external-communications/Counterparty-Response-SLA-and-Escalation-MASTER.md` or `06_dashboard/37_response-escalation/` when silence, late acknowledgment, or delayed reply creates real commercial, operational, or compliance exposure.
- Use `01_templates/11_external-communications/Counterparty-Trust-Tier-and-Release-Posture-Matrix-MASTER.md` or `06_dashboard/39_trust-posture/` when trust quality must convert into explicit release posture, growth pace, escalation intensity, or sourcing fallback.
- Store live customer or supplier communication evidence inside the owning deal, shipment, customer, or supplier folder, not only in email.

## 7. CRM Entity Management

Maintain these entities consistently:

- Leads
- Customers
- Suppliers
- Deals
- Shipments
- Tasks

Rules:

- Leads belong in `02_crm/01_leads/`.
- Approved customers belong in `02_crm/02_customers/`.
- Approved suppliers belong in `02_crm/03_suppliers/`.
- Active opportunities belong in `02_crm/04_deals/active/`.
- Won deals move to `02_crm/04_deals/won/`.
- Lost deals move to `02_crm/04_deals/lost/`.
- Before issuing a proforma for a strategic, low-margin, or concession-driven deal, complete a pricing governance review that records the guardrail, requested exception, rationale, and release decision.
- When a deal is won and execution is starting, complete a deal launch handoff that links commercial commitments, owners, payment gates, compliance path, and operational release conditions.
- Before moving a deal to `won/` or `lost/`, complete a win/loss review that captures the decision driver, commercial gap, competitor or alternate source, internal lesson, and re-entry potential.
- Tasks belong in `02_crm/05_tasks/` unless they are shipment-specific, then place them in `03_operations/`.
- Every active deal should clearly show customer, supplier, product, quantity, incoterm, target margin, and next step.
- Every shipment should clearly show booking status, key dates, ports, broker, carrier, and missing documents.
- Before a shipment is treated as ETD-ready or externally released, complete a pre-shipment release review covering packet integrity, filing readiness, release blockers, and final owner approval.
- After arrival or delivery, complete a shipment review log so operational lessons, service quality, claims exposure, and supplier-performance signals are captured before closeout or archive.
- After the trade economics are materially known, complete a trade profitability review so planned versus realized margin, variance drivers, and next-cycle pricing rules are governed before final closeout.
- A lead should exist before a customer record is opened.
- A customer record should exist before a deal is treated as structurally active.
- A supplier intake should exist before supplier approval, and supplier approval should exist before live purchasing.
- A deal should exist before proforma, sales contract, or shipment execution starts.
- A shipment should exist before operational document packets and live filing control are treated as active.
- A complaint or CAPA should always link back to the relevant shipment, lot, supplier, and customer.
- Strategic cross-functional matters should use a matter control index when multiple record sets must stay synchronized for release or stage decisions.
- Founder approvals that change pricing, credit posture, trust posture, release timing, compliance posture, or archive authorization should be captured in a founder decision register, not left only in dashboard notes.
- If the founder decides to proceed despite fragile or only controlled trust posture, record the override class, what still remains blocked, the recheck trigger, and the proof needed to return to standard rules.
- If a trust-linked founder override is active, keep the founder decision register, trust posture matrix, matter control index, and any linked release, payment, or sourcing controls synchronized before treating the matter as executable.
- When multiple deals or shipments compete for the same cash, capacity, or release bandwidth, capture the prioritization in a capital allocation and release priority review before relaxing controls.
- When a high-impact risk could force fast cross-functional action, convert it into an executive scenario and contingency review before the trigger lands.
- When a major plan, forecast, or release path depends on something that still needs proof, capture it in an executive assumption and dependency review before treating it as operating truth.
- When quarter priorities, milestone timing, or founder commitments start drifting from the agreed plan, capture the gap in an executive plan variance and recovery review before quietly redefining success.
- When the same strategic issue keeps resurfacing despite clear ownership, capture it in an executive owner accountability and follow-through review before assuming the system only needs more visibility.
- When a trust-linked founder override reaches the live executable stage, convert the check into a task record with owner, deadline, gate, and closure evidence instead of leaving it only in dashboards or founder notes.
- When multiple executable checks are active or one executable check is moving from live gate into closeout and archive proof, capture them in a trust-override executable check control board before treating the system as fully controlled.
- When supplier, freight, broker, duty, or other shipment-linked payments are due, capture the release basis in a funding and payables release review before treating urgency alone as approval.
- When a complaint, service issue, or quality variance creates potential credit, replacement, or supplier-recovery exposure, capture it in a claims, credits, and recovery review before it disappears into ad hoc concessions.
- When a complaint, inspection finding, supplier issue, or repeated service failure still has weak root-cause logic or unfinished preventive action, capture it in a CAPA and preventive action review before treating the case as closed.
- When multiple founder-approved exceptions or temporary deviations start stacking on the same matter, capture them in an executive exceptions and override review before they become invisible policy.
- Trust-linked overrides should stay narrower than ordinary exceptions and must never be treated as blanket permission across release, payment, pricing, and sourcing.
- When a founder approval depends on multiple linked dashboards or source records, confirm the matter in an executive control integrity and decision readiness review before treating the call as decision-ready.
- A trust override is not decision-ready until the same override class, blocked actions, and return-to-standard rule appear consistently across the linked records that will govern execution.
- If a task has an owner, deadline, and blocker, it should become a task record, not just a note.
- Follow `05_sops/04_crm/Commercial-Execution-Lifecycle-SOP.md` when deciding stage transitions.

## 8. Compliance Entity Management

Maintain these compliance entities consistently:

- ISF
- FSVP
- Prior Notice
- Traceability
- Inspections

Rules:

- ISF files belong in `04_compliance/01_isf/`.
- FSVP files belong in `04_compliance/02_fsvp/`.
- Prior Notice files belong in `04_compliance/03_prior-notice/`.
- Traceability files belong in `04_compliance/04_traceability/`.
- Inspection records belong in `04_compliance/05_inspections/`.
- Supplier qualification and approval material belongs in `04_compliance/06_supplier-approval/`.
- Each live import program must have an auditable path from supplier approval to shipment clearance.
- Each compliance file should identify the product, supplier, customer, importer, shipment or lot, responsible owner, due dates, and status.
- Never bury compliance approvals inside general notes.
- Keep intake files, supporting evidence, and final approvals together.

## 9. Archive Rules

- Archive only completed, inactive, or superseded material.
- Do not archive active deals, open complaints, active supplier approvals, or in-transit shipments.
- Preserve original dates and version history when archiving.
- Use `07_archive/` for clean long-term storage by function.
- Use `01_templates/08_closeout/Closeout-and-Archive-Record-MASTER.md` for cross-functional matters before final archive release.
- Follow `05_sops/07_archive/Archive-Closeout-SOP.md` when deciding readiness, retention, and archive approval.
- If a trust-linked executable check was part of the live path, preserve its closure evidence in the document register, shipment review, and closeout package before archive release.

## 10. Daily Operating Standard

- Start from `06_dashboard/01_executive/`.
- Update CRM first.
- Create working copies second.
- Update operations and compliance status third.
- Update tasks and command-center dashboards only after source records are current.
- Archive only after a deal, shipment, or project is fully closed.

## 11. Output Quality Standard

- Everything created here must feel boardroom-ready.
- Content should be concise, structured, and operationally useful.
- If uncertain where a file belongs, prefer the folder that supports active execution, not passive storage.
