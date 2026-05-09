# Atlantic Foods Cash Outlook

| Cash Outlook Control | Current Standard |
| --- | --- |
| Cash Outlook ID | `CASH-2026-005` |
| Customer | Atlantic Foods Distribution |
| Forecast period | May 2026 rolling 30-day outlook |
| Main dependency | Atlantic Foods receivable timing |
| Status | Active founder watch |
| Purpose | Convert Atlantic Foods receivable timing, release-dependent exposure, downside timing risk, outgoing funding pressure, and founder allocation decisions into one customer-specific liquidity view. |
| Source rule | Update collections case, credit release control, daily collections dashboard, cash forecast, funding release, capital allocation, active deal, response SLA, trust posture, and risk/scenario records first, then refresh this cash outlook. |
| Decision rule | Do not approve wider release, supplier funding, reservation spend, or account-growth confidence unless the cash outlook, collection proof, credit posture, and live release gates support the same answer. |

## Current Liquidity Reading

| Field | Current Answer |
| --- | --- |
| Cash posture | Tight but governable if release discipline holds. |
| Forecast confidence | Medium confidence with known Atlantic Foods collection timing sensitivity. |
| Open receivable | USD 96,000 `INV-2026-041` / garlic program deposit balance remains founder-visible. |
| One-week delay effect | A slipped Atlantic Foods payment creates a USD 96,000 timing shift. |
| Release-dependent cash at risk | USD 128,000 remains active in the credit and release view. |
| Downside gap | USD 92,000 stress gap remains wider than the desired below-USD 50,000 posture. |
| Outgoing funding pressure | Controlled but still too exposed to shipment-linked payment timing. |
| Founder posture | Only top release priorities should move until collection timing tightens and release-dependent exposure falls. |

## Source Refresh Stack

