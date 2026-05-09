# Counterparty Response SLA and Escalation Board

| Dashboard Control | Current Standard |
| --- | --- |
| Status | LIVE WORKING DASHBOARD |
| Purpose | Founder and management control board for counterparty response windows, overdue communication, escalation discipline, controlled reminder cadence, and containment-aligned revalidation timing. |
| Source rule | Update the communication control board, live communication records, message frameworks, executable-check control board, executive scenario and contingency review, executive risk register, and linked functional control records first, then refresh this board. |
| Decision rule | If delay from a customer or supplier could affect pricing validity, shipment release, cash timing, compliance posture, claim recovery, or contained movement, escalate through a controlled sequence rather than ad hoc follow-up. |

## Board Header

| Field | Current Answer |
| --- | --- |
| Date | 2026-05-02 |
| Cycle | Weekly founder posture refresh |
| Owner | Founder office with commercial, operations, and compliance owners |
| Main counterparty risk | Atlantic Foods acknowledgment and deposit-response timing can still change pricing validity, release confidence, and contained-movement posture. |
| Main overdue matter | No confirmed overdue closure label; the active risk is response freshness before movement, release, or closeout language widens. |
| Escalation posture | Stage-2 watch applies immediately if any response gap affects pricing validity, release posture, supplier confirmation, claim recovery, or containment. |
| Hold or release posture | Hold widened movement until dated response and linked control revalidation are current. |
| Containment revalidation posture | EXECCHK-2026-001, SCEN-2026-005, RISK-2026-008, FUND-2026-001, and REL-2026-001 must match before any outward message implies broader movement. |

## Source Refresh Stack

| Source Layer | Evidence Route | Founder Control Purpose |
| --- | --- | --- |
| Communication control board | `06_dashboard/36_external-communications/Counterparty-Communication-Control-Board.md` | Confirms formal messages, packet release, response due dates, and outward wording discipline. |
| Strategic counterparty trust review | `06_dashboard/38_counterparty-trust/Strategic-Counterparty-Trust-and-Response-Review.md` | Converts response behavior into trust posture and escalation burden. |
| Trust posture matrix | `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` | Ties missed responses to release posture, account growth, supplier timing, and revalidation cadence. |
| Atlantic Foods communication control | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMCTRL-2026-Q2_AtlanticFoods-Communication-Control/README.md` | Holds customer-facing communication controls for offer, release posture, and contained-movement language. |
| Atlantic Foods response SLA | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` | Governs acknowledgment timing, reminder cadence, pricing validity, and release-confidence revalidation. |
| Atlantic Foods offer packet | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md` | Carries the formal packet that requires receipt, commercial review, and offer decision within the validity window. |
| Golden Harvest supplier release packet | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` | Carries supplier receipt, document review, and execution confirmation requirements. |
| Executable-check board | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Confirms whether delayed responses can affect owner, cutoff, evidence state, release consequence, and archive readiness. |
| Scenario and risk controls | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` and `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Keeps response delays connected to contained-movement stop rules and escalation consequences. |
| Claim, CAPA, and recovery records | `04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/README.md`, `04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/CAPA-2026-001_AtlanticFoods-Garlic-Containment-and-Prevention/README.md`, and `04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/RECOV-2026-001_AtlanticFoods-Claim-Recovery/README.md` | Prevents complaint calm or recovery language from outrunning containment proof. |

## KPI Snapshot

| KPI | Value | Notes |
| --- | --- | --- |
| Responses due today | 2 | Atlantic Foods commercial review and Golden Harvest release confirmation remain the active response-control paths. |
| Overdue confirmations | 0 labeled overdue | Current risk is freshness and revalidation before movement, not a closed overdue label. |
| Matters at escalation stage 2 or higher | 1 watch path | Atlantic Foods moves to stage-2 watch if acknowledgment or deposit-response timing slips again. |
| Revenue or shipment value exposed | Material live-gate exposure | Exposure is tied to Atlantic Foods release confidence, supplier confirmation timing, and contained movement. |
| Communications on hold pending response | 2 | Atlantic Foods outward movement language and Golden Harvest supplier release language should remain narrow until responses are current. |
| Communications requiring containment-aligned revalidation | 2 | Customer and supplier packets must stay aligned with EXECCHK-2026-001, SCEN-2026-005, RISK-2026-008, FUND-2026-001, and REL-2026-001. |

