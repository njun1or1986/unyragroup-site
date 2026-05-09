# Atlantic Foods Collections Case

| Collections Control | Current Standard |
| --- | --- |
| Collection ID | `COLLECT-2026-001` |
| Customer | Atlantic Foods Distribution |
| Exposure | `INV-2026-041` / garlic program deposit balance |
| Outstanding amount | USD 96,000 |
| Status | Reminder sent, founder follow-up pending |
| Forecast window | May 2026 rolling 30-day cash-control window |
| Purpose | Convert the Atlantic Foods receivable into one controlled view of promise-to-pay evidence, cash forecast effect, release-control consequence, escalation timing, and founder closeout. |
| Source rule | Update customer account room, cash outlook, credit release control, daily collections dashboard, cash forecast, response SLA, formal offer, funding release, capital allocation, and trust posture first, then refresh this collections case. |
| Decision rule | Do not treat the USD 96,000 receivable as release confidence until the dated plan, customer response, credit posture, and cash forecast all carry the same answer. |

## Current Receivable Reading

| Field | Current Answer |
| --- | --- |
| Receivable status | Open and founder-visible. |
| Collection posture | Reminder sent, founder follow-up pending. |
| Reliability reading | Not clean enough for normal release confidence while founder follow-up is pending. |
| Miss risk | Medium; one-week delay creates a USD 96,000 timing shift in the cash forecast. |
| Release consequence | Release acceleration remains held until dated collection plan, deposit proof, pricing guardrail, and credit release posture align. |
| Cash consequence | The May 2026 outlook stays tight but governable only if this receivable converts on time. |
| Account consequence | Growth remains controlled because cash behavior is still part of the fragile trust posture. |
| Founder posture | Finance owner must confirm the dated collection plan before any release or account-growth confidence widens. |

## Source Refresh Stack

| Source Layer | Evidence Route | Collections-Control Purpose |
| --- | --- | --- |
| Customer account room | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/README.md` | Keeps the receivable tied to account health, trust, release quality, concentration, pricing, and claim posture. |
| Cash outlook | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CASH-2026-005_AtlanticFoods-Cash-Outlook/README.md` and `06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.md` | Converts the USD 96,000 receivable into the 30-day cash view, stress gap, and downside timing consequence. |
| Credit release controls | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` and `06_dashboard/09_credit-risk/Credit-and-Release-Control-Board.md` | Blocks release confidence from widening before collection timing, deposit proof, and release evidence are current. |
| Collections dashboard | `06_dashboard/06_collections/Daily-Collections-Control-Center.md` | Provides portfolio-level aging, promise-to-pay, escalation, trade-hold, and next-seven-day action context. |
| Trust posture controls | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/TPST-2026-Q2_AtlanticFoods-Trust-Posture/README.md` and `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` | Keeps fragile trust tied to payment behavior and two-clean-cycle recovery logic. |
| Formal offer and response controls | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md` and `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` | Links acknowledgment, commercial review, offer decision, and deposit-response timing to collection quality. |
| Funding and capital controls | `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md`, and `06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.md` | Prevents outgoing cash, supplier settlement, and reservation spend from outrunning receivable proof. |
| Revenue and pricing controls | `06_dashboard/23_revenue-forecast/Revenue-Forecast-and-Commitments-Review.md`, `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/README.md`, and `06_dashboard/12_pricing-governance/Pricing-Governance-Board.md` | Prevents the USD 214,000 active opportunity from being treated as cleaner than payment evidence supports. |

## Promise-to-Pay Evidence Standard

| Evidence Item | Minimum Standard | If Missing | Owner |
| --- | --- | --- | --- |
| Dated collection plan | Customer provides date, amount, and payer-side confirmation path for the USD 96,000 balance. | Keep founder follow-up pending and release acceleration blocked. | Finance owner |
| Deposit proof or payment-structure proof | Deposit evidence or payment-structure confirmation is retrievable and matches credit release control. | Revalidate cash outlook and do not widen release language. | Finance and commercial owners |
| Customer acknowledgment | Packet receipt, commercial review status, and payment-response timing are current. | Refresh response SLA and preserve commercial-review-only posture. | Commercial owner |
| Cash forecast update | May 2026 rolling view reflects the latest promise date and downside timing risk. | Treat forecast confidence as medium and keep stress gap visible. | Finance owner |
| Credit posture update | Collections result is reflected in credit release control and the credit board. | Do not treat collection promise as release permission. | Founder and finance owners |

## Daily Follow-Up Cadence

| Cadence Moment | Required Action | Control Output | Evidence Route |
| --- | --- | --- | --- |
| Same day after reminder | Confirm whether buyer received the receivable reminder and can provide a dated plan. | Acknowledgment state is recorded and response clock is current. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` |
| Next finance check | Confirm amount, expected date, payer contact, and proof method. | Promise-to-pay quality is classified as clean, fragile, or missing. | `06_dashboard/06_collections/Daily-Collections-Control-Center.md` |
| Before release review | Reconcile collection plan against credit release, trust posture, and cash outlook. | Release posture either remains held or enters controlled revalidation. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` |
| If timing slips | Refresh forecast, escalate to founder visibility, and preserve release hold. | USD 96,000 timing shift is visible before cash or shipment movement changes. | `06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.md` |
| End of cycle | Record collection status, release consequence, cash consequence, and next owner action. | Founder review can see whether the receivable reduced risk or kept controls active. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/COLLECT-2026-001_April-Receivable/README.md` |

