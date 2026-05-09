# Customer Communication Control

| Communication Control | Current Standard |
| --- | --- |
| Control ID | `COMMCTRL-2026-Q2` |
| Status | Live control set |
| Purpose | Govern every Atlantic Foods customer-facing communication tied to the garlic offer before any message widens commitment, response expectation, pricing validity, release posture, payment confidence, or movement language. |
| Linked deal | `DEAL-2026-001` Atlantic Foods garlic offer |
| Controlled packet | `COMM-2026-001` formal offer packet |
| Owner | Commercial owner with founder-office oversight when wording, silence, pricing, trust, release, or movement confidence changes. |
| Source rule | Update formal offer packet, response SLA, language reference, pricing review, deal room, matter control, trust posture, credit release, executable-check, scenario, and risk records first, then refresh this communication control. |
| Control rule | No customer-facing message may create commercial, release, shipment, supplier, payment, or forecast confidence that the current evidence stack does not support. |

## Current Communication Posture

| Field | Current Reading |
| --- | --- |
| Communication posture | Live customer communication is allowed only inside contained commercial review. |
| Offer posture | USD 214,000 high-confidence opportunity remains uncommitted until response, pricing, payment, and release proof align. |
| Response posture | Receipt, commercial review, offer decision, revision requests, silence, and deposit proof are governed by live SLA control. |
| Language posture | Subject, opening, action request, deadline, reminder, and escalation wording must follow the institutional language reference. |
| Trust posture | Atlantic Foods remains fragile enough that dated acknowledgment and deposit proof affect release confidence. |
| Movement posture | Supplier allocation, shipment release, broker handoff, payment clearance, and revenue commitment language remain blocked without live gate proof. |

## Source Refresh Stack

| Source Layer | Evidence Route | Communication Control Purpose |
| --- | --- | --- |
| Formal offer packet | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md` | Defines the controlled packet, offer terms, specification review, validity window, and buyer action request. |
| Response and language controls | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md`, `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMSTYLE-2026-Q2_AtlanticFoods-Institutional-Language-Reference/README.md`, and `06_dashboard/37_response-escalation/Counterparty-Response-SLA-and-Escalation-Board.md` | Keeps response timing, reminder cadence, escalation language, and approved wording synchronized. |
| Pricing and forecast controls | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/PRICE-2026-001_AtlanticFoods-Garlic-Pricing-Review/README.md`, `06_dashboard/12_pricing-governance/Pricing-Governance-Board.md`, and `06_dashboard/23_revenue-forecast/Revenue-Forecast-and-Commitments-Review.md` | Prevents offer language, concession language, or forecast confidence from outrunning pricing proof. |
| Deal and matter controls | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/README.md`, `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control/README.md`, and `06_dashboard/10_matter-control/Active-Matter-Control-Board.md` | Keeps each outward message tied to the live control-before-commitment answer. |
| Customer trust and credit controls | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/README.md`, `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/TPST-2026-Q2_AtlanticFoods-Trust-Posture/README.md`, and `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` | Connects customer-facing language to trust, deposit proof, payment structure, credit posture, and release confidence. |
| Executable and containment controls | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXECCHK-2026-001_AtlanticFoods-Override-Closure/README.md`, `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md`, `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md`, and `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Blocks any message that would imply live movement without owner path, cutoff, gate status, evidence state, scenario, and risk alignment. |
| Shipment, release, and funding controls | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/README.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md`, and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` | Prevents customer communication from implying supplier allocation, broker handoff, shipment release, or payment clearance. |
| External communication standards | `06_dashboard/36_external-communications/Counterparty-Communication-Control-Board.md`, `00_brand/02_guidelines/UNYRA-Institutional-Communication-Style-Guide.md`, and `05_sops/08_external-communications/Counterparty-Communication-Standard-SOP.md` | Keeps cadence, tone, action requests, escalation, and institutional polish consistent across the system. |

## Communication Register Standard

| Register Field | Required Entry | Why It Matters | Evidence Route |
| --- | --- | --- | --- |
| Message ID or thread marker | Unique reference for the packet, reminder, revision, or escalation thread. | Prevents scattered inbox records from replacing the control log. | `06_dashboard/36_external-communications/Counterparty-Communication-Control-Board.md` |
| Send timestamp and owner | Date, time, sender, and commercial owner. | Starts the response clock and assigns accountability. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` |
| Message type | Packet transmittal, receipt request, commercial review follow-up, revision response, payment proof request, reminder, or escalation. | Determines which wording and SLA standard applies. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMSTYLE-2026-Q2_AtlanticFoods-Institutional-Language-Reference/README.md` |
| Action requested | Exact buyer action, deadline, and consequence if timing slips. | Keeps the message commercially clear without pressure drift. | `06_dashboard/37_response-escalation/Counterparty-Response-SLA-and-Escalation-Board.md` |
| Movement boundary | Clear statement that offer review does not equal supplier allocation, shipment release, payment clearance, or revenue commitment. | Protects founder control before commitment. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |
| Evidence destination | Where receipt, review, decision, payment proof, revision, or escalation will be recorded. | Makes closeout recoverable without reconstructing email history. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control/README.md` |

