# Formal Offer Packet

| Packet Control | Current Standard |
| --- | --- |
| Packet ID | `COMM-2026-001` |
| Status | Controlled communication set |
| Purpose | Controlled customer-facing release packet for a formal Atlantic Foods commercial offer, response window, pricing validity, and buyer review. |
| Customer | Atlantic Foods Distribution |
| Linked deal | `DEAL-2026-001` Atlantic Foods garlic offer |
| Owner | Sales desk with commercial owner oversight |
| Source rule | Update active deal room, pricing review, response SLA, communication control, language reference, customer room, trust posture, credit release, executable-check, scenario, risk, and pricing governance records first, then refresh this packet. |
| Wording rule | The packet may confirm commercial review, response deadline, pricing validity, and required buyer action only; it must not imply supplier final allocation, shipment release, or payment clearance. |

## Packet Profile

| Field | Current Reading |
| --- | --- |
| Room type | Customer-facing formal offer packet |
| Offer posture | Contained / commercial review only |
| Deal stage | Offer review |
| Pricing posture | Founder concession review active |
| Revenue context | USD 214,000 high-confidence opportunity while pricing, response, payment, and release controls remain current. |
| Trust posture | Atlantic Foods remains fragile enough that dated acknowledgment and deposit proof still affect release confidence. |
| Current executable-check posture | `EXECCHK-2026-001` remains active tight watch for any movement or payment implication. |
| Current containment posture | `SCEN-2026-005` and `RISK-2026-008` define the same contained-movement answer before outward language can widen. |

## Source Refresh Stack

| Source Layer | Evidence Route | Founder Control Purpose |
| --- | --- | --- |
| Active deal room | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/README.md` | Keeps the customer-facing packet tied to the live deal's control-before-commitment posture. |
| Pricing review | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/PRICE-2026-001_AtlanticFoods-Garlic-Pricing-Review/README.md` | Confirms concession requests and guardrail decisions before a controlled proforma leaves the company. |
| Response SLA control | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` | Governs acknowledgment timing, reminder cadence, offer validity, and escalation before confidence changes. |
| Customer communication control | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMCTRL-2026-Q2_AtlanticFoods-Communication-Control/README.md` | Centralizes what was sent, response deadline, escalation path, and contained-movement wording. |
| Institutional language reference | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMSTYLE-2026-Q2_AtlanticFoods-Institutional-Language-Reference/README.md` | Keeps subject, opening, action request, deadline, and escalation wording stable and institutional. |
| Customer account room | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/README.md` | Connects offer posture to trust, release, collections, cash, concentration, pricing, and claim recovery. |
| Trust posture record | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/TPST-2026-Q2_AtlanticFoods-Trust-Posture/README.md` | Converts fragile trust into allowed, blocked, and founder-only commercial movement. |
| Credit release control | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` | Prevents release confidence from widening without dated acknowledgment and deposit proof. |
| Executable-check source | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXECCHK-2026-001_AtlanticFoods-Override-Closure/README.md` | Confirms whether any trust-linked movement implication is executable before the packet implies action. |
| Matter control and founder decisions | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control/README.md` and `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/DEC-2026-001_AtlanticFoods-Founder-Decisions/README.md` | Keeps live matter, override, exception, and founder-decision logic synchronized before commitment widens. |
| Pricing governance board | `06_dashboard/12_pricing-governance/Pricing-Governance-Board.md` | Reconciles concession, proforma validity, margin guardrails, forecast quality, and capital discipline. |
| Response escalation board | `06_dashboard/37_response-escalation/Counterparty-Response-SLA-and-Escalation-Board.md` | Keeps customer receipt, commercial review, offer decision, and deposit-response timing governed. |
| Scenario and risk controls | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` and `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Carries contained-movement stop rule, next safe movement, and same-day founder escalation consequence. |

## Packet Contents

| Working File | Role | Release Control Purpose |
| --- | --- | --- |
| Official document transmittal | Confirms what is being released and why. | Prevents the customer from treating the packet as broader movement approval. |
| Packet index | Keeps every attachment and response requirement visible. | Creates a retrievable map of the offer set, response duty, and evidence trail. |
| Institutional trade correspondence | Carries the formal commercial message. | Keeps the tone controlled, professional, and aligned to approved language rules. |
| Proforma invoice | Defines pricing, validity, and payment expectation. | Keeps pricing confidence tied to guardrail, validity window, and payment structure. |
| Product specification sheet | Anchors the product representation and buyer review. | Prevents buyer review from drifting outside the represented product and quality basis. |

