# Daily Operations Command Center

| Dashboard Control | Current Standard |
| --- | --- |
| Status | LIVE WORKING DASHBOARD |
| Purpose | Daily operations control sheet for purchasing release, logistics coordination, document packets, executable-check closure, contained-movement discipline, working-file control, and escalation management. |
| Source rule | Update purchasing, logistics, shipment, funding release, pre-shipment release reviews, executable-check control board, executive scenario and contingency review, executive risk register, linked task records, and working-file source records first, then refresh this dashboard. |
| Decision rule | Do not treat packet completeness, supplier urgency, or commercial pressure as movement approval unless release, funding, executable-check, document, and containment records carry the same current answer. |

## Control Header

| Field | Current Answer |
| --- | --- |
| Date | 2026-05-02 |
| Prepared for | Founder Review |
| Prepared by | UNYRA Leadership Office |
| Operating cycle | May 2026 live execution and release-control cycle |
| Primary lane or program | China to USA garlic shipment linked to Atlantic Foods and Golden Harvest control posture |
| Highest operational risk | Shipment movement or supplier payment could widen faster than executable-check closure, packet proof, or contained-movement revalidation. |
| Current operating posture | Controlled with one active same-day closure watch and one containment-mode live gate. |
| Owner | Operations owner with finance, compliance, sourcing, and founder office support |

## Source Refresh Stack

| Source Layer | Evidence Route | Founder Control Purpose |
| --- | --- | --- |
| Live China to USA shipment room | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/README.md` | Holds the founder-level shipment narrative for release-before-movement, funding synchronization, packet proof, and contained movement. |
| Shipment control tower | `06_dashboard/05_shipments/Daily-Shipment-Control-Tower.md` | Carries daily shipment execution, document readiness, filing, trust-linked release watch, and next 24-hour movement posture. |
| Pre-shipment release gate | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` | Confirms whether broker handoff, forwarder release, or ETD-ready status is formally cleared. |
| Funding release record | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` and `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` | Keeps supplier settlement, freight, broker, clearance, and trust-linked cash discipline aligned before payment moves. |
| Document control packet | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` | Holds PO, CI, PL, SI, filing intake, traceability, and compliance packet proof. |
| Supplier release packet | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` | Controls supplier-facing release instructions, receipt, document review, and execution confirmation. |
| Shipment review log | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` | Preserves post-move evidence, learning capture, and closeout readiness. |
| Executable-check control board | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Confirms owner, cutoff, live gate, evidence state, containment answer, and archive readiness before movement widens. |
| Founder execution queue | `02_crm/05_tasks/TASK-2026-001_Founder-Execution-Queue/README.md` | Keeps the live deposit, funding, and release task tied to named owner follow-through until the gate is truly closed. |
| Scenario and risk controls | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` and `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Carries same-day stop rules, next safe movement, and escalation consequences. |
| Working files staging lane | `03_operations/05_working-files/README.md` | Prevents temporary support files from becoming hidden custody, unmanaged proof, or stale operating exceptions. |
| Supplier capacity review | `06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.md` | Keeps Golden Harvest capacity, backup sourcing, and supplier concentration visible before operations accelerates. |

## KPI Snapshot

| KPI | Current Result | Founder Note |
| --- | --- | --- |
| POs pending release | 1 controlled supplier release path | Golden Harvest supplier release instructions are active and must stay inside the live shipment gate answer. |
| Shipments in active coordination | 1 | SHIP-2026-001 is the live China to USA route under document, release, funding, and containment watch. |
| Document packets incomplete or under issue | 1 controlled issue | DOCCTRL-2026-001 is broker-packet released under controlled issue, so proof discipline remains active. |
| Payment releases pending control | 2 holds plus 1 shipment-linked watch | Funding review shows two conditional holds and one shipment-linked payment path needing tighter basis. |
| Executable checks still open | 2 | EXECCHK-2026-001 remains active tight watch; EXECCHK-2026-002 is closing with proof. |
| Containment-mode gates active | 1 | Atlantic Foods-linked outgoing shipment cash and movement still carry containment mode. |
| Critical blockers open | 3 | Executable-check closure, matched funding/release answer, and closeout-ready evidence remain the key blockers. |

## Purchasing Release Watch