## Response Class Matrix

| Communication Class | Receipt Confirmation SLA | Full Response SLA | Current Risk Note | Evidence Route |
| --- | --- | --- | --- | --- |
| Formal offer packet | Same business day acknowledgment | Within offer-validity window before pricing or release confidence widens | Atlantic Foods acknowledgment and deposit-response timing still affect release confidence. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md` and `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` |
| Shipment release instruction | Same business day acknowledgment | Before shipment, broker handoff, or payment movement widens | Supplier confirmation must not arrive so late that packet and release proof compress. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` |
| Containment or movement-status notice | Same day | Same day before any widened movement restarts | Outward language may state only the narrow movement currently allowed by linked controls. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` and `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` |
| Document deficiency notice | Same business day acknowledgment | Before packet is treated as complete | Document control should remain evidence-led, not inbox-led. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |
| Collections reminder | Same business day acknowledgment | Before release confidence or payment promise is reused | Collections timing can change cash, release, and trust posture. | `06_dashboard/09_credit-risk/Credit-and-Release-Control-Board.md` and `06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.md` |
| Claims or remedy notice | Same business day acknowledgment | Before case closure or recovery posture is softened | Customer calm cannot replace CAPA and recovery proof. | `04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/README.md` and `06_dashboard/30_claims-recovery/Claims-Credits-and-Recovery-Review.md` |
| Compliance or legal notice | Same business day acknowledgment | Before compliance posture or liability language is finalized | Legal or compliance silence should escalate before closure language widens. | `06_dashboard/31_capa-governance/CAPA-and-Preventive-Action-Review.md` |

## Active Escalation Tracker

| Communication Ref | Counterparty | Linked Matter | Date Sent | SLA Due | Current Stage | Movement Posture | Next UNYRA Action | Evidence Route | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| COMM-2026-001 | Atlantic Foods Distribution | Atlantic Foods formal offer and release-confidence path | Active packet window | Same business day acknowledgment and validity-window decision | Stage-1 controlled follow-up; stage-2 if acknowledgment or deposit timing slips | Contained / commercial review only | Confirm receipt, commercial review, and offer decision without implying supplier allocation, shipment release, or payment clearance. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md` and `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` | Sales desk and commercial owner |
| COMM-2026-002 | Golden Harvest Produce | China to USA supplier release packet | Active packet window | Same business day acknowledgment and execution confirmation before release widening | Stage-1 controlled follow-up; escalate if confirmation compresses release window | Contained / correction and confirmation only | Confirm receipt, document review, and execution against released instructions while preserving narrow movement language. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` | Operations desk |
| COMP-2026-001 | Atlantic Foods Distribution | Atlantic Foods claim containment and recovery | Active complaint review | Same-cycle response before closure or recovery language widens | Watch path; escalate if CAPA proof or recovery response slips | Controlled complaint scenario | Reconfirm CAPA ownership, current evidence, and recovery consequence before treating the case as stable. | `04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/README.md`, `04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/CAPA-2026-001_AtlanticFoods-Garlic-Containment-and-Prevention/README.md`, and `04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/RECOV-2026-001_AtlanticFoods-Claim-Recovery/README.md` | Compliance owner |

## Reminder and Escalation Queue

| Priority | Counterparty | Why It Matters | Next Communication Step | Deadline | Evidence Route | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Atlantic Foods Distribution | Response timing can affect pricing validity, deposit confidence, release posture, and fragile trust tier. | Send controlled stage-1 reminder and move to stage-2 founder visibility if acknowledgment or deposit timing slips. | 2026-05-03 | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` and `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` | Commercial owner |
| 2 | Golden Harvest Produce | Supplier confirmation timing can compress packet discipline, release confidence, and backup-source posture. | Confirm document review and execution readiness earlier than the release window. | 2026-05-04 | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` and `06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.md` | Operations and sourcing owners |
| 3 | Atlantic Foods Distribution | Complaint calm should not become closure before CAPA and recovery proof are current. | Reconfirm containment proof, recovery consequence, and proof-trail sufficiency before closure language. | 2026-05-06 | `04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/CAPA-2026-001_AtlanticFoods-Garlic-Containment-and-Prevention/README.md` and `04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/RECOV-2026-001_AtlanticFoods-Claim-Recovery/README.md` | Compliance owner |

## Business Consequence Watch

| Linked Matter | Silence or Delay Risk | Commercial or Operational Consequence | Hold, Revalidate, or Escalate | Evidence Route |
| --- | --- | --- | --- | --- |
| Atlantic Foods formal offer and release-confidence path | Missing acknowledgment, delayed commercial review, or soft deposit response can make pricing and release confidence stale. | Founder could approve wider release or account growth from partial truth. | Hold acceleration, revalidate pricing and release posture, and escalate to founder visibility if timing slips. | `06_dashboard/12_pricing-governance/Pricing-Governance-Board.md`, `06_dashboard/09_credit-risk/Credit-and-Release-Control-Board.md`, and `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` |
| Golden Harvest supplier release packet | Supplier confirmation too close to release can compress document control and shipment proof. | Release or broker handoff can outrun packet discipline. | Revalidate release gate, require earlier confirmation, and keep backup-source watch active. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md`, and `06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.md` |
| Atlantic Foods claim containment and recovery | Customer or supplier response lag can make remedy and closure language stronger than proof. | Complaint can appear commercially stable before prevention or recovery proof is real. | Hold closure language, refresh CAPA and recovery records, and escalate if containment proof weakens. | `06_dashboard/31_capa-governance/CAPA-and-Preventive-Action-Review.md` and `06_dashboard/30_claims-recovery/Claims-Credits-and-Recovery-Review.md` |

