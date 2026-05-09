# Active Shipments

This lane governs live shipment rooms while movement, packet proof, release gates, funding gates, traceability, supplier response, and closeout evidence are still active. It is the founder-facing control layer for deciding whether a shipment may move, remain contained, or exit active custody.

## Lane Control

| Field | Current Standard |
| --- | --- |
| Lane purpose | Govern live shipment custody until movement, release, funding, packet, review, and archive proof are resolved. |
| Folder naming | `SHIP-YYYY-###_Origin-to-Destination` |
| Active shipment count | One live shipment room currently governs the China to USA garlic program. |
| Primary live room | `SHIP-2026-001_China-to-USA/README.md` |
| Control posture | Movement remains controlled; packet completeness, supplier pressure, or commercial urgency cannot widen release by itself. |
| Founder risk | Release, funding, packet, or closeout confidence can drift if the lane does not force every proof surface to agree. |

## Source Refresh Stack

| Source | Route | Founder Use |
| --- | --- | --- |
| Live shipment room | `SHIP-2026-001_China-to-USA/README.md` | Holds the shipment-level control narrative for release, funding, packet, supplier, traceability, and containment. |
| Operations command center | `06_dashboard/03_operations/Daily-Operations-Command-Center.md` | Shows same-day operating posture, owner follow-through, and shipment proof watch items. |
| Shipment control tower | `06_dashboard/05_shipments/Daily-Shipment-Control-Tower.md` | Gives the dashboard-level shipment view for movement, filing, traceability, and funding status. |
| Founder execution queue | `02_crm/05_tasks/TASK-2026-001_Founder-Execution-Queue/README.md` | Keeps live gate closure tied to named owner proof and deadline discipline. |
| Executable-check board | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Confirms trust-linked movement, payment, and archive proof do not widen without formal control. |
| Scenario response review | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` | Preserves stop rules and next safe movement if cash, customer, supplier, or release assumptions diverge. |
| Executive risk register | `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Keeps late proof, weak closure, and movement-risk consequences founder-visible. |
| Working files lane | `03_operations/05_working-files/README.md` | Prevents temporary support files from becoming hidden custody outside shipment records. |

## Active Shipment Register

| Shipment | Current Posture | Governed By | Movement Boundary |
| --- | --- | --- | --- |
| `SHIP-2026-001_China-to-USA/README.md` | Controlled, not fully stabilized. | Atlantic Foods commercial path and Golden Harvest supplier controls. | Narrow movement only when release, funding, executable-check, packet, traceability, and risk records agree. |

## Required Shipment Modules