| PO or Deal Reference | Supplier | Status | Release Gate | Executable Check Task | Due Date | Owner | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SHIP-2026-001 garlic supplier release | Golden Harvest Produce | Supplier release packet active under contained confirmation posture | REL-2026-001 released for broker handoff, but widening still depends on matched proof | TASK-2026-001 and EXECCHK-2026-001 | 2026-05-03 same-day closure watch | Operations owner with finance support | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md`, and `02_crm/05_tasks/TASK-2026-001_Founder-Execution-Queue/README.md` |
| Conditional Rio Verde supplier-slot path | Supplier reservation path | Conditional hold only | No full release until demand proof and allocation review clear | Not opened as live executable check | 2026-05-04 allocation recheck | Founder and sourcing owner | `06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.md` and `06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.md` |

## Logistics Coordination Queue

| Shipment ID | Route | Current Coordination Stage | Broker or Forwarder | Next Action | Owner | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- |
| SHIP-2026-001 | Qingdao to Orlando via Port Newark | Docs filed; released for broker handoff under controlled issue | Broker and forwarder path governed by release and document controls | Confirm release gate, funding answer, packet proof, and supplier confirmation still match before movement widens. | Operations owner | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/README.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md`, and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |
| SHIP-2026-001 closeout path | China to USA shipment review | Review-ready after movement or gate answer changes | Not applicable | Keep shipment review log ready for proof retention, lessons, and closeout once movement occurs or the gate changes. | Operations control | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` |

## Document Packet Control

| Linked Record | PO | CI | PL | SI | Status | Gap | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DOCCTRL-2026-001 garlic export packet | In packet scope | In packet scope | In packet scope | In packet scope | Broker packet released under controlled issue | Final release proof must stay linked across document control, release gate, funding gate, shipment review, and closeout path. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |
| COMM-2026-002 supplier release packet | Purchase order included in supplier packet | Packet coordination dependent | Packet coordination dependent | Shipping instructions included in supplier packet | Controlled communication set | Supplier execution confirmation must not outrun the release and funding answer. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` |

## Funding and Payables Watch

| Shipment or Deal | Payment Item | Amount | Release Basis | Executable Check Task | Owner | Status | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SHIP-2026-001 | Supplier balance for committed garlic program | USD 62,000 | Deposit, packet integrity, supplier trust posture, and release approval remain aligned | TASK-2026-001 / EXECCHK-2026-001 | Founder and operations owner | Controlled release | `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` |
| SHIP-2026-001 | Ocean freight and origin handling | USD 28,000 | Booking confirmation and packet control stay current | Operational funding control | Operations owner | Cleared | `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` |
| SHIP-2026-001 | Customs broker and clearance funding | USD 17,000 | Filing status, document lock, and release gate stay clean | Operational and compliance control | Operations and compliance owners | Planned | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` and `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` |
| Conditional Rio Verde path | Supplier slot deposit | USD 32,000 conditional deposit pressure | Buyer acceptance, backup-source posture, and trust-linked payment watch must be confirmed first | Not approved as live movement | Founder and sourcing owner | On hold | `06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.md` |

## Executable Check Watch

| Matter or Shipment | Live Gate | Linked Task | What Still Must Be Proved | Owner | Deadline | Status | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Atlantic Foods / SHIP-2026-001 | Funding release and pre-shipment release | TASK-2026-001 | Task, gate, packet, containment answer, shipment review, closeout, and archive proof must carry the same closure story. | Finance and operations owners | 2026-05-03 same-day cutoff | Active tight watch | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md`, and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` |
| Harbor Fresh launch proof | Shipment review and archive closeout | TASK-2026-004 reference in executable board | Retrieval package still needs final founder-office release note before reused as precedent. | Operations owner and founder office | 2026-05-01 archive cutoff | Closing with proof | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` and `02_crm/04_deals/won/DEAL-2026-003_HarborFresh_Garlic/README.md` |

## Contained Movement Watch

| Matter or Shipment | Scenario and Risk Reference | Current Stop Rule | Next Safe Movement | Same-Day Revalidation Owner | Status | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- |
| SHIP-2026-001 / Atlantic Foods-linked outgoing shipment cash | SCEN-2026-005, RISK-2026-008, and EXECCHK-2026-001 | Hold any widened supplier settlement pace, broker handoff funding, or shipment acceleration until executable-check, funding, and pre-shipment records restate the same answer. | Resume only the narrow movement explicitly reconfirmed by the executable-check board, funding review, and pre-shipment gate. | Founder office with finance and operations owners | Active containment | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md`, `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md`, and `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` |
| Golden Harvest supplier confirmation path | Supplier trust and release-timing watch | Do not treat packet completeness as supplier release permission if release, funding, or containment proof diverges. | Confirm only the narrow supplier action currently supported by live controls. | Operations owner | Controlled confirmation | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` and `06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.md` |

## Working Files Cleanup Watch

