# Founder Execution Queue

This governed founder queue holds the live executable move until the release, funding, packet, owner, and evidence gates all close through source records rather than memory, chat pressure, or repeated founder rescue.

## Queue Control

| Field | Reading |
| --- | --- |
| Task ID | `TASK-2026-001` |
| Task | Close deposit confirmation and release Atlantic Foods execution sequence. |
| Linked commercial record | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/README.md` |
| Linked executable check | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXECCHK-2026-001_AtlanticFoods-Override-Closure/README.md` |
| Linked shipment | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/README.md` |
| Current posture | Execution in progress under active tight watch. |
| Owner standard | Finance and operations owners must close the gate through route-backed evidence, not ad hoc founder chasing. |
| Closeout condition | Funding, release, packet, shipment review, and control-integrity records carry the same closure story. |

## Source Refresh Stack

| Source | Route | Use |
| --- | --- | --- |
| Founder dashboard | `06_dashboard/01_executive/Daily-Founder-Dashboard.md` | Confirms the founder-level task remains visible before follow-through is judged. |
| Operations command center | `06_dashboard/03_operations/Daily-Operations-Command-Center.md` | Keeps the live shipment, packet, release, and task gate aligned. |
| Executable-check board | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Provides formal same-day closure discipline for trust-linked movement. |
| Owner accountability review | `06_dashboard/28_owner-accountability/Executive-Owner-Accountability-and-Follow-Through-Review.md` | Confirms named owner action, deadline, and follow-through without founder rescue. |
| Funding and payables review | `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` | Tests whether payment or supplier release movement can proceed without outrunning proof. |
| Control-integrity review | `06_dashboard/34_control-integrity/Executive-Control-Integrity-and-Decision-Readiness-Review.md` | Confirms override logic does not widen into uncontrolled movement. |
| Executive risk register | `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Tracks the risk of executable checks closing late or with weak evidence. |
| System adoption board | `06_dashboard/35_system-adoption/Operating-System-Adoption-and-Readiness-Board.md` | Confirms the queue is being used as operating discipline, not optional admin. |

## Live Gate Board

| Gate | Required Proof | Current Control Read | Do Not Close Until |
| --- | --- | --- | --- |
| Deposit confirmation | Deposit status, buyer-side confirmation, and cash timing are visible. | Required before the execution sequence can be treated as clean. | Finance confirms the deposit trail and cash impact through source records. |
| Funding release | Supplier balance, release amount, payment basis, and approval path are aligned. | Controlled release remains available only inside the approved gate. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` is current. |
| Pre-shipment release | Release approval, trust posture, packet integrity, and broker handoff remain synchronized. | Movement must not widen beyond the bounded override. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` is current. |
| Document packet | Export packet, customer promise, supplier release packet, and shipment facts tell one story. | Packet proof is part of execution, not after-the-fact archive work. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` is current. |
| Shipment review | Loading, release, packet, and funding facts can be reviewed together. | The task cannot close if operations proof remains fragmented. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` is current. |
| Closeout proof | Executable check, matter control, archive path, and owner accountability agree. | Closure should be reusable evidence, not a verbal update. | The board, task room, and related source rooms carry the same status. |

## Founder Reading Order

