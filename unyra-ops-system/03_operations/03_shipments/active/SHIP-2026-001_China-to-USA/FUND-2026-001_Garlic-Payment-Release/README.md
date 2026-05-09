# Funding Release Record

| Funding Control | Current Standard |
| --- | --- |
| Record ID | `FUND-2026-001` |
| Linked shipment | `SHIP-2026-001` |
| Funding theme | Garlic shipment payment and release control. |
| Purpose | Keep shipment-linked payment control inside the active shipment folder when supplier settlement, freight funding, broker fees, or clearance cash need governed release. |
| Linked executable check task | `TASK-2026-001` |
| Primary lens | Cash follows proof; pressure does not create payment permission. |
| Current posture | Controlled shipment-linked funding with one payment path still needing tighter basis. |
| Founder rule | Do not release outgoing cash faster than packet integrity, filing readiness, trust posture, liquidity timing, release approval, and executable-check closure can support. |

## Funding Snapshot

| Signal | Current Reading | Founder Interpretation |
| --- | --- | --- |
| Supplier balance | USD 62,000 Golden Harvest balance under controlled release. | Supplier continuity matters, but payment should stay inside current gate proof. |
| Freight and origin handling | USD 28,000 cleared operational vendor path. | Logistics funding can move only while booking and packet status remain current. |
| Broker and clearance funding | USD 17,000 planned readiness funding. | Clearance cash should follow filing-ready status, not assumption. |
| Customer-side trust | Atlantic Foods remains fragile. | Outgoing shipment cash should not outrun customer-side release confidence. |
| Supplier-side trust | Golden Harvest remains controlled. | Payment confidence should not imply wider supplier trust. |

## Source Refresh Stack

| Source Layer | Evidence Route | Founder Control Purpose |
| --- | --- | --- |
| Funding and payables review | `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` | Governs outgoing cash sequencing, supplier deposits, freight, broker, and clearance payments. |
| Cash forecast and exposure | `06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.md` | Confirms liquidity timing before outgoing cash is released. |
| Capital allocation review | `06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.md` | Confirms whether scarce cash, supplier capacity, and release approvals are sequenced intentionally. |
| Live shipment room | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/README.md` | Keeps payment logic tied to release-before-movement and packet proof. |
| Pre-shipment release gate | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` | Confirms whether payment can support broker handoff or remains bounded. |
| Document control packet | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` | Confirms packet integrity, filing readiness, and proof needed before broker or clearance cash moves. |
| Executable-check board | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Confirms owner, cutoff, live gate, evidence state, containment answer, and archive readiness before payment widens. |
| Trust posture matrix | `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` | Converts fragile customer trust and controlled supplier trust into payment consequences. |
| Scenario and risk controls | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` and `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Carries the stop rule, next safe movement, and same-day escalation consequence. |

## Payment Release Stack

| Payment Item | Payee or Path | Amount | Release Condition | Current Status |
| --- | --- | --- | --- | --- |
| Supplier balance | Golden Harvest Produce | USD 62,000 | Deposit, packet integrity, supplier trust posture, and release approval remain aligned. | Controlled release. |
| Ocean freight and origin handling | Forwarder and origin vendors | USD 28,000 | Booking confirmation and packet control stay current. | Cleared. |
| Customs broker and clearance funding | Broker and clearance partners | USD 17,000 | Filing status, document lock, and release gate stay clean. | Planned. |
| Atlantic Foods-linked outgoing shipment cash | Shipment-linked release path | Governed by live funding basis | Funding review, executable-check board, and pre-shipment gate restate the same answer. | Active containment. |

## Release Conditions

| Condition | Required Proof | Founder Risk if Skipped | Evidence Route |
| --- | --- | --- | --- |
| Liquidity timing | Cash forecast supports the next 14-day release sequence. | Outgoing cash compresses working capital before revenue quality is secure. | `06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.md` |
| Packet integrity | Document control shows packet status and filing readiness. | Cash moves for a shipment that is not actually ready to clear or move. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |
| Release approval | `REL-2026-001` supports only the current narrow movement answer. | Payment creates implied broader movement permission. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` |
| Executable-check closure | Owner path, cutoff, evidence state, and containment answer are current. | Founder override becomes execution habit instead of controlled proof. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |
| Trust posture | Customer and supplier trust consequences are current. | Relationship optimism outruns cash discipline. | `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` |