| Module | Required When | Current Route |
| --- | --- | --- |
| Pre-shipment release review | Broker handoff, forwarder release, ETD readiness, or shipment movement needs formal clearance. | `SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` |
| Funding and payables release review | Supplier, freight, broker, duty, clearance, or shipment-linked cash may move. | `SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` |
| Document control register | Commercial documents, packet versions, filing intake, traceability references, or broker packet proof need custody. | `SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |
| Supplier release packet | Supplier-facing instructions, receipt, document review, execution confirmation, or narrow movement language are active. | `SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` |
| Shipment review log | Movement occurs, gate posture changes, proof needs closeout, or lessons must be retained. | `SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` |

## Proof Gate Map

| Gate | Must Agree With | Hold Signal |
| --- | --- | --- |
| Release gate | Pre-shipment release, executable check, scenario response, risk register, and shipment room. | Broker handoff or movement wants to widen before the same answer appears in all control surfaces. |
| Funding gate | Funding release, cash/funding dashboard, executable check, release gate, and packet proof. | Supplier settlement, freight, broker, or clearance cash tries to move ahead of live proof. |
| Packet gate | Document control, supplier packet, traceability room, and shipment review. | Clean-looking documents are treated as authority for movement or filing confidence. |
| Supplier response gate | Supplier release packet, supplier performance, trust posture, and supply resilience. | Golden Harvest confirmation arrives too late and compresses release or payment decisions. |
| Traceability gate | Traceability room, document control, compliance dashboard, claim/CAPA records, and shipment review. | Filing, challenge-defense, recovery, or FDA readiness language widens while an evidence gap remains open. |
| Closeout gate | Shipment review, archive path, task room, executable-check board, and document control. | Active proof is not retrievable but closeout or archive confidence is requested. |

## Movement Permission Matrix

| Movement | Allowed When | Not Allowed When |
| --- | --- | --- |
| Broker handoff | `REL-2026-001`, shipment room, executable check, and risk controls carry the same narrow answer. | Packet completeness or urgency is being used as substitute release authority. |
| Supplier payment | `FUND-2026-001`, funding review, deposit logic, release gate, and packet proof are synchronized. | Supplier pressure, shipment timing, or clean documents outrun cash and release proof. |
| Supplier instruction | `COMM-2026-002` confirms only the action supported by release and funding posture. | Supplier wording implies full shipment release, unrestricted broker handoff, or payment acceleration. |
| Filing confidence | Document control and traceability boundary are current. | Traceability or packet proof is incomplete, stale, or only implied. |
| Shipment closeout | Shipment review captures movement, service quality, document quality, supplier performance, and follow-up actions. | Closeout depends on memory, temporary files, or unlinked packet proof. |

## Founder Reading Order

| Step | Open | Founder Question Answered |
| --- | --- | --- |
| 1 | `OPEN-HERE.html` | What shipments are active, and what lane-level gates control movement? |
| 2 | `SHIP-2026-001_China-to-USA/OPEN-HERE.html` | What is the current live shipment posture and next safe movement? |
| 3 | `SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/OPEN-HERE.html` | Is release authority current and bounded? |
| 4 | `SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/OPEN-HERE.html` | Can any outgoing shipment-linked cash move? |
| 5 | `SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/OPEN-HERE.html` | Is packet, filing, and document proof controlled? |
| 6 | `SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/OPEN-HERE.html` | Is post-move proof ready for review, lessons, and closeout? |

## Lane Exit Rules

| Exit Path | Required Before Exit | Destination |
| --- | --- | --- |
| Completed shipment closeout | Shipment review, document control, release proof, funding proof, supplier response, traceability posture, and archive note agree. | Archive lane or retained shipment closeout route. |
| Cancelled or held shipment | Founder decision, risk posture, supplier/customer communication, and any funding exposure are documented. | CRM, archive, or exception control depending on final posture. |
| Reopened movement | Release, funding, packet, scenario, and risk records refresh before movement resumes. | Stays in active lane. |
| Temporary support files settle | Owner and destination are known. | Working files must route to governed custody before lane status improves. |

## Visual Preview Stack

| Preview | Route | Founder Use |
| --- | --- | --- |
| Shipment control tower | `00_brand/03_exports/02_preview-docs/shipment-control-tower-preview.html` | Reviews active shipment posture, filing confidence, movement gates, and blockers. |
| Operations command center | `00_brand/03_exports/02_preview-docs/operations-command-center-preview.html` | Checks same-day owner action and operations-level proof watch. |
| Pre-shipment release review | `00_brand/03_exports/02_preview-docs/pre-shipment-release-review-preview.html` | Confirms broker handoff and release posture before movement widens. |
| Funding and payables release review | `00_brand/03_exports/02_preview-docs/funding-payables-release-review-preview.html` | Reviews supplier, freight, broker, clearance, and shipment-linked cash discipline. |
| Document control register | `00_brand/03_exports/02_preview-docs/document-control-register-preview.html` | Confirms packet, filing, traceability, and version custody. |
| Shipment review log | `00_brand/03_exports/02_preview-docs/shipment-review-log-preview.html` | Confirms movement evidence, service quality, supplier performance, and closeout lessons. |
| Traceability record | `00_brand/03_exports/02_preview-docs/traceability-record-preview.html` | Keeps compliance confidence bounded where lot-path proof remains open. |

## Escalation and Stop Rules

| Trigger | Immediate Move | Founder Protection |
| --- | --- | --- |
| Release, funding, packet, or risk posture diverges. | Hold movement and refresh shipment room, release gate, funding release, executable-check board, and scenario response. | Prevents operational urgency from becoming unauthorized movement. |
| Packet completeness is used as release authority. | Route through pre-shipment release and document control before action. | Separates proof from permission. |
| Outgoing cash seeks movement before gate proof matches. | Hold payment and refresh funding, release, and executable-check records. | Protects cash discipline and supplier leverage. |
| Traceability gap is hidden by shipment completion. | Keep confidence bounded and refresh traceability, document control, and shipment review. | Protects challenge-defense and regulator credibility. |
| Closeout or archive is requested before review proof is retrievable. | Keep active custody and require shipment review linkage. | Prevents archive finality from outrunning evidence. |

## End-of-Cycle Closeout

| Closeout Item | Standard |
| --- | --- |
| Lane status | Active shipment lane remains a live custody surface until every movement, release, funding, packet, traceability, and closeout proof gate agrees. |
| Founder posture | Treat `SHIP-2026-001` as controlled and proof-gated, not fully stabilized, while widened movement depends on matched source records. |
| Next refresh | Update when release posture, funding basis, packet status, supplier confirmation, traceability gap, shipment review, or archive readiness changes. |