| Working File or Folder | Current Location | Required Final Placement | Age | Owner | Status | Evidence Route |
| --- | --- | --- | --- | --- | --- | --- |
| Temporary operating support files | `03_operations/05_working-files/` | Governed deal, shipment, compliance, archive, or dashboard-controlled room once custody is known | Review each operations cycle | Operations owner | Staging lane, not permanent custody | `03_operations/05_working-files/README.md` |
| Shipment proof attachments and drafts | Working-files lane if not yet placed | DOCCTRL-2026-001, SREV-2026-001, compliance case, or archive path depending on proof type | Same-cycle routing standard | Operations control | Route before closeout | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` |

## Handoff Risks and Escalations

| Topic | Linked Record | Impact | Escalation Trigger | Decision Owner | Evidence Route |
| --- | --- | --- | --- | --- | --- |
| Release and funding answer diverges | Funding release, pre-shipment release, executable-check board | Movement could widen from partial proof instead of current control truth. | Funding, release, or shipment room carries a different stop rule or next safe movement. | Founder office with finance and operations owners | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |
| Packet completeness substitutes for movement approval | Document control packet and shipment room | A clean-looking packet could hide an unclosed live gate. | Broker or supplier handoff is treated as authorized because packet exists. | Operations owner | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |
| Supplier confirmation compresses release window | Golden Harvest supplier release packet | Supplier timing can force rushed broker, release, or payment decisions. | Supplier confirmation or document review arrives too close to movement gate. | Operations and sourcing owners | `06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.md` |
| Working files become hidden custody | Working-files staging lane | Proof becomes hard to retrieve later and archive confidence weakens. | Settled evidence remains in temporary custody after owner and destination are known. | Operations control | `03_operations/05_working-files/README.md` |

## Next 24-Hour Action Queue

| Action | Linked Record | Why It Matters | Owner | Deadline | Status |
| --- | --- | --- | --- | --- | --- |
| Keep release, funding, executable-check, scenario, risk, and shipment room answers identical before movement widens. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md`, `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md`, and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` | Same-day pressure should not create conflicting operating truth. | Founder office with finance and operations owners | 2026-05-03 | In progress |
| Lock broker and clearance funding to filing-ready status. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` and `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` | Avoid paying for movement that is not actually ready to clear. | Operations and compliance owners | 2026-05-03 | Planned |
| Confirm Golden Harvest supplier execution readiness before release compression occurs. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` | Supplier timing should not force late operating decisions. | Operations desk | 2026-05-04 | In progress |
| Link final release proof into document register, shipment review, and closeout path. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` and `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` | The system should be able to prove how the gate closed later without reconstructing the story. | Operations control | 2026-05-03 | In progress |
| Review working-files staging lane and route any settled proof to governed custody. | `03_operations/05_working-files/README.md` | Temporary files should not become hidden source of truth. | Operations owner | 2026-05-03 | Scheduled |

## Operations Quality Gates

| Gate Question | Required Answer Before Status Improves | Primary Evidence Route | Owner |
| --- | --- | --- | --- |
| Is movement authorized by the live release gate, not just document completeness? | Yes, REL-2026-001 and the shipment room must carry the same release answer. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` | Operations owner |
| Is outgoing cash synchronized with packet and release proof? | Yes, FUND-2026-001 and the funding review must match the live gate before payment widens. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` | Finance owner |
| Is executable-check closure recoverable later? | Yes, task, packet, gate, review, closeout, and archive path must tell the same story. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Founder office |
| Is the packet proof in governed custody? | Yes, document control and shipment review should hold proof before closeout confidence improves. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` | Operations control |
| Are temporary working files routed? | Yes, no settled record should remain in temporary staging once destination is known. | `03_operations/05_working-files/README.md` | Operations owner |

## End-of-Cycle Closeout

| Closeout Field | Current Answer | Evidence Route |
| --- | --- | --- |
| Releases completed | REL-2026-001 is released for broker handoff, but widened movement remains tied to matched funding, executable-check, and containment proof. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` |
| Logistics blockers carried forward | Active blockers are proof closure, synchronized release/funding answer, supplier confirmation timing, and closeout-ready evidence. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |
| Working files relocated | No relocation recorded in this refresh; staging lane remains a review item, not permanent custody. | `03_operations/05_working-files/README.md` |
| Escalations triggered | Same-day escalation remains active if release, funding, scenario, risk, or executable-check answers diverge. | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` |
| Next refresh focus | Refresh shipment tower, document packet, funding release, executable-check board, and working-files staging before any status improves. | `06_dashboard/05_shipments/Daily-Shipment-Control-Tower.md` |
