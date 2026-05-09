# Daily Shipment Control Tower

| Dashboard Control | Current Standard |
| --- | --- |
| Status | LIVE WORKING DASHBOARD |
| Purpose | Operating control sheet for daily shipment execution, trust-linked release watch, executable gate closure, contained-movement discipline, document readiness, filing discipline, and escalation management. |
| Source rule | Update shipment folders, logistics source records, compliance filings, pre-shipment release reviews, funding release reviews, executable-check control board, executive scenario and contingency review, executive risk register, credit-release controls, strategic trust reviews, trust posture matrix, supplier capacity reviews, and linked task records first, then refresh this dashboard. |
| Gate rule | Use a pre-shipment release review for any shipment approaching broker handoff, forwarder release, or ETD-ready status, and do not clear the shipment while material customer or supplier trust-linked release consequences remain unresolved. |
| Closeout rule | Use a shipment review log for any shipment that has materially completed arrival or delivery. |

## Control Header

| Field | Current Answer |
| --- | --- |
| Date | 2026-05-02 |
| Prepared for | Founder Review |
| Prepared by | UNYRA Leadership Office |
| Operating cycle | May 2026 live shipment execution and release-control cycle |
| Focus route | SHIP-2026-001 China to USA garlic shipment, Qingdao to Orlando via Port Newark |
| Highest risk | Broker handoff, supplier payment, or packet language could widen faster than executable-check proof and contained-movement revalidation. |
| Current shipment posture | Docs filed; pre-shipment release is cleared for broker handoff under controlled conditions, but widened movement stays gated by matched funding, packet, and closure proof. |
| Owner | Operations owner with finance, compliance, sourcing, and founder office support |

## Source Refresh Stack

| Source Layer | Evidence Route | Founder Control Purpose |
| --- | --- | --- |
| Daily operations command center | `06_dashboard/03_operations/Daily-Operations-Command-Center.md` | Confirms the operating posture before the shipment tower updates movement, payment, or packet confidence. |
| Live shipment room | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/README.md` | Holds the founder-level shipment narrative for release-before-movement, funding synchronization, packet proof, and contained movement. |
| Pre-shipment release gate | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` | Confirms broker handoff, forwarder release, or ETD-ready clearance before movement is treated as authorized. |
| Funding release record | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` and `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` | Keeps supplier settlement, freight, broker, clearance, and trust-linked cash discipline aligned before payment moves. |
| Document control packet | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` | Governs PO, CI, PL, SI, ISF intake, traceability, and linked compliance references. |
| Supplier release packet | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` | Controls supplier-facing release instructions, receipt, document review, and execution confirmation. |
| Shipment review log | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` | Preserves post-move proof, operational learning, and closeout readiness. |
| Executable-check board | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Confirms owner, cutoff, live gate, evidence state, containment answer, and archive readiness before movement widens. |
| Founder execution queue | `02_crm/05_tasks/TASK-2026-001_Founder-Execution-Queue/README.md` | Keeps the live deposit, funding, and release task tied to owner follow-through until the gate is truly closed. |
| Scenario and risk controls | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` and `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Carries same-day stop rules, next safe movement, and escalation consequences. |
| Traceability proof room | `04_compliance/04_traceability/TRACE-2026-001_GoldenHarvest-Garlic-LotPath/README.md` | Keeps lot-path retrieval proof and the open evidence gap visible before compliance confidence widens. |
| Trust posture matrix | `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` | Converts fragile customer trust and controlled supplier trust into release, payment, and sourcing consequences. |

## KPI Snapshot

| KPI | Current Result | Founder Note |
| --- | --- | --- |
| Active shipments | 1 | SHIP-2026-001 is the live China to USA shipment under release, funding, packet, and containment watch. |
| Shipments with document gaps or controlled issue | 1 | DOCCTRL-2026-001 is broker-packet released under controlled issue, so packet proof remains active. |
| Filing readiness watches this week | 1 | ISF intake and compliance references sit inside the packet scope; no broader clearance confidence should be inferred without source refresh. |
| Shipments under trust-linked release watch | 1 | Atlantic Foods fragile posture and Golden Harvest controlled posture both affect movement confidence. |
| Executable checks still open | 2 | EXECCHK-2026-001 remains active tight watch; EXECCHK-2026-002 is closing with proof. |
| Containment-mode shipments | 1 | SHIP-2026-001 stays in containment-mode watch until release, funding, scenario, risk, and executable-check records match. |
| Blocked or caution-status shipments | 1 | The shipment is not fully blocked, but widened movement remains held behind same-day proof and aligned gate answers. |

## Milestone Watch

