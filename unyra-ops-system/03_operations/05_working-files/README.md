# Working Files

This controlled staging lane is the temporary evidence intake surface for support files that have not yet earned permanent custody inside a deal room, shipment room, compliance case, dashboard board, or archive record. It exists to prevent loose drafts, trackers, spreadsheets, packet fragments, and proof attachments from becoming hidden source-of-truth material.

## Staging Control

| Field | Current Standard |
| --- | --- |
| Lane purpose | Temporary custody for live support files while ownership, destination, and proof value are still being confirmed. |
| Permanent custody | Not permitted in this lane. |
| Review owner | Operations owner with CRM, compliance, finance, or archive owner support when evidence crosses functions. |
| Review cadence | Every operations cycle and before shipment, release, funding, archive, or compliance status improves. |
| Closeout condition | Every settled file is routed to a governed room or explicitly retained as temporary with owner, reason, and next review date. |
| Founder risk | Hidden custody can make later release, archive, challenge-defense, or founder review depend on memory instead of retrievable proof. |

## Source Refresh Stack

| Source | Route | Use |
| --- | --- | --- |
| Operations command center | `06_dashboard/03_operations/Daily-Operations-Command-Center.md` | Shows working-files cleanup watch, same-cycle routing expectations, and operating owner follow-through. |
| Operations hub | `03_operations/README.md` | Confirms working files are temporary support files, not a permanent operating lane. |
| Active shipment lane | `03_operations/03_shipments/active/README.md` | Routes staged proof that affects shipment movement, release, funding, packet, or closeout posture. |
| Document control record | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` | Receives export packet, broker packet, traceability packet, and document-spine proof once evidence is settled. |
| Shipment review record | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` | Receives movement, gate, and closeout evidence that must be recoverable after the live shipment changes. |
| Compliance lane | `04_compliance/README.md` | Receives staged proof tied to traceability, claim, CAPA, supplier approval, inspection, or regulator readiness. |
| CRM lane | `02_crm/README.md` | Receives staged proof tied to customer, supplier, deal, task, account, or commercial ownership. |
| Archive lane | `07_archive/README.md` | Receives final retained records only after active ownership and proof linkage are complete. |

## Intake Classification

| File Type | Temporary Use | Required Destination Once Settled |
| --- | --- | --- |
| Shipment packet attachment | Hold briefly while document owner confirms whether it affects packet, release, funding, or shipment review. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` or `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` |
| Release or funding support | Hold only while the live gate answer is still being matched to owner action. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/README.md` or `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/README.md` |
| Supplier or counterparty correspondence | Hold only while the communication owner confirms whether it is formal, working, or superseded. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.md`, CRM communication room, or external communications board. |
| Traceability, claim, or compliance evidence | Hold only while the compliance owner confirms the right case or proof room. | `04_compliance/04_traceability/TRACE-2026-001_GoldenHarvest-Garlic-LotPath/README.md` or the relevant compliance case. |
| Temporary tracker or spreadsheet | Hold while the operating owner is still using it to resolve a live gate. | Dashboard board, task room, shipment room, CRM room, or archive record once it affects a decision. |
| Final closeout file | Working Files should not retain it. | `07_archive/README.md` only after archive readiness and retrieval clarity are confirmed. |

## Custody Decision Gate

| Question | If Yes | If No |
| --- | --- | --- |
| Does the file affect shipment movement, release, funding, broker handoff, or packet proof? | Route to active shipment, document control, release, funding, or shipment review before status improves. | Continue classification. |
| Does the file affect traceability, CAPA, supplier approval, claim recovery, inspection, or regulator readiness? | Route to compliance proof room or case record before confidence language widens. | Continue classification. |
| Does the file affect customer, supplier, deal, task, account, or commercial follow-through? | Route to CRM source room or dashboard board before founder review. | Continue classification. |
| Is the file final, signed, approved, or relied on as proof? | Remove from Working Files and place in governed custody. | Keep temporary only with owner and review date. |
| Is the destination unknown after one operations cycle? | Escalate as a staging exception. | Leave only if owner, reason, and next review are explicit. |

## Founder Reading Order

| Step | Open | Founder Question Answered |
| --- | --- | --- |
| 1 | `OPEN-HERE.html` | What is allowed to sit in temporary custody, and what must move before closeout? |
| 2 | `06_dashboard/03_operations/Daily-Operations-Command-Center.html` | Which working-files cleanup items are scheduled, watched, or blocking operating confidence? |
| 3 | `03_operations/03_shipments/active/OPEN-HERE.html` | Does any staged evidence belong to shipment packet, release, funding, or review proof? |
| 4 | `04_compliance/OPEN-HERE.html` | Does staged evidence affect traceability, CAPA, supplier approval, inspection, or regulator readiness? |
| 5 | `02_crm/OPEN-HERE.html` | Does staged evidence affect a customer, supplier, deal, task, or account record? |
| 6 | `07_archive/OPEN-HERE.html` | Is the file ready for retained archive custody rather than temporary staging? |

## Routing Matrix

| Trigger | Destination | Reason |
| --- | --- | --- |
| File changes same-day operating control. | `06_dashboard/03_operations/Daily-Operations-Command-Center.md` | Founder should see the operational consequence before status improves. |
| File changes shipment proof or closeout posture. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/README.md` | Shipment review needs retrievable evidence, not after-the-fact reconstruction. |
| File changes document packet integrity. | `03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/README.md` | Document control is the packet spine once evidence is settled. |
| File changes compliance confidence. | `04_compliance/README.md` | Compliance proof should not sit in operational staging once the case route is known. |
| File changes commercial ownership. | `02_crm/README.md` | Customer, supplier, deal, and task records must carry their own source proof. |
| File becomes final retained evidence. | `07_archive/README.md` | Archive release requires finality, retrieval clarity, and inactive ownership. |