## Outbound Message Control Map

| Message Type | Allowed Purpose | Required Check Before Sending | Blocked Drift |
| --- | --- | --- | --- |
| Formal offer packet transmittal | Release the controlled offer set for commercial and specification review. | Formal offer packet, pricing review, language reference, and matter control are current. | Do not imply supplier allocation, shipment release, payment clearance, or booked revenue. |
| Receipt-confirmation request | Anchor packet receipt and start the response clock. | Response SLA defines same-day acknowledgment expectation. | Do not imply silence equals acceptance or release permission. |
| Commercial review follow-up | Confirm review status, answer scoped questions, or request a decision. | Pricing validity and approved wording remain current. | Do not introduce new concessions or revised terms without pricing review. |
| Payment proof request | Request deposit proof or payment-structure confirmation as a release-confidence input. | Trust posture and credit release records remain current. | Do not imply payment is cleared or release is approved. |
| Reminder after silence | Preserve validity discipline and trigger revalidation if needed. | Response SLA, pricing governance, and language reference agree on cadence. | Do not use pressure language or promise movement to induce response. |
| Founder escalation message | Document timing, validity, trust, or movement risk with controlled language. | Matter control, scenario, risk, and executable-check records carry one answer. | Do not improvise exceptions, concessions, or movement commitments. |

## Response and Deadline Control

| Response Item | Control Standard | Required Follow-Through | If Weak or Missing |
| --- | --- | --- | --- |
| Receipt confirmation | Same business day while the packet window is active. | Log dated acknowledgment in response SLA and communication control. | Send controlled receipt reminder and keep offer posture contained. |
| Commercial review confirmation | Inside the active review window. | Confirm buyer is reviewing the packet, specification, and commercial terms. | Keep forecast high-confidence only and refresh response tracking. |
| Offer approval or rejection | Before pricing, release, or forecast confidence improves. | Route approval, rejection, or revision request into pricing and response controls. | Revalidate offer before any renewed or widened language leaves. |
| Payment structure or deposit proof | Before release confidence, supplier allocation, or shipment movement widens. | Record proof in credit release and trust posture controls. | Block release language and founder confidence improvement. |
| Silence or delayed decision | Treated as a control event, not passive waiting. | Escalate through response board and refresh pricing or matter control if validity weakens. | Freeze widened confidence until founder review resets the answer. |

## Pricing, Forecast, and Release Boundary

| Boundary Area | Communication Standard | Required Proof Before Confidence Widens | Evidence Route |
| --- | --- | --- | --- |
| Pricing validity | State validity and response requirement without overcommitting price permanence. | Pricing review confirms concession, guardrail, expiry, and margin logic. | `06_dashboard/12_pricing-governance/Pricing-Governance-Board.md` |
| Revenue forecast | Describe the deal as high-confidence only until buyer decision, payment proof, and release controls align. | Forecast board confirms conversion quality. | `06_dashboard/23_revenue-forecast/Revenue-Forecast-and-Commitments-Review.md` |
| Credit and payment | Treat deposit proof or payment structure as a release-confidence input. | Credit release control confirms proof quality. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` |
| Trust posture | Keep language respectful, precise, and proof-led. | Trust posture confirms cleaner response behavior. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/TPST-2026-Q2_AtlanticFoods-Trust-Posture/README.md` |
| Release movement | Reference movement only when executable-check, release, funding, scenario, and risk records match. | Live gate proof is current and retrievable. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |

## Movement-Language Guardrails

