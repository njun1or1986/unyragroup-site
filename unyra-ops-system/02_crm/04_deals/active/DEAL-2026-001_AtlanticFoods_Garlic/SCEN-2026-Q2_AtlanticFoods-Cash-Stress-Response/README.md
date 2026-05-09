# Scenario Response Record

| Scenario Control | Current Standard |
| --- | --- |
| Record ID | `SCEN-2026-Q2` |
| Covered scenario IDs | `SCEN-2026-001` Atlantic Foods cash-timing stress and `SCEN-2026-005` trust-linked live-gate failure. |
| Linked deal | `DEAL-2026-001` |
| Scenario theme | Atlantic Foods cash timing, release containment, and live-gate failure response. |
| Purpose | Pre-define founder response before cash timing, release control, customer concentration, or a trust-linked live gate rapidly changes the operating posture. |
| Primary lens | Pre-decide the hard trade-offs before pressure arrives. |
| Linked live-gate records | `EXECCHK-2026-001`, `FUND-2026-001`, `REL-2026-001`, `DOCCTRL-2026-001`, `SREV-2026-001` |
| Founder rule | If cash timing or live-gate proof weakens, freeze widening first, then decide the narrow next safe movement from route-backed evidence. |

## Scenario Snapshot

| Signal | Current Reading | Founder Interpretation |
| --- | --- | --- |
| Cash-stress posture | Atlantic Foods remains cash-sensitive because collection timing and open release requests can collide. | Release expansion should slow before cash pressure becomes improvised rescue. |
| Live-gate posture | Trust-linked gate containment is active through executable-check, funding, release, scenario, and risk records. | The system should trigger stop logic before founder attention becomes the control. |
| Main downside trigger | Collection slips beyond 7 days while open release or payment requests remain active. | Cash and movement should be resequenced together. |
| Main live-gate trigger | A trust-linked payment or release needs widening without current executable-check ownership. | Payment, broker handoff, or shipment acceleration should freeze immediately. |
| Response readiness | Partially ready; first-48-hour logic is now made explicit in this source record. | Founder should see the decision tree without relying on dashboard summary only. |

## Source Refresh Stack

| Source Layer | Evidence Route | Founder Control Purpose |
| --- | --- | --- |
| Executive scenario review | `06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.md` | Carries the cross-scenario matrix, first-48-hour readiness, owner paths, and contingency queue. |
| Executive risk register | `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` | Confirms severity, velocity, mitigation status, and escalation consequence for cash and live-gate risks. |
| Live deal room | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/README.md` | Keeps scenario response tied to control-before-commitment, fragile trust, pricing, release, and recovery posture. |
| Matter control spine | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control/README.md` | Holds the same stop rule, next safe movement, and owner accountability across commercial, operations, finance, and compliance. |
| Executable-check source | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXECCHK-2026-001_AtlanticFoods-Override-Closure/README.md` | Confirms owner path, cutoff, live gate, evidence state, containment answer, and archive readiness. |
| Funding release record | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` | Prevents supplier settlement, freight, broker, and clearance cash from outrunning proof. |
| Pre-shipment release gate | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` | Confirms whether broker handoff or movement can remain narrow, widen, or freeze. |
| Document control packet | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` | Keeps packet proof, filing readiness, version discipline, and release scope from becoming assumption-led. |
| Cash forecast and credit controls | `06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.md` and `06_dashboard/09_credit-risk/Credit-and-Release-Control-Board.md` | Grounds cash-stress response in liquidity timing, receivable confidence, and release discipline. |
| Founder decision board | `06_dashboard/13_founder-decisions/Executive-Decision-Board.md` | Converts response logic into an explicit founder freeze, downgrade, exception, or override decision. |

## Trigger Map

