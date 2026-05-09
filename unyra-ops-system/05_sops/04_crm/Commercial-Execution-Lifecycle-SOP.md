# Commercial Execution Lifecycle SOP

| SOP control | Current standard |
| --- | --- |
| Status | ACTIVE SOP |
| Purpose | Define the required record flow from first lead capture through customer activation, deal control, shipment execution, compliance closure, and archive. |
| Source rule | Update the live source folder, linked customer or supplier record, deal, shipment, compliance, finance, task, dashboard, and archive records before changing lifecycle stage. |
| Decision rule | Do not advance a commercial matter to the next stage until the current stage has owner clarity, source evidence, linked controls, and a clear exit gate. |
| Template protection | Use approved master templates as protected starting points only; create working records in live matter folders and never use `01_templates/` as a working-copy area. |

Use this SOP when deciding the following lifecycle questions.

| Decision question | Required answer |
| --- | --- |
| When to create a new record | Create the record when the matter has a real owner, stage, and control need. |
| Where the record belongs | Store the record in the live source folder that owns the stage. |
| What must exist before the next stage starts | Close the stage gate with source evidence, owner clarity, and linked controls. |
| When a record can move to archive | Archive only after execution, collections, compliance evidence, and closeout are complete. |

## 1. Operating Principle

Source records come first.

| Principle | Required behavior |
| --- | --- |
| Source before dashboard | Dashboards summarize source records. They never replace them. |
| Stage changes require source evidence | Every stage change should be reflected in the source folder before it appears in a dashboard or executive rollup. |
| One current control answer | The live source record should make the current stage, owner, gate, and next action clear without relying on inbox memory. |

## 2. Lifecycle Spine

| Step | Lifecycle stage | Source-control outcome |
| --- | --- | --- |
| 1 | Lead captured | A real commercial angle exists and the lead is no longer just a name. |
| 2 | Lead qualified | Opportunity theme, authority, and discovery next step are defined. |
| 3 | Customer or supplier onboarding opened | The counterparty deserves structured onboarding or sourcing control. |
| 4 | Deal activated | Product, quantity, offer path, or negotiation structure is specific enough for an active deal. |
| 5 | Offer and contract cycle controlled | Pricing, offer, contract, confidentiality, and broker controls are routed through templates. |
| 6 | Won-deal launch handoff captured | Commercial win is handed into execution with owners, gates, and launch blockers visible. |
| 7 | Purchase and shipment execution opened | Purchasing, shipment, document, and release controls are live before movement widens. |
| 8 | Compliance filings and evidence completed | Filing, approval, evidence, and traceability paths are auditable. |
| 9 | Complaint or CAPA opened if needed | Product, customer, compliance, or recurrence risk is contained and linked. |
| 10 | Deal outcome review captured | Commercial learning is recorded before the opportunity leaves the active pipeline. |
| 11 | Commercial and operational closeout completed | Shipment, margin, collections, lessons, and follow-up are closed strongly enough to trust. |
| 12 | Archive only after full closure | Long-term storage starts only after active risk and execution obligations are complete. |

## 3. Stage Gate Rules