| Movement Topic | Allowed Communication | Blocked Communication | Required Control Route |
| --- | --- | --- | --- |
| Supplier allocation | The offer is under commercial review and supplier allocation is not final until controls support it. | No reserved inventory, final allocation, or sourcing commitment language. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` |
| Shipment release | Shipment movement remains subject to release gate, funding review, and executable-check proof. | No shipment release, acceleration, clearance, or broker-handoff implication from customer packet alone. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` |
| Payment clearance | Payment terms and proof are required inputs to release confidence. | No payment cleared, waived, or sufficient-for-release implication without evidence. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` |
| Contained movement | The next safe movement must be named by executable-check and scenario controls. | No implied founder exception, untracked override, or informal movement promise. | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` |
| Risk consequence | Any divergent movement language becomes same-day founder escalation. | No customer-facing workaround language while risk answer is unresolved. | `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` |

## Escalation Routing

| Trigger | Immediate Control Action | Escalation Surface | Founder Consequence |
| --- | --- | --- | --- |
| Message sent without complete register details | Reconstruct send timestamp, owner, action request, deadline, and evidence destination. | Communication control board. | Founder review remains provisional until log is complete. |
| Response deadline missed | Send controlled reminder and flag stale response risk. | Response SLA and response escalation board. | Pricing, release, and forecast confidence stay contained. |
| Buyer requests revised terms | Pause outbound revision and reopen pricing review. | Pricing governance and formal offer packet. | Founder concession review stays active. |
| Buyer pushes for release or movement | Remove movement language and route to executable-check proof. | Executable-check, scenario response, and risk register. | No broker handoff, shipment release, payment clearance, or supplier allocation widening. |
| Trust or payment proof weakens | Refresh credit, trust, and matter-control records. | Customer room, credit release, and matter control. | Release confidence remains controlled. |

## Owner Handoff and Evidence Log

| Evidence Item | Owner | Required Destination | Control Purpose |
| --- | --- | --- | --- |
| Formal packet send record | Sales desk | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMCTRL-2026-Q2_AtlanticFoods-Communication-Control/README.md` | Starts the response clock and confirms what left UNYRA. |
| Approved message copy | Commercial owner | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMSTYLE-2026-Q2_AtlanticFoods-Institutional-Language-Reference/README.md` | Keeps tone, wording, and movement boundaries governed. |
| Receipt and review proof | Commercial owner | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` | Anchors response timing and prevents passive waiting. |
| Pricing or revision outcome | Founder office and commercial owner | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/PRICE-2026-001_AtlanticFoods-Garlic-Pricing-Review/README.md` | Protects concession, validity, margin, and forecast quality. |
| Payment proof or release confidence input | Finance and commercial owner | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` | Keeps release confidence tied to dated proof. |
| Escalation decision | Founder office | `06_dashboard/37_response-escalation/Counterparty-Response-SLA-and-Escalation-Board.md` | Converts silence, drift, or pressure into visible control action. |

## Founder Review Gate

| Gate Question | Required Answer Before Communication Widens | If Answer Is Weak | Owner |
| --- | --- | --- | --- |
| Is the outgoing message fully logged? | Send time, sender, message type, action request, deadline, movement boundary, and evidence destination are recorded. | Hold confidence improvement and complete the register. | Sales desk and commercial owner |
| Does the wording match approved language? | Subject, opening, action request, deadline, and escalation language match the language reference. | Rewrite before sending. | Commercial owner |
| Does response timing support pricing validity? | Receipt, review, decision, and revision status support active proforma logic. | Revalidate pricing first. | Founder office and commercial owner |
| Does customer proof support release confidence? | Trust posture, deposit proof, credit release, and payment structure are current. | Keep release and movement language blocked. | Finance and commercial owner |
| Does movement language stay within live gate proof? | Executable-check, release gate, funding, scenario, and risk records all match. | Escalate same day and remove movement language. | Founder office |

## End-of-Cycle Closeout

| Closeout Field | Current Answer | Evidence Route |
| --- | --- | --- |
| Communication status | Live control set now governs message logging, approved wording, response deadlines, pricing validity, proof handoff, escalation, and movement boundaries. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMCTRL-2026-Q2_AtlanticFoods-Communication-Control/README.md` |
| Packet status | Formal offer remains contained to commercial and specification review until buyer response, pricing, payment, and release proof align. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md` |
| Response status | Response timing and stale-response consequences remain governed by SLA and escalation board. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` |
| Language status | Institutional wording remains controlled and contained. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMSTYLE-2026-Q2_AtlanticFoods-Institutional-Language-Reference/README.md` |
| Movement status | Customer communication does not widen supplier allocation, shipment release, broker handoff, payment clearance, or revenue commitment without live gate proof. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |
