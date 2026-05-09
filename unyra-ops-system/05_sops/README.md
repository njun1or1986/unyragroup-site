# 05 SOPs

This layer is the controlled procedure library for the UNYRA operating system. It translates founder cadence, commercial progression, communication release, adoption discipline, and archive closeout into repeatable standards without replacing the live CRM, operations, compliance, dashboard, or archive records that own current decisions.

## SOP Control Posture

| Control Field | Current Standard | Founder Use |
| --- | --- | --- |
| Layer status | Active operating-standard library | Use this hub when the founder needs the rule behind a workflow, not the live status of a matter. |
| Primary purpose | Define how UNYRA should run cadence, transitions, communication, adoption, and closeout discipline. | Keeps procedures consistent while live rooms continue to own action. |
| Source rule | Source records, dashboards, and working rooms must be current before an SOP is used to approve behavior. | Prevents polished standards from masking stale execution evidence. |
| Template protection | SOPs may reference protected template standards but must not create working copies inside `01_templates/`. | Preserves approved master templates and keeps live work outside protected folders. |
| Founder decision rule | SOPs set behavior; founder decisions still land in the governed room, board, shipment, claim, task, or archive record. | Avoids turning the SOP layer into a shadow operating log. |

## Open First

| Priority | SOP | Founder Use |
| --- | --- | --- |
| Cadence standard | `06_dashboard/Founder-Operating-Cadence-SOP.md` | Set the daily, weekly, monthly, and quarterly operating rhythm. |
| Adoption standard | `06_dashboard/Operating-System-Rollout-and-Adoption-SOP.md` | Control system rollout, adoption discipline, and review-layer upkeep. |
| Commercial lifecycle | `04_crm/Commercial-Execution-Lifecycle-SOP.md` | Govern lead, customer, supplier, deal, and won-deal-to-execution transitions. |
| External communication | `08_external-communications/Counterparty-Communication-Standard-SOP.md` | Control institutional outbound language, response discipline, and release readiness. |
| Archive closeout | `07_archive/Archive-Closeout-SOP.md` | Decide when a matter is complete enough to leave the active layer. |

## SOP Lanes

| Lane | Standard Owned | Live Evidence Layer |
| --- | --- | --- |
| Dashboard cadence | Founder rhythm, adoption discipline, monthly review behavior, and control-layer upkeep. | `06_dashboard/README.md` |
| CRM progression | Lead qualification, customer readiness, supplier use, deal movement, and commercial execution handoff. | `02_crm/README.md` |
| Operations release | Shipment gates, release proof, document control, payment release, and post-shipment review behavior. | `03_operations/README.md` |
| Compliance proof | Inspection, traceability, supplier approval, CAPA, recovery, and regulatory readiness standards. | `04_compliance/README.md` |
| External communication | Counterparty language, institutional tone, controlled sends, escalation, and response discipline. | `06_dashboard/36_external-communications/Counterparty-Communication-Control-Board.md` |
| Archive closeout | Evidence sufficiency, closure permission, retention discipline, and archive movement. | `07_archive/README.md` |

## Founder Routing Rules

| Founder Question | Open the SOP When | Open the Live Record When |
| --- | --- | --- |
| What is the rule? | The founder needs the approved standard, cadence, or behavior pattern. | The founder needs current status, owner, deadline, or evidence. |
| Can this move forward? | The founder needs to confirm the required procedure before approving movement. | The founder needs the room, board, shipment, claim, or task that owns the decision. |
| Is the team using the system correctly? | The founder needs the adoption or cadence standard. | The founder needs the adoption board, control routing matrix, owner board, or executable-check board. |
| Can communication go out? | The founder needs tone, structure, or release requirements. | The founder needs the communication control board or the counterparty room tied to the send. |
| Can this be archived? | The founder needs closeout criteria. | The founder needs the archive record and the source matter being closed. |

## Adoption Control Stack

| Control Surface | Route | SOP Relationship |
| --- | --- | --- |
| Adoption board | `06_dashboard/35_system-adoption/Operating-System-Adoption-and-Readiness-Board.md` | Tests whether the SOP library is becoming operating habit rather than shelfware. |
| Control routing matrix | `06_dashboard/33_control-routing/Founder-Control-Routing-Matrix.md` | Decides which live layer owns the next action when the SOP points to multiple surfaces. |
| Control integrity review | `06_dashboard/34_control-integrity/Executive-Control-Integrity-and-Decision-Readiness-Review.md` | Confirms linked records are current before a founder decision relies on a procedure. |
| Executable-check board | `06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.md` | Prevents release, payment, movement, or trust overrides from bypassing live gate proof. |
| Owner accountability board | `06_dashboard/28_owner-accountability/Executive-Owner-Accountability-and-Follow-Through-Review.md` | Keeps SOP-driven actions attached to accountable owners and dated follow-through. |
| Working files room | `03_operations/05_working-files/README.md` | Keeps drafts, exports, and working copies outside protected template folders. |

## Change Protection Standard

| Change Type | Required Handling | Founder Risk Prevented |
| --- | --- | --- |
| Procedure wording cleanup | Update the SOP only when the behavior standard remains unchanged. | Avoids unnecessary control churn for copy polish. |
| Procedure behavior change | Update the governed source record, affected live board, and SOP route together. | Prevents rule changes from drifting away from operating evidence. |
| Template-linked change | Preserve approved master templates and route live copies outside `01_templates/`. | Protects founder-approved template assets from contamination. |
| Dashboard-linked change | Refresh source rooms before changing the dashboard interpretation. | Keeps visual polish from outrunning real operating proof. |
| Communication-linked change | Reconcile the communication SOP with the communication control board and active counterparty room. | Prevents polished language from being sent before release controls are satisfied. |
| Archive-linked change | Confirm closeout proof before moving a matter into retained history. | Prevents archive from becoming a hiding place for unresolved work. |

## Founder Review Cadence

| Cadence | Review Move | Closeout Standard |
| --- | --- | --- |
| Daily | Use the cadence SOP and task queue to confirm the day’s live decision surfaces. | The founder can see what needs approval, action, or escalation without searching chats. |
| Weekly | Check CRM, operations, compliance, and communication standards against active rooms. | Live work is still following the correct procedure before movement widens. |
| Monthly | Open the adoption board and control routing matrix before declaring system maturity. | Adoption is proven by pre-decision use, not by polished documents alone. |
| Quarterly | Reconcile SOPs against dashboard, archive, and template-protection behavior. | Standards remain current without weakening protected assets or source ownership. |

## Operating Guardrails

| Guardrail | Required Behavior | Escalation Trigger |
| --- | --- | --- |
| SOPs are standards, not status logs | Keep live status in the owning room or board. | Any SOP starts carrying current owner, deadline, or live exception details. |
| Live records own action | Use SOPs to confirm procedure, then return to the active room for execution. | A team member treats an SOP as approval to skip the governed source record. |
| Founder approval needs evidence | Route approvals through the correct decision, release, integrity, or executable-check layer. | An approval is requested from chat, memory, or a polished SOP alone. |
| Protected templates remain protected | Keep working copies and drafts outside `01_templates/`. | Any live draft, customer packet, or supplier document appears in a template folder. |
| Archive requires proof | Archive only after closeout criteria and retained evidence are visible. | A matter is moved out of active view while CAPA, recovery, payment, or founder follow-up remains open. |