| Stage | Open or update | Required controlled record | Exit gate |
| --- | --- | --- | --- |
| Lead stage | Create a lead record in `02_crm/01_leads/` when a contact has a real commercial angle, not just a name. | Use `01_templates/07_crm/Lead-Intake-Form-MASTER.md`. Do not create a deal yet if product, timing, and next step are still unclear. | Move forward only when the lead has a defined opportunity theme, identifiable contact authority, and a real discovery next step. |
| Customer activation stage | Create a customer record in `02_crm/02_customers/` when the lead is commercially credible and deserves structured onboarding. | Use `01_templates/07_crm/Customer-Intake-Form-MASTER.md` and preserve the lead record for early funnel history. | A customer should not be treated as fully active until payment fit, operational needs, and compliance path are understood. |
| Supplier activation stage | Create a supplier intake record in `02_crm/03_suppliers/` when sourcing becomes real. Open supplier approval in `04_compliance/06_supplier-approval/` before live purchasing. | Use `01_templates/07_crm/Supplier-Intake-Form-MASTER.md` with `01_templates/05_compliance/Supplier-Approval-Form-MASTER.md`. | No supplier becomes active for purchasing until intake, sample fit if applicable, and compliance approval are aligned. |
| Deal activation stage | Create an active deal in `02_crm/04_deals/active/` when there is a defined product, quantity, offer path, or structured negotiation. | Use `01_templates/01_sales/Internal-Deal-Summary-MASTER.md` as the control memo and link the deal to the correct customer and supplier records. | A deal should not advance into live execution until commercial assumptions, source references, and next-step ownership are clear. |
| Offer and contract stage | Control all formal offers, terms, confidentiality, and intermediary commitments before they become executable. | Use `01_templates/01_sales/Pricing-Governance-Review-MASTER.md`, `01_templates/01_sales/Proforma-Invoice-MASTER.md`, `01_templates/04_legal/Sales-Contract-MASTER.md`, `01_templates/04_legal/NDA-MASTER.md`, and `01_templates/04_legal/Commission-Agreement-MASTER.md` when those controls apply. | Do not release purchasing or shipment execution on verbal acceptance alone. Written confirmation, controlled issue, record alignment, and approved pricing posture are required. |
| Won deal launch handoff stage | Use the handoff when a deal is commercially won and operational release is starting. Store the handoff in `02_crm/04_deals/won/`. | Use `01_templates/01_sales/Deal-Launch-Handoff-MASTER.md` to capture sold commitments, payment structure, linked controls, execution owners, and launch blockers. | Do not start live purchasing or shipment execution until owners, release gates, and linked source references are clear. |
| Purchasing and shipment execution stage | Open live purchasing work in `03_operations/01_purchasing/` or in the relevant active deal folder. Open shipment work in `03_operations/03_shipments/active/` when booking, coordination, or document prep begins. | Use `01_templates/02_purchasing/Purchase-Order-MASTER.md`, `01_templates/03_logistics/Commercial-Invoice-MASTER.md`, `01_templates/03_logistics/Packing-List-MASTER.md`, `01_templates/03_logistics/Shipping-Instructions-MASTER.md`, `01_templates/03_logistics/Pre-Shipment-Release-Review-MASTER.md`, `01_templates/03_logistics/Shipment-Review-Log-MASTER.md`, and `01_templates/09_finance/Trade-Profitability-Review-MASTER.md` as applicable. | Shipment execution may proceed only when commercial and compliance controls are live, packet integrity and filing readiness are closed, shipment lessons are captured, and trade economics are understood. |
| Compliance stage | Open ISF in `04_compliance/01_isf/`, FSVP in `04_compliance/02_fsvp/`, Prior Notice in `04_compliance/03_prior-notice/`, traceability in `04_compliance/04_traceability/`, and inspections, complaints, or CAPA in `04_compliance/05_inspections/`. | Use the compliance source folders and related templates before the matter is treated as fully controlled. | A shipment is not fully controlled until required filings, evidence, approvals, and traceability path are auditable. |
| Incident and CAPA stage | Open a complaint or incident file whenever the issue affects product quality, customer confidence, compliance confidence, or repeat business. | Use `01_templates/07_crm/Complaint-Form-MASTER.md` and `06_dashboard/31_capa-governance/CAPA-and-Preventive-Action-Review.md`, then link the case to shipment, lot, supplier, and customer records. | Do not close a case until containment, root-cause direction, customer response, preventive action, and closure evidence are documented strongly enough to trust. |
| Deal outcome review stage | Complete the win/loss review whenever a deal is won or lost. Store the final review in `02_crm/04_deals/won/` or `02_crm/04_deals/lost/`. | Use `01_templates/01_sales/Deal-Win-Loss-Review-MASTER.md` to capture decision driver, competitor or alternate source, price or term gap, internal lesson, and re-entry potential. | Do not move a deal out of `02_crm/04_deals/active/` without recording outcome logic and commercial learning. |
| Archive stage | Move won or completed commercial matters into the right archive path only after execution, collections, and closeout are done. Move lost deals into `02_crm/04_deals/lost/` and use `07_archive/` for completed long-term storage by function. | Use `01_templates/08_closeout/Closeout-and-Archive-Record-MASTER.md` for cross-functional matters and follow `05_sops/07_archive/Archive-Closeout-SOP.md` for archive readiness and retrieval discipline. | Never archive active shipments, open complaints, live supplier approvals, or unresolved compliance records. |

### Contained Movement Overlay

| Trigger | Required overlay |
| --- | --- |
| Offer or contract under contained movement | Proforma and contract wording should carry the current stop rule, next safe movement, and linked executable-check or scenario references instead of implying broader operational release. |
| Shipment or payment path under contained movement | Purchase order and shipping instructions should state what the supplier, forwarder, or broker may treat as authorized, what remains on hold, and who owns same-day revalidation before any wider movement. |

## 4. Task Creation Rule

Create a task when all of the following conditions are true.

| Task trigger | Required threshold |
| --- | --- |
| Owner | The work has a real owner. |
| Deadline | The work has a real deadline. |
| Business consequence | The work affects revenue, timing, compliance, or execution quality. |
| Slip risk | The work could slip if it is only mentioned in chat or email. |

Use `01_templates/07_crm/Task-Tracker-MASTER.md` for any action that needs governed follow-through.

## 5. Dashboard Synchronization Rule

Update records in the following order.

| Sequence | Record layer | Rule |
| --- | --- | --- |
| 1 | CRM or source record | Update the live source of truth first. |
| 2 | Operations or compliance record | Update execution and evidence records before rollup. |
| 3 | Task record | Create or refresh action control if follow-through is needed. |
| 4 | Dashboard or command center | Reflect the already-controlled source state last. |

Never reverse this order.

## 6. Minimum Linkage Standard

At every meaningful stage, source records should point to the related record set.

| Linkage | Required connection |
| --- | --- |
| Lead to customer intake | The qualified lead should connect to customer onboarding once activation starts. |
| Customer to deal | The customer record should show the active or historical deal relationship. |
| Supplier intake to supplier approval | Sourcing records should connect to compliance approval before purchasing. |
| Deal to proforma and contract | Commercial offer and commitment records should point back to the controlling deal. |
| Shipment to logistics packet | Movement records should connect to the packet that governed release. |
| Shipment to compliance filings | Shipment execution should connect to filing and evidence records. |
| Complaint to shipment, lot, supplier, and customer | Incident control should make root cause, counterparty, and product scope traceable. |

## 7. Decision Rule

If the next step is unclear, do not create more documents first.

| Clarifying question | Required answer before creating more records |
| --- | --- |
| What stage is the matter really in? | Identify the current lifecycle stage before adding documents. |
| What record is the current source of truth? | Confirm the controlling source record before updating dashboards or opening parallel files. |
| What single gate must close before the next stage? | Define the next gate, owner, and evidence requirement before widening execution. |

Then create only the records needed for that stage.