| Trigger | Trigger Type | First Reading | Immediate Control Response | Evidence Route |
| --- | --- | --- | --- | --- |
| Atlantic Foods collection slips beyond 7 days while release or payment requests remain active. | Cash timing | Cash-stress scenario is active. | Freeze discretionary release expansion and refresh cash forecast, credit posture, and founder decision logic. | `06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.md` |
| Supplier settlement, broker handoff funding, or shipment acceleration is requested without current executable-check ownership. | Live-gate failure | `SCEN-2026-005` containment is active. | Freeze widening and refresh executable-check, funding, release, scenario, and risk records. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXECCHK-2026-001_AtlanticFoods-Override-Closure/README.md` |
| Packet completeness is cited as authority for movement. | Proof failure | Packet proof is being confused with release permission. | Hold movement and route through document control and pre-shipment release. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |
| Founder rescue is needed to close a gate in real time. | Governance failure | System readiness is not yet enough. | Downgrade to controlled hold, assign owner accountability, and preserve evidence before retry. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |
| More than one exception call lands in the same cycle. | Bandwidth risk | Founder decision bandwidth is under pressure. | Prioritize cash preservation and live-gate containment before commercial acceleration. | `06_dashboard/13_founder-decisions/Executive-Decision-Board.md` |

## First 48-Hour Response

| Time Window | Required Action | Owner | Success Condition |
| --- | --- | --- | --- |
| Same day | Freeze widened payment, broker handoff funding, shipment acceleration, or release expansion if cash or live-gate trigger activates. | Founder office with finance and operations owners | No new movement widens without a route-backed answer. |
| Same day | Reconcile executable-check, funding release, pre-shipment release, matter control, scenario, and risk wording. | Operations control | All live-gate records state the same stop rule and next safe movement. |
| Within 24 hours | Reset cash forecast, credit posture, collection follow-up, and customer response path. | Finance and commercial owners | Cash-stress response is dated, owned, and visible in founder decision logic. |
| Within 24 hours | Confirm packet, filing, supplier response, and shipment review proof are preserved. | Operations and compliance owners | Proof can be retrieved without reconstructing the gate story from memory. |
| Within 48 hours | Decide whether to hold, narrow, retry, downgrade, or return to standard posture. | Founder office | Decision is recorded with evidence route and owner follow-through. |

## Stop Rule and Next Safe Movement

| Control Question | Current Scenario Answer | Next Safe Movement | If Answer Is Weak |
| --- | --- | --- | --- |
| What is blocked? | Widened supplier settlement pace, broker handoff funding, shipment acceleration, release expansion, and customer-facing confidence language. | Keep only the narrow movement already supported by matched source records. | Freeze and refresh executable-check board. |
| What can continue? | Controlled commercial review, narrow broker handoff if still supported, packet proof retention, and owner follow-up. | Continue only where release, funding, packet, and risk records agree. | Downgrade to controlled hold. |
| What must be refreshed first? | Cash forecast, credit posture, executable-check, funding, release, document control, scenario, and risk records. | Refresh source layers before any outward or cash movement. | Treat the scenario as active founder escalation. |
| What proves recovery? | Collection path, live-gate owner path, evidence state, closeout proof, and archive readiness are all route-backed. | Return to standard posture only after proof is recoverable. | Keep scenario open. |

## Owner Path and Command Cadence

| Stakeholder | Decision Duty | Timing Standard | Evidence Route |
| --- | --- | --- | --- |
| Founder office | Decide freeze, hold, retry, downgrade, or return-to-standard posture. | Same day on trigger activation. | `06_dashboard/13_founder-decisions/Executive-Decision-Board.md` |
| Finance owner | Reconcile cash forecast, funding basis, payment timing, and collection action. | Same day for cash trigger; within 24 hours for reset. | `06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.md` |
| Operations owner | Confirm live gate, broker handoff, packet proof, supplier response, and next safe movement. | Same day before movement. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` |
| Commercial owner | Reset customer message, response expectation, and commitment language. | Within 24 hours. | `02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/README.md` |
| Compliance owner | Keep filing, traceability, packet, and challenge-defense confidence bounded. | Within 24 hours. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |

## Visual Preview Stack

| Preview | Route | Founder Use |
| --- | --- | --- |
| Executive scenario and contingency review | `00_brand/03_exports/02_preview-docs/executive-scenario-contingency-review-preview.html` | Review the scenario matrix and contingency posture visually. |
| Trust override executable check board | `00_brand/03_exports/02_preview-docs/trust-override-executable-check-board-preview.html` | Confirm live-gate ownership, cutoff, evidence state, and containment answer. |
| Funding and payables release review | `00_brand/03_exports/02_preview-docs/funding-payables-release-review-preview.html` | Confirm outgoing cash is sequenced behind proof. |
| Pre-shipment release review | `00_brand/03_exports/02_preview-docs/pre-shipment-release-review-preview.html` | Confirm broker handoff and movement posture remain narrow or frozen as needed. |

## Founder Decision Matrix

| Decision Question | Required Reading | Greenlight Condition | Current Answer |
| --- | --- | --- | --- |
| Is cash-stress response active? | Cash forecast, credit controls, deal room, scenario dashboard. | Collection slip or release/cash conflict is confirmed. | Prepared, trigger-dependent. |
| Is live-gate failure response active? | Executable-check, funding, release, matter control, risk register. | Any payment or movement needs widening without current proof ownership. | Active containment path. |
| Can movement continue narrowly? | Release gate, funding record, document control, shipment room. | Source records match and no new confidence is implied. | Yes, if bounded by current proof. |
| Can payment widen? | Funding record, cash forecast, trust posture, executable-check. | Liquidity timing, trust posture, and live gate proof match. | Not without refreshed proof. |
| Can scenario close? | Founder decision board, executable-check source, shipment review, archive path. | Stop rule, next safe movement, owner path, and closure proof are recoverable. | Not final. |

## Escalation and Stop Rules

| Trigger | Immediate Action | Founder Consequence | Evidence Route |
| --- | --- | --- | --- |
| Cash-stress trigger activates and release pressure remains live. | Freeze discretionary release expansion and refresh cash, credit, and founder decision records. | Cash preservation outranks commercial acceleration. | `06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.md` |
| Trust-linked gate widens before executable-check proof is current. | Freeze widening and route through executable-check board and matter control. | Same-day founder escalation remains active. | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` |
| Funding, release, scenario, and risk records disagree. | Hold payment and movement until all records restate one answer. | No next safe movement is authorized. | `06_dashboard/18_executive-risk-register/Executive-Risk-Register.md` |
| Packet or filing readiness is used as substitute for release authority. | Revalidate document control and release gate. | Packet remains evidence, not permission. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` |
| Founder rescue becomes the only closure path. | Downgrade to controlled hold and assign owner-accountability review. | System readiness is not considered adequate. | `06_dashboard/35_system-adoption/Operating-System-Adoption-and-Readiness-Board.md` |

## End-of-Cycle Closeout

| Closeout Field | Current Answer | Required Before Scenario Closure |
| --- | --- | --- |
| Scenario state | Prepared and active as a containment reference for Atlantic Foods cash timing and live-gate failure. | Trigger status, owner path, stop rule, next safe movement, and closeout proof must be route-backed. |
| Founder posture | Pre-decide freeze and narrow movement logic before pressure arrives. | Founder attention should not remain the hidden fallback. |
| Primary blocker | First-48-hour logic and gate-containment proof need to stay synchronized across source records. | Executable-check, funding, release, matter control, scenario, risk, and founder decision records must agree. |
| Operational posture | Narrow movement may continue only if source records match. | Any divergence freezes widening. |
| Record standard | Source module now carries route-backed scenario scope, source stack, trigger map, first-48-hour response, stop rule, owner path, visual previews, founder decision matrix, escalation rules, and closeout logic. | Refresh when trigger status, cash posture, gate status, or owner path changes. |