| Shipment ID | Route | Current Milestone | ETD | ETA | Next Action | Owner | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SHIP-2026-001 | Qingdao to Orlando via Port Newark | Docs filed; released for broker handoff under controlled issue | Not stated in inspected source records | Not stated in inspected source records | Reconfirm release gate, funding answer, packet proof, and supplier execution confirmation before movement widens. | Operations owner | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/README.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md`, and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |
| SHIP-2026-001 closeout path | China to USA shipment review | Review-ready once movement occurs or the gate answer changes | Not applicable | Not applicable | Keep shipment review log ready for proof retention, lessons, and closeout. | Operations control | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` |

## Document Readiness

| Shipment ID | PO | Commercial Invoice | Packing List | Shipping Instructions | Status | Gap | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SHIP-2026-001 | In packet scope | In packet scope | In packet scope | In packet scope | Broker packet released under controlled issue | Final release proof must stay linked across document control, release gate, funding gate, shipment review, and closeout path. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |
| SHIP-2026-001 supplier release packet | Purchase order included in packet | Packet coordination dependent | Packet coordination dependent | Shipping instructions included in packet | Controlled communication set | Supplier receipt, document review, and execution confirmation must not outrun release and funding proof. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` |

## Funding Release and Payment Control

| Shipment ID | Supplier Payment | Freight or Broker Funding | Clearance Funding | Executable Check Task | Status | Gap | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SHIP-2026-001 | USD 62,000 supplier balance under controlled release | USD 28,000 ocean freight and origin handling cleared | USD 17,000 customs broker and clearance funding planned | TASK-2026-001 / EXECCHK-2026-001 | Controlled with one shipment-linked payment path still needing tighter basis | Payment movement must not outrun deposit, packet integrity, trust posture, release approval, and executable-check closure. | `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` |
| Conditional Rio Verde path | USD 32,000 conditional supplier-slot deposit pressure | Not applicable | Not applicable | Not approved as live movement | On hold | Weighted upside should not consume shipment-linked cash discipline before demand and allocation proof improve. | `06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.md` and `06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.md` |

## Compliance and Filing Control

| Shipment ID | ISF | Prior Notice | FSVP | Broker Status | Blocking Risk | Owner | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SHIP-2026-001 | Included in DOCCTRL-2026-001 packet scope as ISF intake | Compliance reference not separately closed in inspected shipment source | Compliance reference not separately closed in inspected shipment source | Broker packet released under controlled issue | Filing confidence should not widen beyond packet proof, traceability proof, and release gate alignment. | Operations and compliance owners | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` and `04_compliance/04_traceability/TRACE-2026-001_GoldenHarvest-Garlic-LotPath/README.md` |
| TRACE-2026-001 | Not a filing, but supports challenge defense | Not a filing, but supports challenge defense | Not a filing, but supports challenge defense | Not applicable | Retrieval drill is complete with one open evidence gap, so compliance confidence should stay bounded. | Founder compliance review | `04_compliance/04_traceability/TRACE-2026-001_GoldenHarvest-Garlic-LotPath/README.md` |

## Trust-Linked Release Watch

| Shipment ID | Customer Trust Tier | Supplier Trust Tier | Release Consequence | Executable Check Status | Next Trigger | Owner | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SHIP-2026-001 | Atlantic Foods fragile | Golden Harvest controlled | No accelerated movement or payment widening without dated response, deposit proof, supplier confirmation, and matched gate answers. | EXECCHK-2026-001 active tight watch | Customer acknowledgment, payment structure, supplier confirmation, or packet proof drifts. | Founder office with finance and operations owners | `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md`, `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md`, and `06_dashboard/37_response-escalation/Counterparty-Response-SLA-and-Escalation-Board.md` |
| SHIP-2026-001 supplier side | Not applicable | Golden Harvest controlled | Release only against earlier supplier confirmation and packet completion; maintain backup-source discipline. | Tied to release and funding gates | Supplier confirms too close to release window again. | Sourcing and operations owners | `02_crm/03_suppliers/SUP-2026-001_GoldenHarvest-Produce/README.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md`, and `06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.md` |

## Containment and Safe Movement Watch