| Step | Open | Founder Question Answered |
| --- | --- | --- |
| 1 | `OPEN-HERE.html` | What live executable move is still open, who owns it, and what proof is required? |
| 2 | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXECCHK-2026-001_AtlanticFoods-Override-Closure/OPEN-HERE.html` | Is the trust-linked override gate ready to close without widening blocked movement? |
| 3 | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html` | Does the formal control board agree with this task room? |
| 4 | `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.html` | Can payment or supplier-release movement proceed without outrunning proof? |
| 5 | `06_dashboard/28_owner-accountability/Executive-Owner-Accountability-and-Follow-Through-Review.html` | Which owner is accountable if the same-day gate remains open? |
| 6 | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/OPEN-HERE.html` | Does shipment reality still match the commercial and funding story? |

## Owner Accountability Matrix

| Owner Lane | Must Own | Evidence Required | Founder Escalation Trigger |
| --- | --- | --- | --- |
| Finance owner | Deposit confirmation, supplier-balance basis, cash timing, and payment-release proof. | Funding record, cash impact, approval basis, and updated payable posture. | Payment release is requested without current deposit or cash proof. |
| Operations owner | Pre-shipment release, broker handoff, packet integrity, and shipment-review facts. | Release record, document-control record, shipment review, and supplier packet status. | Shipment movement widens before packet and release proof align. |
| Founder office | Boundary of override, final go or no-go posture, and archive-ready interpretation. | Executable-check board and control-integrity review match the source records. | Owners attempt to close by verbal update instead of route-backed evidence. |
| Record owner | Status synchronization across task, executable check, shipment, funding, release, and archive path. | All linked rooms carry the same closure story and date logic. | One record says closed while another still shows active tight watch. |

## Movement Permission Rules

| Movement | Allowed When | Blocked When |
| --- | --- | --- |
| Deposit-dependent execution | Deposit proof, release gate, and cash impact are current. | Deposit status is assumed, stale, or held outside source records. |
| Supplier payment release | Funding review, supplier release packet, and trust posture are aligned. | Payment basis outruns packet proof or founder-approved boundary. |
| Pre-shipment release | Release record, document packet, and operations command center agree. | Broker handoff or loading movement is requested before proof synchronization. |
| Override step-down | The executable check closes through owner evidence and no founder rescue remains needed. | Same-day closure still depends on founder chasing or informal updates. |
| Archive preparation | Closeout proof, shipment review, and task record tell the same final story. | Any route remains active, provisional, or contradictory. |

## Evidence Closeout Board

| Evidence Class | Source Route | Closeout Standard |
| --- | --- | --- |
| Commercial gate | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/README.md` | Active deal posture matches the task action and does not imply broader approval. |
| Executable check | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXECCHK-2026-001_AtlanticFoods-Override-Closure/README.md` | Gate status, owner, cutoff, evidence, and allowed movement are explicit. |
| Follow-through | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/ACCTY-2026-Q3_AtlanticFoods-Follow-Through/README.md` | Owner action is time-boxed and no longer dependent on founder rescue. |
| Funding release | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` | Payment basis is current, bounded, and tied to deposit and release proof. |
| Pre-shipment release | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` | Release is controlled and does not widen beyond approved trust logic. |
| Document control | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` | Export packet supports the same movement decision. |
| Shipment review | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` | Operations facts support closeout, not just movement. |

## Decision Matrix

| Founder Question | Evidence Mix | Current Answer |
| --- | --- | --- |
| Can the live gate close? | Task room, executable-check board, funding record, release record, and shipment review. | Not until all source records carry the same closure proof. |
| Can payment move? | Funding review, deposit proof, supplier release packet, and capital discipline. | Controlled only inside the bounded gate. |
| Can release widen? | Pre-shipment release, packet integrity, trust posture, and control-integrity review. | No widening without refreshed proof. |
| Can founder step back? | Owner accountability, executable-check closure, and system adoption board. | Only after owner-led closure no longer depends on founder chase. |
| Can the task archive? | Closeout proof, shipment review, archive path, and final owner evidence. | Not while any linked record remains active tight watch. |

## Escalation and Stop Rules

| Trigger | Immediate Move | Founder Protection |
| --- | --- | --- |
| Same-day cutoff passes without source-backed closure. | Escalate through owner accountability and executable-check board. | Prevents a live gate from becoming another reminder cycle. |
| Payment release is requested without deposit proof. | Hold funding movement and refresh funding, cash, and credit context. | Protects cash discipline and supplier leverage. |
| Shipment movement is requested while packet proof is stale. | Hold release widening and refresh document-control and shipment-review rooms. | Prevents operations from outrunning controlled proof. |
| One record says closed while another remains active. | Reconcile status before founder reads the task as complete. | Keeps the operating system trustworthy. |
| Owner attempts to close by verbal update. | Require route-backed evidence in the task, executable-check, and source rooms. | Converts activity into durable institutional memory. |

## Visual Preview Stack

| Preview | Route | Founder Use |
| --- | --- | --- |
| Task tracker preview | `00_brand/03_exports/02_preview-docs/task-tracker-preview.html` | Reviews the visual queue surface before treating execution as current. |
| Founder dashboard preview | `00_brand/03_exports/02_preview-docs/founder-dashboard-preview.html` | Confirms the task remains visible at founder level. |
| Operations command center preview | `00_brand/03_exports/02_preview-docs/operations-command-center-preview.html` | Checks shipment, packet, funding, and release status in one control view. |
| Executive owner accountability preview | `00_brand/03_exports/02_preview-docs/executive-owner-accountability-review-preview.html` | Tests whether named owners have closed the gate without founder rescue. |
| Funding and payables preview | `00_brand/03_exports/02_preview-docs/funding-payables-release-review-preview.html` | Reviews payment-release basis before movement widens. |
| Executive control integrity preview | `00_brand/03_exports/02_preview-docs/executive-control-integrity-review-preview.html` | Confirms bounded override logic remains contained. |

## End-of-Cycle Closeout

| Closeout Item | Standard |
| --- | --- |
| Queue status | Keep active tight watch until funding, release, packet, shipment review, owner accountability, and executable-check records agree. |
| Founder posture | Do not treat the task as complete because the work moved; complete only when the evidence closes. |
| Next refresh | Update this room when deposit proof, funding basis, release approval, shipment review, owner status, or executable-check posture changes. |