## Containment Revalidation Watch

| Communication Ref | Linked Matter | Scenario and Risk Reference | Trigger for Revalidation | Next Allowed UNYRA Message Step | Evidence Route | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| COMM-2026-001 | Atlantic Foods formal offer and release-confidence path | SCEN-2026-005 and RISK-2026-008 | Any customer response gap, deposit timing shift, or request that implies broader release, supplier allocation, or payment clearance. | Confirm receipt, commercial review, and deadline only; do not imply movement beyond the current contained answer. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/README.md`, `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md`, and `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Founder office with commercial owner |
| COMM-2026-002 | China to USA active shipment | SCEN-2026-005 and RISK-2026-008 | Any supplier confirmation gap, document revision, or release instruction that would widen shipment, broker handoff, or payment movement. | Confirm the narrow next movement step only after REL-2026-001 and FUND-2026-001 match the executable-check answer. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md`, `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md`, and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` | Operations owner |

## Management Notes

| Note | Founder Reading | Evidence Route |
| --- | --- | --- |
| Response discipline is now a trust signal | Atlantic Foods should remain fragile until acknowledgment and deposit timing are clean enough for two response cycles. | `06_dashboard/38_counterparty-trust/Strategic-Counterparty-Trust-and-Response-Review.md` |
| Supplier timing is a release-control issue | Golden Harvest can remain controlled, but confirmation timing must move earlier to reduce release compression. | `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` |
| Containment language must stay synchronized | Outward wording should never imply broader movement than EXECCHK-2026-001, SCEN-2026-005, RISK-2026-008, FUND-2026-001, and REL-2026-001 currently allow. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |

## End-of-Cycle Closeout

| Closeout Field | Current Answer | Evidence Route |
| --- | --- | --- |
| Overdue matters closed | No overdue matter is labeled closed this cycle; active response-control paths remain under watch. | `06_dashboard/37_response-escalation/Counterparty-Response-SLA-and-Escalation-Board.md` |
| New escalations opened | Stage-2 readiness remains active for Atlantic Foods if acknowledgment or deposit-response timing slips again. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/README.md` |
| Holds or revalidations triggered | Widened customer and supplier movement language stays held behind containment-aligned revalidation. | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` and `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |
| Standards reinforced | Counterparty response is now treated as pricing, release, cash, compliance, claim, and containment control evidence. | `06_dashboard/36_external-communications/Counterparty-Communication-Control-Board.md`, `06_dashboard/38_counterparty-trust/Strategic-Counterparty-Trust-and-Response-Review.md`, and `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` |