| Shipment ID | Scenario and Risk Reference | Current Stop Rule | Next Safe Movement | Same-Day Revalidation Owner | Status | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- |
| SHIP-2026-001 | SCEN-2026-005, RISK-2026-008, and EXECCHK-2026-001 | Hold any widened supplier settlement pace, broker handoff funding, or shipment acceleration until executable-check, funding, and pre-shipment records restate the same answer. | Resume only the narrow movement explicitly reconfirmed by executable-check board, funding review, pre-shipment gate, and shipment room. | Founder office with finance and operations owners | Active containment | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md`, `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md`, and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` |
| SHIP-2026-001 supplier coordination | Golden Harvest release-timing and trust watch | Do not treat packet completeness as supplier release permission if release, funding, or containment proof diverges. | Confirm only the narrow supplier action currently supported by live controls. | Operations owner | Controlled confirmation | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` |

## Exception and Escalation Log

| Shipment ID | Exception | Impact | Escalation Trigger | Decision Owner | Evidence Route |
| --- | --- | --- | --- | --- | --- |
| SHIP-2026-001 | Broker packet released under controlled issue | Packet can look complete while final movement proof still needs synchronization. | Packet completeness is used as substitute for movement authorization. | Operations owner | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |
| SHIP-2026-001 | Funding and release answer must match same-day | Supplier payment, broker handoff, or shipment acceleration can outrun live gate truth. | Funding, release, executable-check, scenario, or risk record carries a different stop rule or next safe movement. | Founder office with finance and operations owners | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |
| SHIP-2026-001 | Traceability proof has one open evidence gap | Compliance challenge defense and claim recovery confidence should stay bounded. | Traceability or complaint consequence is treated as closed before evidence gap is resolved. | Founder compliance review | `04_compliance/04_traceability/TRACE-2026-001_GoldenHarvest-Garlic-LotPath/README.md` |
| SHIP-2026-001 | Supplier confirmation may compress release timing | Late confirmation can create rushed payment, broker, and document decisions. | Golden Harvest confirmation or document review arrives too close to movement gate. | Operations and sourcing owners | `06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.md` |

## Next 24-Hour Action Queue

| Action | Shipment ID | Why It Matters | Owner | Deadline | Status | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- |
| Keep release, funding, executable-check, scenario, risk, and shipment room answers identical before movement widens. | SHIP-2026-001 | Same-day pressure should not create conflicting shipment truth. | Founder office with finance and operations owners | 2026-05-03 | In progress | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md`, and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` |
| Lock broker and clearance funding to filing-ready status. | SHIP-2026-001 | Avoid paying for movement that is not actually ready to clear. | Operations and compliance owners | 2026-05-03 | Planned | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` and `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` |
| Confirm Golden Harvest supplier execution readiness before release compression occurs. | SHIP-2026-001 | Supplier timing should not force late operating decisions. | Operations desk | 2026-05-04 | In progress | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` |
| Link final release proof into document register, shipment review, and closeout path. | SHIP-2026-001 | The system should be able to prove how the gate closed later without reconstructing the story. | Operations control | 2026-05-03 | In progress | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` |
| Keep traceability gap visible until proof chain is founder-safe. | SHIP-2026-001 | Filing and claim confidence should not outrun retrieval proof. | Compliance owner | 2026-05-03 | Active watch | `04_compliance/04_traceability/TRACE-2026-001_GoldenHarvest-Garlic-LotPath/README.md` |

## Shipment Quality Gates

| Gate Question | Required Answer Before Status Improves | Primary Evidence Route | Owner |
| --- | --- | --- | --- |
| Is movement authorized by live release proof, not document appearance? | REL-2026-001, the shipment room, and executable-check board must carry the same answer. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` | Operations owner |
| Is outgoing cash synchronized with release and packet proof? | FUND-2026-001 and the funding review must match the live gate before payment widens. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` | Finance owner |
| Is filing and traceability confidence bounded correctly? | DOCCTRL-2026-001 and TRACE-2026-001 must support the same challenge-defense posture. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` and `04_compliance/04_traceability/TRACE-2026-001_GoldenHarvest-Garlic-LotPath/README.md` | Compliance owner |
| Is supplier confirmation early enough to avoid compressed release decisions? | Supplier release packet and capacity watch should confirm timing before the movement gate tightens. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` | Operations and sourcing owners |
| Is closeout proof ready before the shipment leaves active watch? | Shipment review log must preserve proof, lessons, and gate closure after movement occurs. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` | Operations control |

## End-of-Cycle Closeout

| Closeout Field | Current Answer | Evidence Route |
| --- | --- | --- |
| Shipments stabilized | SHIP-2026-001 is controlled, not fully stabilized; widened movement remains tied to matched release, funding, executable-check, and containment proof. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/README.md` |
| Open blockers carried forward | Packet controlled issue, traceability evidence gap, supplier confirmation timing, payment basis, and executable-check closure remain active watch items. | `06_dashboard/03_operations/Daily-Operations-Command-Center.md` |
| Records updated | Shipment tower now carries route-backed milestone, document, funding, compliance, trust, containment, escalation, and closeout logic. | `06_dashboard/05_shipments/Daily-Shipment-Control-Tower.md` |
| Escalations triggered | Same-day escalation remains active if release, funding, executable-check, scenario, risk, traceability, or supplier-confirmation answers diverge. | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` |
| Next refresh focus | Update REL-2026-001, FUND-2026-001, DOCCTRL-2026-001, COMM-2026-002, TRACE-2026-001, and SREV-2026-001 before status improves. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` |
