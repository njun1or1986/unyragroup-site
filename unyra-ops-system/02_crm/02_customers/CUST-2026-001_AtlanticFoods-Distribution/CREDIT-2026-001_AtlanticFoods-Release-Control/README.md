# Credit Release Control

| Credit Release Control | Current Standard |
| --- | --- |
| Credit Control ID | `CREDIT-2026-001` |
| Customer | Atlantic Foods Distribution |
| Linked deal | `DEAL-2026-001` Atlantic Foods garlic offer |
| Status | Approved with release controls |
| Trust tier | Fragile |
| Purpose | Convert Atlantic Foods credit approval, receivable timing, deposit proof, response behavior, release evidence, and founder override posture into explicit release permission. |
| Source rule | Update customer account room, trust posture, collections case, cash outlook, formal offer, response SLA, pricing review, founder decision module, executable-check, shipment release, funding release, credit board, and trust matrix first, then refresh this release-control record. |
| Decision rule | Approval with release controls is not normal release permission; no exposure, movement, or customer-facing release language widens until dated acknowledgment, deposit proof, collection posture, pricing guardrail, and live-gate evidence support the same answer. |

## Current Release Reading

| Field | Current Answer |
| --- | --- |
| Credit posture | Approved with release controls only. |
| Release posture | No accelerated release without dated acknowledgment, deposit proof, pricing guardrail, and collection plan. |
| Receivable posture | USD 96,000 remains open and founder-visible. |
| Offer posture | USD 214,000 remains high-confidence but not committed until response, payment, pricing, and release proof align. |
| Working-capital posture | USD 82,000 working-capital and supplier-slot need cannot move ahead of customer-side proof. |
| Cash-risk posture | USD 128,000 release-dependent cash risk remains active in the credit board. |
| Founder-gated capital | USD 186,000 remains too large to run on informal comfort. |
| Closeout posture | Return to standard release rules is blocked until trust, collections, cash, funding, and release records carry one answer. |

## Source Refresh Stack

| Source Layer | Evidence Route | Release-Control Purpose |
| --- | --- | --- |
| Customer account room | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/README.md` | Keeps credit posture tied to account health, claim exposure, trust behavior, concentration, cash timing, and growth permission. |
| Trust posture controls | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/TPST-2026-Q2_AtlanticFoods-Trust-Posture/README.md`, `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md`, and `06_dashboard/38_counterparty-trust/Strategic-Counterparty-Trust-and-Response-Review.md` | Converts fragile trust into release speed limits, same-cycle proof requirements, and founder-visible escalation. |
| Collections and cash controls | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/COLLECT-2026-001_April-Receivable/README.md`, `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CASH-2026-005_AtlanticFoods-Cash-Outlook/README.md`, and `06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.md` | Anchors the USD 96,000 receivable, promise-to-pay timing, release-dependent cash risk, and downside timing view. |
| Offer and response controls | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md`, `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md`, and `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMCTRL-2026-Q2_AtlanticFoods-Communication-Control/README.md` | Confirms dated acknowledgment, commercial review status, payment-structure proof, reminder cadence, and contained customer language. |
| Deal and pricing controls | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/README.md`, `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/PRICE-2026-001_AtlanticFoods-Garlic-Pricing-Review/README.md`, and `06_dashboard/12_pricing-governance/Pricing-Governance-Board.md` | Prevents quote confidence, concession logic, margin guardrail, or revenue forecast from outrunning proof. |
| Founder and exception controls | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/DEC-2026-001_AtlanticFoods-Founder-Decisions/README.md`, `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXC-2026-Q2_AtlanticFoods-Exception-Review/README.md`, and `06_dashboard/32_exception-governance/Executive-Exceptions-and-Override-Review.md` | Keeps any release exception attached to founder approval, blocked actions, recheck triggers, and return-to-standard proof. |
| Executable and shipment gates | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXECCHK-2026-001_AtlanticFoods-Override-Closure/README.md`, `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md`, and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` | Blocks shipment acceleration, broker handoff, supplier allocation, supplier settlement, or payment movement unless live gates match. |
| Credit board and release queue | `06_dashboard/09_credit-risk/Credit-and-Release-Control-Board.md` and `06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.md` | Places the Atlantic Foods release decision in the portfolio-level credit, capital, and founder-gated release queue. |

