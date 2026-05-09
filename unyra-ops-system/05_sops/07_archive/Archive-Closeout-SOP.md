# Archive Closeout SOP

| SOP control | Current standard |
| --- | --- |
| Status | ACTIVE SOP |
| Purpose | Define when a matter is truly ready for archive, how to preserve cross-functional evidence, and how to avoid archiving work that still carries commercial, operational, financial, or compliance risk. |
| Source rule | Review the live matter folder, closeout record, linked deal, shipment, customer, supplier, compliance, payment, dashboard, executable-check, and founder-decision records before archive release. |
| Decision rule | Do not archive a matter while any commercial, operational, financial, compliance, claim, release, funding, or retrieval answer can still change. |
| Template protection | Use the approved closeout/archive master record when required; do not edit protected template masters during archive cleanup. |

Use this SOP when deciding the following archive questions.

| Decision question | Required answer |
| --- | --- |
| Whether a matter is ready for archive | Confirm every live risk, obligation, and evidence requirement has a closed answer. |
| What final records must be preserved | Preserve the closeout record, final versions, evidence path, approvals, and retrieval owner. |
| How to split archived material by function | Store the long-term reference copy in the owning archive lane while preserving cross-functional linkage. |
| Who must approve archive release | Assign approval to the function carrying the main residual business risk, with founder review when the matter is material. |

## 1. Core Rule

Archive is a controlled release, not a cleanup shortcut.

| Core rule | Required behavior |
| --- | --- |
| Live risk stays active | If a matter still carries live business risk, it stays in its live source folder. |
| Archive requires evidence | The archive decision should be supported by source records, closeout evidence, owner approval, and retrieval clarity. |
| Linkage survives movement | Archive movement must not break the relationship between deal, shipment, customer, supplier, compliance, payment, and decision records. |

## 2. Minimum Archive Readiness Test

All applicable conditions below should be true before archive release.

| Readiness condition | Required closeout answer |
| --- | --- |
| Commercial execution | Commercial execution is complete or explicitly closed with a final outcome. |
| Shipment posture | Shipment is delivered, cancelled, or otherwise fully closed with evidence. |
| Collections | Collections are settled or clearly documented as resolved. |
| Compliance | Compliance filings, approvals, traceability, and evidence are closed. |
| Quality or CAPA | Complaints, CAPA, or inspection actions are closed. |
| Open task risk | No open task remains that could change the commercial, operational, financial, or regulatory outcome. |
| Executable-check closure | No open executable check remains if a trust-linked override or live release gate was used. |

If any condition is not true, the matter should remain in the live source folder.

## 3. Required Closeout Record

Use `01_templates/08_closeout/Closeout-and-Archive-Record-MASTER.md` for any matter that crosses more than one function or has meaningful business value.

The closeout record should identify the following fields.

| Closeout field | Required answer |
| --- | --- |
| Source live folder | The exact live folder the matter is leaving. |
| Primary archive destination | The archive lane that will carry the long-term reference copy. |
| Linked operating records | Deal, shipment, customer, supplier, compliance, payment, and dashboard references as applicable. |
| Executable-check references | Linked executable-check records if a trust-linked override or live release gate was used. |
| Final version list | The final controlled documents and versions included in the archive set. |
| Residual risk | Any open watch item, retrieval condition, or future reference constraint that remains after closure. |
| Release owner and archive approver | The person releasing the record and the person approving archive readiness. |

## 4. Archive Split by Function

Archive by the function that owns the final long-term reference copy.

| Function | Archive destination | Use when |
| --- | --- | --- |
| Brand | `07_archive/01_brand/` | Historical brand material is superseded and retained for reference. |
| Templates | `07_archive/02_templates/` | Template versions are superseded and no longer active. |
| CRM | `07_archive/03_crm/` | Completed deals, closed customer/supplier relationship records, or inactive commercial matters need long-term reference. |
| Operations | `07_archive/04_operations/` | Completed purchasing, shipment, logistics, or execution records need long-term reference. |
| Compliance | `07_archive/05_compliance/` | Closed regulatory, traceability, approval, inspection, complaint, or CAPA records need long-term reference. |
| SOPs | `07_archive/06_sops/` | Operating procedures are superseded and should no longer guide live execution. |
| Dashboards | `07_archive/07_dashboards/` | Historical dashboard cycles are closed and retained as evidence. |

If a matter spans multiple functions, keep one closeout record that points to the full archived record set.

## 5. What Must Not Be Archived

Do not archive any matter with one of these live conditions.

| Live condition | Why it blocks archive |
| --- | --- |
| Active deals | Commercial posture can still change. |
| In-transit shipments | Movement, delivery, claims, or document status can still change. |
| Open collections issues without documented resolution | Financial outcome is not yet closed. |
| Active supplier approvals | Sourcing authority is still pending. |
| Open compliance filings | Regulatory or evidence posture is not yet auditable. |
| Open complaint, incident, or CAPA cases | Quality, customer, or recurrence risk is still live. |
| Draft records still waiting for approval | The controlled version is not final. |

## 6. Naming and Linkage Standard

Archive folders should remain explicit and founder-readable.

| Matter type | Preferred pattern | Linkage requirement |
| --- | --- | --- |
| Deal | `DEAL-YYYY-###_Customer_Product-CLOSED` | Preserve customer, supplier, contract, payment, and outcome-review references. |
| Shipment | `SHIP-YYYY-###_Origin-to-Destination-CLOSED` | Preserve shipment, packet, filing, release, and review-log references. |
| Complaint or incident | `COMP-YYYY-###_Customer-Issue-CLOSED` | Preserve customer, shipment, lot, supplier, response, CAPA, and closure references. |

Each archive folder should preserve the original matter references instead of renaming them into something generic.

## 7. Approval Rule

Archive release should be approved by the owner of the function carrying the main business risk.

| Approval scenario | Required approver |
| --- | --- |
| Completed deal | Commercial owner. |
| Completed shipment | Operations lead. |
| Completed regulatory or quality matter | Compliance lead. |
| Cross-functional or strategically material matter | Function owner plus founder review when the matter could affect relationship, audit, finance, or future operating decisions. |

Founder review is recommended for the following triggers.

| Founder-review trigger | Reason |
| --- | --- |
| Strategically important transaction | The archive may become future relationship or planning evidence. |
| Material financial value | The record may affect finance, margin, collections, or capital-allocation review. |
| Complaint, dispute, or compliance escalation | The record may be needed for defense, prevention, or audit posture. |
| Fast retrieval need | The archive set may need to be recovered quickly for relationship, financing, audit, or operational reasons. |

## 8. Retrieval Standard

Archived material should remain easy to recover.

At minimum, each archived matter should preserve the following retrieval fields.

| Retrieval field | Required answer |
| --- | --- |
| Matter outcome | What happened and why the matter closed. |
| Final records | What final records exist. |
| Executable-gate closure | How the executable gate was closed if applicable. |
| Record location | Where those records live after archive release. |
| Retrieval owner | Who owns retrieval if the archive must be reopened for reference. |

If retrieval would require searching multiple folders blindly, the archive is not ready.
