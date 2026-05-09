# Pre-Shipment Release Gate

| Release Control | Current Standard |
| --- | --- |
| Review ID | `REL-2026-001` |
| Shipment ID | `SHIP-2026-001` |
| Route | Qingdao to Orlando via Port Newark |
| Purpose | Govern the final gate review before broker handoff, forwarder release, customer-facing release language, or any wider movement tied to the active garlic shipment. |
| Primary lens | Broker handoff is narrow permission, not full movement authority. |
| Current status | Released for broker handoff under controlled conditions. |
| Linked executable check task | `TASK-2026-001` |
| Linked containment references | `SCEN-2026-005`, `RISK-2026-008` |
| Founder rule | Do not widen movement unless release, funding, document control, executable-check, scenario, and risk records carry the same current answer. |

## Release Snapshot

| Signal | Current Reading | Founder Interpretation |
| --- | --- | --- |
| Release posture | Broker handoff is released under controlled conditions. | External coordination can continue, but broader movement remains proof-gated. |
| Packet posture | Broker packet is released under controlled issue. | Packet completeness should not be treated as unrestricted authority. |
| Funding posture | Supplier and shipment-linked cash remain controlled. | Payment should stay synchronized with live gate proof. |
| Executable-check posture | `EXECCHK-2026-001` remains active tight watch. | Same-day owner path and closure evidence still matter. |
| Trust posture | Atlantic Foods is fragile and Golden Harvest is controlled. | Trust-linked consequences should slow acceleration if proof weakens. |

## Source Refresh Stack

| Source Layer | Evidence Route | Founder Control Purpose |
| --- | --- | --- |
| Live shipment room | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/README.md` | Keeps release-before-movement logic, funding synchronization, packet proof, and same-day containment visible. |
| Shipment control tower | `06_dashboard/05_shipments/Daily-Shipment-Control-Tower.md` | Confirms daily movement posture before release status improves. |
| Document control packet | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` | Confirms whether packet scope, filing intake, version proof, and release evidence are current. |
| Funding release record | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` | Keeps supplier settlement, freight, broker, and clearance funding aligned with the live release answer. |
| Supplier release packet | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` | Ensures supplier-facing wording stays inside the narrow release currently approved. |
| Executable-check board | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Confirms owner, cutoff, gate, evidence state, containment answer, and archive readiness before movement widens. |
| Scenario and risk controls | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` and `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Carries the stop rule, next safe movement, and same-day escalation consequence. |
| Shipment review log | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` | Preserves proof after movement or gate posture changes. |

## Gate Decision Surface

| Gate Question | Required Current Answer | Evidence Route | Current Gate State |
| --- | --- | --- | --- |
| Is broker handoff allowed? | Yes, but only under controlled conditions and current packet scope. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` | Released narrow handoff. |
| Is unrestricted movement allowed? | No, widened movement still needs matched proof. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Blocked until synchronized. |
| Is supplier payment allowed to accelerate? | No, supplier settlement remains governed by funding release and executable-check proof. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` | Controlled. |
| Is customer-facing release confidence ready to widen? | Only if trust posture and packet proof stay current. | `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` | Bounded. |
| Is closeout proof ready? | Not final until release proof is linked to document control and shipment review. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` | In progress. |

## Handoff Authorization

| Handoff Path | What Is Authorized | What Is Not Authorized | Required Proof Before Widening |
| --- | --- | --- | --- |
| Broker handoff | Controlled broker coordination against the current packet. | Unrestricted broker movement or assumption-led clearance confidence. | Document lock, filing readiness, funding alignment, and executable-check closure. |
| Forwarder coordination | Preparation against current release posture. | Shipment acceleration beyond the live gate. | Release, funding, scenario, and risk records restate the same answer. |
| Supplier confirmation | Confirmation of narrow released instructions. | Supplier action outside approved packet language. | Supplier receipt, document review, and execution confirmation are logged. |
| Customer-facing update | Controlled status language if proof remains current. | Customer confidence claims that outrun release or trust posture. | Account trust and live gate records remain aligned. |