## Approved Release Boundary

| Boundary Item | Current Rule | What It Allows | What It Does Not Allow |
| --- | --- | --- | --- |
| Credit approval | Approved with release controls. | Controlled commercial review and release revalidation after proof is current. | Normal release speed, informal shipment movement, or expanded credit exposure. |
| Trust tier | Fragile. | Release decisions may be reconsidered only through proof-led trust and credit controls. | Acceleration based on relationship history, deal attractiveness, or verbal comfort. |
| Receivable status | USD 96,000 remains open. | Founder-visible collection plan and cash-outlook alignment. | Release confidence improvement while promise-to-pay timing is weak or unclear. |
| Offer value | USD 214,000 high-confidence opportunity remains not committed. | Guarded quote follow-through while response and payment proof are open. | Treating the offer as booked revenue or release clearance. |
| Working-capital need | USD 82,000 supplier-slot need remains proof-gated. | Narrow capital review after customer-side evidence aligns. | Supplier-slot funding ahead of payment, trust, and release proof. |

## Proof Requirements Before Release Widens

| Required Proof | Minimum Standard | If Missing | Evidence Route |
| --- | --- | --- | --- |
| Dated acknowledgment | Buyer acknowledgment is dated, retrievable, and tied to the formal offer packet. | Preserve commercial-review-only posture and trigger controlled follow-up. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` |
| Deposit proof or payment structure | Deposit evidence or payment-structure confirmation supports the release ask. | Keep release confidence blocked and update collections/cash posture. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/COLLECT-2026-001_April-Receivable/README.md` |
| Collection plan | USD 96,000 receivable has a dated owner, promise-to-pay path, and escalation status. | Keep credit posture at controlled hold and preserve founder follow-up. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CASH-2026-005_AtlanticFoods-Cash-Outlook/README.md` |
| Pricing guardrail | Offer validity, concession, margin guardrail, and response freshness are current. | Revalidate pricing before confidence or release language changes. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/PRICE-2026-001_AtlanticFoods-Garlic-Pricing-Review/README.md` |
| Live gate alignment | Executable-check, release gate, funding release, scenario, and risk answers match. | Block shipment, broker, supplier, payment, and release movement language. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |

## Allowed, Blocked, and Founder-Only Movement

| Movement Class | Current Rule | Required Evidence | Owner |
| --- | --- | --- | --- |
| Allowed | Commercial review, controlled receipt follow-up, and release revalidation may continue. | Formal packet, response SLA, communication control, and pricing review stay current. | Commercial owner |
| Allowed with proof | Release posture may be reconsidered after dated acknowledgment, deposit proof, collection plan, pricing guardrail, and live gate alignment. | Trust posture, credit board, collections case, cash outlook, executable-check, release gate, and founder decision agree. | Founder, finance, commercial, and operations owners |
| Blocked | Accelerated release, expanded credit, widened shipment movement, broker handoff implication, supplier allocation implication, and payment-clearance language. | Not applicable until proof set is complete. | Founder office |
| Blocked | Treating the USD 214,000 opportunity as committed revenue or release clearance. | Response, pricing, payment, release, and revenue forecast records must align first. | Commercial owner |
| Founder-only | Any exception that widens exposure, supplier funding, shipment movement, or customer-facing release language before the proof set closes. | Founder decision, exception review, executable-check, credit board, and capital allocation records carry one answer. | Founder office |

## Exposure and Cash Alignment

| Exposure Item | Current Reading | Release-Control Consequence | Evidence Route |
| --- | --- | --- | --- |
| Open receivable | USD 96,000 INV-2026-041 / garlic program deposit balance. | Largest near-term receivable must govern release confidence. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/COLLECT-2026-001_April-Receivable/README.md` |
| Release-dependent cash risk | USD 128,000 remains active in the credit board. | Release controls stay disciplined until incoming and outgoing cash assumptions match. | `06_dashboard/09_credit-risk/Credit-and-Release-Control-Board.md` |
| Founder-gated capital | USD 186,000 remains visible in the portfolio release view. | Capital movement cannot rely on informal comfort. | `06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.md` |
| Working-capital / supplier slot | USD 82,000 need is tied to the Atlantic Foods offer path. | Supplier-slot funding stays behind customer-side proof. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/README.md` |
| Cash outlook | May 2026 rolling 30-day outlook remains active founder watch. | Any promise slip or release posture change reopens the forecast. | `06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.md` |

## Revalidation Triggers

| Trigger | Immediate Action | Release Consequence | Owner |
| --- | --- | --- | --- |
| Dated acknowledgment is absent or stale | Refresh response SLA and communication control. | No release confidence improvement. | Commercial owner |
| Deposit proof or payment-structure proof is absent | Refresh collections, cash outlook, and credit board. | Keep accelerated release blocked. | Finance and commercial owners |
| USD 96,000 collection timing slips | Reconcile promise-to-pay, cash forecast, and release posture. | Preserve hold until cash timing is credible. | Finance owner |
| Pricing validity or concession guardrail weakens | Reopen pricing governance before any revised terms or release language leave. | Freeze quote confidence and release implication. | Founder office and commercial owner |
| Executable-check, shipment release, or funding proof diverges | Route through live gates and scenario/risk controls. | Block shipment, broker, supplier, payment, and archive movement. | Founder office with operations owner |
| Two clean response cycles close with payment proof current | Reopen return-to-standard review. | Release may move from fragile hold to controlled review only after all records are refreshed. | Founder and commercial owner |

## Founder Review Gate

| Gate Question | Required Answer Before Release Widens | If Answer Is Weak | Owner |
| --- | --- | --- | --- |
| Is credit approval still bounded? | The record says approved with release controls, not normal release permission. | Keep the hold and refresh the credit board. | Founder office |
| Is trust proof current? | Trust posture, matrix, and strategic review support the same fragile-tier release answer. | Keep release acceleration blocked. | Founder and commercial owner |
| Is payment proof current? | Deposit proof, collection plan, and cash outlook support release posture. | Keep release and supplier funding held. | Finance owner |
| Is movement proof current? | Executable-check, pre-shipment release, funding release, scenario, and risk records agree. | Remove movement language and escalate same day. | Founder office with operations owner |
| Is the exception recoverable later? | Founder decision, exception review, credit board, and account room prove why release was held or widened. | Keep return-to-standard blocked. | Founder office |

## End-of-Cycle Closeout

| Closeout Field | Current Answer | Evidence Route |
| --- | --- | --- |
| Credit status | Atlantic Foods remains approved with release controls. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` |
| Release status | Accelerated release remains blocked without dated acknowledgment, deposit proof, pricing guardrail, collection plan, and live gate alignment. | `06_dashboard/09_credit-risk/Credit-and-Release-Control-Board.md` |
| Trust status | Fragile trust continues to govern release speed and growth posture. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/TPST-2026-Q2_AtlanticFoods-Trust-Posture/README.md` |
| Cash status | USD 96,000 receivable, USD 128,000 release-dependent cash risk, and USD 186,000 founder-gated capital remain visible. | `06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.md` |
| Records updated | Release control now carries route-backed approval boundary, proof requirements, allowed/blocked/founder-only movement, exposure alignment, revalidation triggers, founder gates, and closeout logic. | `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` |