## Exception Control

| Exception | Immediate Handling | Founder Protection |
| --- | --- | --- |
| Settled evidence remains in Working Files after destination is known. | Move to governed custody before closeout language improves. | Prevents hidden source of truth. |
| A file supports release, funding, or broker handoff but is not linked to a shipment record. | Hold movement and route through document control, release, funding, or shipment review. | Prevents live movement from outrunning proof. |
| Compliance proof is staged without case ownership. | Assign compliance owner and route to traceability, CAPA, inspection, supplier approval, or claim record. | Prevents audit or challenge-defense confidence from widening around loose evidence. |
| A temporary tracker is reused for founder decisions. | Convert the decision-relevant content into a dashboard, CRM, operations, or compliance record. | Keeps founder review durable and source-backed. |
| File destination is unclear after one cycle. | Escalate through operations command center. | Avoids quiet drift. |

## Visual Preview Stack

| Preview | Route | Founder Use |
| --- | --- | --- |
| Operations command center | `00_brand/03_exports/02_preview-docs/operations-command-center-preview.html` | Reviews cleanup watch, owner action, and same-cycle routing. |
| Document control register | `00_brand/03_exports/02_preview-docs/document-control-register-preview.html` | Confirms packet and proof materials belong in controlled document custody. |
| Shipment control tower | `00_brand/03_exports/02_preview-docs/shipment-control-tower-preview.html` | Checks whether staged files affect shipment movement or release posture. |
| Shipment review log | `00_brand/03_exports/02_preview-docs/shipment-review-log-preview.html` | Confirms movement and closeout proof should become review evidence. |
| Compliance control center | `00_brand/03_exports/02_preview-docs/compliance-control-center-preview.html` | Checks whether staged files affect traceability, supplier approval, CAPA, or inspection posture. |
| Archive closeout record | `00_brand/03_exports/02_preview-docs/archive-closeout-record-preview.html` | Confirms final records should leave temporary custody only after archive readiness. |

## End-of-Cycle Closeout

| Closeout Item | Standard |
| --- | --- |
| Lane status | Working Files remains a temporary staging lane, not an archive, source of truth, or permanent custody layer. |
| Founder posture | Do not allow settled proof to remain here once owner, destination, or archive status is known. |
| Next refresh | Review during each operations cycle and before shipment, release, funding, compliance, or archive status improves. |