## Customer Response Gate

| Required Customer Response | Timing Standard | Why It Matters | Escalation Consequence | Evidence Route |
| --- | --- | --- | --- | --- |
| Confirm receipt. | Same business day while the packet window is active. | Establishes that Atlantic Foods is reviewing the controlled packet, not scattered attachments or informal messages. | Escalate if acknowledgment timing weakens pricing validity, trust posture, or release confidence. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` |
| Confirm commercial review. | Inside the active review window. | Proves the buyer is evaluating the offer and specification set before UNYRA adjusts forecast confidence. | Keep the opportunity high-confidence only, not committed, if review proof is stale. | `06_dashboard/23_revenue-forecast/Revenue-Forecast-and-Commitments-Review.md` |
| Approve or reject the offer inside validity window. | Before pricing, payment, or release confidence changes. | Prevents stale offer confidence from turning into assumed commitment. | Revalidate pricing and packet language if the decision window slips. | `06_dashboard/12_pricing-governance/Pricing-Governance-Board.md` |
| Confirm payment structure or deposit proof when required. | Before release or capital posture widens. | Keeps customer-side cash proof aligned with release and working-capital discipline. | Keep release posture controlled if proof is absent or payment timing drifts. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` |

## Movement and Wording Guardrails

| Control Question | Current Answer | Allowed Wording | Blocked Wording or Action | Evidence Route |
| --- | --- | --- | --- | --- |
| Can the packet imply supplier final allocation? | No. It can confirm commercial review and buyer response only. | Confirm offer terms, specification review, deadline, and required buyer action. | Do not imply supplier final allocation, inventory reservation, or sourcing commitment beyond current controls. | `06_dashboard/12_pricing-governance/Pricing-Governance-Board.md` |
| Can the packet imply shipment release? | No. Shipment movement must remain behind live release, funding, and executable-check proof. | Refer only to commercial review and controlled next steps. | Do not imply shipment release, broker handoff, or logistics acceleration. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` |
| Can the packet imply payment clearance? | No. Payment and deposit logic must remain current in credit and cash controls. | State payment expectation and response requirement without implying cleared status. | Do not imply payment clearance, release clearance, or working-capital movement. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` |
| Can language widen if the customer responds cleanly? | Only after linked control revalidation. | Widen only after receipt, review, decision, payment structure, and control records align. | Do not widen based on verbal comfort or partial acknowledgment. | `06_dashboard/37_response-escalation/Counterparty-Response-SLA-and-Escalation-Board.md` and `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |

## Pricing and Proforma Validity Gate

| Gate | Current Reading | Required Control Before Confidence Improves | Founder Risk if Skipped | Evidence Route |
| --- | --- | --- | --- | --- |
| Concession guardrail | Founder concession review is active. | Final concession logic must show expiry, recovery, and margin guardrail. | Account-entry flexibility could become unintended pricing precedent. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/PRICE-2026-001_AtlanticFoods-Garlic-Pricing-Review/README.md` |
| Proforma validity | Offer remains controlled by response window and payment expectation. | Validity and response proof must be current before forecast or release confidence changes. | Stale offer confidence could be mistaken for commitment. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` |
| Forecast treatment | USD 214,000 remains high-confidence, not committed. | Approval, payment structure, and release controls must align before forecast band improves. | Revenue quality can outrun pricing proof and cash discipline. | `06_dashboard/23_revenue-forecast/Revenue-Forecast-and-Commitments-Review.md` and `06_dashboard/12_pricing-governance/Pricing-Governance-Board.md` |
| Cash and release confidence | Atlantic Foods trust and credit posture remain fragile and controlled. | Dated acknowledgment and deposit proof are required before release acceleration. | Commercial attractiveness could pull release speed faster than trust quality supports. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/TPST-2026-Q2_AtlanticFoods-Trust-Posture/README.md` |

## Executable and Containment Controls