## Trust-Linked Payment Watch

| Counterparty or Path | Trust Posture | Payment Consequence | Current Guardrail |
| --- | --- | --- | --- |
| Golden Harvest Produce | Controlled supplier path. | Keep supplier funding inside governed shipment logic. | Do not prepay beyond current shipment need while fallback posture remains partially mature. |
| Atlantic Foods-linked shipment cash | Fragile customer-side path. | Outgoing shipment cash should not outrun customer release confidence. | Maintain deposit proof, acknowledgment discipline, and matched gate answers. |
| Broker and clearance partners | Operational vendor standard. | Funding can support readiness only when filing status is clean. | Tie broker and clearance cash to document lock and release gate. |
| Founder override path | Active tight watch. | Payment cannot widen because the founder is monitoring it. | Use executable-check proof, not attention, as the permission standard. |

## Same-Day Revalidation

| Revalidation Layer | Required Same-Day Answer | Owner | Status |
| --- | --- | --- | --- |
| Funding record | Payment basis, amount, and release condition are current. | Finance owner | In progress |
| Release gate | Broker handoff or movement posture is unchanged and bounded. | Operations owner | In progress |
| Document control | Packet, filing, and broker status support the requested cash movement. | Operations and compliance owners | Planned |
| Executable check | Owner path, cutoff, evidence state, and containment answer remain current. | Founder office | Active watch |
| Scenario and risk | Stop rule and next safe movement match funding and release records. | Founder office | Active containment |

## Visual Preview Stack

| Preview | Route | Founder Use |
| --- | --- | --- |
| Funding and payables release review | `00_brand/03_exports/02_preview-docs/funding-payables-release-review-preview.html` | Review the outgoing cash decision surface before payment widens. |
| Counterparty trust posture matrix | `00_brand/03_exports/02_preview-docs/counterparty-trust-posture-matrix-preview.html` | Confirm whether fragile or controlled trust should slow payment. |

## Founder Decision Matrix

| Decision Question | Required Reading | Greenlight Condition | Current Answer |
| --- | --- | --- | --- |
| Can supplier balance release continue? | Funding record, release gate, trust matrix. | Supplier payment stays inside current shipment need and controlled trust posture. | Controlled release. |
| Can freight and origin handling stay cleared? | Funding review and shipment control tower. | Booking and packet control remain current. | Yes, while proof stays current. |
| Can broker and clearance funding move? | Document control, release gate, funding review. | Filing status, document lock, and release gate agree. | Planned, not automatic. |
| Can payment pace widen? | Executable-check board, scenario, risk, funding review. | Same-day proof restates the same next safe movement. | Not yet. |
| Can funding close? | Shipment review, document control, funding dashboard. | Payment proof, packet proof, and gate closure are retrievable. | Not final. |

## Escalation and Stop Rules

| Trigger | Immediate Action | Founder Consequence | Evidence Route |
| --- | --- | --- | --- |
| Vendor pressure arrives without packet or release support. | Hold payment and refresh funding basis. | Cash does not move on urgency alone. | `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` |
| Clearance funding is requested before filing status is stable. | Revalidate document control and broker readiness. | Broker or clearance cash stays planned. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |
| Release, funding, scenario, and risk records diverge. | Route through same-day containment review. | No widened payment pace. | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` |
| Trust posture weakens or supplier confirmation compresses timing. | Refresh trust posture and response escalation before payment widens. | Payment remains controlled. | `06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.md` |
| Payment proof is not linked into closeout. | Keep funding record open until shipment review captures proof. | Archive readiness is blocked. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` |

## End-of-Cycle Closeout

| Closeout Field | Current Answer | Required Before Final Close |
| --- | --- | --- |
| Funding status | Controlled shipment-linked funding with supplier balance in controlled release, freight cleared, and broker or clearance funding planned. | Payment proof, release proof, packet proof, and executable-check closure must align. |
| Founder posture | Cash follows proof. | Do not widen payment based on urgency, packet appearance, or founder attention alone. |
| Primary blocker | Same-day containment alignment and closeout-proof linkage remain active. | Funding, release, document control, scenario, risk, and shipment review records must agree. |
| Record standard | Source module now carries route-backed source stack, payment release stack, release conditions, trust watch, same-day revalidation, previews, decision matrix, stop rules, and closeout logic. | Refresh when amount, payment status, or release authority changes. |