| Source Layer | Evidence Route | Cash-Control Purpose |
| --- | --- | --- |
| Collections case | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/COLLECT-2026-001_April-Receivable/README.md` | Anchors the USD 96,000 receivable, promise-to-pay evidence, escalation status, and release-hold consequence. |
| Credit release controls | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` and `06_dashboard/09_credit-risk/Credit-and-Release-Control-Board.md` | Keeps release confidence, supplier funding, and credit exposure behind collection proof and live-gate evidence. |
| Collections and cash dashboards | `06_dashboard/06_collections/Daily-Collections-Control-Center.md` and `06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.md` | Connects the customer-specific cash outlook to portfolio inflows, committed collections, stress gap, and release-dependent cash risk. |
| Customer account room | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/README.md` | Reconciles cash timing with account health, fragile trust, concentration, claim exposure, pricing, and growth posture. |
| Trust posture controls | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/TPST-2026-Q2_AtlanticFoods-Trust-Posture/README.md` and `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` | Keeps cash behavior tied to fragile trust, two-clean-cycle logic, and release-speed limits. |
| Offer and response controls | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/README.md`, `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md`, and `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md` | Confirms whether the USD 214,000 opportunity, payment structure, acknowledgment timing, and customer decision can support cash confidence. |
| Funding and capital controls | `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md`, and `06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.md` | Prevents outgoing cash, supplier settlement, shipment funding, and reservation spend from moving faster than inflow quality. |
| Risk and scenario controls | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` and `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Keeps downside response sequenced before another release request or cash-intensive exception is approved. |

## Outlook Snapshot

| KPI | Current Result | Target | Founder Note |
| --- | --- | --- | --- |
| Expected inflows next 30 days | USD 486,000 | USD 500,000+ | Acceptable only if two key promises convert on time. |
| Committed collections next 14 days | USD 214,000 | USD 240,000+ | Near-term cash relies too heavily on a narrow collection cluster. |
| Atlantic Foods receivable | USD 96,000 | Dated collection plan and proof current | Largest near-term dependency and active founder watch. |
| Release-dependent cash at risk | USD 128,000 | Below USD 75,000 | Exposure is manageable only while release controls remain disciplined. |
| Downside gap under stress view | USD 92,000 | Below USD 50,000 | Stress gap remains too wide for comfortable scaling. |
| Forecast confidence | Medium | Medium-high or better | Confidence improves only after collection proof and release posture align. |

## Forward Cash Movement

| Week | Opening Cash | Expected Inflows | Expected Outflows | Net Movement | Ending Cash | Founder Control Read |
| --- | --- | --- | --- | --- | --- | --- |
| Week 1 | USD 182,000 | USD 96,000 | USD 121,000 | -USD 25,000 | USD 157,000 | Most sensitive to Atlantic Foods conversion; do not widen release if proof is absent. |
| Week 2 | USD 157,000 | USD 118,000 | USD 84,000 | USD 34,000 | USD 191,000 | Governable if Week 1 collection timing is clean. |
| Week 3 | USD 191,000 | USD 142,000 | USD 97,000 | USD 45,000 | USD 236,000 | Medium confidence; preserve release discipline until inflow quality improves. |
| Week 4 | USD 236,000 | USD 130,000 | USD 104,000 | USD 26,000 | USD 262,000 | Improved but still not enough to justify loose supplier or reservation movement. |

## Exposure and Release Dependencies

| Exposure Item | Cash Impact | Dependency | Release Consequence | Evidence Route |
| --- | --- | --- | --- | --- |
| Atlantic Foods receivable | USD 96,000 | Collection promise converts on committed date with proof. | Release acceleration stays held until dated plan, deposit proof, pricing guardrail, and credit posture align. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/COLLECT-2026-001_April-Receivable/README.md` |
| Atlantic Foods release-dependent cash risk | USD 128,000 | Credit and release controls remain synchronized with cash proof. | Keep release-dependent exposure from rising with commercial momentum. | `06_dashboard/09_credit-risk/Credit-and-Release-Control-Board.md` |
| Atlantic Foods working-capital / supplier-slot need | USD 82,000 | Customer-side proof supports supplier-side movement. | Supplier-slot funding remains behind collection and release evidence. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` |
| Harbor Fresh proof path | USD 58,000 release exposure | Deposit, release evidence, and realized-margin proof stay visible. | May committed revenue should not become precedent until proof closes. | `02_crm/04_deals/won/DEAL-2026-003_HarborFresh_Garlic/PROFIT-2026-001_HarborFresh-Garlic-Trade-Review/README.md` |
| Rio Verde conditional reservation | USD 46,000 reservation pressure | Demand proof and allocation review clear the path. | Keep reservation spend conditional while cash gap remains wide. | `06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.md` |

## Scenario and Stress View

| Scenario | Cash Impact | Probability | Trigger | Required Response |
| --- | --- | --- | --- | --- |
| Atlantic Foods pays one week late | -USD 96,000 timing shift | Medium | Promise date slips or dated plan is absent. | Refresh cash forecast, preserve release hold, and intensify founder follow-up. |
| Strategic pricing exception approved without recovery path | Margin pressure and weaker inflow quality | Medium | Commercial urgency overrides pricing discipline. | Force pricing-governance review before release or forecast confidence improves. |
| Supplier watch item delays shipment cycle | -USD 42,000 timing shift | Low to medium | Shipment ready date slips. | Reconfirm backup sourcing and sequence cash needs. |
| Non-priority reservation spend moves early | USD 46,000 conditional cash pressure | Medium if weighted upside is over-treated | Rio Verde or supplier-slot pressure moves before demand proof. | Keep reservation and allocation spend conditional. |
| Release-dependent exposure rises instead of falls | USD 128,000 risk persists or widens | Medium | Release posture loosens before collections convert. | Freeze non-priority release movement and update credit board. |

## Revalidation Triggers

| Trigger | Immediate Action | Cash Consequence | Owner |
| --- | --- | --- | --- |
| Atlantic Foods dated collection plan is missing | Refresh collections case and keep founder follow-up pending. | Keep forecast confidence medium and preserve release hold. | Finance owner |
| Promise date slips by one week | Refresh 30-day cash forecast and stress gap. | USD 96,000 timing shift remains visible before movement changes. | Finance owner |
| Release posture changes | Reconcile credit board, cash outlook, funding release, and executable gates. | Do not allow release-dependent cash at risk to widen silently. | Founder and finance owners |
| Shipment-linked outgoing cash seeks movement | Revalidate funding release, pre-shipment release, and capital allocation. | Outgoing cash cannot outrun incoming cash confidence. | Finance and operations owners |
| Pricing or forecast confidence improves | Confirm payment structure, response proof, pricing guardrail, and cash outlook first. | Revenue confidence cannot substitute for cash proof. | Founder office and commercial owner |

## Founder Decision Gate

| Gate Question | Required Answer Before Cash Posture Improves | If Answer Is Weak | Owner |
| --- | --- | --- | --- |
| Is the Atlantic Foods collection plan dated? | Amount, expected date, payer path, and proof method are recorded. | Keep forecast confidence medium and release hold active. | Finance owner |
| Is release-dependent exposure falling? | USD 128,000 risk is stable or moving down, not widening. | Freeze non-priority release and supplier movement. | Founder and finance owners |
| Is the stress gap narrowing? | USD 92,000 gap moves toward the below-USD 50,000 target. | Preserve downside scenario and capital allocation discipline. | Founder office |
| Are outgoing cash commitments sequenced? | Funding release and capital allocation match collections reality. | Do not approve supplier settlement, broker handoff, or reservation spend expansion. | Finance and operations owners |
| Is the decision recoverable later? | Cash, collections, credit, funding, trust, response, and risk records prove the same answer. | Keep cash outlook under active founder watch. | Founder office |

## End-of-Cycle Closeout

| Closeout Field | Current Answer | Evidence Route |
| --- | --- | --- |
| Cash outlook status | Active founder watch remains appropriate. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CASH-2026-005_AtlanticFoods-Cash-Outlook/README.md` |
| Receivable status | USD 96,000 remains the largest near-term customer-specific cash dependency. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/COLLECT-2026-001_April-Receivable/README.md` |
| Release status | Release confidence remains constrained by collection proof, credit posture, and live gate alignment. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` |
| Downside posture | USD 92,000 stress gap keeps scenario response and capital allocation discipline active. | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` |
| Records updated | Cash outlook now carries route-backed liquidity reading, source stack, KPI snapshot, weekly movement, exposure dependencies, scenario stress view, revalidation triggers, founder gates, and closeout logic. | `06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.md` |