| Control | Current Role | Packet Consequence | Evidence Route |
| --- | --- | --- | --- |
| `EXECCHK-2026-001` | Trust-linked executable check with active tight watch. | Packet wording cannot imply movement unless owner path, cutoff, gate status, and evidence state are current. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXECCHK-2026-001_AtlanticFoods-Override-Closure/README.md` |
| `SCEN-2026-005` | Trust-linked live-gate failure scenario. | Any pressure to widen payment, release, or movement without current executable proof triggers containment. | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` |
| `RISK-2026-008` | Risk consequence for improvised live-gate failure. | Divergent packet, response, payment, or movement language becomes same-day founder escalation. | `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` |
| `COMMCTRL-2026-Q2` | Live communication control set. | Every formal release, response deadline, and escalation path stays logged. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMCTRL-2026-Q2_AtlanticFoods-Communication-Control/README.md` |
| `RESP-2026-Q2` | Live response-control record. | Acknowledgment timing, reminder sequence, offer validity, and release consequence remain governed. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` |
| `COMMSTYLE-2026-Q2` | Live language control. | Subject, opening, action request, deadline, and escalation wording stay institutional and bounded. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMSTYLE-2026-Q2_AtlanticFoods-Institutional-Language-Reference/README.md` |

## Internal Follow-Through

| Follow-Through Item | Required Owner Action | Deadline or Timing | Status | Evidence Route |
| --- | --- | --- | --- | --- |
| Packet release record | Sales desk confirms what was sent, when response is due, and what escalation path applies. | Same business day as packet release | Active packet window | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMCTRL-2026-Q2_AtlanticFoods-Communication-Control/README.md` |
| Offer response tracking | Commercial owner monitors receipt, commercial review, approval or rejection, and deposit-response timing. | Inside validity window | Live response control | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` |
| Pricing revalidation | Founder and commercial owner revalidate concession logic before any proforma confidence widens. | Before forecast or release confidence changes | Founder concession review | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/PRICE-2026-001_AtlanticFoods-Garlic-Pricing-Review/README.md` |
| Containment revalidation | Founder office confirms scenario, risk, executable-check, and outward wording still carry the same answer. | Same day on any movement-pressure change | Active containment | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |
| Account-level synchronization | Customer room, credit posture, and trust posture reflect the packet response outcome. | Before growth or release posture widens | Controlled growth watch | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/README.md` |

## Founder Review Gates

| Gate Question | Required Answer Before Permission Widens | If Answer Is Weak | Primary Evidence Route | Owner |
| --- | --- | --- | --- | --- |
| Does the customer-facing packet match the current deal control answer? | Formal offer language matches matter control, founder decision, and exception posture. | Hold broader commitment language and refresh matter control. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control/README.md` | Founder office and commercial owner |
| Does pricing validity remain current? | Concession, proforma validity, response window, and payment expectation are aligned. | Revalidate offer before treating revenue confidence as stronger. | `06_dashboard/12_pricing-governance/Pricing-Governance-Board.md` | Founder and commercial owner |
| Does response proof support movement confidence? | Receipt, commercial review, approval or rejection, and deposit proof are current. | Keep packet at commercial review only and escalate response discipline. | `06_dashboard/37_response-escalation/Counterparty-Response-SLA-and-Escalation-Board.md` | Commercial owner |
| Does executable-check closure support any movement implication? | `EXECCHK-2026-001`, scenario, risk, funding, and live release layers match. | Block any supplier allocation, shipment release, or payment-clearance implication. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Founder office |
| Is the packet proof trail ready for later challenge or audit? | Packet index, correspondence, proforma, specification, response record, and communication control are retrievable. | Keep follow-through open until evidence route is complete. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMCTRL-2026-Q2_AtlanticFoods-Communication-Control/README.md` | Sales desk |

## End-of-Cycle Closeout

| Closeout Field | Current Answer | Evidence Route |
| --- | --- | --- |
| Formal offer packet status | Active controlled communication set for commercial review, pricing validity, response requirement, and buyer decision. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md` |
| Movement posture | Contained; no supplier final allocation, shipment release, or payment clearance is implied by the packet. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` and `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` |
| Pricing posture | Founder concession review remains active and must close before proforma confidence widens. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/PRICE-2026-001_AtlanticFoods-Garlic-Pricing-Review/README.md` |
| Response posture | Receipt, commercial review, and approval or rejection remain governed by live response control. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` |
| Records updated | Formal offer packet now carries route-backed packet contents, customer response duties, wording guardrails, pricing validity, executable checks, follow-through gates, and closeout logic. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md` |
