# Matter Control

| Matter Control | Current Standard |
| --- | --- |
| Matter Control ID | `MCTRL-2026-001` |
| Matter | Atlantic Foods garlic launch |
| Scope | Commercial, shipment, compliance, collections, pricing, credit, funding, release, executable-check, scenario, and archive-proof linkage. |
| Status | Founder visibility active |
| Purpose | Govern the strategic live transaction across CRM, operations, compliance, finance, and leadership so no stage, cargo, funding, or outbound commitment widens unless the same control answer is current everywhere. |
| Source rule | Update founder decision, trust posture, exception review, pricing, formal offer, credit, collections, funding, pre-shipment release, supplier packet, document control, executable-check, scenario, risk, shipment review, closeout, and archive records first, then refresh this matter-control module. |
| Decision rule | Treat this folder as the compact source-of-truth for whether the matter is controlled, executable, contained, blocked, or ready to close. |

## Matter Profile

| Field | Current Reading |
| --- | --- |
| Customer | Atlantic Foods Distribution |
| Supplier | Golden Harvest Produce |
| Product | Fresh Garlic |
| Live stage | Pre-release launch control with offer review and shipment-linked execution watch. |
| Trust override sync status | Founder decision, trust matrix, exception review, and release controls are strategically aligned. |
| Executable-check posture | `EXECCHK-2026-001` is active and required before live movement widens. |
| Live-gate containment posture | `SCEN-2026-005` and `RISK-2026-008` define the contained-movement answer that must match `EXECCHK-2026-001`, `FUND-2026-001`, and `REL-2026-001` before widening resumes. |
| Highest current risk | Founder-approved growth logic could be mistaken for blanket execution comfort if proof, cutoff, funding, packet, and release records diverge. |

## Source Refresh Stack

| Source Layer | Evidence Route | Founder Control Purpose |
| --- | --- | --- |
| Active deal room | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/README.md` | Keeps the live deal narrative tied to control before commitment. |
| Active matter control board | `06_dashboard/10_matter-control/Active-Matter-Control-Board.md` | Shows how this matter sits inside the broader cross-functional matter portfolio. |
| Founder decision register | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/DEC-2026-001_AtlanticFoods-Founder-Decisions/README.md` and `06_dashboard/13_founder-decisions/Executive-Decision-Board.md` | Confirms override class, blocked actions, recheck trigger, and return-to-standard proof. |
| Exception review | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXC-2026-Q2_AtlanticFoods-Exception-Review/README.md` and `06_dashboard/32_exception-governance/Executive-Exceptions-and-Override-Review.md` | Keeps pricing, release, claims, and CAPA deviations visible as one exception cluster. |
| Trust posture | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/TPST-2026-Q2_AtlanticFoods-Trust-Posture/README.md` and `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` | Converts fragile trust into explicit release, growth, and recheck consequences. |
| Customer room and credit control | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/README.md` and `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` | Keeps trust, release, collections, cash, concentration, and credit posture synchronized. |
| Pricing and offer controls | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/PRICE-2026-001_AtlanticFoods-Garlic-Pricing-Review/README.md`, `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md`, and `06_dashboard/12_pricing-governance/Pricing-Governance-Board.md` | Keeps concession logic, proforma validity, response duties, and contained movement language aligned. |
| Response and communication controls | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` and `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMCTRL-2026-Q2_AtlanticFoods-Communication-Control/README.md` | Governs acknowledgment timing, silence escalation, and outbound language before confidence changes. |
| Shipment, funding, and packet controls | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/README.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md`, and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` | Prevents payment, supplier settlement, broker handoff, or shipment movement from outrunning current gate proof. |
| Evidence and closeout records | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md`, and `07_archive/03_crm/DEAL-2026-001_AtlanticFoods_Garlic-CLOSED/README.md` | Makes the live gate closure story recoverable after movement, review, closeout, and archive. |
| Executable-check and containment layers | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXECCHK-2026-001_AtlanticFoods-Override-Closure/README.md`, `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md`, `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md`, and `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Carries owner path, cutoff, evidence state, stop rule, next safe movement, and same-day escalation consequence. |

## Override Alignment