## Release and Trade-Hold Consequence

| Control Question | Current Answer | Release or Trade Consequence | Evidence Route |
| --- | --- | --- | --- |
| Can release confidence widen? | Not yet. | No accelerated release until dated collection plan, deposit proof, pricing guardrail, and live gate alignment are current. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` |
| Can account growth widen? | Not yet. | Growth remains controlled while payment behavior contributes to fragile trust. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/TPST-2026-Q2_AtlanticFoods-Trust-Posture/README.md` |
| Can supplier funding move faster? | No. | Outgoing cash should not outrun incoming cash confidence. | `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` |
| Can the USD 214,000 opportunity be treated as committed? | No. | Revenue remains high-confidence only until response, payment structure, pricing, and release proof align. | `06_dashboard/23_revenue-forecast/Revenue-Forecast-and-Commitments-Review.md` |
| Can collection proof support return to standard rules? | Only after proof closes. | Two clean response cycles, payment proof, and refreshed trust/credit records are required. | `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` |

## Cash Forecast Linkage

| Cash Signal | Current Reading | Collection Consequence | Founder Control Rule |
| --- | --- | --- | --- |
| Expected inflows next 30 days | USD 486,000 versus USD 500,000+ target. | The collection window is workable only if top promises convert on time. | Keep release decisions tied to cash proof, not commercial momentum. |
| Committed collections next 14 days | USD 214,000 versus USD 240,000+ target. | Daily follow-up is required because the near-term cluster is narrow. | Treat missed promises as forecast events, not routine delay. |
| Release-dependent cash at risk | USD 128,000 versus below USD 75,000 target. | Collection proof should reduce release-dependent exposure before movement widens. | Maintain credit holds until cash risk moves down. |
| Stress gap | USD 92,000 versus below USD 50,000 target. | A slipped Atlantic Foods promise keeps downside response active. | Freeze non-priority release and reservation movement if gap widens. |
| One-week delay impact | USD 96,000 timing shift. | The receivable can materially distort the 30-day view. | Escalate immediately if dated plan is absent or slips. |

## Escalation Triggers

| Trigger | Immediate Action | Release Consequence | Owner |
| --- | --- | --- | --- |
| Dated plan is not received | Escalate from routine reminder to founder-visible follow-up. | Keep release acceleration blocked. | Finance owner |
| Payment date slips by one week | Refresh cash forecast and stress view. | Preserve credit hold and revalidate funding release. | Finance owner |
| Deposit proof or payment-structure proof is absent | Refresh credit release and trust posture. | Do not widen release confidence or movement language. | Finance and commercial owners |
| Formal offer response becomes stale | Refresh response SLA, pricing validity, and communication control. | Keep revenue high-confidence only, not committed. | Commercial owner |
| Outgoing shipment funding pressure appears | Reconcile funding release, executable-check, and cash outlook. | No supplier settlement or broker handoff widening without aligned proof. | Founder office with finance and operations owners |

## Founder Review Gate

| Gate Question | Required Answer Before Collection Risk Reduces | If Answer Is Weak | Owner |
| --- | --- | --- | --- |
| Is the collection plan dated? | Date, amount, payer path, and proof method are recorded. | Keep founder follow-up pending. | Finance owner |
| Is the cash forecast refreshed? | 30-day outlook, stress gap, and release-dependent exposure reflect the latest promise. | Treat liquidity posture as tight and unproven. | Finance owner |
| Is credit posture synchronized? | Credit release control and credit board carry the same collection answer. | Keep release acceleration blocked. | Founder and finance owners |
| Is customer response current? | Offer acknowledgment, commercial review, and deposit-response timing are current. | Escalate response control before release or pricing language changes. | Commercial owner |
| Is the case recoverable later? | Collections, cash, credit, trust, response, and funding records can prove the decision trail. | Keep closeout provisional. | Founder office |

## End-of-Cycle Closeout

| Closeout Field | Current Answer | Evidence Route |
| --- | --- | --- |
| Collection status | USD 96,000 remains open with reminder sent and founder follow-up pending. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/COLLECT-2026-001_April-Receivable/README.md` |
| Release status | Release acceleration remains held until collection proof supports credit posture. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` |
| Cash status | May 2026 cash outlook remains active founder watch because the receivable drives near-term timing sensitivity. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CASH-2026-005_AtlanticFoods-Cash-Outlook/README.md` |
| Trust status | Payment behavior remains part of the fragile-tier operating constraint. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/TPST-2026-Q2_AtlanticFoods-Trust-Posture/README.md` |
| Records updated | Collections case now carries route-backed promise-to-pay evidence, daily cadence, release/trade-hold consequence, cash forecast linkage, escalation triggers, founder gates, and closeout logic. | `06_dashboard/06_collections/Daily-Collections-Control-Center.md` |