## Trust and Containment Checks

| Check | Current Reading | Stop Rule | Owner |
| --- | --- | --- | --- |
| Customer trust | Atlantic Foods remains fragile. | Do not use release posture to imply commercial stabilization. | Founder office and commercial owner |
| Supplier trust | Golden Harvest remains controlled. | Do not let supplier confirmation or pressure widen release or payment. | Operations and sourcing owners |
| Funding trust | Shipment-linked outgoing cash is controlled. | No widened payment without matching funding and executable-check evidence. | Finance owner |
| Scenario containment | `SCEN-2026-005` remains live. | Divergent release, funding, or movement wording triggers scenario refresh. | Founder office |
| Risk containment | `RISK-2026-008` remains live. | Improvised movement rescue becomes same-day founder escalation. | Founder office |

## Visual Preview Stack

| Preview | Route | Founder Use |
| --- | --- | --- |
| Pre-shipment release review | `00_brand/03_exports/02_preview-docs/pre-shipment-release-review-preview.html` | Review the release gate as a formal pre-handoff artifact. |
| Document control register | `00_brand/03_exports/02_preview-docs/document-control-register-preview.html` | Confirm packet proof and document-lock logic. |
| Shipment control tower | `00_brand/03_exports/02_preview-docs/shipment-control-tower-preview.html` | Compare release posture against daily shipment movement posture. |
| Counterparty trust posture matrix | `00_brand/03_exports/02_preview-docs/counterparty-trust-posture-matrix-preview.html` | Confirm whether fragile or controlled trust should slow movement. |

## Founder Decision Matrix

| Decision Question | Required Reading | Greenlight Condition | Current Answer |
| --- | --- | --- | --- |
| Can broker handoff proceed? | Release gate, document control, shipment tower. | Packet scope and release gate remain current. | Yes, controlled handoff only. |
| Can movement widen? | Executable-check board, funding release, scenario, risk. | All live-gate records restate the same next safe movement. | Not yet. |
| Can payment widen? | Funding record, funding dashboard, trust matrix. | Funding basis, trust posture, and release gate align. | Not yet. |
| Can release language be used externally? | Supplier packet, customer trust posture, document control. | Wording stays narrow and evidence-backed. | Yes, bounded language only. |
| Can the release close? | Shipment review, document control, closeout path. | Final proof is linked and retrievable. | Not final. |

## Escalation and Stop Rules

| Trigger | Immediate Action | Founder Consequence | Evidence Route |
| --- | --- | --- | --- |
| Packet completeness is treated as movement authority. | Freeze widening and refresh executable-check board. | Release remains broker-handoff only. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |
| Funding or supplier pressure moves faster than release proof. | Hold payment acceleration and refresh funding review. | Supplier settlement stays controlled. | `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` |
| Scenario, risk, funding, and release wording diverge. | Route through same-day containment revalidation. | Founder escalation remains active. | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` |
| Supplier confirmation changes the movement answer. | Reconfirm supplier packet and release gate before action. | No informal movement widening. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md` |
| Closeout proof is not linked. | Keep release open until shipment review captures gate closure. | Archive readiness is blocked. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` |

## End-of-Cycle Closeout

| Closeout Field | Current Answer | Required Before Final Close |
| --- | --- | --- |
| Release status | Released for broker handoff under controlled conditions. | Widened movement requires matched release, funding, executable-check, scenario, and risk proof. |
| Founder posture | Controlled movement only. | No unrestricted movement or payment acceleration. |
| Primary blocker | Same-day synchronized proof and closeout linkage are still active. | Document control, funding release, executable check, and shipment review must agree. |
| Record standard | Source module now carries route-backed gate decisions, handoff scope, trust checks, visual previews, decision matrix, stop rules, and closeout logic. | Refresh when movement posture or proof state changes. |