| Alignment Requirement | Current Answer | Proof Standard | Evidence Route |
| --- | --- | --- | --- |
| Override class | Fragile-trust growth override under controlled gates. | Founder decision, trust posture, exception review, and matter control all name the same class. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/DEC-2026-001_AtlanticFoods-Founder-Decisions/README.md` and `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` |
| Blocked actions | No widened payment, broker handoff, shipment acceleration, supplier final allocation, or blanket execution comfort unless live proof matches. | Blocked actions remain visible in founder, executable-check, funding, release, and communication records. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` |
| Recheck timing | Same-day revalidation before movement, payment, or outward language widens. | Any movement-day change reopens executable-check, scenario, risk, funding, and release records. | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` |
| Return-to-standard trigger | Two clean response cycles, dated acknowledgment, deposit proof, aligned funding and release gate, and recoverable closure evidence. | Matter does not return to standard rules until trust, credit, funding, release, and archive proof all support it. | `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/TPST-2026-Q2_AtlanticFoods-Trust-Posture/README.md` and `02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/README.md` |

## Containment Alignment

| Containment Requirement | Current Answer | Stop Rule or Next Safe Movement | Evidence Route | Owner |
| --- | --- | --- | --- | --- |
| Current stop rule | Hold widened payment and shipment movement until executable-check, funding, and pre-shipment records restate the same same-day answer. | No widened supplier settlement, broker handoff, shipment acceleration, or payment movement without matched proof. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Founder office with finance and operations owners |
| Next safe movement | Resume only the narrow movement explicitly allowed by the refreshed executable-check board and live gate. | Narrow movement must be supported by `FUND-2026-001`, `REL-2026-001`, packet proof, and response proof. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` | Finance and operations owners |
| Scenario response consequence | Freeze widening immediately if a trust-linked payment or release needs movement without current executable-check ownership. | Route through matter control, executable-check board, owner accountability, and scenario response before retry. | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` | Founder office |
| Executive risk consequence | Divergent gate, payment, packet, or release wording becomes same-day founder escalation. | Do not treat founder override confidence as executable movement permission. | `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Founder office |
| Same-day revalidation owner | Founder office with finance and operations owners. | One current answer must be visible before any movement or payment widens. | `06_dashboard/13_founder-decisions/Executive-Decision-Board.md` and `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Founder office |

## Live Gate Control Map

| Gate or Record | Current Reading | What It Allows | What It Still Blocks | Evidence Route |
| --- | --- | --- | --- | --- |
| `COMM-2026-001` formal offer packet | Contained commercial review only. | Customer can review offer, proforma, specification, validity, and response duties. | Supplier final allocation, shipment release, payment clearance, and broader movement implication. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md` |
| `COMM-2026-002` supplier release packet | Contained correction and confirmation only. | Supplier can confirm receipt, document review, and execution against narrow released instructions. | Full shipment release, unrestricted broker handoff, and unrestricted payment movement. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` |
| `REL-2026-001` pre-shipment release | Released for broker handoff with live-gate discipline. | Narrow broker handoff to the extent current release proof supports it. | Any widening not restated in executable-check, funding, and containment layers. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` |
| `FUND-2026-001` funding release | Supplier payment remains controlled and synchronized with gate proof. | Controlled supplier settlement only inside approved funding posture. | Payment acceleration based on urgency, supplier pressure, or packet polish alone. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` |
| `DOCCTRL-2026-001` document control | Broker packet released under controlled issue. | Versioned packet proof and document spine for live gate and later challenge. | Archive readiness without final proof linkage. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |

## Proof and Archive Readiness

| Proof Area | Current State | Required Closure Evidence | Evidence Route | Archive Readiness |
| --- | --- | --- | --- | --- |
| Executable-check proof | Active tight watch. | Owner path, cutoff, gate status, evidence state, blocked movement, and containment answer are current. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXECCHK-2026-001_AtlanticFoods-Override-Closure/README.md` | Not ready until same-day closure proof is linked. |
| Packet proof | Customer and supplier packets are controlled and route-backed. | Formal offer response, supplier acknowledgment, document review, and movement wording are retrievable. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMCTRL-2026-Q2_AtlanticFoods-Communication-Control/README.md` and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` | Conditional. |
| Funding and release proof | Funding and pre-shipment release records are current but same-day alignment still matters. | `FUND-2026-001`, `REL-2026-001`, executable-check, scenario, and risk records carry the same answer. | `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` and `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Not ready if any layer diverges. |
| Shipment review proof | Shipment review is available for post-move evidence and lessons. | Movement, service quality, document quality, supplier performance, and follow-up actions are captured. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` | Ready only after final gate story is retrievable. |
| Archive proof | Archive path exists but should not be treated as final until closure proof is complete. | Closeout retains task, document control, release, funding, and executable-check proof. | `07_archive/03_crm/DEAL-2026-001_AtlanticFoods_Garlic-CLOSED/README.md` | Not final. |

## Founder Review Gates

| Gate Question | Required Answer Before Matter Widening | If Answer Is Weak | Primary Evidence Route | Owner |
| --- | --- | --- | --- | --- |
| Is the matter strategically aligned? | Founder decision, exception review, trust posture, and matter control all carry the same override class and blocked actions. | Hold stage widening and refresh founder decision logic. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/DEC-2026-001_AtlanticFoods-Founder-Decisions/README.md` | Founder office |
| Is the matter executable? | `EXECCHK-2026-001`, `TASK-2026-001`, `FUND-2026-001`, and `REL-2026-001` show owner, cutoff, evidence, and gate status. | Freeze movement and route through executable-check control board. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Founder office with finance and operations owners |
| Is the matter contained? | `SCEN-2026-005` and `RISK-2026-008` match the live gate stop rule and next safe movement. | Treat divergence as same-day founder escalation. | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` and `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Founder office |
| Is outward communication bounded? | Customer and supplier packets confirm only commercial review, correction, confirmation, or narrow movement allowed by the live gate. | Block broader wording until communication controls are refreshed. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md` and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` | Commercial and operations owners |
| Is proof ready for closeout? | Document control, shipment review, closeout, and archive paths can prove what happened without reconstructing it from memory. | Keep archive finality blocked and require proof linkage. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` and `07_archive/03_crm/DEAL-2026-001_AtlanticFoods_Garlic-CLOSED/README.md` | Operations control |

## End-of-Cycle Closeout

| Closeout Field | Current Answer | Evidence Route |
| --- | --- | --- |
| Matter status | Founder visibility active with strategic alignment in place and live-gate proof still under same-day discipline. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control/README.md` |
| Override status | Fragile-trust growth override remains bounded; approval does not equal blanket execution permission. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/DEC-2026-001_AtlanticFoods-Founder-Decisions/README.md` and `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` |
| Containment status | Active containment remains in force until executable-check, funding, pre-shipment release, scenario, and risk records match. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md`, `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md`, and `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` |
| Movement posture | No widened payment, broker handoff, shipment acceleration, supplier final allocation, or payment clearance should be inferred without matched proof. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` |
| Records updated | Matter control now carries route-backed override alignment, containment alignment, live-gate map, proof readiness, founder gates, and closeout logic. | `06_dashboard/10_matter-control/Active-Matter-Control-Board.md` |
