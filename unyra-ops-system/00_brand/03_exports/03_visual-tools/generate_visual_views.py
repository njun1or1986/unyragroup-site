#!/usr/bin/env python3

from __future__ import annotations

import html
import math
import re
from datetime import datetime
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[3]
CSS_PATH = REPO_ROOT / "00_brand/03_exports/01_visual-standard/unyra-premium-docs.css"
LOCKUP_PATH = REPO_ROOT / "00_brand/01_assets/05_approved-compositions/unyra-logo-horizontal-approved-v1.png"
SEAL_PATH = REPO_ROOT / "00_brand/01_assets/05_approved-compositions/unyra-seal-full-approved.png"
PREVIEW_HUB_PATH = REPO_ROOT / "00_brand/03_exports/02_preview-docs/index.html"
BRAND_RELATIVE = "00_brand"
BRAND_ASSETS_RELATIVE = "00_brand/01_assets"
BRAND_GUIDELINES_RELATIVE = "00_brand/02_guidelines"
EXPORTS_RELATIVE = "00_brand/03_exports"
PREVIEW_DOCS_RELATIVE = "00_brand/03_exports/02_preview-docs"
VISUAL_STANDARD_RELATIVE = "00_brand/03_exports/01_visual-standard"
CRM_RELATIVE = "02_crm"
LEADS_RELATIVE = "02_crm/01_leads"
LEAD_ROOM_RELATIVE = f"{LEADS_RELATIVE}/LEAD-2026-001_CrescentMarket-Wholesale"
CUSTOMERS_RELATIVE = "02_crm/02_customers"
SUPPLIERS_RELATIVE = "02_crm/03_suppliers"
SUPPLIER_ROOM_RELATIVE = f"{SUPPLIERS_RELATIVE}/SUP-2026-001_GoldenHarvest-Produce"
DEALS_RELATIVE = "02_crm/04_deals"
ACTIVE_DEALS_RELATIVE = "02_crm/04_deals/active"
ACTIVE_DEAL_ROOM_RELATIVE = "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic"
WON_DEALS_RELATIVE = f"{DEALS_RELATIVE}/won"
LOST_DEALS_RELATIVE = f"{DEALS_RELATIVE}/lost"
WON_DEAL_ROOM_RELATIVE = f"{WON_DEALS_RELATIVE}/DEAL-2026-003_HarborFresh_Garlic"
LOST_DEAL_ROOM_RELATIVE = f"{LOST_DEALS_RELATIVE}/DEAL-2026-002_CrescentMarket_Ginger"
WON_DEAL_TRADE_REVIEW_RELATIVE = f"{WON_DEAL_ROOM_RELATIVE}/PROFIT-2026-001_HarborFresh-Garlic-Trade-Review"
TASKS_RELATIVE = "02_crm/05_tasks"
TASK_ROOM_RELATIVE = f"{TASKS_RELATIVE}/TASK-2026-001_Founder-Execution-Queue"
ACCOUNT_ROOM_RELATIVE = "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution"
CUSTOMER_ACCOUNT_BOARD_RELATIVE = "06_dashboard/08_customer-accounts/Customer-Account-Review-Board.html"
SALES_PIPELINE_BOARD_RELATIVE = "06_dashboard/02_sales-pipeline/Daily-Sales-Pipeline-Command-Center.html"
OPERATIONS_RELATIVE = "03_operations"
SHIPMENTS_RELATIVE = "03_operations/03_shipments"
ACTIVE_SHIPMENTS_RELATIVE = "03_operations/03_shipments/active"
ACTIVE_SHIPMENT_ROOM_RELATIVE = "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA"
SHIPMENT_CONTROL_TOWER_RELATIVE = "06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html"
WORKING_FILES_RELATIVE = "03_operations/05_working-files"
COMPLIANCE_RELATIVE = "04_compliance"
TRACEABILITY_RELATIVE = "04_compliance/04_traceability"
TRACEABILITY_ROOM_RELATIVE = f"{TRACEABILITY_RELATIVE}/TRACE-2026-001_GoldenHarvest-Garlic-LotPath"
INSPECTIONS_RELATIVE = "04_compliance/05_inspections"
CLAIM_ROOM_RELATIVE = "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim"
CLAIMS_RECOVERY_BOARD_RELATIVE = "06_dashboard/30_claims-recovery/Claims-Credits-and-Recovery-Review.html"
FDA_READINESS_ROOM_RELATIVE = "04_compliance/05_inspections/INSP-2026-001_FDA-Readiness-Review"
COMPLIANCE_CONTROL_CENTER_RELATIVE = "06_dashboard/04_compliance/Daily-Compliance-Control-Center.html"
SUPPLIER_APPROVAL_RELATIVE = "04_compliance/06_supplier-approval"
SUPPLIER_APPROVAL_ROOM_RELATIVE = "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce"
SUPPLIER_PERFORMANCE_BOARD_RELATIVE = "06_dashboard/07_supplier-performance/Supplier-Performance-Review-Board.html"
SUPPLY_RESILIENCE_BOARD_RELATIVE = "06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.html"
RESPONSE_ESCALATION_BOARD_RELATIVE = "06_dashboard/37_response-escalation/Counterparty-Response-SLA-and-Escalation-Board.html"
EXECUTABLE_CHECKS_BOARD_RELATIVE = "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html"
OWNER_ACCOUNTABILITY_BOARD_RELATIVE = "06_dashboard/28_owner-accountability/Executive-Owner-Accountability-and-Follow-Through-Review.html"
ARCHIVE_RELATIVE = "07_archive"
ARCHIVED_CRM_RELATIVE = "07_archive/03_crm"
ARCHIVED_CLOSED_DEAL_RELATIVE = f"{ARCHIVED_CRM_RELATIVE}/DEAL-2026-001_AtlanticFoods_Garlic-CLOSED"
ROOT_INDEX_PATH = REPO_ROOT / "index.html"
ROOT_START_PATH = REPO_ROOT / "START-HERE.html"

SKIP_DIR_NAMES = {
    ".git",
    "__pycache__",
}

TOP_LEVEL_COPY = {
    "00_brand": "Brand assets, approved identity, visual standards, and exported presentation layers.",
    "01_templates": "Protected master templates for sales, logistics, compliance, legal, finance, and governance.",
    "02_crm": "Leads, customers, suppliers, deals, tasks, and commercial relationship records.",
    "03_operations": "Purchasing, live shipments, logistics coordination, packet control, and working files.",
    "04_compliance": "ISF, FSVP, Prior Notice, traceability, inspections, supplier controls, and CAPA paths.",
    "05_sops": "Written operating procedures that govern how records should move and be maintained.",
    "06_dashboard": "Founder and executive dashboards, command centers, reviews, and governance layers.",
    "07_archive": "Closed records, retained matter history, and governed archive storage.",
}

AREA_LABELS = {
    "00_brand": "Brand",
    "01_templates": "Templates",
    "02_crm": "CRM",
    "03_operations": "Operations",
    "04_compliance": "Compliance",
    "05_sops": "SOP",
    "06_dashboard": "Dashboard",
    "07_archive": "Archive",
}

GENERATED_MARKER = "<!-- Generated by generate_visual_views.py -->"
EMPTY_MARKDOWN_STATE_HTML = '<div class="empty-state">This file does not contain readable Markdown content yet.</div>'

BREADCRUMB_LABEL_OVERRIDES = {}


def relative_url(from_dir: Path, to_path: Path) -> str:
    return Path(
        Path(
            __import__("os").path.relpath(to_path, from_dir)
        )
    ).as_posix()


def room_has_brief(room_dir: Path) -> bool:
    return (room_dir / "README.md").exists()


def get_room_entry_href(from_dir: Path, room_dir: Path) -> str:
    if room_has_brief(room_dir):
        return relative_url(from_dir, room_dir / "README.html")
    return f"{relative_url(from_dir, room_dir / 'OPEN-HERE.html')}#founder-start-here"


def get_room_entry_label(room_dir: Path, brief_label: str, room_label: str) -> str:
    return brief_label if room_has_brief(room_dir) else room_label


def is_active_deal_room(directory: Path) -> bool:
    if directory == REPO_ROOT:
        return False
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == ACTIVE_DEAL_ROOM_RELATIVE
    except ValueError:
        return False


def get_active_deal_room_return_context(directory: Path) -> dict[str, str] | None:
    if not is_active_deal_room(directory):
        return None

    return {
        "room_view_href": relative_url(directory, directory / "OPEN-HERE.html"),
        "room_view_cta": "Open Room View",
        "brief_href": relative_url(directory, directory / "README.html"),
        "brief_cta": "Open Deal Brief",
        "lane_href": relative_url(directory, REPO_ROOT / ACTIVE_DEALS_RELATIVE / "OPEN-HERE.html"),
        "lane_cta": "Open Active Deals",
        "hub_href": relative_url(directory, REPO_ROOT / DEALS_RELATIVE / "OPEN-HERE.html"),
        "hub_cta": "Open Deals",
        "preview_href": relative_url(directory, PREVIEW_HUB_PATH),
        "preview_cta": "Open Preview Docs",
    }


def is_active_deal_room_module(directory: Path) -> bool:
    if directory == REPO_ROOT or directory.parent == REPO_ROOT:
        return False
    try:
        return directory.parent.relative_to(REPO_ROOT).as_posix() == ACTIVE_DEAL_ROOM_RELATIVE
    except ValueError:
        return False


def get_active_deal_module_context(directory: Path) -> dict[str, object] | None:
    if not is_active_deal_room_module(directory):
        return None

    parent = directory.parent
    current_profile = build_folder_card_profile(parent, directory) or {}
    room_profile = build_portal_hero_context(parent) or {}
    sequence_links = get_module_sequence_jump_links(directory) or {}
    path_context = get_module_room_path_context(parent, directory)
    room_stats = list(room_profile.get("stats", []))
    next_action = sequence_links.get("next_action")
    next_action_label = "Open Active Deals"
    next_action_href = relative_url(directory, REPO_ROOT / ACTIVE_DEALS_RELATIVE / "OPEN-HERE.html")
    if isinstance(next_action, tuple) and len(next_action) >= 2:
        next_action_label = str(next_action[0])
        next_action_href = str(next_action[1])

    return {
        "module_title": str(current_profile.get("title") or humanize_surface_name(directory.name)),
        "module_pill": str(current_profile.get("pill") or "Deal Module"),
        "module_portal_href": relative_url(directory, directory / "OPEN-HERE.html"),
        "module_memo_href": relative_url(directory, directory / "README.html"),
        "room_title": str(room_profile.get("title") or humanize_surface_name(parent.name)),
        "room_entry_label": get_room_entry_label(parent, "Open Deal Brief", "Open Deal Room"),
        "room_entry_href": get_room_entry_href(directory, parent),
        "room_portal_href": relative_url(directory, parent / "OPEN-HERE.html"),
        "room_path": str(path_context["pill"]) if path_context else "Support",
        "room_decision": str(room_stats[1][0]) if len(room_stats) > 1 else "Commit",
        "room_escalation": str(room_stats[2][0]) if len(room_stats) > 2 else "Same-Day",
        "sequence_position": str(sequence_links.get("position_value") or "Live Step"),
        "next_action_label": next_action_label,
        "next_action_href": next_action_href,
        "next_pill": str(sequence_links.get("next_pill") or "Next Route"),
        "active_deals_href": relative_url(directory, REPO_ROOT / ACTIVE_DEALS_RELATIVE / "OPEN-HERE.html"),
        "deals_href": relative_url(directory, REPO_ROOT / DEALS_RELATIVE / "OPEN-HERE.html"),
    }


def is_active_shipment_room(directory: Path) -> bool:
    if directory == REPO_ROOT:
        return False
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == ACTIVE_SHIPMENT_ROOM_RELATIVE
    except ValueError:
        return False


def get_active_shipment_room_return_context(directory: Path) -> dict[str, str] | None:
    if not is_active_shipment_room(directory):
        return None

    return {
        "room_view_href": relative_url(directory, directory / "OPEN-HERE.html"),
        "room_view_cta": "Open Room View",
        "brief_href": relative_url(directory, directory / "README.html"),
        "brief_cta": "Open Shipment Brief",
        "lane_href": relative_url(directory, REPO_ROOT / ACTIVE_SHIPMENTS_RELATIVE / "OPEN-HERE.html"),
        "lane_cta": "Open Active Shipments",
        "hub_href": relative_url(directory, REPO_ROOT / SHIPMENTS_RELATIVE / "OPEN-HERE.html"),
        "hub_cta": "Open Shipments",
        "board_href": relative_url(directory, REPO_ROOT / SHIPMENT_CONTROL_TOWER_RELATIVE),
        "board_cta": "Open Shipment Control Tower",
    }


def is_active_shipment_room_module(directory: Path) -> bool:
    if directory == REPO_ROOT or directory.parent == REPO_ROOT:
        return False
    try:
        return directory.parent.relative_to(REPO_ROOT).as_posix() == ACTIVE_SHIPMENT_ROOM_RELATIVE
    except ValueError:
        return False


def get_active_shipment_module_context(directory: Path) -> dict[str, object] | None:
    if not is_active_shipment_room_module(directory):
        return None

    parent = directory.parent
    current_profile = build_folder_card_profile(parent, directory) or {}
    room_profile = build_portal_hero_context(parent) or {}
    sequence_links = get_module_sequence_jump_links(directory) or {}
    path_context = get_module_room_path_context(parent, directory)
    room_stats = list(room_profile.get("stats", []))
    next_action = sequence_links.get("next_action")
    next_action_label = "Open Active Shipments"
    next_action_href = relative_url(directory, REPO_ROOT / ACTIVE_SHIPMENTS_RELATIVE / "OPEN-HERE.html")
    if isinstance(next_action, tuple) and len(next_action) >= 2:
        next_action_label = str(next_action[0])
        next_action_href = str(next_action[1])

    return {
        "module_title": str(current_profile.get("title") or humanize_surface_name(directory.name)),
        "module_pill": str(current_profile.get("pill") or "Shipment Module"),
        "module_portal_href": relative_url(directory, directory / "OPEN-HERE.html"),
        "module_memo_href": relative_url(directory, directory / "README.html"),
        "room_title": str(room_profile.get("title") or humanize_surface_name(parent.name)),
        "room_entry_label": get_room_entry_label(parent, "Open Shipment Brief", "Open Shipment Room"),
        "room_entry_href": get_room_entry_href(directory, parent),
        "room_portal_href": relative_url(directory, parent / "OPEN-HERE.html"),
        "room_path": str(path_context["pill"]) if path_context else "Move",
        "room_decision": str(room_stats[1][0]) if len(room_stats) > 1 else "Move",
        "room_escalation": str(room_stats[2][0]) if len(room_stats) > 2 else "Same-Day",
        "sequence_position": str(sequence_links.get("position_value") or "Live Step"),
        "next_action_label": next_action_label,
        "next_action_href": next_action_href,
        "next_pill": str(sequence_links.get("next_pill") or "Next Route"),
        "active_shipments_href": relative_url(directory, REPO_ROOT / ACTIVE_SHIPMENTS_RELATIVE / "OPEN-HERE.html"),
        "shipments_href": relative_url(directory, REPO_ROOT / SHIPMENTS_RELATIVE / "OPEN-HERE.html"),
    }


def is_active_account_room(directory: Path) -> bool:
    if directory == REPO_ROOT:
        return False
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == ACCOUNT_ROOM_RELATIVE
    except ValueError:
        return False


def get_active_account_room_return_context(directory: Path) -> dict[str, str] | None:
    if not is_active_account_room(directory):
        return None

    return {
        "room_view_href": relative_url(directory, directory / "OPEN-HERE.html"),
        "room_view_cta": "Open Room View",
        "brief_href": relative_url(directory, directory / "README.html"),
        "brief_cta": "Open Account Brief",
        "lane_href": relative_url(directory, REPO_ROOT / CUSTOMERS_RELATIVE / "OPEN-HERE.html"),
        "lane_cta": "Open Customers",
        "hub_href": relative_url(directory, REPO_ROOT / "02_crm/OPEN-HERE.html"),
        "hub_cta": "Open CRM",
        "board_href": relative_url(directory, REPO_ROOT / CUSTOMER_ACCOUNT_BOARD_RELATIVE),
        "board_cta": "Open Customer Board",
    }


def is_active_account_room_module(directory: Path) -> bool:
    if directory == REPO_ROOT or directory.parent == REPO_ROOT:
        return False
    try:
        return directory.parent.relative_to(REPO_ROOT).as_posix() == ACCOUNT_ROOM_RELATIVE
    except ValueError:
        return False


def get_active_account_module_context(directory: Path) -> dict[str, object] | None:
    if not is_active_account_room_module(directory):
        return None

    parent = directory.parent
    current_profile = build_folder_card_profile(parent, directory) or {}
    room_profile = build_portal_hero_context(parent) or {}
    sequence_links = get_module_sequence_jump_links(directory) or {}
    path_context = get_module_room_path_context(parent, directory)
    room_stats = list(room_profile.get("stats", []))
    next_action = sequence_links.get("next_action")
    next_action_label = "Open Customers"
    next_action_href = relative_url(directory, REPO_ROOT / CUSTOMERS_RELATIVE / "OPEN-HERE.html")
    if isinstance(next_action, tuple) and len(next_action) >= 2:
        next_action_label = str(next_action[0])
        next_action_href = str(next_action[1])

    return {
        "module_title": str(current_profile.get("title") or humanize_surface_name(directory.name)),
        "module_pill": str(current_profile.get("pill") or "Account Module"),
        "module_portal_href": relative_url(directory, directory / "OPEN-HERE.html"),
        "module_memo_href": relative_url(directory, directory / "README.html"),
        "room_title": str(room_profile.get("title") or humanize_surface_name(parent.name)),
        "room_entry_label": get_room_entry_label(parent, "Open Account Brief", "Open Account Room"),
        "room_entry_href": get_room_entry_href(directory, parent),
        "room_portal_href": relative_url(directory, parent / "OPEN-HERE.html"),
        "room_path": str(path_context["pill"]) if path_context else "Hold",
        "room_decision": str(room_stats[1][0]) if len(room_stats) > 1 else "Hold",
        "room_escalation": str(room_stats[2][0]) if len(room_stats) > 2 else "Monthly",
        "sequence_position": str(sequence_links.get("position_value") or "Live Step"),
        "next_action_label": next_action_label,
        "next_action_href": next_action_href,
        "next_pill": str(sequence_links.get("next_pill") or "Next Route"),
        "customers_href": relative_url(directory, REPO_ROOT / CUSTOMERS_RELATIVE / "OPEN-HERE.html"),
        "crm_href": relative_url(directory, REPO_ROOT / "02_crm/OPEN-HERE.html"),
    }


def is_active_claim_room(directory: Path) -> bool:
    if directory == REPO_ROOT:
        return False
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == CLAIM_ROOM_RELATIVE
    except ValueError:
        return False


def get_active_claim_room_return_context(directory: Path) -> dict[str, str] | None:
    if not is_active_claim_room(directory):
        return None

    return {
        "room_view_href": relative_url(directory, directory / "OPEN-HERE.html"),
        "room_view_cta": "Open Room View",
        "brief_href": relative_url(directory, directory / "README.html"),
        "brief_cta": "Open Claim Brief",
        "lane_href": relative_url(directory, REPO_ROOT / INSPECTIONS_RELATIVE / "OPEN-HERE.html"),
        "lane_cta": "Open Inspection Cases",
        "hub_href": relative_url(directory, REPO_ROOT / "04_compliance/OPEN-HERE.html"),
        "hub_cta": "Open Compliance",
        "board_href": relative_url(directory, REPO_ROOT / CLAIMS_RECOVERY_BOARD_RELATIVE),
        "board_cta": "Open Claims Recovery",
    }


def is_active_claim_room_module(directory: Path) -> bool:
    if directory == REPO_ROOT or directory.parent == REPO_ROOT:
        return False
    try:
        return directory.parent.relative_to(REPO_ROOT).as_posix() == CLAIM_ROOM_RELATIVE
    except ValueError:
        return False


def get_active_claim_module_context(directory: Path) -> dict[str, object] | None:
    if not is_active_claim_room_module(directory):
        return None

    parent = directory.parent
    current_profile = build_folder_card_profile(parent, directory) or {}
    room_profile = build_portal_hero_context(parent) or {}
    sequence_links = get_module_sequence_jump_links(directory) or {}
    path_context = get_module_room_path_context(parent, directory)
    room_stats = list(room_profile.get("stats", []))
    next_action = sequence_links.get("next_action")
    next_action_label = "Open Inspection Cases"
    next_action_href = relative_url(directory, REPO_ROOT / INSPECTIONS_RELATIVE / "OPEN-HERE.html")
    if isinstance(next_action, tuple) and len(next_action) >= 2:
        next_action_label = str(next_action[0])
        next_action_href = str(next_action[1])

    return {
        "module_title": str(current_profile.get("title") or humanize_surface_name(directory.name)),
        "module_pill": str(current_profile.get("pill") or "Claim Module"),
        "module_portal_href": relative_url(directory, directory / "OPEN-HERE.html"),
        "module_memo_href": relative_url(directory, directory / "README.html"),
        "room_title": str(room_profile.get("title") or humanize_surface_name(parent.name)),
        "room_entry_label": get_room_entry_label(parent, "Open Claim Brief", "Open Claim Room"),
        "room_entry_href": get_room_entry_href(directory, parent),
        "room_portal_href": relative_url(directory, parent / "OPEN-HERE.html"),
        "room_path": str(path_context["pill"]) if path_context else "Contain",
        "room_decision": str(room_stats[1][0]) if len(room_stats) > 1 else "Recover",
        "room_escalation": str(room_stats[2][0]) if len(room_stats) > 2 else "Weekly",
        "sequence_position": str(sequence_links.get("position_value") or "Live Step"),
        "next_action_label": next_action_label,
        "next_action_href": next_action_href,
        "next_pill": str(sequence_links.get("next_pill") or "Next Route"),
        "inspection_cases_href": relative_url(directory, REPO_ROOT / INSPECTIONS_RELATIVE / "OPEN-HERE.html"),
        "compliance_href": relative_url(directory, REPO_ROOT / "04_compliance/OPEN-HERE.html"),
    }


def is_supplier_approval_room_module(directory: Path) -> bool:
    if directory == REPO_ROOT or directory.parent == REPO_ROOT:
        return False
    try:
        return directory.parent.relative_to(REPO_ROOT).as_posix() == SUPPLIER_APPROVAL_ROOM_RELATIVE
    except ValueError:
        return False


def get_supplier_approval_module_context(directory: Path) -> dict[str, object] | None:
    if not is_supplier_approval_room_module(directory):
        return None

    parent = directory.parent
    current_profile = build_folder_card_profile(parent, directory) or {}
    room_profile = build_portal_hero_context(parent) or {}
    module_relative = directory.relative_to(REPO_ROOT).as_posix()

    path_label = "Approval"
    sequence_position = "Track 01"
    next_action_label = "Open Resilience Module"
    next_action_href = relative_url(
        directory,
        parent / "CAPACITY-2026-Q2_GoldenHarvest-Backup-Sourcing-Review" / "OPEN-HERE.html",
    )
    next_pill = "Resilience Route"
    board_href = relative_url(directory, REPO_ROOT / SUPPLIER_PERFORMANCE_BOARD_RELATIVE)
    board_cta = "Open Supplier Performance Board"
    secondary_board_href = relative_url(directory, REPO_ROOT / SUPPLY_RESILIENCE_BOARD_RELATIVE)
    secondary_board_cta = "Open Supply Resilience Board"

    if module_relative.endswith("CAPACITY-2026-Q2_GoldenHarvest-Backup-Sourcing-Review"):
        path_label = "Resilience"
        sequence_position = "Track 02"
        next_action_label = "Open Supply Resilience Board"
        next_action_href = relative_url(directory, REPO_ROOT / SUPPLY_RESILIENCE_BOARD_RELATIVE)
        next_pill = "Board Route"
        board_href = relative_url(directory, REPO_ROOT / SUPPLY_RESILIENCE_BOARD_RELATIVE)
        board_cta = "Open Supply Resilience Board"
        secondary_board_href = relative_url(directory, REPO_ROOT / SUPPLIER_PERFORMANCE_BOARD_RELATIVE)
        secondary_board_cta = "Open Supplier Performance Board"

    return {
        "module_title": str(current_profile.get("title") or humanize_surface_name(directory.name)),
        "module_pill": str(current_profile.get("pill") or "Supplier Module"),
        "module_portal_href": relative_url(directory, directory / "OPEN-HERE.html"),
        "module_memo_href": relative_url(directory, directory / "README.html"),
        "room_title": str(room_profile.get("title") or humanize_surface_name(parent.name)),
        "room_entry_label": get_room_entry_label(parent, "Open Supplier Brief", "Open Supplier Room"),
        "room_entry_href": get_room_entry_href(directory, parent),
        "room_portal_href": relative_url(directory, parent / "OPEN-HERE.html"),
        "room_path": path_label,
        "room_decision": "Approve",
        "room_escalation": "Monthly",
        "sequence_position": sequence_position,
        "next_action_label": next_action_label,
        "next_action_href": next_action_href,
        "next_pill": next_pill,
        "supplier_approval_href": relative_url(directory, REPO_ROOT / SUPPLIER_APPROVAL_RELATIVE / "OPEN-HERE.html"),
        "compliance_href": relative_url(directory, REPO_ROOT / "04_compliance/OPEN-HERE.html"),
        "board_href": board_href,
        "board_cta": board_cta,
        "secondary_board_href": secondary_board_href,
        "secondary_board_cta": secondary_board_cta,
    }


def is_fda_readiness_room(directory: Path) -> bool:
    if directory == REPO_ROOT:
        return False
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == FDA_READINESS_ROOM_RELATIVE
    except ValueError:
        return False


def get_fda_readiness_room_return_context(directory: Path) -> dict[str, str] | None:
    if not is_fda_readiness_room(directory):
        return None

    return {
        "room_view_href": relative_url(directory, directory / "OPEN-HERE.html"),
        "room_view_cta": "Open Room View",
        "brief_href": relative_url(directory, directory / "README.html"),
        "brief_cta": "Open Readiness Brief",
        "lane_href": relative_url(directory, REPO_ROOT / INSPECTIONS_RELATIVE / "OPEN-HERE.html"),
        "lane_cta": "Open Inspection Cases",
        "hub_href": relative_url(directory, REPO_ROOT / "04_compliance/OPEN-HERE.html"),
        "hub_cta": "Open Compliance",
        "board_href": relative_url(directory, REPO_ROOT / COMPLIANCE_CONTROL_CENTER_RELATIVE),
        "board_cta": "Open Compliance Control",
    }


def is_supplier_approval_room(directory: Path) -> bool:
    if directory == REPO_ROOT:
        return False
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == SUPPLIER_APPROVAL_ROOM_RELATIVE
    except ValueError:
        return False


def get_supplier_approval_room_return_context(directory: Path) -> dict[str, str] | None:
    if not is_supplier_approval_room(directory):
        return None

    return {
        "room_view_href": relative_url(directory, directory / "OPEN-HERE.html"),
        "room_view_cta": "Open Room View",
        "brief_href": relative_url(directory, directory / "README.html"),
        "brief_cta": "Open Supplier Brief",
        "lane_href": relative_url(directory, REPO_ROOT / SUPPLIER_APPROVAL_RELATIVE / "OPEN-HERE.html"),
        "lane_cta": "Open Supplier Approval",
        "hub_href": relative_url(directory, REPO_ROOT / "04_compliance/OPEN-HERE.html"),
        "hub_cta": "Open Compliance",
        "board_href": relative_url(directory, REPO_ROOT / SUPPLIER_PERFORMANCE_BOARD_RELATIVE),
        "board_cta": "Open Supplier Performance Board",
        "resilience_href": relative_url(directory, REPO_ROOT / SUPPLY_RESILIENCE_BOARD_RELATIVE),
        "resilience_cta": "Open Supply Resilience Board",
    }


def humanize_slug(value: str) -> str:
    cleaned = value.replace("_", " ").replace("-", " ")
    cleaned = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", cleaned)
    cleaned = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    if not cleaned:
        return "UNYRA File"
    acronyms = {
        "crm": "CRM",
        "sop": "SOP",
        "sops": "SOPs",
        "isf": "ISF",
        "fsvp": "FSVP",
        "nda": "NDA",
        "kpi": "KPI",
        "capa": "CAPA",
        "po": "PO",
    }
    words = []
    for part in cleaned.split(" "):
        lowered = part.lower()
        if lowered in acronyms:
            words.append(acronyms[lowered])
        elif part.isupper() or any(ch.isdigit() for ch in part):
            words.append(part)
        else:
            words.append(part.capitalize())
    return " ".join(words)


def humanize_breadcrumb_label(value: str) -> str:
    if value in AREA_LABELS:
        return AREA_LABELS[value]
    override = BREADCRUMB_LABEL_OVERRIDES.get(value.lower())
    if override:
        return override
    stripped = re.sub(r"^\d+[_ -]*", "", value)
    if stripped and stripped != value:
        return humanize_slug(stripped)
    return humanize_slug(value)


def extract_record_suffix(value: str) -> str | None:
    match = re.match(r"^[A-Z]+(?:-[0-9A-Z]+)+_(.+)$", value)
    if match:
        return match.group(1)
    return None


def humanize_surface_name(value: str) -> str:
    suffix = extract_record_suffix(value)
    if suffix:
        return humanize_slug(suffix)
    return humanize_breadcrumb_label(value)


def get_profile_pill_label(pill: object) -> str:
    if isinstance(pill, (tuple, list)) and pill:
        return str(pill[0]).strip()
    return str(pill).strip()


def detect_kind(path: Path) -> str:
    if path.name == "AGENTS.md":
        return "System Rules"
    if path.name == "README.md":
        profile = build_doc_card_profile(path.parent, path)
        if profile and profile.get("kind"):
            return str(profile["kind"])
        return "Overview"
    if path.name.endswith("-MASTER.md"):
        return "Master Template"
    guideline_doc = get_brand_guideline_doc_context(path)
    if guideline_doc:
        return str(guideline_doc["kind"])
    area = AREA_LABELS.get(path.parts[len(REPO_ROOT.parts)], "Document")
    if path.parts[len(REPO_ROOT.parts)] == "05_sops":
        return "SOP"
    if path.parts[len(REPO_ROOT.parts)] == "06_dashboard":
        return "Dashboard"
    if path.parts[len(REPO_ROOT.parts)] == "02_crm":
        return "CRM Record"
    if path.parts[len(REPO_ROOT.parts)] == "03_operations":
        return "Operations Record"
    if path.parts[len(REPO_ROOT.parts)] == "04_compliance":
        return "Compliance Record"
    return area


def is_meta_line(text: str) -> bool:
    return bool(re.match(r"^[A-Za-z][A-Za-z0-9 /&()_-]{1,40}:\s+.+$", text))


def is_markdown_structure_line(text: str) -> bool:
    return bool(
        text.startswith("|")
        or text.startswith("```")
        or text == "---"
        or text.startswith(">")
        or re.match(r"^([-*+]\s+|\d+\.\s+)", text)
    )


def clean_markdown_summary(text: str) -> str:
    cleaned = re.sub(r"`([^`]+)`", r"\1", text)
    cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cleaned)
    cleaned = cleaned.replace("**", "").replace("__", "")
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" -")
    return cleaned


def clamp_summary(text: str, max_length: int = 260) -> str:
    if len(text) <= max_length:
        return text
    truncated = text[: max_length + 1].rsplit(" ", 1)[0].rstrip(" ,;:/-")
    return f"{truncated}..."


def split_chunks(items: list[tuple[str, str]], chunk_size: int) -> list[list[tuple[str, str]]]:
    if not items:
        return []
    return [items[index : index + chunk_size] for index in range(0, len(items), chunk_size)]


def format_count_label(count: int, singular: str, plural: str | None = None) -> str:
    plural = plural or f"{singular}s"
    return f"{count} {singular if count == 1 else plural}"


def count_label(count: int, singular: str, plural: str | None = None) -> str:
    return singular if count == 1 else (plural or f"{singular}s")


def meta_to_dict(meta: list[tuple[str, str]]) -> dict[str, str]:
    return {key: value for key, value in meta}


def is_preview_docs_directory(directory: Path) -> bool:
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == PREVIEW_DOCS_RELATIVE
    except ValueError:
        return False


def is_exports_directory(directory: Path) -> bool:
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == EXPORTS_RELATIVE
    except ValueError:
        return False


def is_brand_guidelines_directory(directory: Path) -> bool:
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == BRAND_GUIDELINES_RELATIVE
    except ValueError:
        return False


def is_brand_assets_directory(directory: Path) -> bool:
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == BRAND_ASSETS_RELATIVE
    except ValueError:
        return False


def is_templates_directory(directory: Path) -> bool:
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == "01_templates"
    except ValueError:
        return False


def is_sops_directory(directory: Path) -> bool:
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == "05_sops"
    except ValueError:
        return False


def is_crm_directory(directory: Path) -> bool:
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == CRM_RELATIVE
    except ValueError:
        return False


def is_operations_directory(directory: Path) -> bool:
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == OPERATIONS_RELATIVE
    except ValueError:
        return False


def is_compliance_directory(directory: Path) -> bool:
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == COMPLIANCE_RELATIVE
    except ValueError:
        return False


def is_dashboard_directory(directory: Path) -> bool:
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == "06_dashboard"
    except ValueError:
        return False


def is_dashboard_pack_directory(directory: Path) -> bool:
    try:
        relative = directory.relative_to(REPO_ROOT).as_posix()
        return relative.startswith("06_dashboard/") and len(relative.split("/")) == 2
    except ValueError:
        return False


def get_dashboard_pack_primary_doc(directory: Path) -> Path | None:
    if not is_dashboard_pack_directory(directory):
        return None
    markdowns = sorted(
        child
        for child in directory.iterdir()
        if child.is_file() and child.suffix.lower() == ".md" and child.name != "README.md"
    )
    return markdowns[0] if markdowns else None


def is_archive_directory(directory: Path) -> bool:
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == ARCHIVE_RELATIVE
    except ValueError:
        return False


def is_brand_directory(directory: Path) -> bool:
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == BRAND_RELATIVE
    except ValueError:
        return False


def is_visual_standard_directory(directory: Path) -> bool:
    try:
        return directory.relative_to(REPO_ROOT).as_posix() == VISUAL_STANDARD_RELATIVE
    except ValueError:
        return False


def count_preview_hub_cards(page_text: str, section_id: str, card_class: str) -> int:
    match = re.search(
        rf'<section class="home-section" id="{re.escape(section_id)}">(.*?)</section>',
        page_text,
        re.S,
    )
    if not match:
        return 0
    return len(re.findall(rf'<(?:article|a) class="{re.escape(card_class)}"', match.group(1)))


def get_preview_hub_metrics(directory: Path) -> dict[str, int]:
    if not is_preview_docs_directory(directory):
        return {"benchmark_count": 0, "pathway_count": 0, "domain_lane_count": 0, "brand_anchor_count": 0}

    benchmark_count = len(list(directory.glob("*-preview.html")))
    index_text = PREVIEW_HUB_PATH.read_text(encoding="utf-8") if PREVIEW_HUB_PATH.exists() else ""
    return {
        "benchmark_count": benchmark_count,
        "pathway_count": count_preview_hub_cards(index_text, "founder-pathways", "route-card"),
        "domain_lane_count": count_preview_hub_cards(index_text, "full-catalog", "route-card"),
        "brand_anchor_count": count_preview_hub_cards(index_text, "brand-anchors", "asset-card"),
    }


def get_exports_metrics(directory: Path) -> dict[str, int]:
    if not is_exports_directory(directory):
        return {"benchmark_count": 0, "domain_lane_count": 0, "reference_surface_count": 0}

    preview_metrics = get_preview_hub_metrics(directory / "02_preview-docs")
    reference_surface_count = sum(
        int((directory / relative_path / "OPEN-HERE.html").exists())
        for relative_path in ("01_visual-standard", "02_preview-docs")
    )
    return {
        "benchmark_count": preview_metrics["benchmark_count"],
        "domain_lane_count": preview_metrics["domain_lane_count"],
        "reference_surface_count": reference_surface_count,
    }


def get_brand_guidelines_metrics(directory: Path) -> dict[str, int]:
    if not is_brand_guidelines_directory(directory):
        return {"guidance_count": 0, "governance_surface_count": 0, "reference_layer_count": 0}

    guidance_count = sum(
        1
        for child in directory.iterdir()
        if child.is_file() and child.suffix.lower() == ".md" and child.name != "README.md"
    )
    governance_surface_count = int((REPO_ROOT / VISUAL_STANDARD_RELATIVE / "OPEN-HERE.html").exists())
    reference_layer_count = int((REPO_ROOT / EXPORTS_RELATIVE / "OPEN-HERE.html").exists())
    return {
        "guidance_count": guidance_count,
        "governance_surface_count": governance_surface_count,
        "reference_layer_count": reference_layer_count,
    }


def get_brand_guideline_doc_context(path: Path) -> dict[str, object] | None:
    current_dir = path.parent
    if not is_brand_guidelines_directory(current_dir):
        return None

    profiles: dict[str, dict[str, object]] = {
        "UNYRA-Visual-Identity.md": {
            "eyebrow": "Identity Standard",
            "focus_summary": "Palette / Style Rules / Asset Direction",
            "track_value": "Identity Rules",
            "reference_title": "Assets",
            "reference_href": "../01_assets/OPEN-HERE.html",
            "reference_cta": "Open Assets",
            "toolbar_routes": [
                ("Open Assets", "../01_assets/OPEN-HERE.html"),
                ("Open Visual Standard", "../03_exports/01_visual-standard/OPEN-HERE.html"),
            ],
            "closeout_eyebrow": "Identity Return",
            "closeout_title": "Close this standard on the routes that reconnect brand identity, approved assets, and governed document styling.",
            "closeout_copy": "This closing layer returns the founder to brand guidelines, assets, the premium document standard, or the visual standard instead of defaulting to generic source routing.",
            "closeout_state": "Identity / Assets / Standard",
            "closeout_routes": [
                {
                    "title": "Brand Guidelines",
                    "pill": "Guidance Hub",
                    "copy": "Return to the guidance hub when the founder needs the wider rule set behind identity, document design, and institutional voice.",
                    "cta": "Open Brand Guidelines",
                    "href": "OPEN-HERE.html",
                },
                {
                    "title": "Assets",
                    "pill": "Asset Hub",
                    "copy": "Move into assets when the next answer depends on approved logos, signatures, and protected compositions rather than written identity rules alone.",
                    "cta": "Open Assets",
                    "href": "../01_assets/OPEN-HERE.html",
                },
                {
                    "title": "Premium Document Standard",
                    "pill": "Sibling Standard",
                    "copy": "Open the premium document standard when the founder needs the execution rules that carry identity decisions into layouts, tables, and branded document control.",
                    "cta": "Open Document Standard",
                    "href": "UNYRA-Premium-Document-Standard.html",
                },
                {
                    "title": "Visual Standard",
                    "pill": "Governance Surface",
                    "copy": "Widen into the visual standard when the founder needs the governed styling system that turns identity rules into branded founder-facing surfaces.",
                    "cta": "Open Visual Standard",
                    "href": "../03_exports/01_visual-standard/OPEN-HERE.html",
                },
            ],
        },
        "UNYRA-Premium-Document-Standard.md": {
            "eyebrow": "Document Standard",
            "focus_summary": "Layout / Typography / Composition Control",
            "track_value": "Document Standard",
            "reference_title": "Approved Compositions",
            "reference_href": "../01_assets/05_approved-compositions/OPEN-HERE.html",
            "reference_cta": "Open Approved Compositions",
            "toolbar_routes": [
                ("Open Approved Compositions", "../01_assets/05_approved-compositions/OPEN-HERE.html"),
                ("Open Visual Standard", "../03_exports/01_visual-standard/OPEN-HERE.html"),
            ],
            "closeout_eyebrow": "Document Return",
            "closeout_title": "Close this standard on the routes that reconnect document design, approved compositions, and live visual governance.",
            "closeout_copy": "This closing layer returns the founder to brand guidelines, approved compositions, visual identity, or the visual standard instead of defaulting to generic source routing.",
            "closeout_state": "Layout / Assets / Standard",
            "closeout_routes": [
                {
                    "title": "Brand Guidelines",
                    "pill": "Guidance Hub",
                    "copy": "Return to the guidance hub when the founder needs the full rule set behind identity, document design, and institutional voice.",
                    "cta": "Open Brand Guidelines",
                    "href": "OPEN-HERE.html",
                },
                {
                    "title": "Approved Compositions",
                    "pill": "Asset Surface",
                    "copy": "Move into approved compositions when the next answer depends on lockups, seals, and protected layout assets rather than written document rules alone.",
                    "cta": "Open Approved Compositions",
                    "href": "../01_assets/05_approved-compositions/OPEN-HERE.html",
                },
                {
                    "title": "Visual Identity",
                    "pill": "Sibling Standard",
                    "copy": "Open visual identity when the founder needs the governing palette, spacing, and asset direction that sits underneath the document standard.",
                    "cta": "Open Visual Identity",
                    "href": "UNYRA-Visual-Identity.html",
                },
                {
                    "title": "Visual Standard",
                    "pill": "Governance Surface",
                    "copy": "Widen into the visual standard when the founder needs the exported founder-facing layer where this document standard becomes live review behavior.",
                    "cta": "Open Visual Standard",
                    "href": "../03_exports/01_visual-standard/OPEN-HERE.html",
                },
            ],
        },
        "UNYRA-Institutional-Communication-Style-Guide.md": {
            "eyebrow": "Communication Standard",
            "focus_summary": "Tone / Subject Lines / Formal Request Control",
            "track_value": "Voice Discipline",
            "reference_title": "Exports",
            "reference_href": "../03_exports/OPEN-HERE.html",
            "reference_cta": "Open Exports",
            "toolbar_routes": [
                ("Open Exports", "../03_exports/OPEN-HERE.html"),
                ("Open Visual Standard", "../03_exports/01_visual-standard/OPEN-HERE.html"),
            ],
            "closeout_eyebrow": "Communication Return",
            "closeout_title": "Close this standard on the routes that reconnect institutional voice, outbound execution, and governed document posture.",
            "closeout_copy": "This closing layer returns the founder to brand guidelines, exports, the premium document standard, or the visual standard instead of defaulting to generic source routing.",
            "closeout_state": "Voice / Outbound / Standard",
            "closeout_routes": [
                {
                    "title": "Brand Guidelines",
                    "pill": "Guidance Hub",
                    "copy": "Return to the guidance hub when the founder needs the wider rule set behind identity, document design, and institutional voice.",
                    "cta": "Open Brand Guidelines",
                    "href": "OPEN-HERE.html",
                },
                {
                    "title": "Exports",
                    "pill": "Outbound Surface",
                    "copy": "Move into exports when the next answer depends on outbound founder-facing documents, preview docs, and branded review surfaces rather than language rules alone.",
                    "cta": "Open Exports",
                    "href": "../03_exports/OPEN-HERE.html",
                },
                {
                    "title": "Premium Document Standard",
                    "pill": "Sibling Standard",
                    "copy": "Open the premium document standard when the founder needs the document structure that carries institutional voice into controlled layouts and outward-facing packets.",
                    "cta": "Open Document Standard",
                    "href": "UNYRA-Premium-Document-Standard.html",
                },
                {
                    "title": "Visual Standard",
                    "pill": "Governance Surface",
                    "copy": "Widen into the visual standard when the founder needs the governed styling system that keeps institutional language aligned with branded founder-facing outputs.",
                    "cta": "Open Visual Standard",
                    "href": "../03_exports/01_visual-standard/OPEN-HERE.html",
                },
            ],
        },
    }

    profile = profiles.get(path.name)
    if not profile:
        return None

    return {
        "kind": "Guidance Standard",
        "primary_title": "Brand Guidelines",
        "primary_href": "OPEN-HERE.html",
        "primary_cta": "Open Brand Guidelines",
        "track_href": "OPEN-HERE.html#supporting-files",
        "track_cta": "Open Guidance Standards",
        "governance_title": "Visual Standard",
        "governance_href": "../03_exports/01_visual-standard/OPEN-HERE.html",
        "governance_cta": "Open Visual Standard",
        "source_label": "Guidance Source",
        "source_cta": "Open Guidance Source",
        **profile,
    }


def get_dashboard_doc_context(path: Path) -> dict[str, str] | None:
    current_dir = path.parent
    try:
        parent_relative = current_dir.parent.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return None

    if parent_relative != "06_dashboard" or path.name == "README.md":
        return None

    hero_profile = build_portal_hero_context(current_dir)
    board_title = str(hero_profile.get("title", "")).strip() if hero_profile else ""
    if not board_title:
        board_title = f"{humanize_surface_name(current_dir.name)} Board"

    related_title = "Founder Dashboard"
    related_href = "../01_executive/Daily-Founder-Dashboard.html"
    related_cta = "Open Founder Dashboard"
    related_pill = "Founder Route"
    return_state = "Board / Hub / Founder"

    if current_dir.name == "01_executive":
        related_title = "Control Routing"
        related_href = "../33_control-routing/Founder-Control-Routing-Matrix.html"
        related_cta = "Open Control Routing"
        related_pill = "Routing Surface"
        return_state = "Board / Hub / Routing"
    elif current_dir.name == "33_control-routing":
        related_title = "Executable Checks"
        related_href = "../40_executable-checks/Trust-Override-Executable-Check-Control-Board.html"
        related_cta = "Open Executable Checks"
        related_pill = "Execution Watch"
        return_state = "Board / Hub / Watch"
    elif current_dir.name == "40_executable-checks":
        related_title = "Control Routing"
        related_href = "../33_control-routing/Founder-Control-Routing-Matrix.html"
        related_cta = "Open Control Routing"
        related_pill = "Routing Surface"
        return_state = "Board / Hub / Routing"

    return {
        "board_title": board_title,
        "board_cta": f"Open {board_title}",
        "board_href": "OPEN-HERE.html",
        "routes_title": "Board Routes",
        "routes_cta": "Open Board Routes",
        "routes_href": "OPEN-HERE.html#featured-routes",
        "hub_title": "Dashboards",
        "hub_cta": "Open Dashboards",
        "hub_href": "../OPEN-HERE.html",
        "related_title": related_title,
        "related_cta": related_cta,
        "related_href": related_href,
        "related_pill": related_pill,
        "return_state": return_state,
    }


def get_master_template_doc_context(path: Path) -> dict[str, str] | None:
    current_dir = path.parent
    try:
        parent_relative = current_dir.parent.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return None

    if parent_relative != "01_templates" or not path.name.endswith("-MASTER.md"):
        return None

    hero_profile = build_portal_hero_context(current_dir)
    domain_title = str(hero_profile.get("title", "")).strip() if hero_profile else ""
    if not domain_title:
        domain_title = f"{humanize_surface_name(current_dir.name)} Templates"

    related_title = "Founder Control Templates"
    related_href = "../10_governance/OPEN-HERE.html"
    related_cta = "Open Founder Control Templates"
    related_pill = "Governance Route"
    return_state = "Domain / Hub / Governance"

    if current_dir.name == "10_governance":
        related_title = "Outbound Pack"
        related_href = "../11_external-communications/OPEN-HERE.html"
        related_cta = "Open Outbound Pack"
        related_pill = "Outbound Route"
        return_state = "Domain / Hub / Outbound"

    return {
        "domain_title": domain_title,
        "domain_cta": f"Open {domain_title}",
        "domain_href": "OPEN-HERE.html",
        "pack_title": "Template Pack",
        "pack_cta": "Open Template Pack",
        "pack_href": "OPEN-HERE.html#supporting-files",
        "hub_title": "Templates",
        "hub_cta": "Open Templates",
        "hub_href": "../OPEN-HERE.html",
        "routes_title": "Template Fast Routes",
        "routes_cta": "Open Fast Routes",
        "routes_href": "../OPEN-HERE.html#featured-routes",
        "related_title": related_title,
        "related_cta": related_cta,
        "related_href": related_href,
        "related_pill": related_pill,
        "return_state": return_state,
    }


def get_sop_doc_context(path: Path) -> dict[str, str] | None:
    current_dir = path.parent
    try:
        parent_relative = current_dir.parent.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return None

    if parent_relative != "05_sops":
        return None

    hero_profile = build_portal_hero_context(current_dir)
    domain_title = str(hero_profile.get("title", "")).strip() if hero_profile else ""
    if not domain_title:
        domain_title = f"{humanize_surface_name(current_dir.name)} Procedures"

    related_title = "SOPs"
    related_href = "../OPEN-HERE.html"
    related_cta = "Open SOPs"
    related_pill = "Procedure Hub"
    return_state = "Procedure / Hub / Control"

    if current_dir.name == "06_dashboard":
        related_title = "Founder Dashboard"
        related_href = "../../06_dashboard/01_executive/Daily-Founder-Dashboard.html"
        related_cta = "Open Founder Dashboard"
        related_pill = "Founder Route"
        return_state = "Procedure / Hub / Founder"
    elif current_dir.name == "04_crm":
        related_title = "CRM"
        related_href = "../../02_crm/OPEN-HERE.html"
        related_cta = "Open CRM"
        related_pill = "Commercial Route"
        return_state = "Procedure / Hub / CRM"
    elif current_dir.name == "07_archive":
        related_title = "Archive"
        related_href = "../../07_archive/OPEN-HERE.html"
        related_cta = "Open Archive"
        related_pill = "Archive Route"
        return_state = "Procedure / Hub / Archive"
    elif current_dir.name == "08_external-communications":
        related_title = "Brand Guidelines"
        related_href = "../../00_brand/02_guidelines/OPEN-HERE.html"
        related_cta = "Open Brand Guidelines"
        related_pill = "Guidance Route"
        return_state = "Procedure / Hub / Guidance"

    return {
        "domain_title": domain_title,
        "domain_cta": f"Open {domain_title}",
        "domain_href": "OPEN-HERE.html",
        "stack_title": "Procedure Stack",
        "stack_cta": "Open Procedure Stack",
        "stack_href": "OPEN-HERE.html#supporting-files",
        "hub_title": "SOPs",
        "hub_cta": "Open SOPs",
        "hub_href": "../OPEN-HERE.html",
        "routes_title": "SOP Fast Routes",
        "routes_cta": "Open Fast Routes",
        "routes_href": "../OPEN-HERE.html#featured-routes",
        "related_title": related_title,
        "related_cta": related_cta,
        "related_href": related_href,
        "related_pill": related_pill,
        "return_state": return_state,
    }


def get_brand_assets_metrics(directory: Path) -> dict[str, int]:
    if not is_brand_assets_directory(directory):
        return {"asset_set_count": 0, "review_surface_count": 0, "protected_set_count": 0}

    asset_directories = [
        child
        for child in directory.iterdir()
        if child.is_dir() and child.name not in SKIP_DIR_NAMES
    ]
    asset_set_count = len(asset_directories)
    review_surface_count = sum(int((child / "OPEN-HERE.html").exists()) for child in asset_directories)
    protected_set_count = max(asset_set_count - review_surface_count, 0)
    return {
        "asset_set_count": asset_set_count,
        "review_surface_count": review_surface_count,
        "protected_set_count": protected_set_count,
    }


def get_template_layer_metrics(directory: Path) -> dict[str, int]:
    if not is_templates_directory(directory):
        return {"master_template_count": 0, "template_domain_count": 0, "fast_route_count": 0}

    child_directories = [
        child
        for child in directory.iterdir()
        if child.is_dir() and child.name not in SKIP_DIR_NAMES
    ]
    master_template_count = sum(
        1
        for child_dir in child_directories
        for child in child_dir.iterdir()
        if child.is_file() and child.suffix.lower() == ".md"
    )
    return {
        "master_template_count": master_template_count,
        "template_domain_count": len(child_directories),
        "fast_route_count": 3,
    }


def get_sop_layer_metrics(directory: Path) -> dict[str, int]:
    if not is_sops_directory(directory):
        return {
            "sop_surface_count": 0,
            "founder_standard_count": 0,
            "fast_route_count": 0,
        }

    sop_surface_count = sum(
        1
        for child in directory.iterdir()
        if child.is_dir() and child.name not in SKIP_DIR_NAMES
    )
    founder_standard_targets = (
        directory / "06_dashboard" / "Founder-Operating-Cadence-SOP.md",
        directory / "06_dashboard" / "Operating-System-Rollout-and-Adoption-SOP.md",
        directory / "04_crm" / "Commercial-Execution-Lifecycle-SOP.md",
        directory / "08_external-communications" / "Counterparty-Communication-Standard-SOP.md",
        directory / "07_archive" / "Archive-Closeout-SOP.md",
    )
    founder_standard_count = sum(int(path.exists()) for path in founder_standard_targets)
    return {
        "sop_surface_count": sop_surface_count,
        "founder_standard_count": founder_standard_count,
        "fast_route_count": 3,
    }


def get_crm_layer_metrics(directory: Path) -> dict[str, int]:
    if not is_crm_directory(directory):
        return {
            "counterparty_layer_count": 0,
            "deal_posture_count": 0,
            "execution_queue_count": 0,
            "fast_route_count": 0,
        }

    counterparty_layer_count = sum(
        int((directory / relative_path / "OPEN-HERE.html").exists())
        for relative_path in ("01_leads", "02_customers", "03_suppliers")
    )
    deal_root = directory / "04_deals"
    deal_posture_count = sum(
        1
        for child in deal_root.iterdir()
        if deal_root.exists() and child.is_dir() and child.name not in SKIP_DIR_NAMES
    ) if deal_root.exists() else 0
    execution_queue_root = directory / "05_tasks"
    execution_queue_count = sum(
        1
        for child in execution_queue_root.iterdir()
        if execution_queue_root.exists() and child.is_dir() and child.name not in SKIP_DIR_NAMES
    ) if execution_queue_root.exists() else 0
    return {
        "counterparty_layer_count": counterparty_layer_count,
        "deal_posture_count": deal_posture_count,
        "execution_queue_count": execution_queue_count,
        "fast_route_count": 3,
    }


def get_operations_layer_metrics(directory: Path) -> dict[str, int]:
    if not is_operations_directory(directory):
        return {
            "active_shipment_count": 0,
            "execution_domain_count": 0,
            "fast_route_count": 0,
        }

    execution_domain_count = sum(
        1
        for child in directory.iterdir()
        if child.is_dir() and child.name not in SKIP_DIR_NAMES and child.name != "99_archive"
    )
    active_shipment_root = directory / "03_shipments" / "active"
    active_shipment_count = sum(
        1
        for child in active_shipment_root.iterdir()
        if active_shipment_root.exists() and child.is_dir() and child.name not in SKIP_DIR_NAMES
    ) if active_shipment_root.exists() else 0
    return {
        "active_shipment_count": active_shipment_count,
        "execution_domain_count": execution_domain_count,
        "fast_route_count": 3,
    }


def get_compliance_layer_metrics(directory: Path) -> dict[str, int]:
    if not is_compliance_directory(directory):
        return {
            "governed_case_count": 0,
            "compliance_domain_count": 0,
            "fast_route_count": 0,
        }

    compliance_domain_count = sum(
        1
        for child in directory.iterdir()
        if child.is_dir() and child.name not in SKIP_DIR_NAMES and child.name != "99_archive"
    )
    governed_case_count = 0
    for relative_path in ("04_traceability", "05_inspections", "06_supplier-approval"):
        domain = directory / relative_path
        if not domain.exists():
            continue
        governed_case_count += sum(
            1
            for child in domain.iterdir()
            if child.is_dir() and child.name not in SKIP_DIR_NAMES
        )
    return {
        "governed_case_count": governed_case_count,
        "compliance_domain_count": compliance_domain_count,
        "fast_route_count": 3,
    }


def get_dashboard_layer_metrics(directory: Path) -> dict[str, int]:
    if not is_dashboard_directory(directory):
        return {
            "dashboard_surface_count": 0,
            "founder_cadence_count": 0,
            "fast_route_count": 0,
        }

    dashboard_surface_count = sum(
        1
        for child in directory.iterdir()
        if child.is_dir() and child.name not in SKIP_DIR_NAMES and child.name != "99_archive"
    )
    founder_cadence_targets = (
        directory / "01_executive" / "Daily-Founder-Dashboard.md",
        directory / "14_weekly-executive-review" / "Weekly-Executive-Operating-Review.md",
        directory / "15_monthly-strategic-review" / "Monthly-Strategic-Business-Review.md",
        directory / "22_quarterly-operating-plan" / "Quarterly-Operating-Plan.md",
    )
    founder_cadence_count = sum(int(path.exists()) for path in founder_cadence_targets)
    return {
        "dashboard_surface_count": dashboard_surface_count,
        "founder_cadence_count": founder_cadence_count,
        "fast_route_count": 3,
    }


def get_archive_layer_metrics(directory: Path) -> dict[str, int]:
    if not is_archive_directory(directory):
        return {
            "archived_matter_count": 0,
            "archive_function_count": 0,
            "fast_route_count": 0,
        }

    archive_functions = [
        child
        for child in directory.iterdir()
        if child.is_dir() and child.name not in SKIP_DIR_NAMES
    ]
    archived_matter_count = sum(
        1
        for archive_function in archive_functions
        for child in archive_function.iterdir()
        if child.is_dir() and child.name not in SKIP_DIR_NAMES
    )
    return {
        "archived_matter_count": archived_matter_count,
        "archive_function_count": len(archive_functions),
        "fast_route_count": 3,
    }


def get_system_layer_metrics(directory: Path) -> dict[str, int]:
    if directory != REPO_ROOT:
        return {
            "operating_hub_count": 0,
            "founder_cadence_count": 0,
            "live_control_route_count": 0,
        }

    operating_hubs = [
        child
        for child in directory.iterdir()
        if child.is_dir() and child.name not in SKIP_DIR_NAMES
    ]
    founder_cadence_targets = (
        directory / "06_dashboard" / "01_executive" / "Daily-Founder-Dashboard.md",
        directory / "06_dashboard" / "14_weekly-executive-review" / "Weekly-Executive-Operating-Review.md",
        directory / "06_dashboard" / "15_monthly-strategic-review" / "Monthly-Strategic-Business-Review.md",
        directory / "06_dashboard" / "22_quarterly-operating-plan" / "Quarterly-Operating-Plan.md",
    )
    live_control_targets = (
        directory / "06_dashboard" / "01_executive" / "Daily-Founder-Dashboard.md",
        directory / "06_dashboard" / "33_control-routing" / "Founder-Control-Routing-Matrix.md",
        directory / "06_dashboard" / "40_executable-checks" / "Trust-Override-Executable-Check-Control-Board.md",
    )
    return {
        "operating_hub_count": len(operating_hubs),
        "founder_cadence_count": sum(int(path.exists()) for path in founder_cadence_targets),
        "live_control_route_count": sum(int(path.exists()) for path in live_control_targets),
    }


def get_brand_layer_metrics(directory: Path) -> dict[str, int]:
    if not is_brand_directory(directory):
        return {"asset_set_count": 0, "guidance_count": 0, "preview_benchmark_count": 0}

    asset_root = directory / "01_assets"
    asset_set_count = sum(
        1
        for child in asset_root.iterdir()
        if asset_root.exists() and child.is_dir() and child.name not in SKIP_DIR_NAMES
    ) if asset_root.exists() else 0
    guidance_count = get_brand_guidelines_metrics(directory / "02_guidelines")["guidance_count"]
    preview_benchmark_count = get_preview_hub_metrics(REPO_ROOT / PREVIEW_DOCS_RELATIVE)["benchmark_count"]
    return {
        "asset_set_count": asset_set_count,
        "guidance_count": guidance_count,
        "preview_benchmark_count": preview_benchmark_count,
    }


def classify_control_list_item(text: str) -> str | None:
    normalized = text.strip().lower()
    if not normalized:
        return None

    posture_prefixes = (
        "movement posture",
        "current movement posture",
        "current movement answer",
        "what the supplier may treat as authorized",
        "what the forwarder or broker may treat as authorized",
        "what unyra may state outwardly",
        "what the packet may evidence outwardly",
    )
    stop_prefixes = (
        "current stop rule",
        "what remains on hold",
        "what remains on hold or under revalidation",
        "what this proforma does not authorize",
        "what contract execution does not authorize",
        "what unyra must not imply",
    )
    next_prefixes = (
        "next safe movement",
        "revalidation trigger",
        "revalidation owner",
        "same-day revalidation owner",
        "movement posture approved by",
        "contained-movement revalidation notice",
        "what remains on hold or under revalidation",
    )
    reference_prefixes = (
        "linked executable-check",
        "linked executable check",
        "linked scenario and risk",
        "containment references",
        "linked executable-check or live-gate reference",
        "linked scenario and risk reference",
    )

    if normalized.startswith(posture_prefixes):
        return "posture"
    if normalized.startswith(stop_prefixes):
        return "stop"
    if normalized.startswith(next_prefixes):
        return "next"
    if normalized.startswith(reference_prefixes):
        return "reference"
    return None


def classify_section_list(heading: str | None) -> str | None:
    if not heading:
        return None

    normalized = re.sub(r"[^a-z0-9 ]+", " ", heading.lower())
    normalized = re.sub(r"\s+", " ", normalized).strip()

    if normalized in {"immediate founder actions", "founder actions today", "next founder actions"}:
        return "action"
    if normalized in {"decision agenda", "what this room is designed to answer"}:
        return "decision"
    if normalized in {"escalation triggers", "escalation watch"}:
        return "escalation"
    if normalized in {"core modules in this room", "key modules in this room"}:
        return "modules"
    if normalized in {"founder usage standard", "usage standard"}:
        return "usage"
    return None


def extract_document_parts(markdown_text: str, fallback_title: str) -> tuple[str, str, list[tuple[str, str]], list[str]]:
    lines = markdown_text.splitlines()
    title = fallback_title
    meta: list[tuple[str, str]] = []
    subtitle_lines: list[str] = []
    body_start = 0

    for index, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip() or fallback_title
            cursor = index + 1
            while cursor < len(lines):
                stripped = lines[cursor].strip()
                if not stripped:
                    cursor += 1
                    continue
                if stripped.startswith("#"):
                    break
                if is_meta_line(stripped):
                    key, value = stripped.split(":", 1)
                    meta.append((key.strip(), value.strip()))
                    cursor += 1
                    continue
                if is_markdown_structure_line(stripped):
                    break
                subtitle_lines.append(stripped)
                cursor += 1
                if cursor < len(lines) and not lines[cursor].strip():
                    cursor += 1
                    break
            body_start = cursor
            break

    body_lines = lines[body_start:] if body_start else lines
    subtitle = clean_markdown_summary(" ".join(subtitle_lines).strip())
    if not subtitle:
        for key, value in meta:
            if key.lower() == "purpose":
                subtitle = clean_markdown_summary(value)
                break
    if not subtitle or subtitle == "-":
        for line in body_lines:
            stripped = line.strip()
            if (
                stripped
                and not stripped.startswith("#")
                and not is_markdown_structure_line(stripped)
            ):
                subtitle = clean_markdown_summary(stripped)
                break
    subtitle = clamp_summary(subtitle)
    return title, subtitle, meta, body_lines


def normalize_heading(text: str) -> str:
    normalized = re.sub(r"[^a-z0-9 ]+", " ", text.lower())
    return re.sub(r"\s+", " ", normalized).strip()


def slugify_heading(text: str) -> str:
    normalized = normalize_heading(text)
    return normalized.replace(" ", "-") if normalized else "section"


def strip_open_prefix(label: str) -> str:
    cleaned = label.strip()
    if cleaned.lower().startswith("open "):
        return cleaned[5:].strip()
    return cleaned


def strip_module_suffix(label: str) -> str:
    cleaned = label.strip()
    if cleaned.lower().endswith(" module"):
        return cleaned[:-7].strip()
    return cleaned


def get_stack_module_anchor_id(module_directory: Path) -> str:
    return f"stack-module-{slugify_heading(module_directory.name)}"


def get_room_module_stack_href(room_directory: Path, target_path: Path) -> str | None:
    try:
        room_relative = target_path.relative_to(room_directory)
    except ValueError:
        return None
    if target_path.name == "OPEN-HERE.html" and len(room_relative.parts) >= 2:
        return f"#{get_stack_module_anchor_id(target_path.parent)}"
    return None


def extract_section_list_items(lines: list[str], heading: str) -> list[str]:
    target_heading = normalize_heading(heading)
    items: list[str] = []
    in_section = False

    for line in lines:
        stripped = line.strip()
        heading_match = re.match(r"^#{2,4}\s+(.+)$", stripped)
        if heading_match:
            current_heading = normalize_heading(heading_match.group(1))
            if in_section:
                break
            in_section = current_heading == target_heading
            continue

        if not in_section:
            continue

        if not stripped:
            continue

        unordered = re.match(r"^- (.+)$", stripped)
        ordered = re.match(r"^\d+\. (.+)$", stripped)
        if unordered or ordered:
            items.append(unordered.group(1) if unordered else ordered.group(1))
            continue

        if items:
            break

    return items


def extract_markdown_headings(lines: list[str], minimum_level: int = 2, maximum_level: int = 3) -> list[str]:
    headings: list[str] = []
    for line in lines:
        stripped = line.strip()
        heading_match = re.match(r"^(#{2,6})\s+(.+)$", stripped)
        if not heading_match:
            continue
        level = len(heading_match.group(1))
        if minimum_level <= level <= maximum_level:
            headings.append(heading_match.group(2).strip())
    return headings


def extract_section_table_rows(lines: list[str], heading: str) -> list[tuple[str, str]]:
    target_heading = normalize_heading(heading)
    in_section = False
    table_lines: list[str] = []

    for line in lines:
        stripped = line.strip()
        heading_match = re.match(r"^#{2,4}\s+(.+)$", stripped)
        if heading_match:
            current_heading = normalize_heading(heading_match.group(1))
            if in_section:
                break
            in_section = current_heading == target_heading
            continue

        if not in_section:
            continue

        if stripped.startswith("|"):
            table_lines.append(stripped)
            continue

        if table_lines and stripped:
            break

    rows: list[list[str]] = []
    for line in table_lines:
        if re.match(r"^\|\s*[:\-| ]+\|\s*$", line):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 2:
            rows.append(cells[:2])

    if len(rows) < 2:
        return []

    return [(signal, reading) for signal, reading in rows[1:]]


def extract_module_titles(lines: list[str], heading: str) -> list[str]:
    module_titles: list[str] = []
    seen: set[str] = set()
    for item in extract_section_list_items(lines, heading):
        code_titles = re.findall(r"`([^`]+)`", item)
        candidates = code_titles or [item.split(":", 1)[0].strip()]
        for candidate in candidates:
            normalized = normalize_heading(candidate)
            if normalized and normalized not in seen:
                seen.add(normalized)
                module_titles.append(candidate.strip())
    return module_titles


def extract_inline_code_titles(text: str) -> list[str]:
    return [title.strip() for title in re.findall(r"`([^`]+)`", text) if title.strip()]


def get_brief_action_anchor_id(index: int) -> str:
    return f"brief-action-{index:02d}"


def get_brief_decision_anchor_id(index: int) -> str:
    return f"brief-decision-{index:02d}"


def get_brief_trigger_anchor_id(index: int) -> str:
    return f"brief-trigger-{index:02d}"


def get_brief_usage_anchor_id(index: int) -> str:
    return f"brief-usage-{index:02d}"


def get_brief_module_anchor_id(index: int, title: str) -> str:
    return f"brief-module-{index:02d}-{slugify_heading(strip_module_suffix(title))}"


def get_brief_reading_anchor_id(signal: str, index: int) -> str:
    return f"brief-reading-{index:02d}-{slugify_heading(signal)}"


def get_brief_support_anchor_id(index: int, title: str) -> str:
    return f"brief-support-{index:02d}-{slugify_heading(title)}"


def get_brief_related_anchor_id(index: int, title: str) -> str:
    return f"brief-related-{index:02d}-{slugify_heading(title)}"


def get_brief_source_anchor_id(index: int, title: str) -> str:
    return f"brief-source-{index:02d}-{slugify_heading(title)}"


def get_brief_focus_anchor_id(label: str) -> str:
    return f"brief-focus-{slugify_heading(label)}"


def get_brief_distribution_anchor_id(label: str) -> str:
    return f"brief-distribution-{slugify_heading(label)}"


def summarize_brief_operating_label(item: str, index: int, fallback_prefix: str) -> str:
    code_titles = extract_inline_code_titles(item)
    if code_titles:
        return f"{index:02d} {strip_module_suffix(strip_open_prefix(code_titles[0]))}"

    plain_text = re.sub(r"`[^`]+`", " ", item).strip()
    normalized = normalize_heading(plain_text)
    phrase_labels = [
        ("controlled review", "Controlled Review"),
        ("narrative complaint record", "Narrative Record"),
        ("sample executive pattern", "Executive Pattern"),
        ("operationally ready", "Move Readiness"),
        ("release confidence", "Release Confidence"),
        ("commercial weight", "Commercial Weight"),
        ("packet quality", "Packet Quality"),
        ("proof trail", "Proof Trail"),
        ("contained movement", "Contained Movement"),
        ("funding release", "Funding Release"),
        ("pre shipment release", "Release Sync"),
        ("recovery consequence", "Recovery Consequence"),
        ("customer consequence", "Customer Consequence"),
        ("containment evidence", "Containment Evidence"),
        ("trust quality", "Trust Quality"),
        ("collections confidence", "Collections Confidence"),
        ("cash outlook", "Cash Outlook"),
        ("concentration", "Concentration"),
        ("exposure growth", "Exposure Growth"),
        ("packet completeness", "Packet Completeness"),
        ("outbound language", "Outbound Control"),
    ]
    for phrase, label in phrase_labels:
        if phrase in normalized:
            return f"{index:02d} {label}"

    stopwords = {
        "a",
        "an",
        "and",
        "as",
        "at",
        "before",
        "beyond",
        "by",
        "for",
        "from",
        "if",
        "in",
        "into",
        "is",
        "it",
        "of",
        "on",
        "or",
        "so",
        "than",
        "that",
        "the",
        "this",
        "to",
        "until",
        "use",
        "verify",
        "confirm",
        "reconfirm",
        "review",
        "release",
        "hold",
        "keep",
        "move",
        "open",
        "start",
        "treat",
        "whether",
        "will",
        "with",
    }
    filtered_words = [word for word in re.findall(r"[A-Za-z0-9]+", plain_text) if word.lower() not in stopwords]
    label = " ".join(filtered_words[:2]).title() if filtered_words else f"{fallback_prefix} {index:02d}"
    return f"{index:02d} {label}"


def summarize_brief_action_label(item: str, index: int) -> str:
    return summarize_brief_operating_label(item, index, "Action")


def summarize_brief_decision_label(item: str, index: int) -> str:
    return summarize_brief_operating_label(item, index, "Decision")


def summarize_brief_trigger_label(item: str, index: int) -> str:
    return summarize_brief_operating_label(item, index, "Trigger")


def summarize_brief_signal_label(signal: str) -> str:
    replacements = {
        "current status": "Status",
        "relationship posture": "Trust Posture",
        "commitment posture": "Commitment",
        "outbound posture": "Outbound",
        "release posture": "Release",
        "funding posture": "Funding",
        "proof posture": "Proof",
        "exposure question": "Exposure",
        "strategic weight": "Strategic Weight",
    }
    normalized = normalize_heading(signal)
    return replacements.get(normalized, signal.strip())


def get_brief_reading_signal_profile(signal: str) -> tuple[str, str, str]:
    normalized = normalize_heading(signal)
    if any(term in normalized for term in {"posture", "question", "weight", "status", "stage"}):
        return ("Decision Signal", "brief-reading-card--decision", "meta-pill--brief-signal-decision")
    if any(term in normalized for term in {"id", "customer", "counterparty", "route", "region", "product"}):
        return ("Reference Signal", "brief-reading-card--reference", "meta-pill--brief-signal-reference")
    return ("Live Signal", "brief-reading-card--live", "meta-pill--brief-signal-live")


def remove_section(lines: list[str], heading: str) -> list[str]:
    target_heading = normalize_heading(heading)
    cleaned_lines: list[str] = []
    skipping = False

    for line in lines:
        stripped = line.strip()
        heading_match = re.match(r"^#{2,4}\s+(.+)$", stripped)
        if heading_match:
            current_heading = normalize_heading(heading_match.group(1))
            if skipping and current_heading != target_heading:
                skipping = False
            if current_heading == target_heading:
                skipping = True
                continue

        if not skipping:
            cleaned_lines.append(line)

    return cleaned_lines


def render_inline(text: str, current_dir: Path) -> str:
    safe = html.escape(text, quote=False)
    code_tokens: list[str] = []

    def hold_code(match: re.Match[str]) -> str:
        code_tokens.append(f"<code>{html.escape(match.group(1), quote=False)}</code>")
        return f"@@CODE{len(code_tokens) - 1}@@"

    safe = re.sub(r"`([^`]+)`", hold_code, safe)

    def render_link(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2)
        normalized_target = target
        if target.endswith(".md"):
            candidate = (current_dir / target).resolve()
            if candidate.exists():
                normalized_target = target[:-3] + ".html"
        href = html.escape(normalized_target, quote=True)
        return f'<a href="{href}">{label}</a>'

    safe = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", render_link, safe)
    safe = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", safe)
    safe = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", safe)
    safe = re.sub(r"(?<!_)_([^_]+)_(?!_)", r"<em>\1</em>", safe)

    for index, token in enumerate(code_tokens):
        safe = safe.replace(f"@@CODE{index}@@", token)
    return safe


def parse_table(lines: list[str], start_index: int, current_dir: Path) -> tuple[str, int]:
    header_cells = [cell.strip() for cell in lines[start_index].strip().strip("|").split("|")]
    body_rows = []
    index = start_index + 2
    while index < len(lines):
        stripped = lines[index].strip()
        if not stripped.startswith("|") or "|" not in stripped[1:]:
            break
        body_rows.append([cell.strip() for cell in stripped.strip("|").split("|")])
        index += 1

    header_html = "".join(f"<th>{render_inline(cell, current_dir)}</th>" for cell in header_cells)
    body_html = []
    for row in body_rows:
        cells = "".join(f"<td>{render_inline(cell, current_dir)}</td>" for cell in row)
        body_html.append(f"<tr>{cells}</tr>")

    table_html = [
        '<table class="premium-table">',
        "<thead>",
        f"<tr>{header_html}</tr>",
        "</thead>",
        "<tbody>",
        "".join(body_html),
        "</tbody>",
        "</table>",
    ]
    return "".join(table_html), index


def render_markdown(lines: list[str], current_dir: Path) -> str:
    html_parts: list[str] = []
    paragraph_buffer: list[str] = []
    list_type: str | None = None
    list_items: list[str] = []
    current_heading: str | None = None
    in_code = False
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        if paragraph_buffer:
            text = " ".join(item.strip() for item in paragraph_buffer if item.strip())
            if text:
                html_parts.append(f"<p>{render_inline(text, current_dir)}</p>")
            paragraph_buffer.clear()

    def flush_list() -> None:
        nonlocal list_type
        if list_type and list_items:
            tag = "ul" if list_type == "ul" else "ol"
            section_class = classify_section_list(current_heading)
            item_classes = [classify_control_list_item(item) for item in list_items]
            list_classes: list[str] = []
            if any(item_classes):
                list_classes.append("markdown-control-list")
            if section_class:
                list_classes.extend(["markdown-brief-list", f"markdown-brief-list--{section_class}"])
            list_class = f' class="{" ".join(list_classes)}"' if list_classes else ""
            items_html_parts = []
            for item, item_class in zip(list_items, item_classes):
                item_class_names: list[str] = []
                if section_class:
                    item_class_names.extend(["markdown-brief-item", f"markdown-brief-item--{section_class}"])
                if item_class:
                    item_class_names.extend(["markdown-control-item", f"markdown-control-item--{item_class}"])
                class_attr = f' class="{" ".join(item_class_names)}"' if item_class_names else ""
                items_html_parts.append(f"<li{class_attr}>{render_inline(item, current_dir)}</li>")
            html_parts.append(f"<{tag}{list_class}>{''.join(items_html_parts)}</{tag}>")
        list_type = None
        list_items.clear()

    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if in_code:
            if stripped.startswith("```"):
                code_html = html.escape("\n".join(code_lines), quote=False)
                html_parts.append(f"<pre><code>{code_html}</code></pre>")
                in_code = False
                code_lines.clear()
            else:
                code_lines.append(line)
            index += 1
            continue

        if stripped.startswith("```"):
            flush_paragraph()
            flush_list()
            in_code = True
            index += 1
            continue

        if not stripped:
            flush_paragraph()
            flush_list()
            index += 1
            continue

        if (
            stripped.startswith("|")
            and index + 1 < len(lines)
            and re.match(r"^\|\s*[:\-| ]+\|\s*$", lines[index + 1].strip())
        ):
            flush_paragraph()
            flush_list()
            table_html, next_index = parse_table(lines, index, current_dir)
            html_parts.append(table_html)
            index = next_index
            continue

        if re.match(r"^#{2,4}\s+", stripped):
            flush_paragraph()
            flush_list()
            level = len(stripped) - len(stripped.lstrip("#"))
            heading = stripped[level:].strip()
            current_heading = heading
            heading_id = slugify_heading(heading)
            heading_text = render_inline(heading, current_dir)
            html_parts.append(
                f'<h{level} id="{heading_id}">'
                f'<span>{heading_text}</span>'
                f'<a class="heading-anchor" href="#{heading_id}" aria-label="Link to {html.escape(heading, quote=True)} section">Link</a>'
                f"</h{level}>"
            )
            index += 1
            continue

        if re.match(r"^(-{3,}|\*{3,})$", stripped):
            flush_paragraph()
            flush_list()
            html_parts.append("<hr />")
            index += 1
            continue

        unordered = re.match(r"^- (.+)$", stripped)
        ordered = re.match(r"^\d+\. (.+)$", stripped)
        if unordered or ordered:
            flush_paragraph()
            current_type = "ul" if unordered else "ol"
            item_text = unordered.group(1) if unordered else ordered.group(1)
            if list_type and list_type != current_type:
                flush_list()
            list_type = current_type
            list_items.append(item_text)
            index += 1
            continue

        blockquote = re.match(r"^> (.+)$", stripped)
        if blockquote:
            flush_paragraph()
            flush_list()
            html_parts.append(f"<blockquote>{render_inline(blockquote.group(1), current_dir)}</blockquote>")
            index += 1
            continue

        paragraph_buffer.append(stripped)
        index += 1

    flush_paragraph()
    flush_list()

    if in_code and code_lines:
        code_html = html.escape("\n".join(code_lines), quote=False)
        html_parts.append(f"<pre><code>{code_html}</code></pre>")

    return "\n".join(html_parts) if html_parts else EMPTY_MARKDOWN_STATE_HTML


def collect_markdown_files() -> list[Path]:
    results: list[Path] = []
    for path in REPO_ROOT.rglob("*.md"):
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        results.append(path)
    return sorted(results)


def collect_directories(markdown_files: list[Path]) -> list[Path]:
    directories: set[Path] = {REPO_ROOT}
    for path in markdown_files:
        current = path.parent
        while True:
            directories.add(current)
            if current == REPO_ROOT:
                break
            current = current.parent
    return sorted(directories)


def build_breadcrumbs(current_path: Path, current_dir: Path) -> str:
    crumbs = [f'<a class="breadcrumb-link" href="{relative_url(current_dir, ROOT_INDEX_PATH)}">UNYRA Visual</a>']
    relative_parts = current_path.relative_to(REPO_ROOT).parts
    for index in range(len(relative_parts)):
        target = REPO_ROOT.joinpath(*relative_parts[: index + 1])
        if target.is_dir():
            href = relative_url(current_dir, target / "OPEN-HERE.html")
            label = humanize_breadcrumb_label(relative_parts[index])
        else:
            href = relative_url(current_dir, target.with_suffix(".html"))
            label = humanize_breadcrumb_label(target.stem)
        crumbs.append(f'<span class="breadcrumb-sep">/</span><a class="breadcrumb-link" href="{href}">{label}</a>')
    return "".join(crumbs)


def build_portal_breadcrumbs(current_dir: Path, hero_profile: dict[str, object] | None) -> str:
    if not hero_profile or not hero_profile.get("breadcrumb_label"):
        return build_breadcrumbs(current_dir, current_dir)

    crumbs = [f'<a class="breadcrumb-link" href="{relative_url(current_dir, ROOT_INDEX_PATH)}">UNYRA Visual</a>']
    relative_parts = current_dir.relative_to(REPO_ROOT).parts
    for index in range(len(relative_parts)):
        target = REPO_ROOT.joinpath(*relative_parts[: index + 1])
        href = relative_url(current_dir, target / "OPEN-HERE.html")
        if index == len(relative_parts) - 1:
            label = str(hero_profile["breadcrumb_label"])
        else:
            ancestor_profile = build_portal_hero_context(target)
            if ancestor_profile and ancestor_profile.get("breadcrumb_label"):
                label = str(ancestor_profile["breadcrumb_label"])
            else:
                label = humanize_breadcrumb_label(relative_parts[index])
        crumbs.append(f'<span class="breadcrumb-sep">/</span><a class="breadcrumb-link" href="{href}">{html.escape(label)}</a>')
    return "".join(crumbs)


def build_brief_breadcrumbs(current_path: Path, current_dir: Path) -> str:
    profile = build_doc_card_profile(current_dir, current_path) or {}
    hero_profile = build_portal_hero_context(current_dir)
    if hero_profile and hero_profile.get("breadcrumb_label"):
        crumbs = [build_portal_breadcrumbs(current_dir, hero_profile)]
    else:
        crumbs = [build_breadcrumbs(current_dir, current_dir)]
    brief_label = strip_open_prefix(str(profile.get("cta") or "Open Brief"))
    brief_href = relative_url(current_dir, current_path.with_suffix(".html"))
    crumbs.append(
        f'<span class="breadcrumb-sep">/</span><a class="breadcrumb-link" href="{html.escape(brief_href, quote=True)}">{html.escape(brief_label)}</a>'
    )
    return "".join(crumbs)


def build_overview_breadcrumbs(current_path: Path, current_dir: Path) -> str:
    hero_profile = build_portal_hero_context(current_dir)
    if hero_profile and hero_profile.get("breadcrumb_label"):
        crumbs = [build_portal_breadcrumbs(current_dir, hero_profile)]
    else:
        crumbs = [build_breadcrumbs(current_dir, current_dir)]
    overview_title = (
        str(hero_profile.get("title", "")).strip()
        if hero_profile and hero_profile.get("title")
        else "System"
        if current_dir == REPO_ROOT
        else humanize_surface_name(current_dir.name)
    )
    memo_label = get_overview_memo_label(current_dir, overview_title)
    memo_href = relative_url(current_dir, current_path.with_suffix(".html"))
    crumbs.append(
        f'<span class="breadcrumb-sep">/</span><a class="breadcrumb-link" href="{html.escape(memo_href, quote=True)}">{html.escape(memo_label)}</a>'
    )
    return "".join(crumbs)


def get_overview_memo_label(current_dir: Path, overview_title: str) -> str:
    if current_dir == REPO_ROOT:
        return "System Memo"
    try:
        relative = current_dir.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        relative = ""
    if relative == BRAND_ASSETS_RELATIVE:
        return "Asset Custody Memo"
    return f"{overview_title} Memo"


def build_document_breadcrumbs(current_path: Path, current_dir: Path, title: str) -> str:
    hero_profile = build_portal_hero_context(current_dir)
    if hero_profile and hero_profile.get("breadcrumb_label"):
        crumbs = [build_portal_breadcrumbs(current_dir, hero_profile)]
    else:
        crumbs = [build_breadcrumbs(current_dir, current_dir)]
    doc_label = clean_markdown_summary(title.strip()) or humanize_breadcrumb_label(current_path.stem)
    doc_href = relative_url(current_dir, current_path.with_suffix(".html"))
    crumbs.append(
        f'<span class="breadcrumb-sep">/</span><a class="breadcrumb-link" href="{html.escape(doc_href, quote=True)}">{html.escape(doc_label)}</a>'
    )
    return "".join(crumbs)


def resolve_document_toolbar_target(current_dir: Path, base_href: str, target: str) -> str:
    if target.startswith("#"):
        return f"{base_href}{target}"
    if target.startswith("./") or target.startswith("../"):
        if "#" in target:
            path_part, anchor = target.split("#", 1)
            return f"{relative_url(current_dir, current_dir / path_part)}#{anchor}"
        return relative_url(current_dir, current_dir / target)
    if "#" in target:
        path_part, anchor = target.split("#", 1)
        if path_part.startswith("./") or path_part.startswith("../"):
            return f"{relative_url(current_dir, current_dir / path_part)}#{anchor}"
        return f"{relative_url(current_dir, REPO_ROOT / path_part)}#{anchor}"
    return relative_url(current_dir, REPO_ROOT / target)


def build_overview_viewer_actions(
    path: Path,
    current_dir: Path,
    root_href: str,
    folder_href: str,
    source_href: str,
    overview_profile: dict[str, object] | None,
    overview_title: str,
) -> list[tuple[str, str, str]]:
    base_href = root_href if current_dir == REPO_ROOT else folder_href
    if current_dir == REPO_ROOT:
        return [
            ("button-primary", base_href, "Open UNYRA System"),
            ("button-secondary", "06_dashboard/01_executive/Daily-Founder-Dashboard.html", "Open Founder Dashboard"),
            ("button-secondary", "06_dashboard/33_control-routing/Founder-Control-Routing-Matrix.html", "Open Control Routing"),
            ("button-secondary", "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html", "Open Executable Checks"),
        ]
    if is_archive_directory(current_dir):
        return [
            ("button-primary", base_href, "Open Archive"),
            ("button-secondary", "03_crm/OPEN-HERE.html", "Open Archived CRM"),
            ("button-secondary", "../05_sops/07_archive/Archive-Closeout-SOP.html", "Open Archive Closeout SOP"),
            ("button-secondary", "03_crm/DEAL-2026-001_AtlanticFoods_Garlic-CLOSED/README.html", "Open Closed Deal Memo"),
        ]
    if is_sops_directory(current_dir):
        return [
            ("button-primary", base_href, "Open SOPs"),
            ("button-secondary", "06_dashboard/Founder-Operating-Cadence-SOP.html", "Open Founder Cadence SOP"),
            ("button-secondary", "04_crm/Commercial-Execution-Lifecycle-SOP.html", "Open Commercial Lifecycle SOP"),
            ("button-secondary", "08_external-communications/Counterparty-Communication-Standard-SOP.html", "Open Communication Standard SOP"),
        ]
    if is_dashboard_directory(current_dir):
        return [
            ("button-primary", base_href, "Open Dashboards"),
            ("button-secondary", "01_executive/Daily-Founder-Dashboard.html", "Open Founder Dashboard"),
            ("button-secondary", "40_executable-checks/Trust-Override-Executable-Check-Control-Board.html", "Open Executable Checks"),
            ("button-secondary", "14_weekly-executive-review/Weekly-Executive-Operating-Review.html", "Open Weekly Review"),
        ]
    if is_compliance_directory(current_dir):
        return [
            ("button-primary", base_href, "Open Compliance"),
            ("button-secondary", "05_inspections/OPEN-HERE.html", "Open Inspection Cases"),
            ("button-secondary", "06_supplier-approval/OPEN-HERE.html", "Open Supplier Approval"),
            ("button-secondary", "04_traceability/OPEN-HERE.html", "Open Traceability"),
        ]
    if is_operations_directory(current_dir):
        return [
            ("button-primary", base_href, "Open Operations"),
            ("button-secondary", "03_shipments/active/OPEN-HERE.html", "Open Active Shipments"),
            ("button-secondary", "../06_dashboard/03_operations/Daily-Operations-Command-Center.html", "Open Operations Command"),
            ("button-secondary", "05_working-files/OPEN-HERE.html", "Open Working Files"),
        ]
    if is_crm_directory(current_dir):
        return [
            ("button-primary", base_href, "Open CRM"),
            ("button-secondary", "04_deals/active/OPEN-HERE.html", "Open Active Deals"),
            ("button-secondary", "05_tasks/TASK-2026-001_Founder-Execution-Queue/README.html", "Open Founder Queue"),
            ("button-secondary", "02_customers/OPEN-HERE.html", "Open Customer Accounts"),
        ]
    if is_templates_directory(current_dir):
        return [
            ("button-primary", base_href, "Open Templates"),
            ("button-secondary", f"{base_href}#featured-routes", "Open Fast Routes"),
            ("button-secondary", "10_governance/OPEN-HERE.html", "Open Founder Control Templates"),
            ("button-secondary", "11_external-communications/OPEN-HERE.html", "Open Outbound Pack"),
        ]
    if is_brand_assets_directory(current_dir):
        return [
            ("button-primary", base_href, "Open Assets"),
            ("button-secondary", "../OPEN-HERE.html", "Open Brand"),
            ("button-secondary", "04_signatures/OPEN-HERE.html", "Open Brand Signatures"),
            ("button-secondary", "05_approved-compositions/OPEN-HERE.html", "Open Approved Compositions"),
        ]
    if is_brand_directory(current_dir):
        return [
            ("button-primary", base_href, "Open Brand"),
            ("button-secondary", "01_assets/OPEN-HERE.html", "Open Assets"),
            ("button-secondary", "02_guidelines/OPEN-HERE.html", "Open Brand Guidelines"),
            ("button-secondary", "03_exports/OPEN-HERE.html", "Open Exports"),
        ]
    if is_brand_guidelines_directory(current_dir):
        return [
            ("button-primary", base_href, "Open Brand Guidelines"),
            ("button-secondary", "../03_exports/01_visual-standard/OPEN-HERE.html", "Open Visual Standard"),
            ("button-secondary", "../03_exports/OPEN-HERE.html", "Open Exports"),
            ("button-secondary", source_href, "Open Memo Source"),
        ]
    if is_exports_directory(current_dir):
        return [
            ("button-primary", base_href, "Open Exports"),
            ("button-secondary", "02_preview-docs/OPEN-HERE.html", "Open Preview Docs"),
            ("button-secondary", "02_preview-docs/index.html#full-catalog", "Open Domain Lanes"),
            ("button-secondary", "01_visual-standard/OPEN-HERE.html", "Open Visual Standard"),
        ]
    if is_preview_docs_directory(current_dir):
        return [
            ("button-primary", base_href, "Open Preview Docs"),
            ("button-secondary", "index.html#founder-pathways", "Open Founder Pathways"),
            ("button-secondary", "index.html#full-catalog", "Open Domain Lanes"),
            ("button-secondary", "index.html#brand-anchors", "Open Brand Anchors"),
        ]
    if is_visual_standard_directory(current_dir):
        return [
            ("button-primary", base_href, "Open Visual Standard"),
            ("button-secondary", "../02_preview-docs/OPEN-HERE.html", "Open Preview Docs"),
            ("button-secondary", "../OPEN-HERE.html", "Open Exports"),
            ("button-secondary", source_href, "Open Memo Source"),
        ]
    relative = current_dir.relative_to(REPO_ROOT).as_posix() if current_dir != REPO_ROOT else ""
    if relative == "00_brand/01_assets/04_signatures":
        return [
            ("button-primary", base_href, "Open Brand Signatures"),
            ("button-secondary", "../OPEN-HERE.html", "Open Assets"),
            ("button-secondary", "../05_approved-compositions/OPEN-HERE.html", "Open Approved Compositions"),
            ("button-secondary", "../../03_exports/01_visual-standard/OPEN-HERE.html", "Open Visual Standard"),
        ]
    if relative == "00_brand/01_assets/05_approved-compositions":
        return [
            ("button-primary", base_href, "Open Approved Compositions"),
            ("button-secondary", "../OPEN-HERE.html", "Open Assets"),
            ("button-secondary", "../04_signatures/OPEN-HERE.html", "Open Brand Signatures"),
            ("button-secondary", "../../03_exports/01_visual-standard/OPEN-HERE.html", "Open Visual Standard"),
        ]
    if relative == "02_crm/04_deals":
        return [
            ("button-primary", base_href, "Open Deals"),
            ("button-secondary", "active/OPEN-HERE.html", "Open Active Deals"),
            ("button-secondary", "won/OPEN-HERE.html", "Open Won Deals"),
            ("button-secondary", "lost/OPEN-HERE.html", "Open Lost Deals"),
        ]
    if relative == "02_crm/04_deals/won":
        return [
            ("button-primary", base_href, "Open Won Deals"),
            ("button-secondary", "DEAL-2026-003_HarborFresh_Garlic/OPEN-HERE.html", "Open Harbor Fresh Won Deal"),
            ("button-secondary", "../OPEN-HERE.html", "Open Deals"),
            ("button-secondary", source_href, "Open Memo Source"),
        ]
    if relative == "02_crm/04_deals/lost":
        return [
            ("button-primary", base_href, "Open Lost Deals"),
            ("button-secondary", "DEAL-2026-002_CrescentMarket_Ginger/OPEN-HERE.html", "Open Crescent Market Lost Deal"),
            ("button-secondary", "../OPEN-HERE.html", "Open Deals"),
            ("button-secondary", source_href, "Open Memo Source"),
        ]
    if relative == "02_crm/04_deals/won/DEAL-2026-003_HarborFresh_Garlic":
        return [
            ("button-primary", base_href, "Open Harbor Fresh Garlic Won Deal Room"),
            ("button-secondary", "PROFIT-2026-001_HarborFresh-Garlic-Trade-Review/OPEN-HERE.html", "Open Trade Review"),
            ("button-secondary", "../OPEN-HERE.html", "Open Won Deals"),
            ("button-secondary", "../../active/OPEN-HERE.html", "Open Active Deals"),
        ]
    if relative == "02_crm/04_deals/won/DEAL-2026-003_HarborFresh_Garlic/PROFIT-2026-001_HarborFresh-Garlic-Trade-Review":
        return [
            ("button-primary", base_href, "Open Harbor Fresh Garlic Trade Review"),
            ("button-secondary", "../OPEN-HERE.html", "Open Won Deal Room"),
            ("button-secondary", "../../OPEN-HERE.html", "Open Won Deals"),
            ("button-secondary", "../../../active/OPEN-HERE.html", "Open Active Deals"),
        ]
    if relative == "02_crm/04_deals/lost/DEAL-2026-002_CrescentMarket_Ginger":
        return [
            ("button-primary", base_href, "Open Crescent Market Ginger Lost Deal Room"),
            ("button-secondary", "../OPEN-HERE.html", "Open Lost Deals"),
            ("button-secondary", "../../active/OPEN-HERE.html", "Open Active Deals"),
            ("button-secondary", "../../OPEN-HERE.html", "Open Deals"),
        ]
    if relative == "03_operations/03_shipments/active":
        return [
            ("button-primary", base_href, "Open Active Shipments"),
            ("button-secondary", f"{base_href}#featured-routes", "Open Route Lanes"),
            (
                "button-secondary",
                "../../../06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html",
                "Open Shipment Control Tower",
            ),
            (
                "button-secondary",
                "SHIP-2026-001_China-to-USA/OPEN-HERE.html",
                "Open China to USA Shipment",
            ),
        ]
    if relative == "02_crm/04_deals/active":
        return [
            ("button-primary", base_href, "Open Active Deals"),
            ("button-secondary", f"{base_href}#featured-routes", "Open Founder Routes"),
            (
                "button-secondary",
                "DEAL-2026-001_AtlanticFoods_Garlic/OPEN-HERE.html",
                "Open Atlantic Foods Deal",
            ),
            ("button-secondary", source_href, "Open Memo Source"),
        ]
    active_deal_module = get_active_deal_module_context(current_dir)
    if active_deal_module:
        secondary_candidates = [
            (
                str(active_deal_module["room_entry_label"]),
                str(active_deal_module["room_entry_href"]),
            ),
            (
                str(active_deal_module["next_action_label"]),
                str(active_deal_module["next_action_href"]),
            ),
            ("Open Active Deals", str(active_deal_module["active_deals_href"])),
        ]
        deduped_secondaries: list[tuple[str, str]] = []
        seen_targets: set[str] = {str(active_deal_module["module_portal_href"])}
        for label, href in secondary_candidates:
            if href in seen_targets:
                continue
            seen_targets.add(href)
            deduped_secondaries.append((label, href))
        return [
            ("button-primary", str(active_deal_module["module_portal_href"]), f"Open {str(active_deal_module['module_title'])}"),
            *[
                ("button-secondary", href, label)
                for label, href in deduped_secondaries[:3]
            ],
        ]
    active_shipment_module = get_active_shipment_module_context(current_dir)
    if active_shipment_module:
        secondary_candidates = [
            (
                str(active_shipment_module["room_entry_label"]),
                str(active_shipment_module["room_entry_href"]),
            ),
            (
                str(active_shipment_module["next_action_label"]),
                str(active_shipment_module["next_action_href"]),
            ),
            ("Open Active Shipments", str(active_shipment_module["active_shipments_href"])),
        ]
        deduped_secondaries: list[tuple[str, str]] = []
        seen_targets: set[str] = {str(active_shipment_module["module_portal_href"])}
        for label, href in secondary_candidates:
            if href in seen_targets:
                continue
            seen_targets.add(href)
            deduped_secondaries.append((label, href))
        return [
            ("button-primary", str(active_shipment_module["module_portal_href"]), f"Open {str(active_shipment_module['module_title'])}"),
            *[
                ("button-secondary", href, label)
                for label, href in deduped_secondaries[:3]
            ],
        ]
    active_account_module = get_active_account_module_context(current_dir)
    if active_account_module:
        secondary_candidates = [
            (
                str(active_account_module["room_entry_label"]),
                str(active_account_module["room_entry_href"]),
            ),
            (
                str(active_account_module["next_action_label"]),
                str(active_account_module["next_action_href"]),
            ),
            ("Open Customers", str(active_account_module["customers_href"])),
        ]
        deduped_secondaries: list[tuple[str, str]] = []
        seen_targets: set[str] = {str(active_account_module["module_portal_href"])}
        for label, href in secondary_candidates:
            if href in seen_targets:
                continue
            seen_targets.add(href)
            deduped_secondaries.append((label, href))
        return [
            ("button-primary", str(active_account_module["module_portal_href"]), f"Open {str(active_account_module['module_title'])}"),
            *[
                ("button-secondary", href, label)
                for label, href in deduped_secondaries[:3]
            ],
        ]
    active_claim_module = get_active_claim_module_context(current_dir)
    if active_claim_module:
        secondary_candidates = [
            (
                str(active_claim_module["room_entry_label"]),
                str(active_claim_module["room_entry_href"]),
            ),
            (
                str(active_claim_module["next_action_label"]),
                str(active_claim_module["next_action_href"]),
            ),
            ("Open Inspection Cases", str(active_claim_module["inspection_cases_href"])),
        ]
        deduped_secondaries: list[tuple[str, str]] = []
        seen_targets: set[str] = {str(active_claim_module["module_portal_href"])}
        for label, href in secondary_candidates:
            if href in seen_targets:
                continue
            seen_targets.add(href)
            deduped_secondaries.append((label, href))
        return [
            ("button-primary", str(active_claim_module["module_portal_href"]), f"Open {str(active_claim_module['module_title'])}"),
            *[
                ("button-secondary", href, label)
                for label, href in deduped_secondaries[:3]
            ],
        ]
    supplier_approval_module = get_supplier_approval_module_context(current_dir)
    if supplier_approval_module:
        secondary_candidates = [
            (
                str(supplier_approval_module["room_entry_label"]),
                str(supplier_approval_module["room_entry_href"]),
            ),
            (
                str(supplier_approval_module["next_action_label"]),
                str(supplier_approval_module["next_action_href"]),
            ),
            (
                str(supplier_approval_module["board_cta"]),
                str(supplier_approval_module["board_href"]),
            ),
        ]
        deduped_secondaries: list[tuple[str, str]] = []
        seen_targets: set[str] = {str(supplier_approval_module["module_portal_href"])}
        for label, href in secondary_candidates:
            if href in seen_targets:
                continue
            seen_targets.add(href)
            deduped_secondaries.append((label, href))
        return [
            ("button-primary", str(supplier_approval_module["module_portal_href"]), f"Open {str(supplier_approval_module['module_title'])}"),
            *[
                ("button-secondary", href, label)
                for label, href in deduped_secondaries[:3]
            ],
        ]
    current_doc_href = relative_url(current_dir, path.with_suffix(".html"))
    child_dirs = [
        child
        for child in current_dir.iterdir()
        if child.is_dir() and child.name not in SKIP_DIR_NAMES
    ]
    readable_layers = sum(
        1
        for child in current_dir.iterdir()
        if child.is_file() and child.suffix.lower() == ".md" and child.name not in {"README.md", "AGENTS.md"}
    )
    primary_label = (
        "Open UNYRA System"
        if current_dir == REPO_ROOT
        else str(overview_profile.get("cta") or f"Open {overview_title}")
        if overview_profile
        else f"Open {overview_title}"
    )
    viewer_actions: list[tuple[str, str, str]] = [("button-primary", base_href, primary_label)]
    secondary_candidates: list[tuple[str, str]] = []

    if current_dir == REPO_ROOT:
        secondary_candidates.extend(
            [
                ("Open Featured Routes", f"{root_href}#featured-routes"),
                ("Open Operating Areas", f"{root_href}#room-modules"),
            ]
        )
    else:
        hero_actions = list(overview_profile.get("actions", [])) if overview_profile else []
        for label, target, _style in hero_actions:
            resolved_href = resolve_document_toolbar_target(current_dir, base_href, str(target))
            if resolved_href == current_doc_href:
                continue
            secondary_candidates.append((str(label), resolved_href))
        if child_dirs and not any("#room-modules" in href for _, href in secondary_candidates):
            secondary_candidates.insert(0, (f"Open {overview_title} Surfaces", f"{folder_href}#room-modules"))

    if readable_layers:
        secondary_candidates.append(("Open Readable Layers", f"{base_href}#supporting-files"))
    if current_dir != REPO_ROOT:
        secondary_candidates.append(("Open Source Integrity", f"{base_href}#visual-system"))

    deduped_secondaries: list[tuple[str, str]] = []
    seen_targets: set[str] = set()
    for label, href in secondary_candidates:
        if href == current_doc_href or href in seen_targets:
            continue
        seen_targets.add(href)
        deduped_secondaries.append((label, href))

    viewer_actions.extend(
        ("button-secondary", href, label)
        for label, href in deduped_secondaries[:2]
    )
    viewer_actions.append(("button-secondary", source_href, "Open Memo Source"))
    return viewer_actions[:4]


def build_standard_viewer_actions(
    path: Path,
    current_dir: Path,
    root_href: str,
    folder_href: str,
    source_href: str,
    doc_kind: str,
    title: str,
) -> list[tuple[str, str, str]]:
    hero_profile = build_portal_hero_context(current_dir)
    base_href = root_href if current_dir == REPO_ROOT else folder_href
    guideline_doc = get_brand_guideline_doc_context(path)
    if guideline_doc:
        toolbar_routes = list(guideline_doc.get("toolbar_routes", []))
        viewer_actions: list[tuple[str, str, str]] = [
            ("button-primary", base_href, str(guideline_doc["primary_cta"]))
        ]
        viewer_actions.extend(
            ("button-secondary", href, label)
            for label, href in toolbar_routes[:2]
        )
        viewer_actions.append(("button-secondary", source_href, str(guideline_doc["source_cta"])))
        return viewer_actions[:4]
    master_template_doc = get_master_template_doc_context(path)
    if master_template_doc:
        return [
            ("button-primary", str(master_template_doc["pack_href"]), str(master_template_doc["pack_cta"])),
            ("button-secondary", str(master_template_doc["domain_href"]), str(master_template_doc["domain_cta"])),
            ("button-secondary", str(master_template_doc["hub_href"]), str(master_template_doc["hub_cta"])),
            ("button-secondary", source_href, get_doc_card_source_cta(doc_kind)),
        ]
    sop_doc = get_sop_doc_context(path)
    if sop_doc:
        return [
            ("button-primary", str(sop_doc["stack_href"]), str(sop_doc["stack_cta"])),
            ("button-secondary", str(sop_doc["domain_href"]), str(sop_doc["domain_cta"])),
            ("button-secondary", str(sop_doc["hub_href"]), str(sop_doc["hub_cta"])),
            ("button-secondary", source_href, get_doc_card_source_cta(doc_kind)),
        ]
    dashboard_doc = get_dashboard_doc_context(path)
    if dashboard_doc:
        return [
            ("button-primary", base_href, str(dashboard_doc["board_cta"])),
            ("button-secondary", str(dashboard_doc["routes_href"]), str(dashboard_doc["routes_cta"])),
            ("button-secondary", str(dashboard_doc["hub_href"]), str(dashboard_doc["hub_cta"])),
            ("button-secondary", source_href, get_doc_card_source_cta(doc_kind)),
        ]
    current_doc_href = relative_url(current_dir, path.with_suffix(".html"))
    child_dirs = [
        child
        for child in current_dir.iterdir()
        if child.is_dir() and child.name not in SKIP_DIR_NAMES
    ]
    readable_layers = sum(
        1
        for child in current_dir.iterdir()
        if child.is_file() and child.suffix.lower() == ".md" and child.name not in {"README.md", "AGENTS.md"}
    )
    surface_title = (
        str(hero_profile.get("title", "")).strip()
        if hero_profile and hero_profile.get("title")
        else humanize_surface_name(current_dir.name)
        if current_dir != REPO_ROOT
        else "UNYRA System"
    )
    surface_pill = get_doc_card_surface_pill(current_dir, path, doc_kind)
    primary_label = (
        "Open UNYRA System"
        if current_dir == REPO_ROOT
        else str(hero_profile.get("cta", "")).strip()
        if hero_profile and hero_profile.get("cta")
        else f"Open {surface_title}"
        if hero_profile and surface_title
        else get_doc_card_primary_cta(doc_kind, surface_pill)
        if surface_pill
        else f"Open {surface_title}"
    )

    viewer_actions: list[tuple[str, str, str]] = [("button-primary", base_href, primary_label)]
    secondary_candidates: list[tuple[str, str]] = []

    if current_dir == REPO_ROOT:
        secondary_candidates.extend(
            [
                ("Open Featured Routes", f"{root_href}#featured-routes"),
                ("Open Operating Areas", f"{root_href}#room-modules"),
            ]
        )
    else:
        hero_actions = list(hero_profile.get("actions", [])) if hero_profile else []
        for label, target, _style in hero_actions:
            resolved_href = resolve_document_toolbar_target(current_dir, base_href, str(target))
            if resolved_href in {current_doc_href, base_href}:
                continue
            secondary_candidates.append((str(label), resolved_href))
        if child_dirs and not any("#room-modules" in href for _, href in secondary_candidates):
            secondary_candidates.append((f"Open {surface_title} Surfaces", f"{folder_href}#room-modules"))

    if readable_layers and not any("#supporting-files" in href for _, href in secondary_candidates):
        secondary_candidates.append(("Open Readable Layers", f"{base_href}#supporting-files"))
    if current_dir != REPO_ROOT and not any("#visual-system" in href for _, href in secondary_candidates):
        secondary_candidates.append(("Open Source Integrity", f"{base_href}#visual-system"))

    deduped_secondaries: list[tuple[str, str]] = []
    seen_targets: set[str] = set()
    for label, href in secondary_candidates:
        if href == current_doc_href or href in seen_targets:
            continue
        seen_targets.add(href)
        deduped_secondaries.append((label, href))

    viewer_actions.extend(
        ("button-secondary", href, label)
        for label, href in deduped_secondaries[:2]
    )
    viewer_actions.append(("button-secondary", source_href, get_doc_card_source_cta(doc_kind)))
    return viewer_actions[:4]


def build_portal_section_profile(directory: Path) -> dict[str, str] | None:
    relative = directory.relative_to(REPO_ROOT).as_posix() if directory != REPO_ROOT else ""
    try:
        parent_relative = directory.parent.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        parent_relative = ""
    if relative == PREVIEW_DOCS_RELATIVE:
        return {
            "docs_eyebrow": "Preview Memo",
            "docs_title": "Open the benchmark memo before widening preview review.",
            "docs_copy": "Use this memo when the founder needs the written map behind pathways, domain lanes, brand anchors, and the benchmark library before opening a single preview.",
        }
    active_deal_module = get_active_deal_module_context(directory)
    if active_deal_module:
        module_title = str(active_deal_module["module_title"])
        room_title = str(active_deal_module["room_title"])
        return {
            "docs_eyebrow": "Module Memo",
            "docs_title": f"Open the memo and return routes behind {module_title}.",
            "docs_copy": f"Use this memo layer when the founder wants the governed reading view for {module_title.lower()} without losing the live context of {room_title}, Active Deals, and the wider deals hub.",
        }
    active_shipment_module = get_active_shipment_module_context(directory)
    if active_shipment_module:
        module_title = str(active_shipment_module["module_title"])
        room_title = str(active_shipment_module["room_title"])
        return {
            "docs_eyebrow": "Module Memo",
            "docs_title": f"Open the memo and return routes behind {module_title}.",
            "docs_copy": f"Use this memo layer when the founder wants the governed reading view for {module_title.lower()} without losing the live context of {room_title}, Active Shipments, and the wider shipments hub.",
        }
    active_account_module = get_active_account_module_context(directory)
    if active_account_module:
        module_title = str(active_account_module["module_title"])
        room_title = str(active_account_module["room_title"])
        return {
            "docs_eyebrow": "Module Memo",
            "docs_title": f"Open the memo and return routes behind {module_title}.",
            "docs_copy": f"Use this memo layer when the founder wants the governed reading view for {module_title.lower()} without losing the live context of {room_title}, Customers, and the wider CRM hub.",
        }
    active_claim_module = get_active_claim_module_context(directory)
    if active_claim_module:
        module_title = str(active_claim_module["module_title"])
        room_title = str(active_claim_module["room_title"])
        return {
            "docs_eyebrow": "Module Memo",
            "docs_title": f"Open the memo and return routes behind {module_title}.",
            "docs_copy": f"Use this memo layer when the founder wants the governed reading view for {module_title.lower()} without losing the live context of {room_title}, Inspection Cases, and the wider Compliance hub.",
        }
    supplier_approval_module = get_supplier_approval_module_context(directory)
    if supplier_approval_module:
        module_title = str(supplier_approval_module["module_title"])
        room_title = str(supplier_approval_module["room_title"])
        return {
            "docs_eyebrow": "Module Memo",
            "docs_title": f"Open the memo and return routes behind {module_title}.",
            "docs_copy": f"Use this memo layer when the founder wants the governed reading view for {module_title.lower()} without losing the live context of {room_title}, Supplier Approval, and the wider Compliance hub.",
        }
    if is_dashboard_pack_directory(directory):
        primary_doc = get_dashboard_pack_primary_doc(directory)
        board_title = humanize_surface_name(primary_doc.stem) if primary_doc else f"{humanize_surface_name(directory.name)} Board"
        return {
            "docs_eyebrow": "Board Surface",
            "docs_title": f"Open {board_title} as the controlled board surface.",
            "docs_copy": "Use this board card when the founder needs the live dashboard readout before widening back to the dashboard hub or fast-route stack.",
        }
    if parent_relative == "01_templates":
        directory_name = humanize_surface_name(directory.name)
        return {
            "docs_eyebrow": "Master Templates",
            "docs_title": f"Open the approved {directory_name.lower()} masters and drafting pack.",
            "docs_copy": f"Use these master-template cards when the founder wants the protected {directory_name.lower()} drafting system without dropping into raw template custody language.",
        }
    if parent_relative == "05_sops":
        directory_name = humanize_surface_name(directory.name)
        return {
            "docs_eyebrow": "Procedure Stack",
            "docs_title": f"Open the governed {directory_name.lower()} procedures and operating rules.",
            "docs_copy": f"Use these procedure cards when the founder wants the written {directory_name.lower()} operating standard without dropping into generic readable-layer framing.",
        }
    profiles = {
        "": {
            "folders_eyebrow": "Operating Layers",
            "folders_title": "Open the UNYRA system through its major operating layers.",
            "folders_copy": "These cards separate the system into brand, templates, CRM, operations, compliance, SOPs, dashboards, and archive so the founder can widen review without losing structure.",
            "docs_eyebrow": "Founder Orientation",
            "docs_title": "Open the system memo before widening review.",
            "docs_copy": "Use this reading layer when the founder wants the curated system map, operating hubs, and discipline rules before opening a specific hub.",
        },
        "00_brand": {
            "folders_eyebrow": "Brand Surfaces",
            "folders_title": "Open approved assets, brand governance, and export routing surfaces.",
            "folders_copy": "These cards separate assets, guidance rules, and export governance so the founder can move directly to the right brand control layer without mixing identity, rules, and benchmark output.",
            "docs_eyebrow": "Brand Guidance",
            "docs_title": "Open the brand memo and written governance map.",
            "docs_copy": "Use these readable layers when the founder wants the governing narrative behind approved assets, rules, exports, and retained brand control.",
        },
        "00_brand/01_assets": {
            "folders_eyebrow": "Asset Surfaces",
            "folders_title": "Open the review-ready asset surfaces without disturbing protected source sets.",
            "folders_copy": "These cards separate the approved review surfaces from the protected asset custody layer so the founder can assess signatures and compositions without opening raw asset files.",
            "docs_eyebrow": "Asset Guidance",
            "docs_title": "Open the asset memo and custody map.",
            "docs_copy": "Use this readable layer when the founder needs the written map behind approved asset sets, review surfaces, and protected brand source custody.",
        },
        "00_brand/02_guidelines": {
            "docs_eyebrow": "Guidance Layer",
            "docs_title": "Open the memo and governed guidance standards behind brand presentation.",
            "docs_copy": "Use these readable layers when the founder wants the written rule set behind identity, document standard, voice discipline, and their link to exports.",
        },
        "00_brand/03_exports": {
            "folders_eyebrow": "Export Routes",
            "folders_title": "Open the benchmark hub and governing standard that shape founder-facing output.",
            "folders_copy": "These surfaces separate Preview Docs and Visual Standard so the founder can move between benchmark routing and design governance without drifting into raw export folders.",
            "docs_eyebrow": "Export Guidance",
            "docs_title": "Open the export overview and supporting map.",
            "docs_copy": "Use these readable layers when the founder wants the written frame behind preview docs, domain lanes, and visual-standard governance.",
        },
        "00_brand/03_exports/01_visual-standard": {
            "docs_eyebrow": "Standard Guidance",
            "docs_title": "Open the governing memo behind preview governance and export styling.",
            "docs_copy": "Use this memo when the founder needs the written standard behind preview docs, brand governance, and export styling discipline.",
        },
        "01_templates": {
            "folders_eyebrow": "Template Surfaces",
            "folders_title": "Open the protected template surfaces by operating domain.",
            "folders_copy": "These cards separate master formats across sales, logistics, compliance, legal, finance, and governance so the founder can reach the right source format fast.",
            "docs_eyebrow": "Template Guidance",
            "docs_title": "Open the template overview and supporting notes.",
            "docs_copy": "Use these readable layers when the founder wants the governing explanation behind the master templates before opening a specific format family.",
        },
        "02_crm": {
            "folders_eyebrow": "Commercial Surfaces",
            "folders_title": "Open the CRM surfaces that carry relationships and live commercial posture.",
            "folders_copy": "These cards separate customers, suppliers, deals, and task layers so the founder can move straight to the right commercial surface instead of scanning the whole CRM tree.",
            "docs_eyebrow": "CRM Guidance",
            "docs_title": "Open the CRM overview and support layers.",
            "docs_copy": "Use these readable layers when the founder wants the written commercial map behind the rooms, tasks, and relationship records.",
        },
        LEADS_RELATIVE: {
            "folders_eyebrow": "Lead Rooms",
            "folders_title": "Open the governed prospect room and the routes that decide whether qualification should advance or hold.",
            "folders_copy": "This lane keeps lead review explicit by separating the live prospect room from the founder routes that convert qualification into the next commercial move.",
        },
        LEAD_ROOM_RELATIVE: {
            "docs_eyebrow": "Lead Brief",
            "docs_title": "Open the governed lead brief before widening qualification or follow-through review.",
            "docs_copy": "Use this reading layer when the founder wants the qualification narrative, pipeline posture, and next commercial move behind Crescent Market Wholesale.",
        },
        CUSTOMERS_RELATIVE: {
            "folders_eyebrow": "Account Rooms",
            "folders_title": "Open the governed customer room and the routes that decide whether trust, release, and growth posture still hold.",
            "folders_copy": "This lane keeps customer review explicit by separating the live account room from the trust, collections, and concentration routes that confirm account quality.",
        },
        SUPPLIERS_RELATIVE: {
            "folders_eyebrow": "Supplier Rooms",
            "folders_title": "Open the governed sourcing room and the routes that decide whether this supplier should advance, fortify, or escalate.",
            "folders_copy": "This lane keeps supplier review explicit by separating the live sourcing room from the approval and performance routes that confirm continuity confidence.",
        },
        SUPPLIER_ROOM_RELATIVE: {
            "docs_eyebrow": "Supplier Brief",
            "docs_title": "Open the governed supplier brief before widening approval, continuity, or performance review.",
            "docs_copy": "Use this reading layer when the founder wants the sourcing narrative, approval posture, and dependency logic behind Golden Harvest Produce.",
        },
        "02_crm/04_deals": {
            "folders_eyebrow": "Deal Lanes",
            "folders_title": "Open the live and retained deal lanes that shape current commercial posture.",
            "folders_copy": "These cards separate active deal movement from retained wins and lost-deal learning so the founder can widen commercial review without losing chronology or posture.",
            "docs_eyebrow": "Deal Hub Memo",
            "docs_title": "Open the deal-hub memo before widening lane review.",
            "docs_copy": "Use this readable layer when the founder wants the commercial map behind active, won, and lost deal lanes before dropping into a specific deal surface.",
        },
        "02_crm/04_deals/won": {
            "folders_eyebrow": "Reference Win Room",
            "folders_title": "Open the retained commercial win that still matters for precedent and replication.",
            "folders_copy": "This lane keeps the founder inside preserved commercial wins by separating the reference room from live deal pressure and from recovery learning surfaces.",
            "docs_eyebrow": "Won Deal Memo",
            "docs_title": "Open the retained-win memo before widening precedent review.",
            "docs_copy": "Use this readable layer when the founder wants the preserved commercial win, reference route, and replication context without reopening raw repository notes.",
        },
        "02_crm/04_deals/lost": {
            "folders_eyebrow": "Recovery Learning Room",
            "folders_title": "Open the missed commercial matter that still matters for accountability and future resets.",
            "folders_copy": "This lane keeps the founder inside recovery learning by separating the lost-deal room from live commitment pressure and from retained-win precedent.",
            "docs_eyebrow": "Lost Deal Memo",
            "docs_title": "Open the recovery-learning memo before widening loss review.",
            "docs_copy": "Use this readable layer when the founder wants the missed commercial record, learning route, and reset posture without dropping into raw repository notes.",
        },
        "02_crm/04_deals/won/DEAL-2026-003_HarborFresh_Garlic": {
            "folders_eyebrow": "Reference Module",
            "folders_title": "Open the retained execution handoff that still explains why this win mattered.",
            "folders_copy": "This room keeps the founder inside the preserved win record by separating the trade-review module from the room memo and the wider deal lanes.",
            "docs_eyebrow": "Room Memo",
            "docs_title": "Open the reference-win memo before widening precedent review.",
            "docs_copy": "Use this readable layer when the founder wants the retained narrative, handoff logic, and precedent value behind Harbor Fresh Garlic.",
        },
        "02_crm/04_deals/won/DEAL-2026-003_HarborFresh_Garlic/PROFIT-2026-001_HarborFresh-Garlic-Trade-Review": {
            "docs_eyebrow": "Trade Review Memo",
            "docs_title": "Open the trade-review memo before widening retained win review.",
            "docs_copy": "Use this readable layer when the founder wants the margin variance, handoff logic, and precedent signal behind Harbor Fresh Garlic.",
        },
        "02_crm/04_deals/lost/DEAL-2026-002_CrescentMarket_Ginger": {
            "docs_eyebrow": "Learning Memo",
            "docs_title": "Open the recovery memo before widening loss review.",
            "docs_copy": "Use this readable layer when the founder wants the retained miss record, reset logic, and commercial lesson behind Crescent Market Ginger.",
        },
        "02_crm/04_deals/active": {
            "folders_eyebrow": "Deal Rooms",
            "folders_title": "Open the live deal room that still carries pricing, release priority, and outbound commitment.",
            "folders_copy": "This lane keeps the founder inside current commercial movement by separating the live deal room from the broader CRM tree and from the route stack that widens the answer.",
            "docs_eyebrow": "Deal Memo",
            "docs_title": "Open the active-deal memo and founder route brief.",
            "docs_copy": "Use this readable layer when the founder wants the current deal brief, route stack, and outbound posture without dropping into raw repository wording.",
        },
        TASKS_RELATIVE: {
            "folders_eyebrow": "Execution Queues",
            "folders_title": "Open the live founder queue and the routes that decide whether the task should close, hold, or escalate.",
            "folders_copy": "This lane keeps task review explicit by separating the live queue from the executable-check and owner-accountability routes that confirm closure discipline.",
        },
        TASK_ROOM_RELATIVE: {
            "docs_eyebrow": "Execution Brief",
            "docs_title": "Open the governed execution brief before widening gate closure or owner-accountability review.",
            "docs_copy": "Use this reading layer when the founder wants the live blocker, required proof, and follow-through basis behind the Founder Execution Queue.",
        },
        TRACEABILITY_RELATIVE: {
            "folders_eyebrow": "Traceability Rooms",
            "folders_title": "Open the governed lot-path room and the routes that decide whether proof is strong enough to defend movement or challenge.",
            "folders_copy": "This lane keeps proof-chain review explicit by separating the live traceability room from the compliance and recovery routes that confirm audit readiness.",
        },
        TRACEABILITY_ROOM_RELATIVE: {
            "docs_eyebrow": "Traceability Brief",
            "docs_title": "Open the governed traceability brief before widening audit defense or recovery review.",
            "docs_copy": "Use this reading layer when the founder wants the live lot path, retrieval proof, and challenge-readiness logic behind Golden Harvest Garlic.",
        },
        "03_operations": {
            "folders_eyebrow": "Execution Surfaces",
            "folders_title": "Open the execution surfaces that carry movement, packet, and purchasing control.",
            "folders_copy": "These cards separate shipments, purchasing, warehouse, and document operations so the founder can reach the live execution surface without drifting through support folders.",
            "docs_eyebrow": "Operations Guidance",
            "docs_title": "Open the operations overview and support layers.",
            "docs_copy": "Use these readable layers when the founder wants the written operating map behind live shipment rooms, packet control, and purchasing surfaces.",
        },
        "03_operations/03_shipments": {
            "folders_eyebrow": "Shipment Lanes",
            "folders_title": "Open the live shipment surfaces that carry movement, release, and packet proof.",
            "folders_copy": "These cards keep shipment navigation at the right altitude by separating the active shipment lane from the founder route stack behind it.",
        },
        "03_operations/03_shipments/active": {
            "folders_eyebrow": "Shipment Rooms",
            "folders_title": "Open the live shipment room that still carries release readiness, payment proof, and packet control.",
            "folders_copy": "These cards keep the founder inside the active movement lane while the release, packet, and review modules stay grouped under one live shipment room.",
            "docs_eyebrow": "Shipment Brief",
            "docs_title": "Open the shipment memo before widening release or proof review.",
            "docs_copy": "Use this readable layer when the founder needs the written movement brief behind the live shipment room and its release lanes.",
        },
        WORKING_FILES_RELATIVE: {
            "docs_eyebrow": "Staging Memo",
            "docs_title": "Open the staging memo before treating any support file as settled.",
            "docs_copy": "Use this memo when the founder needs the operating rule for temporary trackers, support records, and relocation discipline before closeout.",
        },
        "04_compliance": {
            "folders_eyebrow": "Compliance Surfaces",
            "folders_title": "Open the compliance surfaces that carry proof, readiness, and recovery.",
            "folders_copy": "These cards separate traceability, inspections, supplier approval, and complaint recovery so the founder can move directly to the right governed control surface.",
            "docs_eyebrow": "Compliance Guidance",
            "docs_title": "Open the compliance overview and support layers.",
            "docs_copy": "Use these readable layers when the founder wants the written compliance map behind proof, CAPA, supplier control, and inspection recovery.",
        },
        "04_compliance/05_inspections": {
            "folders_eyebrow": "Case Surfaces",
            "folders_title": "Open the governed complaint and readiness rooms through branded case surfaces.",
            "folders_copy": "These cards separate the live claim room from the FDA-readiness room so the founder can move directly into the right case answer without reopening the full compliance tree.",
        },
        "04_compliance/06_supplier-approval": {
            "folders_eyebrow": "Governed Supplier Rooms",
            "folders_title": "Open the supplier-governance room that carries approval, performance, and resilience review.",
            "folders_copy": "This lane keeps supplier governance readable by separating the governed Golden Harvest room from the wider compliance tree and the boards that confirm performance and backup coverage.",
        },
        "00_brand/01_assets/04_signatures": {
            "docs_eyebrow": "Signature Reference",
            "docs_title": "Open the memo behind approved signature treatments.",
            "docs_copy": "Use this reference memo when the founder needs approved signature hierarchy, identity closure, and outbound-use guidance in one reading surface.",
        },
        "00_brand/01_assets/05_approved-compositions": {
            "docs_eyebrow": "Composition Reference",
            "docs_title": "Open the memo behind approved lockups and seal treatments.",
            "docs_copy": "Use this reference memo when the founder needs approved lockups, seals, and header-use guidance in one reading surface.",
        },
        "05_sops": {
            "folders_eyebrow": "Procedure Surfaces",
            "folders_title": "Open the SOP surfaces that govern how the system should move.",
            "folders_copy": "These cards separate written operating standards by domain so the founder can reach the exact procedure that governs a record, room, or control layer.",
            "docs_eyebrow": "SOP Guidance",
            "docs_title": "Open the SOP overview and support layers.",
            "docs_copy": "Use these readable layers when the founder wants the narrative frame behind the written standards before opening a specific procedure family.",
        },
        "06_dashboard": {
            "folders_eyebrow": "Control Surfaces",
            "folders_title": "Open the executive boards and control towers that summarize live posture.",
            "folders_copy": "These cards separate dashboard families so the founder can move directly into the right command surface for review, escalation, or operating control.",
            "docs_eyebrow": "Dashboard Guidance",
            "docs_title": "Open the dashboard overview and support layers.",
            "docs_copy": "Use these readable layers when the founder wants the written control map behind the board network before opening a specific dashboard family.",
        },
        "07_archive": {
            "folders_eyebrow": "Archive Surfaces",
            "folders_title": "Open the retained record surfaces that preserve institutional memory.",
            "folders_copy": "These cards separate archived histories so the founder can review prior records and closed matters without disturbing the active operating layer.",
            "docs_eyebrow": "Archive Guidance",
            "docs_title": "Open the archive overview and support layers.",
            "docs_copy": "Use these readable layers when the founder wants the written map behind retained records, governed history, and closed-matter continuity.",
        },
        ARCHIVED_CRM_RELATIVE: {
            "folders_eyebrow": "Retained Deal Rooms",
            "folders_title": "Open the retained commercial room and the archive routes that preserve final deal memory.",
            "folders_copy": "This lane keeps archive review explicit by separating the closed deal room from archive closeout standards, live CRM reference, and retained commercial history.",
        },
        ARCHIVED_CLOSED_DEAL_RELATIVE: {
            "docs_eyebrow": "Closed Deal Memo",
            "docs_title": "Open the retained deal memo before using this history for precedent, review, or archive retrieval.",
            "docs_copy": "Use this memo when the founder needs final commercial context, retained proof, and closeout posture without reopening the active CRM layer.",
        },
        "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution": {
            "folders_eyebrow": "Account Modules",
            "folders_title": "Open the account modules that explain Atlantic Foods end to end.",
            "folders_copy": "These modules separate trust, exposure, collections, concentration, and release logic so the founder can open the right customer lens immediately.",
            "docs_eyebrow": "Executive Briefs",
            "docs_title": "Open the account brief and live narrative artifacts.",
            "docs_copy": "Use these readable files when the founder wants the written case summary behind the customer room, not just the control modules.",
        },
        "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic": {
            "folders_eyebrow": "Deal Modules",
            "folders_title": "Open the live deal modules that govern control, commitment, and outbound execution.",
            "folders_copy": "These modules isolate the exact workstreams inside the Atlantic Foods garlic deal so the founder can move straight to the right live issue.",
            "docs_eyebrow": "Deal Briefs",
            "docs_title": "Open the readable deal narrative and decision notes.",
            "docs_copy": "Use these readable files when the founder wants the written context that sits behind the deal war room and its linked controls.",
        },
        "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA": {
            "folders_eyebrow": "Shipment Modules",
            "folders_title": "Open the shipment modules that control release, packet proof, and post-move review.",
            "folders_copy": "These modules separate the live shipment into release, funding, document, communication, and review tracks so operations stays readable under pressure.",
            "docs_eyebrow": "Shipment Briefs",
            "docs_title": "Open the shipment brief and live narrative artifacts.",
            "docs_copy": "Use these readable files when the founder wants the written operating brief behind the shipment room and its release logic.",
        },
        "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim": {
            "folders_eyebrow": "Claim Modules",
            "folders_title": "Open the complaint modules that carry containment, recovery, and proof.",
            "folders_copy": "These modules keep the claim readable by separating corrective action, recovery, and the underlying complaint record into distinct operating tracks.",
            "docs_eyebrow": "Claim Briefs",
            "docs_title": "Open the readable complaint brief and supporting narrative.",
            "docs_copy": "Use these readable files when the founder wants the written complaint record behind the recovery and CAPA layers.",
        },
        "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce": {
            "folders_eyebrow": "Supplier Review Modules",
            "folders_title": "Open the review modules that decide whether Golden Harvest stays approved, resilient, and founder-safe.",
            "folders_copy": "These modules keep supplier governance readable by separating scorecard discipline from backup-sourcing resilience while the room still carries the full approval answer.",
        },
    }
    return profiles.get(relative)


def build_folder_card_profile(current_dir: Path, directory: Path) -> dict[str, str] | None:
    if current_dir == REPO_ROOT:
        return None
    relative_parent = current_dir.relative_to(REPO_ROOT).as_posix()
    child_name = directory.name
    profiles = {
        "03_operations": {
            "03_shipments": {
                "title": "Shipment Hub",
                "copy": "Open the shipment hub for live movement lanes, release gates, packet proof, and founder intervention routes.",
                "pill": "Movement Hub",
                "cta": "Open Shipment Hub",
            },
        },
        "03_operations/03_shipments": {
            "active": {
                "title": "Active Shipments",
                "copy": "Open the active shipment lane for the live brief, release stack, packet proof, and the current movement room.",
                "pill": "Shipment Lane",
                "cta": "Open Active Shipments",
            },
        },
        "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution": {
            "ACCT-2026-Q2_AtlanticFoods-Account-Review": {
                "title": "Account Review Module",
                "copy": "Open the core account-review module for current posture, relationship quality, and commercial standing.",
                "pill": "Account Module",
                "cta": "Open Review Module",
            },
            "CASH-2026-005_AtlanticFoods-Cash-Outlook": {
                "title": "Cash Outlook Module",
                "copy": "Open the customer-specific cash outlook that ties Atlantic Foods timing to liquidity visibility and pressure.",
                "pill": "Cash Module",
                "cta": "Open Cash Module",
            },
            "COLLECT-2026-001_April-Receivable": {
                "title": "Collections Module",
                "copy": "Open the receivables and collection module for current invoices, chase rhythm, and expected recovery timing.",
                "pill": "Collections Module",
                "cta": "Open Collections Module",
            },
            "CONC-2026-Q2_AtlanticFoods-Revenue-Concentration": {
                "title": "Concentration Module",
                "copy": "Open the revenue concentration module to see how much strategic weight Atlantic Foods should carry right now.",
                "pill": "Concentration Module",
                "cta": "Open Concentration Module",
            },
            "CREDIT-2026-001_AtlanticFoods-Release-Control": {
                "title": "Credit Control Module",
                "copy": "Open the release-control module that governs exposure, override logic, and whether this account can widen safely.",
                "pill": "Credit Module",
                "cta": "Open Credit Module",
            },
            "CTRUST-2026-Q2_AtlanticFoods-Relationship-Trust-Review": {
                "title": "Trust Review Module",
                "copy": "Open the institutional trust review for response quality, confidence level, and relationship fragility.",
                "pill": "Trust Module",
                "cta": "Open Trust Module",
            },
            "TPST-2026-Q2_AtlanticFoods-Trust-Posture": {
                "title": "Trust Posture Module",
                "copy": "Open the trust-tier module that converts relationship quality into release posture and growth consequence.",
                "pill": "Posture Module",
                "cta": "Open Posture Module",
            },
        },
        "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic": {
            "ACCTY-2026-Q3_AtlanticFoods-Follow-Through": {
                "title": "Owner Follow-Through Module",
                "copy": "Open the follow-through module for execution ownership, timing, and accountability drift on the live deal.",
                "pill": "Owner Module",
                "cta": "Open Owner Module",
            },
            "ALLOC-2026-Q2_AtlanticFoods-Release-Priority": {
                "title": "Release Priority Module",
                "copy": "Open the capital and release-priority module that ranks this deal against competing matters.",
                "pill": "Priority Module",
                "cta": "Open Priority Module",
            },
            "ASSUMP-2026-Q2_AtlanticFoods-Q3-Assumptions": {
                "title": "Assumptions Module",
                "copy": "Open the assumptions module to review what still has to prove true before the deal can widen safely.",
                "pill": "Assumption Module",
                "cta": "Open Assumption Module",
            },
            "COMM-2026-001_AtlanticFoods-Formal-Offer-Packet": {
                "title": "Formal Offer Packet Module",
                "copy": "Open the send-ready packet that carries the outward offer layer for this deal.",
                "pill": "Outbound Module",
                "cta": "Open Packet Module",
            },
            "COMMCTRL-2026-Q2_AtlanticFoods-Communication-Control": {
                "title": "Communication Control Module",
                "copy": "Open the communication-control module for what has been sent, what is pending, and what still requires disciplined reply.",
                "pill": "Communication Module",
                "cta": "Open Communication Module",
            },
            "COMMSTYLE-2026-Q2_AtlanticFoods-Institutional-Language-Reference": {
                "title": "Language Reference Module",
                "copy": "Open the institutional language reference that keeps this deal sounding bank-grade and controlled.",
                "pill": "Language Module",
                "cta": "Open Language Module",
            },
            "DEC-2026-001_AtlanticFoods-Founder-Decisions": {
                "title": "Founder Decision Module",
                "copy": "Open the founder decision register for this deal's active approvals, overrides, and commitments.",
                "pill": "Decision Module",
                "cta": "Open Decision Module",
            },
            "EXC-2026-Q2_AtlanticFoods-Exception-Review": {
                "title": "Exception Review Module",
                "copy": "Open the exception module when the deal is moving under non-standard conditions or override logic.",
                "pill": "Exception Module",
                "cta": "Open Exception Module",
            },
            "EXECCHK-2026-001_AtlanticFoods-Override-Closure": {
                "title": "Executable Check Module",
                "copy": "Open the executable-check module for the exact closure proof needed before the deal can proceed.",
                "pill": "Check Module",
                "cta": "Open Check Module",
            },
            "MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control": {
                "title": "Matter Control Module",
                "copy": "Open the matter-control spine that keeps the live deal synchronized across all linked controls.",
                "pill": "Control Module",
                "cta": "Open Control Module",
            },
            "PRICE-2026-001_AtlanticFoods-Garlic-Pricing-Review": {
                "title": "Pricing Review Module",
                "copy": "Open the pricing module for current economics, commercial discipline, and quote confidence.",
                "pill": "Pricing Module",
                "cta": "Open Pricing Module",
            },
            "PVAR-2026-Q3_AtlanticFoods-Recovery-Path": {
                "title": "Recovery Path Module",
                "copy": "Open the variance and recovery module to see how the deal returns to plan when it slips.",
                "pill": "Recovery Module",
                "cta": "Open Recovery Module",
            },
            "RESP-2026-Q2_AtlanticFoods-Response-SLA": {
                "title": "Response SLA Module",
                "copy": "Open the response-discipline module for reminder cadence, silence risk, and escalation timing.",
                "pill": "Response Module",
                "cta": "Open Response Module",
            },
            "SCEN-2026-Q2_AtlanticFoods-Cash-Stress-Response": {
                "title": "Scenario Response Module",
                "copy": "Open the scenario module for downside response, containment logic, and founder contingency planning.",
                "pill": "Scenario Module",
                "cta": "Open Scenario Module",
            },
        },
        "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA": {
            "COMM-2026-002_GoldenHarvest-Supplier-Release-Packet": {
                "title": "Supplier Release Packet Module",
                "copy": "Open the supplier-facing packet that controls what may be communicated outwardly on this shipment.",
                "pill": "Supplier Module",
                "cta": "Open Supplier Module",
            },
            "DOCCTRL-2026-001_Garlic-Export-Packet": {
                "title": "Export Packet Module",
                "copy": "Open the core shipment packet module that holds the export document spine for this move.",
                "pill": "Packet Module",
                "cta": "Open Packet Module",
            },
            "FUND-2026-001_Garlic-Payment-Release": {
                "title": "Funding Release Module",
                "copy": "Open the payment-release module for supplier funding logic, timing, and trust-linked cash controls.",
                "pill": "Funding Module",
                "cta": "Open Funding Module",
            },
            "REL-2026-001_Pre-Shipment-Release": {
                "title": "Pre-Shipment Release Module",
                "copy": "Open the live release gate that determines whether this shipment may actually move.",
                "pill": "Release Module",
                "cta": "Open Release Module",
            },
            "SREV-2026-001_Shipment-Review": {
                "title": "Shipment Review Module",
                "copy": "Open the post-shipment review module for evidence, learning capture, and closeout readiness.",
                "pill": "Review Module",
                "cta": "Open Review Module",
            },
        },
        "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim": {
            "CAPA-2026-001_AtlanticFoods-Garlic-Containment-and-Prevention": {
                "title": "CAPA Module",
                "copy": "Open the corrective-action module for containment, preventive action, and owner discipline on the claim.",
                "pill": "CAPA Module",
                "cta": "Open CAPA Module",
            },
            "RECOV-2026-001_AtlanticFoods-Claim-Recovery": {
                "title": "Recovery Module",
                "copy": "Open the recovery module for credit, claim economics, and financial consequence management.",
                "pill": "Recovery Module",
                "cta": "Open Recovery Module",
            },
        },
        "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce": {
            "PERF-2026-Q2_GoldenHarvest-Supplier-Performance": {
                "title": "Supplier Performance Module",
                "copy": "Open the supplier-performance module for scorecard posture, response quality, and whether Golden Harvest still deserves approved-with-controls status.",
                "pill": "Performance Module",
                "cta": "Open Performance Module",
            },
            "CAPACITY-2026-Q2_GoldenHarvest-Backup-Sourcing-Review": {
                "title": "Backup Sourcing Review Module",
                "copy": "Open the backup-sourcing module for capacity confidence, contingency depth, and whether resilience is strong enough to support continued supplier dependence.",
                "pill": "Resilience Module",
                "cta": "Open Resilience Module",
            },
        },
    }
    return profiles.get(relative_parent, {}).get(child_name)


def order_child_directories(current_dir: Path, child_dirs: list[Path]) -> list[Path]:
    relative_parent = current_dir.relative_to(REPO_ROOT).as_posix() if current_dir != REPO_ROOT else ""
    ordered_names = {
        "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution": [
            "ACCT-2026-Q2_AtlanticFoods-Account-Review",
            "CTRUST-2026-Q2_AtlanticFoods-Relationship-Trust-Review",
            "TPST-2026-Q2_AtlanticFoods-Trust-Posture",
            "CREDIT-2026-001_AtlanticFoods-Release-Control",
            "COLLECT-2026-001_April-Receivable",
            "CASH-2026-005_AtlanticFoods-Cash-Outlook",
            "CONC-2026-Q2_AtlanticFoods-Revenue-Concentration",
        ],
        "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic": [
            "MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control",
            "EXECCHK-2026-001_AtlanticFoods-Override-Closure",
            "DEC-2026-001_AtlanticFoods-Founder-Decisions",
            "EXC-2026-Q2_AtlanticFoods-Exception-Review",
            "PRICE-2026-001_AtlanticFoods-Garlic-Pricing-Review",
            "ALLOC-2026-Q2_AtlanticFoods-Release-Priority",
            "ASSUMP-2026-Q2_AtlanticFoods-Q3-Assumptions",
            "PVAR-2026-Q3_AtlanticFoods-Recovery-Path",
            "COMM-2026-001_AtlanticFoods-Formal-Offer-Packet",
            "COMMCTRL-2026-Q2_AtlanticFoods-Communication-Control",
            "RESP-2026-Q2_AtlanticFoods-Response-SLA",
            "COMMSTYLE-2026-Q2_AtlanticFoods-Institutional-Language-Reference",
            "SCEN-2026-Q2_AtlanticFoods-Cash-Stress-Response",
            "ACCTY-2026-Q3_AtlanticFoods-Follow-Through",
        ],
        "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA": [
            "REL-2026-001_Pre-Shipment-Release",
            "FUND-2026-001_Garlic-Payment-Release",
            "DOCCTRL-2026-001_Garlic-Export-Packet",
            "COMM-2026-002_GoldenHarvest-Supplier-Release-Packet",
            "SREV-2026-001_Shipment-Review",
        ],
        "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce": [
            "PERF-2026-Q2_GoldenHarvest-Supplier-Performance",
            "CAPACITY-2026-Q2_GoldenHarvest-Backup-Sourcing-Review",
        ],
        "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim": [
            "CAPA-2026-001_AtlanticFoods-Garlic-Containment-and-Prevention",
            "RECOV-2026-001_AtlanticFoods-Claim-Recovery",
        ],
    }.get(relative_parent, [])
    order_map = {name: index for index, name in enumerate(ordered_names)}
    return sorted(
        child_dirs,
        key=lambda path: (order_map.get(path.name, len(order_map) + 1000), humanize_slug(path.name)),
    )


def build_doc_card_profile(current_dir: Path, markdown_path: Path) -> dict[str, str] | None:
    if markdown_path.name != "README.md" or current_dir == REPO_ROOT:
        return None
    relative_parent = current_dir.relative_to(REPO_ROOT).as_posix()
    profiles = {
        "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution": {
            "kind": "Executive Brief",
            "priority_pill": "Read First",
            "cta": "Open Account Brief",
            "source_cta": "Open Brief Source",
        },
        "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic": {
            "kind": "Executive Brief",
            "priority_pill": "Read First",
            "cta": "Open Deal Brief",
            "source_cta": "Open Brief Source",
        },
        "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA": {
            "kind": "Executive Brief",
            "priority_pill": "Read First",
            "cta": "Open Shipment Brief",
            "source_cta": "Open Brief Source",
        },
        "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim": {
            "kind": "Executive Brief",
            "priority_pill": "Read First",
            "cta": "Open Claim Brief",
            "source_cta": "Open Brief Source",
        },
        "04_compliance/05_inspections/INSP-2026-001_FDA-Readiness-Review": {
            "kind": "Executive Brief",
            "priority_pill": "Read First",
            "cta": "Open Readiness Brief",
            "source_cta": "Open Brief Source",
        },
        "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce": {
            "kind": "Executive Brief",
            "priority_pill": "Read First",
            "cta": "Open Supplier Brief",
            "source_cta": "Open Brief Source",
        },
    }
    direct_profile = profiles.get(relative_parent)
    if direct_profile:
        return direct_profile

    hero_profile = build_portal_hero_context(current_dir)
    if not hero_profile:
        return None

    overview_title = str(hero_profile.get("title", "")).strip() or humanize_surface_name(current_dir.name)
    overview_copy = clamp_summary(
        clean_markdown_summary(
            str(hero_profile.get("note", "")).strip()
            or str(hero_profile.get("copy", "")).strip()
        )
    )
    overview_memo_label = get_overview_memo_label(current_dir, overview_title)
    return {
        "kind": "Overview",
        "title_override": overview_memo_label,
        "cta": f"Open {overview_memo_label}",
        "source_cta": "Open Memo Source",
        "copy_override": overview_copy,
    }


def get_doc_card_surface_pill(current_dir: Path, markdown_path: Path, kind: str) -> str:
    if kind == "Executive Brief":
        return "Brief Layer"
    if kind == "Guidance Standard":
        return "Guidance Standard"
    if kind == "System Rules":
        return "Rule Layer"
    if kind == "Master Template":
        return "Template Layer"
    if kind == "Dashboard":
        return "Control Board"
    if kind == "SOP":
        return "SOP Layer"
    if kind in {"CRM Record", "Operations Record", "Compliance Record"}:
        return kind
    if current_dir == REPO_ROOT and markdown_path.name == "README.md":
        return "System Memo"
    if is_preview_docs_directory(current_dir) and markdown_path.name == "README.md":
        return "Preview Docs"
    hero_profile = build_portal_hero_context(current_dir)
    area = str(hero_profile.get("area", "")).strip() if hero_profile else ""
    if area:
        return area
    return "Readable Layer"


def get_doc_card_source_label(kind: str, markdown_name: str) -> str:
    source_prefix = {
        "Executive Brief": "Brief Source",
        "Guidance Standard": "Guidance Source",
        "System Rules": "Rule Source",
        "Master Template": "Template Source",
        "Dashboard": "Dashboard Source",
        "SOP": "SOP Source",
        "Overview": "Memo Source",
    }.get(kind, "Source Record")
    return f"{source_prefix} / {markdown_name}"


def get_doc_card_source_cta(kind: str) -> str:
    return {
        "Executive Brief": "Open Brief Source",
        "Guidance Standard": "Open Guidance Source",
        "System Rules": "Open Rule Source",
        "Master Template": "Open Template Source",
        "Dashboard": "Open Dashboard Source",
        "SOP": "Open SOP Source",
        "Overview": "Open Memo Source",
    }.get(kind, "Open Source Record")


def get_doc_card_primary_cta(kind: str, surface_pill: str) -> str:
    if kind == "Executive Brief":
        return "Open Executive Brief"
    if kind == "Guidance Standard":
        return "Open Guidance Standard"
    if kind == "System Rules":
        return "Open Rule Layer"
    if kind == "Master Template":
        return "Open Template Layer"
    if kind == "Dashboard":
        return "Open Control Board"
    if kind == "SOP":
        return "Open SOP Layer"
    if kind in {"CRM Record", "Operations Record", "Compliance Record"}:
        return f"Open {kind}"
    if kind == "Overview":
        if surface_pill == "System Memo":
            return "Open System Memo"
        if surface_pill != "Readable Layer":
            return f"Open {surface_pill} Memo"
        return "Open Memo Layer"
    return "Open Readable Layer"


def get_doc_card_kind_label(kind: str, current_dir: Path) -> str:
    if kind == "Overview":
        return "System Memo" if current_dir == REPO_ROOT else "Memo"
    return kind


def get_doc_header_eyebrow(doc_kind: str, current_dir: Path, markdown_path: Path | None = None) -> str:
    if markdown_path:
        guideline_doc = get_brand_guideline_doc_context(markdown_path)
        if guideline_doc:
            return str(guideline_doc["eyebrow"])
        dashboard_doc = get_dashboard_doc_context(markdown_path)
        if dashboard_doc:
            return "Control Board"
        master_template_doc = get_master_template_doc_context(markdown_path)
        if master_template_doc:
            return "Template Master"
        sop_doc = get_sop_doc_context(markdown_path)
        if sop_doc:
            return "Procedure Standard"
    if doc_kind == "Overview":
        active_deal_module = get_active_deal_module_context(current_dir)
        if active_deal_module:
            return f"{str(active_deal_module['module_pill'])} Memo"
        active_shipment_module = get_active_shipment_module_context(current_dir)
        if active_shipment_module:
            return f"{str(active_shipment_module['module_pill'])} Memo"
        active_account_module = get_active_account_module_context(current_dir)
        if active_account_module:
            return f"{str(active_account_module['module_pill'])} Memo"
        active_claim_module = get_active_claim_module_context(current_dir)
        if active_claim_module:
            return f"{str(active_claim_module['module_pill'])} Memo"
        supplier_approval_module = get_supplier_approval_module_context(current_dir)
        if supplier_approval_module:
            return f"{str(supplier_approval_module['module_pill'])} Memo"
        if is_brand_guidelines_directory(current_dir):
            return "Brand Governance Memo"
        if is_dashboard_directory(current_dir):
            return "Dashboard Memo"
        if is_templates_directory(current_dir):
            return "Template Memo"
        if is_sops_directory(current_dir):
            return "SOP Memo"
        try:
            relative = current_dir.relative_to(REPO_ROOT).as_posix()
        except ValueError:
            relative = ""
        if relative == BRAND_RELATIVE:
            return "Brand Memo"
        if relative == BRAND_ASSETS_RELATIVE:
            return "Asset Custody Memo"
        if relative == EXPORTS_RELATIVE:
            return "Exports Memo"
        if relative == PREVIEW_DOCS_RELATIVE:
            return "Preview Docs Memo"
        if relative == VISUAL_STANDARD_RELATIVE:
            return "Visual Standard Memo"
        if relative == CRM_RELATIVE:
            return "CRM Memo"
        if relative == COMPLIANCE_RELATIVE:
            return "Compliance Memo"
        if relative == ARCHIVE_RELATIVE:
            return "Archive Memo"
        if relative == LEAD_ROOM_RELATIVE:
            return "Lead Brief"
        if relative == SUPPLIER_ROOM_RELATIVE:
            return "Supplier Brief"
        if relative == TASK_ROOM_RELATIVE:
            return "Execution Brief"
        if relative == TRACEABILITY_ROOM_RELATIVE:
            return "Traceability Brief"
        if relative == ARCHIVED_CLOSED_DEAL_RELATIVE:
            return "Closed Deal Memo"
        if relative == OPERATIONS_RELATIVE:
            return "Operations Memo"
        if relative == ACTIVE_SHIPMENTS_RELATIVE:
            return "Active Shipment Memo"
        if relative == WORKING_FILES_RELATIVE:
            return "Staging Memo"
        deal_memo_eyebrows = {
            DEALS_RELATIVE: "Deal Hub Memo",
            ACTIVE_DEALS_RELATIVE: "Active Deal Memo",
            WON_DEALS_RELATIVE: "Retained Win Memo",
            LOST_DEALS_RELATIVE: "Recovery Learning Memo",
            WON_DEAL_ROOM_RELATIVE: "Reference Win Memo",
            LOST_DEAL_ROOM_RELATIVE: "Learning Room Memo",
            WON_DEAL_TRADE_REVIEW_RELATIVE: "Trade Review Memo",
        }
        if relative in deal_memo_eyebrows:
            return deal_memo_eyebrows[relative]
        if relative == "00_brand/01_assets/04_signatures":
            return "Signature Reference Memo"
        if relative == "00_brand/01_assets/05_approved-compositions":
            return "Composition Reference Memo"
        return "System Memo" if current_dir == REPO_ROOT else "Layer Memo"
    return doc_kind


def get_doc_card_copy(subtitle: str, kind: str) -> str:
    cleaned = clamp_summary(clean_markdown_summary(subtitle))
    if cleaned:
        return cleaned
    return {
        "Executive Brief": "Use this brief layer before opening live rooms, decisions, and support surfaces.",
        "System Rules": "Use this rule layer to review operating standards without leaving the branded surface.",
        "Master Template": "Use this template layer to review the approved pattern before opening the protected source file.",
        "Overview": "Use this memo layer to stay in the branded reading surface while the source record remains protected.",
    }.get(kind, "Use this readable layer to review the branded record while the protected source stays intact.")


def get_deal_portal_return_profile(relative: str) -> dict[str, str] | None:
    profiles = {
        DEALS_RELATIVE: {
            "eyebrow": "Commercial Return",
            "title": "Close the deal hub on routes that keep live pressure, retained wins, and recovery learning coherent.",
            "copy": "This deal hub now closes on active deals, won deals, lost deals, and the wider CRM hub instead of ending on generic source framing.",
            "card_one_title": "Lane map stays connected",
            "card_one_copy": "Active, won, and lost deal lanes remain visible as one commercial posture map, so founder review can move from live pressure into precedent or learning without losing context.",
            "card_two_title": "CRM context stays visible",
            "card_two_copy": "When deal posture needs wider counterparty context, the founder can return to CRM instead of treating the deal hub as an isolated source layer.",
        },
        ACTIVE_DEALS_RELATIVE: {
            "eyebrow": "Commercial Return",
            "title": "Close active deals on routes that keep live commercial pressure executable.",
            "copy": "This active-deal lane now closes on the lane memo, the live Atlantic Foods room, matter control, and outbound commitment routes instead of ending on generic source framing.",
            "card_one_title": "Live room stays connected",
            "card_one_copy": "The Atlantic Foods room remains the governed live-deal answer behind this lane, so founder review can drop into current pressure without losing the lane map.",
            "card_two_title": "Commitment routes stay visible",
            "card_two_copy": "Matter control, release priority, and offer-packet routing stay adjacent to active deals, keeping commercial movement executable rather than merely readable.",
        },
        WON_DEALS_RELATIVE: {
            "eyebrow": "Commercial Return",
            "title": "Close won deals on routes that keep retained wins useful as precedent.",
            "copy": "This retained-win lane now closes on the Harbor Fresh room, active deals, and the wider deals hub instead of ending on generic source framing.",
            "card_one_title": "Reference room stays connected",
            "card_one_copy": "The Harbor Fresh win remains the preserved commercial example behind this lane, so the founder can reuse precedent without reopening a live commitment path.",
            "card_two_title": "Live posture stays visible",
            "card_two_copy": "Active deals and the wider deal hub remain one step away, keeping retained wins connected to current commercial pressure and replication discipline.",
        },
        LOST_DEALS_RELATIVE: {
            "eyebrow": "Commercial Return",
            "title": "Close lost deals on routes that keep recovery learning actionable.",
            "copy": "This recovery-learning lane now closes on the Crescent Market room, active deals, and the wider deals hub instead of ending on generic source framing.",
            "card_one_title": "Learning room stays connected",
            "card_one_copy": "The Crescent Market miss remains the governed learning record behind this lane, so the founder can inspect what failed without mixing it into active commercial movement.",
            "card_two_title": "Reset routes stay visible",
            "card_two_copy": "Active deals and the wider deal hub remain visible, making the recovery lesson useful for future posture instead of letting the loss become static archive material.",
        },
        WON_DEAL_ROOM_RELATIVE: {
            "eyebrow": "Commercial Return",
            "title": "Close the retained Harbor Fresh room on routes that preserve precedent and execution handoff.",
            "copy": "This reference room now closes on its memo, trade review, won deals, and active deals instead of ending on generic source framing.",
            "card_one_title": "Trade review stays connected",
            "card_one_copy": "The retained economics and execution handoff remain adjacent to the won room, so precedent can be reviewed as an operating pattern, not only a closed story.",
            "card_two_title": "Won and active lanes stay visible",
            "card_two_copy": "The founder can widen from this room into retained wins or active pressure without losing the commercial distinction between precedent and current movement.",
        },
        LOST_DEAL_ROOM_RELATIVE: {
            "eyebrow": "Commercial Return",
            "title": "Close the Crescent Market learning room on routes that preserve loss intelligence.",
            "copy": "This learning room now closes on its memo, lost deals, active deals, and the wider deals hub instead of ending on generic source framing.",
            "card_one_title": "Loss record stays disciplined",
            "card_one_copy": "The miss remains a governed learning room, so the founder can review reset logic and accountability without confusing the record with live deal posture.",
            "card_two_title": "Recovery and live lanes stay visible",
            "card_two_copy": "Lost deals, active deals, and the wider deal hub stay connected, keeping the learning useful for future commercial discipline.",
        },
        WON_DEAL_TRADE_REVIEW_RELATIVE: {
            "eyebrow": "Commercial Return",
            "title": "Close the Harbor Fresh trade review on routes that reconnect retained economics and live pressure.",
            "copy": "This trade-review module now closes on the won room, won deals, and active deals instead of ending on generic source framing.",
            "card_one_title": "Retained economics stay connected",
            "card_one_copy": "The module remains tied to the Harbor Fresh room, so margin variance and handoff logic stay inside the retained commercial narrative.",
            "card_two_title": "Precedent and live posture stay visible",
            "card_two_copy": "Won deals and active deals remain available when the founder needs to turn a retained economics lesson into a current commercial decision pattern.",
        },
    }
    return profiles.get(relative)


def get_doc_card_title(current_dir: Path, markdown_path: Path, title: str, kind: str, surface_pill: str) -> str:
    cleaned = title.strip()
    if markdown_path.name != "README.md" or kind != "Overview" or current_dir == REPO_ROOT:
        return cleaned

    normalized_title = normalize_heading(cleaned)
    structural_titles = {
        normalize_heading(humanize_slug(current_dir.name)),
        normalize_heading(humanize_surface_name(current_dir.name)),
    }
    if normalized_title in structural_titles and surface_pill not in {"Readable Layer", "System Memo"}:
        return f"{surface_pill} Overview"
    return cleaned


def get_overview_display_title(current_dir: Path, title: str) -> str:
    cleaned = title.strip()
    hero_profile = build_portal_hero_context(current_dir)
    if not hero_profile:
        return cleaned

    overview_title = str(hero_profile.get("title", "")).strip() or humanize_surface_name(current_dir.name)
    if not cleaned:
        return overview_title

    normalized_title = normalize_heading(cleaned)
    structural_titles = {
        normalize_heading(humanize_slug(current_dir.name)),
        normalize_heading(humanize_surface_name(current_dir.name)),
        normalize_heading(overview_title),
    }
    placeholder_tokens = {
        "demo",
        "folder",
        "record",
        "preview",
    }
    normalized_words = set(normalized_title.split())
    if normalized_title in structural_titles:
        return overview_title
    if normalized_words & placeholder_tokens:
        return overview_title
    return cleaned


def sort_docs_for_directory(directory: Path, docs: list[dict[str, str]]) -> list[dict[str, str]]:
    def sort_key(item: dict[str, str]) -> tuple[int, str]:
        path = Path(str(item["path"]))
        profile = build_doc_card_profile(directory, path)
        priority = 0 if profile and profile.get("priority_pill") else 1
        return (priority, str(item["title"]))

    return sorted(docs, key=sort_key)


def build_overview_meta_rows(path: Path) -> list[tuple[str, str]]:
    current_dir = path.parent
    hero_profile = build_portal_hero_context(current_dir)
    surface_pill = get_doc_card_surface_pill(current_dir, path, "Overview")
    surface_title = (
        str(hero_profile.get("title", "")).strip()
        if hero_profile and hero_profile.get("title")
        else "UNYRA System"
        if current_dir == REPO_ROOT
        else humanize_surface_name(current_dir.name)
    )
    focus_items = []
    if hero_profile and hero_profile.get("pills"):
        focus_items = [
            label
            for label in (get_profile_pill_label(item) for item in list(hero_profile["pills"]))
            if label
        ]
    if not focus_items:
        focus_items = [surface_title]
    focus_summary = " / ".join(focus_items[:3])
    readable_layers = sum(
        1
        for child in current_dir.iterdir()
        if child.is_file() and child.suffix.lower() == ".md" and child.name not in {"README.md", "AGENTS.md"}
    )
    linked_surfaces = sum(
        1
        for child in current_dir.iterdir()
        if child.is_dir() and child.name not in SKIP_DIR_NAMES
    )
    surface_label = "Connected Surfaces" if linked_surfaces else "Source Route"
    surface_value = str(linked_surfaces) if linked_surfaces else "Source Integrity"
    return [
        ("Memo Type", surface_pill),
        ("Primary Layer", surface_title),
        ("Operating Focus", focus_summary),
        ("Readable Layers", str(readable_layers)),
        (surface_label, surface_value),
        ("Updated", datetime.fromtimestamp(path.stat().st_mtime).strftime("%B %d, %Y")),
    ]


def build_overview_meta_items(path: Path) -> list[dict[str, str]]:
    current_dir = path.parent
    hero_profile = build_portal_hero_context(current_dir)
    relative = current_dir.relative_to(REPO_ROOT).as_posix() if current_dir != REPO_ROOT else ""
    row_map = {label: value for label, value in build_overview_meta_rows(path)}
    base_href = (
        relative_url(current_dir, ROOT_INDEX_PATH)
        if current_dir == REPO_ROOT
        else relative_url(current_dir, current_dir / "OPEN-HERE.html")
    )
    if current_dir == REPO_ROOT:
        system_metrics = get_system_layer_metrics(current_dir)
        return [
            {
                "label": "Memo Type",
                "value": "System Hub",
                "href": f"{base_href}#room-top",
                "cta": "Open System Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "UNYRA System",
                "href": base_href,
                "cta": "Open UNYRA System",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Founder Control / Operating Hubs / Live Decision Routes",
                "href": "06_dashboard/01_executive/Daily-Founder-Dashboard.html",
                "cta": "Open Founder Dashboard",
                "modifier": "focus",
            },
            {
                "label": "Operating Hubs",
                "value": str(system_metrics["operating_hub_count"]),
                "href": f"{base_href}#room-modules",
                "cta": "Open Operating Hubs",
                "modifier": "docs",
            },
            {
                "label": "Founder Cadences",
                "value": str(system_metrics["founder_cadence_count"]),
                "href": "06_dashboard/14_weekly-executive-review/Weekly-Executive-Operating-Review.html",
                "cta": "Open Weekly Review",
                "modifier": "surface",
            },
            {
                "label": "Live Control Routes",
                "value": str(system_metrics["live_control_route_count"]),
                "href": "06_dashboard/33_control-routing/Founder-Control-Routing-Matrix.html",
                "cta": "Open Control Routing",
                "modifier": "source",
            },
        ]
    approved_asset_count = sum(
        1
        for child in current_dir.iterdir()
        if child.is_file() and child.suffix.lower() in {".png", ".jpg", ".jpeg", ".svg", ".webp"}
    )
    if relative == "00_brand/01_assets/04_signatures":
        return [
            {
                "label": "Memo Type",
                "value": "Signature Reference",
                "href": f"{base_href}#room-top",
                "cta": "Open Brand Signatures Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Brand Signatures",
                "href": base_href,
                "cta": "Open Brand Signatures",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Approved Signatures / Identity Closure / Outbound Use",
                "href": "../05_approved-compositions/OPEN-HERE.html",
                "cta": "Open Approved Compositions",
                "modifier": "focus",
            },
            {
                "label": "Approved Signatures",
                "value": str(approved_asset_count),
                "href": base_href,
                "cta": "Open Brand Signatures",
                "modifier": "docs",
            },
            {
                "label": "Asset Hub",
                "value": "Assets",
                "href": "../OPEN-HERE.html",
                "cta": "Open Assets",
                "modifier": "surface",
            },
            {
                "label": "Governance Surface",
                "value": "Visual Standard",
                "href": "../../03_exports/01_visual-standard/OPEN-HERE.html",
                "cta": "Open Visual Standard",
                "modifier": "source",
            },
        ]
    if relative == "00_brand/01_assets/05_approved-compositions":
        return [
            {
                "label": "Memo Type",
                "value": "Composition Reference",
                "href": f"{base_href}#room-top",
                "cta": "Open Approved Compositions Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Approved Compositions",
                "href": base_href,
                "cta": "Open Approved Compositions",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Approved Lockups / Seals / Header Use",
                "href": "../04_signatures/OPEN-HERE.html",
                "cta": "Open Brand Signatures",
                "modifier": "focus",
            },
            {
                "label": "Approved Compositions",
                "value": str(approved_asset_count),
                "href": base_href,
                "cta": "Open Approved Compositions",
                "modifier": "docs",
            },
            {
                "label": "Asset Hub",
                "value": "Assets",
                "href": "../OPEN-HERE.html",
                "cta": "Open Assets",
                "modifier": "surface",
            },
            {
                "label": "Governance Surface",
                "value": "Visual Standard",
                "href": "../../03_exports/01_visual-standard/OPEN-HERE.html",
                "cta": "Open Visual Standard",
                "modifier": "source",
            },
        ]
    if relative == "02_crm/04_deals/won":
        return [
            {
                "label": "Memo Type",
                "value": "Retained Win Lane",
                "href": f"{base_href}#room-top",
                "cta": "Open Won Deals Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Won Deals",
                "href": base_href,
                "cta": "Open Won Deals",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Reference Win / Precedent Route / Narrative Continuity",
                "href": "DEAL-2026-003_HarborFresh_Garlic/OPEN-HERE.html",
                "cta": "Open Harbor Fresh Won Deal",
                "modifier": "focus",
            },
            {
                "label": "Reference Win Rooms",
                "value": "1",
                "href": f"{base_href}#room-modules",
                "cta": "Open Reference Win Room",
                "modifier": "docs",
            },
            {
                "label": "Deal Hub",
                "value": "Deals",
                "href": "../OPEN-HERE.html",
                "cta": "Open Deals",
                "modifier": "surface",
            },
            {
                "label": "Active Deal Lane",
                "value": "Active Deals",
                "href": "../active/OPEN-HERE.html",
                "cta": "Open Active Deals",
                "modifier": "source",
            },
        ]
    if relative == "02_crm/04_deals/lost":
        return [
            {
                "label": "Memo Type",
                "value": "Recovery Learning Lane",
                "href": f"{base_href}#room-top",
                "cta": "Open Lost Deals Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Lost Deals",
                "href": base_href,
                "cta": "Open Lost Deals",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Recovery Learning / Decision Record / Future Reset",
                "href": "DEAL-2026-002_CrescentMarket_Ginger/OPEN-HERE.html",
                "cta": "Open Crescent Market Lost Deal",
                "modifier": "focus",
            },
            {
                "label": "Recovery Learning Rooms",
                "value": "1",
                "href": f"{base_href}#room-modules",
                "cta": "Open Recovery Learning Room",
                "modifier": "docs",
            },
            {
                "label": "Deal Hub",
                "value": "Deals",
                "href": "../OPEN-HERE.html",
                "cta": "Open Deals",
                "modifier": "surface",
            },
            {
                "label": "Active Deal Lane",
                "value": "Active Deals",
                "href": "../active/OPEN-HERE.html",
                "cta": "Open Active Deals",
                "modifier": "source",
            },
        ]
    if relative == "02_crm/04_deals/won/DEAL-2026-003_HarborFresh_Garlic":
        return [
            {
                "label": "Memo Type",
                "value": "Reference Win Room",
                "href": f"{base_href}#room-top",
                "cta": "Open Won Deal Room Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Harbor Fresh Garlic Won Deal Room",
                "href": base_href,
                "cta": "Open Harbor Fresh Garlic Won Deal Room",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Retained Narrative / Trade Review / Execution Handoff",
                "href": "PROFIT-2026-001_HarborFresh-Garlic-Trade-Review/OPEN-HERE.html",
                "cta": "Open Trade Review",
                "modifier": "focus",
            },
            {
                "label": "Reference Module",
                "value": "1",
                "href": "PROFIT-2026-001_HarborFresh-Garlic-Trade-Review/OPEN-HERE.html",
                "cta": "Open Trade Review",
                "modifier": "docs",
            },
            {
                "label": "Won Deal Lane",
                "value": "Won Deals",
                "href": "../OPEN-HERE.html",
                "cta": "Open Won Deals",
                "modifier": "surface",
            },
            {
                "label": "Active Deal Lane",
                "value": "Active Deals",
                "href": "../../active/OPEN-HERE.html",
                "cta": "Open Active Deals",
                "modifier": "source",
            },
        ]
    if relative == "02_crm/04_deals/lost/DEAL-2026-002_CrescentMarket_Ginger":
        return [
            {
                "label": "Memo Type",
                "value": "Recovery Learning Room",
                "href": f"{base_href}#room-top",
                "cta": "Open Lost Deal Room Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Crescent Market Ginger Lost Deal Room",
                "href": base_href,
                "cta": "Open Crescent Market Ginger Lost Deal Room",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Loss Record / Reset Logic / Commercial Lesson",
                "href": base_href,
                "cta": "Open Lost Deal Room",
                "modifier": "focus",
            },
            {
                "label": "Learning Record",
                "value": "Closed Miss",
                "href": base_href,
                "cta": "Open Lost Deal Room",
                "modifier": "docs",
            },
            {
                "label": "Lost Deal Lane",
                "value": "Lost Deals",
                "href": "../OPEN-HERE.html",
                "cta": "Open Lost Deals",
                "modifier": "surface",
            },
            {
                "label": "Active Deal Lane",
                "value": "Active Deals",
                "href": "../../active/OPEN-HERE.html",
                "cta": "Open Active Deals",
                "modifier": "source",
            },
        ]
    if relative == "02_crm/04_deals/won/DEAL-2026-003_HarborFresh_Garlic/PROFIT-2026-001_HarborFresh-Garlic-Trade-Review":
        return [
            {
                "label": "Memo Type",
                "value": "Trade Review Module",
                "href": f"{base_href}#room-top",
                "cta": "Open Trade Review Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Harbor Fresh Garlic Trade Review",
                "href": base_href,
                "cta": "Open Harbor Fresh Garlic Trade Review",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Planned Margin / Realized Margin / Execution Variance",
                "href": "../OPEN-HERE.html",
                "cta": "Open Won Deal Room",
                "modifier": "focus",
            },
            {
                "label": "Reference Win Room",
                "value": "Harbor Fresh Garlic",
                "href": "../OPEN-HERE.html",
                "cta": "Open Won Deal Room",
                "modifier": "docs",
            },
            {
                "label": "Won Deal Lane",
                "value": "Won Deals",
                "href": "../../OPEN-HERE.html",
                "cta": "Open Won Deals",
                "modifier": "surface",
            },
            {
                "label": "Active Deal Lane",
                "value": "Active Deals",
                "href": "../../../active/OPEN-HERE.html",
                "cta": "Open Active Deals",
                "modifier": "source",
            },
        ]
    active_deal_module = get_active_deal_module_context(current_dir)
    if active_deal_module:
        return [
            {
                "label": "Memo Type",
                "value": str(active_deal_module["module_pill"]),
                "href": str(active_deal_module["module_portal_href"]) + "#room-top",
                "cta": f"Open {str(active_deal_module['module_title'])} Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": str(active_deal_module["module_title"]),
                "href": str(active_deal_module["module_portal_href"]),
                "cta": f"Open {str(active_deal_module['module_title'])}",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": f"{str(active_deal_module['room_title'])} / {str(active_deal_module['room_path'])} Path",
                "href": str(active_deal_module["room_entry_href"]),
                "cta": str(active_deal_module["room_entry_label"]),
                "modifier": "focus",
            },
            {
                "label": "Sequence Position",
                "value": str(active_deal_module["sequence_position"]),
                "href": str(active_deal_module["next_action_href"]),
                "cta": str(active_deal_module["next_action_label"]),
                "modifier": "docs",
            },
            {
                "label": "Active Deal Lane",
                "value": "Active Deals",
                "href": str(active_deal_module["active_deals_href"]),
                "cta": "Open Active Deals",
                "modifier": "surface",
            },
            {
                "label": "Deal Hub",
                "value": "Deals",
                "href": str(active_deal_module["deals_href"]),
                "cta": "Open Deals",
                "modifier": "source",
            },
        ]
    active_shipment_module = get_active_shipment_module_context(current_dir)
    if active_shipment_module:
        return [
            {
                "label": "Memo Type",
                "value": str(active_shipment_module["module_pill"]),
                "href": str(active_shipment_module["module_portal_href"]) + "#room-top",
                "cta": f"Open {str(active_shipment_module['module_title'])} Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": str(active_shipment_module["module_title"]),
                "href": str(active_shipment_module["module_portal_href"]),
                "cta": f"Open {str(active_shipment_module['module_title'])}",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": f"{str(active_shipment_module['room_title'])} / {str(active_shipment_module['room_path'])} Path",
                "href": str(active_shipment_module["room_entry_href"]),
                "cta": str(active_shipment_module["room_entry_label"]),
                "modifier": "focus",
            },
            {
                "label": "Sequence Position",
                "value": str(active_shipment_module["sequence_position"]),
                "href": str(active_shipment_module["next_action_href"]),
                "cta": str(active_shipment_module["next_action_label"]),
                "modifier": "docs",
            },
            {
                "label": "Active Shipment Lane",
                "value": "Active Shipments",
                "href": str(active_shipment_module["active_shipments_href"]),
                "cta": "Open Active Shipments",
                "modifier": "surface",
            },
            {
                "label": "Shipment Hub",
                "value": "Shipments",
                "href": str(active_shipment_module["shipments_href"]),
                "cta": "Open Shipments",
                "modifier": "source",
            },
        ]
    active_account_module = get_active_account_module_context(current_dir)
    if active_account_module:
        return [
            {
                "label": "Memo Type",
                "value": str(active_account_module["module_pill"]),
                "href": str(active_account_module["module_portal_href"]) + "#room-top",
                "cta": f"Open {str(active_account_module['module_title'])} Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": str(active_account_module["module_title"]),
                "href": str(active_account_module["module_portal_href"]),
                "cta": f"Open {str(active_account_module['module_title'])}",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": f"{str(active_account_module['room_title'])} / {str(active_account_module['room_path'])} Path",
                "href": str(active_account_module["room_entry_href"]),
                "cta": str(active_account_module["room_entry_label"]),
                "modifier": "focus",
            },
            {
                "label": "Sequence Position",
                "value": str(active_account_module["sequence_position"]),
                "href": str(active_account_module["next_action_href"]),
                "cta": str(active_account_module["next_action_label"]),
                "modifier": "docs",
            },
            {
                "label": "Customer Lane",
                "value": "Customers",
                "href": str(active_account_module["customers_href"]),
                "cta": "Open Customers",
                "modifier": "surface",
            },
            {
                "label": "CRM Hub",
                "value": "CRM",
                "href": str(active_account_module["crm_href"]),
                "cta": "Open CRM",
                "modifier": "source",
            },
        ]
    active_claim_module = get_active_claim_module_context(current_dir)
    if active_claim_module:
        return [
            {
                "label": "Memo Type",
                "value": str(active_claim_module["module_pill"]),
                "href": str(active_claim_module["module_portal_href"]) + "#room-top",
                "cta": f"Open {str(active_claim_module['module_title'])} Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": str(active_claim_module["module_title"]),
                "href": str(active_claim_module["module_portal_href"]),
                "cta": f"Open {str(active_claim_module['module_title'])}",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": f"{str(active_claim_module['room_title'])} / {str(active_claim_module['room_path'])} Path",
                "href": str(active_claim_module["room_entry_href"]),
                "cta": str(active_claim_module["room_entry_label"]),
                "modifier": "focus",
            },
            {
                "label": "Sequence Position",
                "value": str(active_claim_module["sequence_position"]),
                "href": str(active_claim_module["next_action_href"]),
                "cta": str(active_claim_module["next_action_label"]),
                "modifier": "docs",
            },
            {
                "label": "Inspection Lane",
                "value": "Inspection Cases",
                "href": str(active_claim_module["inspection_cases_href"]),
                "cta": "Open Inspection Cases",
                "modifier": "surface",
            },
            {
                "label": "Compliance Hub",
                "value": "Compliance",
                "href": str(active_claim_module["compliance_href"]),
                "cta": "Open Compliance",
                "modifier": "source",
            },
        ]
    supplier_approval_module = get_supplier_approval_module_context(current_dir)
    if supplier_approval_module:
        return [
            {
                "label": "Memo Type",
                "value": str(supplier_approval_module["module_pill"]),
                "href": str(supplier_approval_module["module_portal_href"]) + "#room-top",
                "cta": f"Open {str(supplier_approval_module['module_title'])} Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": str(supplier_approval_module["module_title"]),
                "href": str(supplier_approval_module["module_portal_href"]),
                "cta": f"Open {str(supplier_approval_module['module_title'])}",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": f"{str(supplier_approval_module['room_title'])} / {str(supplier_approval_module['room_path'])} Track",
                "href": str(supplier_approval_module["room_entry_href"]),
                "cta": str(supplier_approval_module["room_entry_label"]),
                "modifier": "focus",
            },
            {
                "label": "Sequence Position",
                "value": str(supplier_approval_module["sequence_position"]),
                "href": str(supplier_approval_module["next_action_href"]),
                "cta": str(supplier_approval_module["next_action_label"]),
                "modifier": "docs",
            },
            {
                "label": "Supplier Lane",
                "value": "Supplier Approval",
                "href": str(supplier_approval_module["supplier_approval_href"]),
                "cta": "Open Supplier Approval",
                "modifier": "surface",
            },
            {
                "label": "Compliance Hub",
                "value": "Compliance",
                "href": str(supplier_approval_module["compliance_href"]),
                "cta": "Open Compliance",
                "modifier": "source",
            },
        ]
    if relative == "02_crm/04_deals":
        return [
            {
                "label": "Memo Type",
                "value": "Deal Hub",
                "href": f"{base_href}#room-top",
                "cta": "Open Deals Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Deals",
                "href": base_href,
                "cta": "Open Deals",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Active Deals / Won Record / Lost Learning",
                "href": "active/OPEN-HERE.html",
                "cta": "Open Active Deals",
                "modifier": "focus",
            },
            {
                "label": "Deal Lanes",
                "value": "3",
                "href": f"{base_href}#room-modules",
                "cta": "Open Deal Lanes",
                "modifier": "docs",
            },
            {
                "label": "Live Deal Lane",
                "value": "Active Deals",
                "href": "active/OPEN-HERE.html",
                "cta": "Open Active Deals",
                "modifier": "surface",
            },
            {
                "label": "Retained Lanes",
                "value": "Won + Lost",
                "href": "won/OPEN-HERE.html",
                "cta": "Open Won Deals",
                "modifier": "source",
            },
        ]
    if relative == "02_crm/04_deals/active":
        return [
            {
                "label": "Memo Type",
                "value": "Deal Flow Lane",
                "href": f"{base_href}#room-top",
                "cta": "Open Active Deals Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Active Deals",
                "href": base_href,
                "cta": "Open Active Deals",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Deal Control / Commitment Routes / Outbound Pack",
                "href": f"{base_href}#featured-routes",
                "cta": "Open Founder Routes",
                "modifier": "focus",
            },
            {
                "label": "Founder Routes",
                "value": "3",
                "href": f"{base_href}#featured-routes",
                "cta": "Open Founder Routes",
                "modifier": "docs",
            },
            {
                "label": "Live Deal Rooms",
                "value": "1",
                "href": f"{base_href}#room-modules",
                "cta": "Open Live Deal Room",
                "modifier": "surface",
            },
            {
                "label": "Communication Route",
                "value": "Formal Offer Packet",
                "href": "DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/OPEN-HERE.html",
                "cta": "Open Formal Offer Packet",
                "modifier": "source",
            },
        ]
    if relative == "03_operations/03_shipments/active":
        return [
            {
                "label": "Memo Type",
                "value": "Active Shipment Lane",
                "href": f"{base_href}#room-top",
                "cta": "Open Active Shipments Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Active Shipments",
                "href": base_href,
                "cta": "Open Active Shipments",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Shipment Brief / Route Lanes / Packet Proof",
                "href": f"{base_href}#featured-routes",
                "cta": "Open Route Lanes",
                "modifier": "focus",
            },
            {
                "label": "Live Shipment Rooms",
                "value": "1",
                "href": f"{base_href}#room-modules",
                "cta": "Open Live Shipment Rooms",
                "modifier": "docs",
            },
            {
                "label": "Route Lanes",
                "value": "3",
                "href": f"{base_href}#featured-routes",
                "cta": "Open Route Lanes",
                "modifier": "surface",
            },
            {
                "label": "Control Surface",
                "value": "Shipment Control Tower",
                "href": "../../../06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html",
                "cta": "Open Shipment Control Tower",
                "modifier": "source",
            },
        ]
    if is_archive_directory(current_dir):
        archive_metrics = get_archive_layer_metrics(current_dir)
        return [
            {
                "label": "Memo Type",
                "value": "Archive Layer",
                "href": f"{base_href}#room-top",
                "cta": "Open Archive Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Archive",
                "href": base_href,
                "cta": "Open Archive",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Archived Matters / Closeout Control / Retrieval Routes",
                "href": "03_crm/OPEN-HERE.html",
                "cta": "Open Archived CRM",
                "modifier": "focus",
            },
            {
                "label": "Archived Matters",
                "value": str(archive_metrics["archived_matter_count"]),
                "href": "03_crm/DEAL-2026-001_AtlanticFoods_Garlic-CLOSED/README.html",
                "cta": "Open Archived Matters",
                "modifier": "docs",
            },
            {
                "label": "Archive Functions",
                "value": str(archive_metrics["archive_function_count"]),
                "href": f"{base_href}#room-modules",
                "cta": "Open Archive Functions",
                "modifier": "surface",
            },
            {
                "label": "Fast Routes",
                "value": str(archive_metrics["fast_route_count"]),
                "href": f"{base_href}#featured-routes",
                "cta": "Open Fast Routes",
                "modifier": "source",
            },
        ]
    if is_sops_directory(current_dir):
        sop_metrics = get_sop_layer_metrics(current_dir)
        return [
            {
                "label": "Memo Type",
                "value": "SOP Layer",
                "href": f"{base_href}#room-top",
                "cta": "Open SOPs Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "SOPs",
                "href": base_href,
                "cta": "Open SOPs",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Founder Cadence / Lifecycle Control / Communication Standards",
                "href": "06_dashboard/Founder-Operating-Cadence-SOP.html",
                "cta": "Open Founder Cadence SOP",
                "modifier": "focus",
            },
            {
                "label": "SOP Surfaces",
                "value": str(sop_metrics["sop_surface_count"]),
                "href": f"{base_href}#room-modules",
                "cta": "Open SOP Surfaces",
                "modifier": "docs",
            },
            {
                "label": "Founder Standards",
                "value": str(sop_metrics["founder_standard_count"]),
                "href": "04_crm/Commercial-Execution-Lifecycle-SOP.html",
                "cta": "Open Founder Standards",
                "modifier": "surface",
            },
            {
                "label": "Fast Routes",
                "value": str(sop_metrics["fast_route_count"]),
                "href": f"{base_href}#featured-routes",
                "cta": "Open Fast Routes",
                "modifier": "source",
            },
        ]
    if is_dashboard_directory(current_dir):
        dashboard_metrics = get_dashboard_layer_metrics(current_dir)
        return [
            {
                "label": "Memo Type",
                "value": "Dashboard Layer",
                "href": f"{base_href}#room-top",
                "cta": "Open Dashboards Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Dashboards",
                "href": base_href,
                "cta": "Open Dashboards",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Founder Control / Cadence Reviews / Executable Checks",
                "href": "01_executive/Daily-Founder-Dashboard.html",
                "cta": "Open Founder Dashboard",
                "modifier": "focus",
            },
            {
                "label": "Dashboard Surfaces",
                "value": str(dashboard_metrics["dashboard_surface_count"]),
                "href": f"{base_href}#room-modules",
                "cta": "Open Dashboard Surfaces",
                "modifier": "docs",
            },
            {
                "label": "Founder Cadences",
                "value": str(dashboard_metrics["founder_cadence_count"]),
                "href": "14_weekly-executive-review/Weekly-Executive-Operating-Review.html",
                "cta": "Open Weekly Review",
                "modifier": "surface",
            },
            {
                "label": "Fast Routes",
                "value": str(dashboard_metrics["fast_route_count"]),
                "href": f"{base_href}#featured-routes",
                "cta": "Open Fast Routes",
                "modifier": "source",
            },
        ]
    if is_compliance_directory(current_dir):
        compliance_metrics = get_compliance_layer_metrics(current_dir)
        return [
            {
                "label": "Memo Type",
                "value": "Compliance Layer",
                "href": f"{base_href}#room-top",
                "cta": "Open Compliance Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Compliance",
                "href": base_href,
                "cta": "Open Compliance",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Governed Cases / Compliance Domains / Fast Routes",
                "href": "05_inspections/OPEN-HERE.html",
                "cta": "Open Inspection Cases",
                "modifier": "focus",
            },
            {
                "label": "Governed Cases",
                "value": str(compliance_metrics["governed_case_count"]),
                "href": "05_inspections/OPEN-HERE.html",
                "cta": "Open Governed Cases",
                "modifier": "docs",
            },
            {
                "label": "Compliance Domains",
                "value": str(compliance_metrics["compliance_domain_count"]),
                "href": f"{base_href}#room-modules",
                "cta": "Open Compliance Domains",
                "modifier": "surface",
            },
            {
                "label": "Fast Routes",
                "value": str(compliance_metrics["fast_route_count"]),
                "href": f"{base_href}#featured-routes",
                "cta": "Open Fast Routes",
                "modifier": "source",
            },
        ]
    if is_operations_directory(current_dir):
        operations_metrics = get_operations_layer_metrics(current_dir)
        return [
            {
                "label": "Memo Type",
                "value": "Operations Layer",
                "href": f"{base_href}#room-top",
                "cta": "Open Operations Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Operations",
                "href": base_href,
                "cta": "Open Operations",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Active Shipments / Founder Control / Working Files",
                "href": "../06_dashboard/03_operations/Daily-Operations-Command-Center.html",
                "cta": "Open Operations Command",
                "modifier": "focus",
            },
            {
                "label": "Active Shipments",
                "value": str(operations_metrics["active_shipment_count"]),
                "href": "03_shipments/active/OPEN-HERE.html",
                "cta": "Open Active Shipments",
                "modifier": "docs",
            },
            {
                "label": "Execution Domains",
                "value": str(operations_metrics["execution_domain_count"]),
                "href": f"{base_href}#room-modules",
                "cta": "Open Execution Domains",
                "modifier": "surface",
            },
            {
                "label": "Fast Routes",
                "value": str(operations_metrics["fast_route_count"]),
                "href": f"{base_href}#featured-routes",
                "cta": "Open Fast Routes",
                "modifier": "source",
            },
        ]
    if is_crm_directory(current_dir):
        crm_metrics = get_crm_layer_metrics(current_dir)
        return [
            {
                "label": "Memo Type",
                "value": "CRM Layer",
                "href": f"{base_href}#room-top",
                "cta": "Open CRM Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "CRM",
                "href": base_href,
                "cta": "Open CRM",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Counterparty Layers / Deal Postures / Founder Queue",
                "href": "04_deals/active/OPEN-HERE.html",
                "cta": "Open Active Deals",
                "modifier": "focus",
            },
            {
                "label": "Counterparty Layers",
                "value": str(crm_metrics["counterparty_layer_count"]),
                "href": "02_customers/OPEN-HERE.html",
                "cta": "Open Counterparty Layers",
                "modifier": "docs",
            },
            {
                "label": "Deal Postures",
                "value": str(crm_metrics["deal_posture_count"]),
                "href": "04_deals/OPEN-HERE.html",
                "cta": "Open Deal Postures",
                "modifier": "surface",
            },
            {
                "label": "Execution Queue",
                "value": str(crm_metrics["execution_queue_count"]),
                "href": "05_tasks/TASK-2026-001_Founder-Execution-Queue/README.html",
                "cta": "Open Founder Queue",
                "modifier": "source",
            },
        ]
    if is_templates_directory(current_dir):
        template_metrics = get_template_layer_metrics(current_dir)
        return [
            {
                "label": "Memo Type",
                "value": "Template Layer",
                "href": f"{base_href}#room-top",
                "cta": "Open Templates Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Templates",
                "href": base_href,
                "cta": "Open Templates",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Protected Masters / Template Domains / Fast Routes",
                "href": f"{base_href}#featured-routes",
                "cta": "Open Fast Routes",
                "modifier": "focus",
            },
            {
                "label": "Master Templates",
                "value": str(template_metrics["master_template_count"]),
                "href": f"{base_href}#room-modules",
                "cta": "Open Template Domains",
                "modifier": "docs",
            },
            {
                "label": "Template Domains",
                "value": str(template_metrics["template_domain_count"]),
                "href": f"{base_href}#room-modules",
                "cta": "Open Template Domains",
                "modifier": "surface",
            },
            {
                "label": "Fast Routes",
                "value": str(template_metrics["fast_route_count"]),
                "href": f"{base_href}#featured-routes",
                "cta": "Open Fast Routes",
                "modifier": "source",
            },
        ]
    if is_brand_assets_directory(current_dir):
        asset_metrics = get_brand_assets_metrics(current_dir)
        current_doc_href = relative_url(current_dir, path.with_suffix(".html"))
        return [
            {
                "label": "Memo Type",
                "value": "Asset Layer",
                "href": f"{base_href}#room-top",
                "cta": "Open Assets Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Assets",
                "href": base_href,
                "cta": "Open Assets",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Review Surfaces / Protected Sets / Brand Control",
                "href": f"{base_href}#room-modules",
                "cta": "Open Review Surfaces",
                "modifier": "focus",
            },
            {
                "label": "Asset Sets",
                "value": str(asset_metrics["asset_set_count"]),
                "href": f"{current_doc_href}#doc-reading-surface",
                "cta": "Open Asset Memo",
                "modifier": "docs",
            },
            {
                "label": "Review Surfaces",
                "value": str(asset_metrics["review_surface_count"]),
                "href": f"{base_href}#room-modules",
                "cta": "Open Review Surfaces",
                "modifier": "surface",
            },
            {
                "label": "Protected Sets",
                "value": str(asset_metrics["protected_set_count"]),
                "href": f"{current_doc_href}#doc-reading-surface",
                "cta": "Open Protected Sets",
                "modifier": "source",
            },
        ]
    if is_brand_directory(current_dir):
        brand_metrics = get_brand_layer_metrics(current_dir)
        return [
            {
                "label": "Memo Type",
                "value": "Brand Layer",
                "href": f"{base_href}#room-top",
                "cta": "Open Brand Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Brand",
                "href": base_href,
                "cta": "Open Brand",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Approved Assets / Guidance Rules / Export Governance",
                "href": "01_assets/OPEN-HERE.html",
                "cta": "Open Assets",
                "modifier": "focus",
            },
            {
                "label": "Asset Sets",
                "value": str(brand_metrics["asset_set_count"]),
                "href": "01_assets/OPEN-HERE.html",
                "cta": "Open Assets",
                "modifier": "docs",
            },
            {
                "label": "Guidance Standards",
                "value": str(brand_metrics["guidance_count"]),
                "href": "02_guidelines/OPEN-HERE.html",
                "cta": "Open Brand Guidelines",
                "modifier": "surface",
            },
            {
                "label": "Preview Benchmarks",
                "value": str(brand_metrics["preview_benchmark_count"]),
                "href": "03_exports/OPEN-HERE.html",
                "cta": "Open Exports",
                "modifier": "source",
            },
        ]
    if is_preview_docs_directory(current_dir):
        preview_metrics = get_preview_hub_metrics(current_dir)
        return [
            {
                "label": "Memo Type",
                "value": "Preview Docs",
                "href": f"{base_href}#room-top",
                "cta": "Open Preview Docs Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Preview Docs",
                "href": base_href,
                "cta": "Open Preview Docs",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Founder Pathways / Domain Lanes / Brand Anchors",
                "href": "index.html#founder-pathways",
                "cta": "Open Founder Pathways",
                "modifier": "focus",
            },
            {
                "label": "Founder Pathways",
                "value": str(preview_metrics["pathway_count"]),
                "href": "index.html#founder-pathways",
                "cta": "Open Founder Pathways",
                "modifier": "docs",
            },
            {
                "label": "Domain Lanes",
                "value": str(preview_metrics["domain_lane_count"]),
                "href": "index.html#full-catalog",
                "cta": "Open Domain Lanes",
                "modifier": "surface",
            },
            {
                "label": "Brand Anchors",
                "value": str(preview_metrics["brand_anchor_count"]),
                "href": "index.html#brand-anchors",
                "cta": "Open Brand Anchors",
                "modifier": "source",
            },
        ]
    if is_exports_directory(current_dir):
        export_metrics = get_exports_metrics(current_dir)
        return [
            {
                "label": "Memo Type",
                "value": "Export Layer",
                "href": f"{base_href}#room-top",
                "cta": "Open Exports Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Exports",
                "href": base_href,
                "cta": "Open Exports",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Preview Docs / Domain Lanes / Visual Standard",
                "href": "02_preview-docs/OPEN-HERE.html",
                "cta": "Open Preview Docs",
                "modifier": "focus",
            },
            {
                "label": "Preview Benchmarks",
                "value": str(export_metrics["benchmark_count"]),
                "href": "02_preview-docs/OPEN-HERE.html",
                "cta": "Open Preview Docs",
                "modifier": "docs",
            },
            {
                "label": "Domain Lanes",
                "value": str(export_metrics["domain_lane_count"]),
                "href": "02_preview-docs/index.html#full-catalog",
                "cta": "Open Domain Lanes",
                "modifier": "surface",
            },
            {
                "label": "Governance Surface",
                "value": "Visual Standard",
                "href": "01_visual-standard/OPEN-HERE.html",
                "cta": "Open Visual Standard",
                "modifier": "source",
            },
        ]
    if is_brand_guidelines_directory(current_dir):
        guidance_metrics = get_brand_guidelines_metrics(current_dir)
        return [
            {
                "label": "Memo Type",
                "value": "Brand Guidance",
                "href": f"{base_href}#room-top",
                "cta": "Open Brand Guidelines Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Brand Guidelines",
                "href": base_href,
                "cta": "Open Brand Guidelines",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Identity Rules / Document Standard / Voice Discipline",
                "href": f"{base_href}#supporting-files",
                "cta": "Open Guidance Standards",
                "modifier": "focus",
            },
            {
                "label": "Guidance Standards",
                "value": str(guidance_metrics["guidance_count"]),
                "href": f"{base_href}#supporting-files",
                "cta": "Open Guidance Standards",
                "modifier": "docs",
            },
            {
                "label": "Governance Surface",
                "value": "Visual Standard",
                "href": "../03_exports/01_visual-standard/OPEN-HERE.html",
                "cta": "Open Visual Standard",
                "modifier": "surface",
            },
            {
                "label": "Reference Layer",
                "value": "Exports",
                "href": "../03_exports/OPEN-HERE.html",
                "cta": "Open Exports",
                "modifier": "source",
            },
        ]
    if is_visual_standard_directory(current_dir):
        preview_metrics = get_preview_hub_metrics(REPO_ROOT / PREVIEW_DOCS_RELATIVE)
        return [
            {
                "label": "Memo Type",
                "value": "Visual Standard Layer",
                "href": f"{base_href}#room-top",
                "cta": "Open Visual Standard Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Visual Standard",
                "href": base_href,
                "cta": "Open Visual Standard",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Design Standard / Preview Governance / Export Styling",
                "href": "../02_preview-docs/OPEN-HERE.html",
                "cta": "Open Preview Docs",
                "modifier": "focus",
            },
            {
                "label": "Preview Benchmarks",
                "value": str(preview_metrics["benchmark_count"]),
                "href": "../02_preview-docs/index.html#full-catalog",
                "cta": "Open Domain Lanes",
                "modifier": "docs",
            },
            {
                "label": "Reference Surface",
                "value": "Export Hub",
                "href": "../OPEN-HERE.html",
                "cta": "Open Exports",
                "modifier": "surface",
            },
            {
                "label": "Updated",
                "value": row_map.get("Updated", ""),
                "href": "README.md",
                "cta": "Open Memo Source",
                "modifier": "source",
            },
        ]
    top_href = f"{base_href}#room-top"
    surface_title = row_map.get("Primary Layer", "").strip() or (
        str(hero_profile.get("title", "")).strip()
        if hero_profile and hero_profile.get("title")
        else humanize_surface_name(current_dir.name)
    )
    readable_layers = sum(
        1
        for child in current_dir.iterdir()
        if child.is_file() and child.suffix.lower() == ".md" and child.name not in {"README.md", "AGENTS.md"}
    )
    connected_surfaces = sum(
        1
        for child in current_dir.iterdir()
        if child.is_dir() and child.name not in SKIP_DIR_NAMES
    )
    primary_cta = (
        "Open UNYRA System"
        if current_dir == REPO_ROOT
        else str(hero_profile.get("cta") or "").strip() or f"Open {surface_title}"
    )
    top_cta = "Open System Top" if current_dir == REPO_ROOT else f"Open {surface_title} Top"
    if relative == LEAD_ROOM_RELATIVE:
        return [
            {
                "label": "Memo Type",
                "value": row_map.get("Memo Type", ""),
                "href": top_href,
                "cta": top_cta,
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": row_map.get("Primary Layer", ""),
                "href": base_href,
                "cta": primary_cta,
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": row_map.get("Operating Focus", ""),
                "href": f"{base_href}#visual-system",
                "cta": "Open Room Return",
                "modifier": "focus",
            },
            {
                "label": "Founder Routes",
                "value": "4",
                "href": "#doc-source-route",
                "cta": "Open Lead Return",
                "modifier": "docs",
            },
            {
                "label": "Return Surface",
                "value": "Lead Return",
                "href": "#doc-source-route",
                "cta": "Open Lead Return",
                "modifier": "surface",
            },
            {
                "label": "Updated",
                "value": row_map.get("Updated", ""),
                "href": "README.md",
                "cta": "Open Memo Source",
                "modifier": "source",
            },
        ]
    if relative == SUPPLIER_ROOM_RELATIVE:
        return [
            {
                "label": "Memo Type",
                "value": row_map.get("Memo Type", ""),
                "href": top_href,
                "cta": top_cta,
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": row_map.get("Primary Layer", ""),
                "href": base_href,
                "cta": primary_cta,
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": row_map.get("Operating Focus", ""),
                "href": f"{base_href}#visual-system",
                "cta": "Open Room Return",
                "modifier": "focus",
            },
            {
                "label": "Founder Routes",
                "value": "4",
                "href": "#doc-source-route",
                "cta": "Open Supplier Return",
                "modifier": "docs",
            },
            {
                "label": "Return Surface",
                "value": "Supplier Return",
                "href": "#doc-source-route",
                "cta": "Open Supplier Return",
                "modifier": "surface",
            },
            {
                "label": "Updated",
                "value": row_map.get("Updated", ""),
                "href": "README.md",
                "cta": "Open Memo Source",
                "modifier": "source",
            },
        ]
    if relative == TASK_ROOM_RELATIVE:
        return [
            {
                "label": "Memo Type",
                "value": row_map.get("Memo Type", ""),
                "href": top_href,
                "cta": top_cta,
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": row_map.get("Primary Layer", ""),
                "href": base_href,
                "cta": primary_cta,
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": row_map.get("Operating Focus", ""),
                "href": f"{base_href}#visual-system",
                "cta": "Open Room Return",
                "modifier": "focus",
            },
            {
                "label": "Founder Routes",
                "value": "4",
                "href": "#doc-source-route",
                "cta": "Open Execution Return",
                "modifier": "docs",
            },
            {
                "label": "Return Surface",
                "value": "Execution Return",
                "href": "#doc-source-route",
                "cta": "Open Execution Return",
                "modifier": "surface",
            },
            {
                "label": "Updated",
                "value": row_map.get("Updated", ""),
                "href": "README.md",
                "cta": "Open Memo Source",
                "modifier": "source",
            },
        ]
    if relative == TRACEABILITY_ROOM_RELATIVE:
        return [
            {
                "label": "Memo Type",
                "value": row_map.get("Memo Type", ""),
                "href": top_href,
                "cta": top_cta,
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": row_map.get("Primary Layer", ""),
                "href": base_href,
                "cta": primary_cta,
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": row_map.get("Operating Focus", ""),
                "href": f"{base_href}#visual-system",
                "cta": "Open Room Return",
                "modifier": "focus",
            },
            {
                "label": "Founder Routes",
                "value": "4",
                "href": "#doc-source-route",
                "cta": "Open Traceability Return",
                "modifier": "docs",
            },
            {
                "label": "Return Surface",
                "value": "Traceability Return",
                "href": "#doc-source-route",
                "cta": "Open Traceability Return",
                "modifier": "surface",
            },
            {
                "label": "Updated",
                "value": row_map.get("Updated", ""),
                "href": "README.md",
                "cta": "Open Memo Source",
                "modifier": "source",
            },
        ]
    if relative == ARCHIVED_CLOSED_DEAL_RELATIVE:
        return [
            {
                "label": "Memo Type",
                "value": row_map.get("Memo Type", ""),
                "href": top_href,
                "cta": top_cta,
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": row_map.get("Primary Layer", ""),
                "href": base_href,
                "cta": primary_cta,
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": row_map.get("Operating Focus", ""),
                "href": base_href,
                "cta": "Open Closed Deal Room",
                "modifier": "focus",
            },
            {
                "label": "Founder Routes",
                "value": "4",
                "href": "#doc-source-route",
                "cta": "Open Archive Return",
                "modifier": "docs",
            },
            {
                "label": "Return Surface",
                "value": "Archive Return",
                "href": "#doc-source-route",
                "cta": "Open Archive Return",
                "modifier": "surface",
            },
            {
                "label": "Updated",
                "value": row_map.get("Updated", ""),
                "href": "README.md",
                "cta": "Open Memo Source",
                "modifier": "source",
            },
        ]
    if relative == WORKING_FILES_RELATIVE:
        return [
            {
                "label": "Memo Type",
                "value": row_map.get("Memo Type", ""),
                "href": top_href,
                "cta": top_cta,
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": row_map.get("Primary Layer", ""),
                "href": base_href,
                "cta": primary_cta,
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": row_map.get("Operating Focus", ""),
                "href": base_href,
                "cta": "Open Working Files",
                "modifier": "focus",
            },
            {
                "label": "Staging Routes",
                "value": "4",
                "href": "#doc-source-route",
                "cta": "Open Staging Return",
                "modifier": "docs",
            },
            {
                "label": "Return Surface",
                "value": "Staging Return",
                "href": "#doc-source-route",
                "cta": "Open Staging Return",
                "modifier": "surface",
            },
            {
                "label": "Updated",
                "value": row_map.get("Updated", ""),
                "href": "README.md",
                "cta": "Open Memo Source",
                "modifier": "source",
            },
        ]
    readable_cta = (
        "Open Readable Layer"
        if readable_layers == 1
        else "Open Readable Layers"
        if readable_layers > 1
        else "Open Memo Source"
    )
    surface_cta = (
        "Open Surface"
        if connected_surfaces == 1
        else "Open Surfaces"
        if connected_surfaces > 1
        else "Open Source Integrity"
    )

    if current_dir == REPO_ROOT:
        focus_href = f"{base_href}#featured-routes"
        focus_cta = "Open Routes"
    elif connected_surfaces:
        focus_href = f"{base_href}#room-modules"
        focus_cta = surface_cta
    elif readable_layers:
        focus_href = f"{base_href}#supporting-files"
        focus_cta = readable_cta
    else:
        focus_href = f"{base_href}#visual-system"
        focus_cta = "Open Source Integrity"

    readable_href = f"{base_href}#supporting-files" if readable_layers else "README.md"
    surface_href = f"{base_href}#room-modules" if connected_surfaces else f"{base_href}#visual-system"
    updated_href = f"{base_href}#visual-system" if connected_surfaces else "README.md"
    updated_cta = "Open Source Integrity" if connected_surfaces else "Open Memo Source"

    return [
        {
            "label": "Memo Type",
            "value": row_map.get("Memo Type", ""),
            "href": top_href,
            "cta": top_cta,
            "modifier": "layer",
        },
        {
            "label": "Primary Layer",
            "value": row_map.get("Primary Layer", ""),
            "href": base_href,
            "cta": primary_cta,
            "modifier": "subject",
        },
        {
            "label": "Operating Focus",
            "value": row_map.get("Operating Focus", ""),
            "href": focus_href,
            "cta": focus_cta,
            "modifier": "focus",
        },
        {
            "label": "Readable Layers",
            "value": row_map.get("Readable Layers", ""),
            "href": readable_href,
            "cta": readable_cta,
            "modifier": "docs",
        },
        {
            "label": "Connected Surfaces" if connected_surfaces else "Source Route",
            "value": row_map.get("Connected Surfaces", "") if connected_surfaces else row_map.get("Source Route", "Source Integrity"),
            "href": surface_href,
            "cta": surface_cta,
            "modifier": "surface",
        },
        {
            "label": "Updated",
            "value": row_map.get("Updated", ""),
            "href": updated_href,
            "cta": updated_cta,
            "modifier": "source",
        },
    ]


def get_standard_doc_focus_summary(meta: list[tuple[str, str]], subtitle: str) -> str:
    meta_map = meta_to_dict(meta)
    preferred_keys = [
        "Purpose",
        "Use when",
        "Primary decision",
        "Decision",
        "Scope",
        "Audience",
    ]
    for key in preferred_keys:
        value = str(meta_map.get(key, "")).strip()
        if value:
            return clamp_summary(clean_markdown_summary(value))
    for key, value in meta:
        normalized = normalize_heading(key)
        if normalized not in {"status", "source rule", "source note", "source discipline"}:
            cleaned = clamp_summary(clean_markdown_summary(value))
            if cleaned:
                return cleaned
    return clamp_summary(clean_markdown_summary(subtitle))


def get_standard_doc_extra_meta_row(meta: list[tuple[str, str]]) -> tuple[str, str] | None:
    preferred_labels = {
        "source rule",
        "source note",
        "source discipline",
        "prepared for",
        "owner",
        "cadence",
        "review date",
        "frequency",
        "primary decision",
    }
    for key, value in meta:
        normalized = normalize_heading(key)
        if normalized in {"status", "purpose"}:
            continue
        cleaned = clamp_summary(clean_markdown_summary(value))
        if not cleaned:
            continue
        if normalized in preferred_labels:
            return (key, cleaned)
    for key, value in meta:
        normalized = normalize_heading(key)
        if normalized in {"status", "purpose"}:
            continue
        cleaned = clamp_summary(clean_markdown_summary(value))
        if cleaned:
            return (key, cleaned)
    return None


def build_standard_doc_meta_items(path: Path, doc_kind: str, meta: list[tuple[str, str]], subtitle: str) -> list[dict[str, str]]:
    current_dir = path.parent
    hero_profile = build_portal_hero_context(current_dir)
    meta_map = meta_to_dict(meta)
    relative = current_dir.relative_to(REPO_ROOT).as_posix() if current_dir != REPO_ROOT else ""
    base_href = (
        relative_url(current_dir, ROOT_INDEX_PATH)
        if current_dir == REPO_ROOT
        else relative_url(current_dir, current_dir / "OPEN-HERE.html")
    )
    top_href = f"{base_href}#room-top"
    guideline_doc = get_brand_guideline_doc_context(path)
    if guideline_doc:
        top_cta = f"Open {str(guideline_doc['eyebrow'])} Top"
        return [
            {
                "label": "Guidance Type",
                "value": str(guideline_doc["eyebrow"]),
                "href": top_href,
                "cta": top_cta,
                "modifier": "layer",
            },
            {
                "label": "Primary Surface",
                "value": str(guideline_doc["primary_title"]),
                "href": str(guideline_doc["primary_href"]),
                "cta": str(guideline_doc["primary_cta"]),
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": str(guideline_doc["focus_summary"]),
                "href": "#doc-reading-surface",
                "cta": "Open Reading",
                "modifier": "focus",
            },
            {
                "label": "Guidance Track",
                "value": str(guideline_doc["track_value"]),
                "href": str(guideline_doc["track_href"]),
                "cta": str(guideline_doc["track_cta"]),
                "modifier": "docs",
            },
            {
                "label": "Reference Surface",
                "value": str(guideline_doc["reference_title"]),
                "href": str(guideline_doc["reference_href"]),
                "cta": str(guideline_doc["reference_cta"]),
                "modifier": "surface",
            },
            {
                "label": "Governance Surface",
                "value": str(guideline_doc["governance_title"]),
                "href": str(guideline_doc["governance_href"]),
                "cta": str(guideline_doc["governance_cta"]),
                "modifier": "source",
            },
        ]
    master_template_doc = get_master_template_doc_context(path)
    if master_template_doc:
        return [
            {
                "label": "Template Type",
                "value": "Template Master",
                "href": top_href,
                "cta": f"Open {str(master_template_doc['domain_title'])} Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Surface",
                "value": str(master_template_doc["domain_title"]),
                "href": str(master_template_doc["domain_href"]),
                "cta": str(master_template_doc["domain_cta"]),
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": get_standard_doc_focus_summary(meta, subtitle) or str(master_template_doc["domain_title"]),
                "href": "#doc-reading-surface",
                "cta": "Open Reading",
                "modifier": "focus",
            },
            {
                "label": "Template Pack",
                "value": str(master_template_doc["pack_title"]),
                "href": str(master_template_doc["pack_href"]),
                "cta": str(master_template_doc["pack_cta"]),
                "modifier": "docs",
            },
            {
                "label": "Template Hub",
                "value": str(master_template_doc["hub_title"]),
                "href": str(master_template_doc["hub_href"]),
                "cta": str(master_template_doc["hub_cta"]),
                "modifier": "surface",
            },
            {
                "label": "Drafting Route",
                "value": str(master_template_doc["routes_title"]),
                "href": str(master_template_doc["routes_href"]),
                "cta": str(master_template_doc["routes_cta"]),
                "modifier": "source",
            },
        ]
    sop_doc = get_sop_doc_context(path)
    if sop_doc:
        return [
            {
                "label": "Procedure Type",
                "value": "Procedure Standard",
                "href": top_href,
                "cta": f"Open {str(sop_doc['domain_title'])} Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Surface",
                "value": str(sop_doc["domain_title"]),
                "href": str(sop_doc["domain_href"]),
                "cta": str(sop_doc["domain_cta"]),
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": get_standard_doc_focus_summary(meta, subtitle) or str(sop_doc["domain_title"]),
                "href": "#doc-reading-surface",
                "cta": "Open Reading",
                "modifier": "focus",
            },
            {
                "label": "Procedure Stack",
                "value": str(sop_doc["stack_title"]),
                "href": str(sop_doc["stack_href"]),
                "cta": str(sop_doc["stack_cta"]),
                "modifier": "docs",
            },
            {
                "label": "Procedure Hub",
                "value": str(sop_doc["hub_title"]),
                "href": str(sop_doc["hub_href"]),
                "cta": str(sop_doc["hub_cta"]),
                "modifier": "surface",
            },
            {
                "label": "Control Route",
                "value": str(sop_doc["related_title"]),
                "href": str(sop_doc["related_href"]),
                "cta": str(sop_doc["related_cta"]),
                "modifier": "source",
            },
        ]
    dashboard_doc = get_dashboard_doc_context(path)
    if dashboard_doc:
        return [
            {
                "label": "Control Surface",
                "value": str(dashboard_doc["board_title"]),
                "href": top_href,
                "cta": f"Open {str(dashboard_doc['board_title'])} Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Surface",
                "value": str(dashboard_doc["board_title"]),
                "href": str(dashboard_doc["board_href"]),
                "cta": str(dashboard_doc["board_cta"]),
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": get_standard_doc_focus_summary(meta, subtitle) or str(dashboard_doc["board_title"]),
                "href": "#doc-reading-surface",
                "cta": "Open Reading",
                "modifier": "focus",
            },
            {
                "label": "Board Routes",
                "value": str(dashboard_doc["routes_title"]),
                "href": str(dashboard_doc["routes_href"]),
                "cta": str(dashboard_doc["routes_cta"]),
                "modifier": "docs",
            },
            {
                "label": "Dashboard Layer",
                "value": str(dashboard_doc["hub_title"]),
                "href": str(dashboard_doc["hub_href"]),
                "cta": str(dashboard_doc["hub_cta"]),
                "modifier": "surface",
            },
            {
                "label": "Founder Route",
                "value": str(dashboard_doc["related_title"]),
                "href": str(dashboard_doc["related_href"]),
                "cta": str(dashboard_doc["related_cta"]),
                "modifier": "source",
            },
        ]
    if relative == LEAD_ROOM_RELATIVE:
        return [
            {
                "label": "Memo Type",
                "value": "Lead Brief",
                "href": f"{base_href}#room-top",
                "cta": "Open Lead Room Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Crescent Market Wholesale Lead Room",
                "href": base_href,
                "cta": "Open Lead Room",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Qualification / Advancement / Response Discipline",
                "href": relative_url(current_dir, REPO_ROOT / SALES_PIPELINE_BOARD_RELATIVE),
                "cta": "Open Sales Pipeline",
                "modifier": "focus",
            },
            {
                "label": "Lead Lane",
                "value": "Leads",
                "href": relative_url(current_dir, REPO_ROOT / LEADS_RELATIVE / "OPEN-HERE.html"),
                "cta": "Open Leads",
                "modifier": "docs",
            },
            {
                "label": "Founder Queue",
                "value": "Founder Execution Queue",
                "href": relative_url(current_dir, REPO_ROOT / TASK_ROOM_RELATIVE / "OPEN-HERE.html"),
                "cta": "Open Founder Queue",
                "modifier": "surface",
            },
            {
                "label": "CRM Hub",
                "value": "CRM",
                "href": relative_url(current_dir, REPO_ROOT / "02_crm/OPEN-HERE.html"),
                "cta": "Open CRM",
                "modifier": "source",
            },
        ]
    if relative == SUPPLIER_ROOM_RELATIVE:
        return [
            {
                "label": "Memo Type",
                "value": "Supplier Brief",
                "href": f"{base_href}#room-top",
                "cta": "Open Supplier Room Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Golden Harvest Produce Supplier Room",
                "href": base_href,
                "cta": "Open Supplier Room",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Approval / Continuity / Backup Readiness",
                "href": relative_url(current_dir, REPO_ROOT / SUPPLIER_APPROVAL_RELATIVE / "OPEN-HERE.html"),
                "cta": "Open Supplier Approval",
                "modifier": "focus",
            },
            {
                "label": "Supplier Lane",
                "value": "Suppliers",
                "href": relative_url(current_dir, REPO_ROOT / SUPPLIERS_RELATIVE / "OPEN-HERE.html"),
                "cta": "Open Suppliers",
                "modifier": "docs",
            },
            {
                "label": "Performance Board",
                "value": "Supplier Performance",
                "href": relative_url(current_dir, REPO_ROOT / SUPPLIER_PERFORMANCE_BOARD_RELATIVE),
                "cta": "Open Supplier Performance",
                "modifier": "surface",
            },
            {
                "label": "CRM Hub",
                "value": "CRM",
                "href": relative_url(current_dir, REPO_ROOT / "02_crm/OPEN-HERE.html"),
                "cta": "Open CRM",
                "modifier": "source",
            },
        ]
    if relative == TASK_ROOM_RELATIVE:
        return [
            {
                "label": "Memo Type",
                "value": "Execution Brief",
                "href": f"{base_href}#room-top",
                "cta": "Open Founder Queue Top",
                "modifier": "layer",
            },
            {
                "label": "Primary Layer",
                "value": "Founder Execution Queue",
                "href": base_href,
                "cta": "Open Founder Queue",
                "modifier": "subject",
            },
            {
                "label": "Operating Focus",
                "value": "Executable Gates / Owner Follow-Through / Live Closeout",
                "href": relative_url(current_dir, REPO_ROOT / EXECUTABLE_CHECKS_BOARD_RELATIVE),
                "cta": "Open Executable Checks",
                "modifier": "focus",
            },
            {
                "label": "Task Lane",
                "value": "Tasks",
                "href": relative_url(current_dir, REPO_ROOT / TASKS_RELATIVE / "OPEN-HERE.html"),
                "cta": "Open Tasks",
                "modifier": "docs",
            },
            {
                "label": "Accountability Board",
                "value": "Owner Accountability",
                "href": relative_url(current_dir, REPO_ROOT / OWNER_ACCOUNTABILITY_BOARD_RELATIVE),
                "cta": "Open Owner Accountability",
                "modifier": "surface",
            },
            {
                "label": "CRM Hub",
                "value": "CRM",
                "href": relative_url(current_dir, REPO_ROOT / "02_crm/OPEN-HERE.html"),
                "cta": "Open CRM",
                "modifier": "source",
            },
        ]
    surface_title = (
        str(hero_profile.get("title", "")).strip()
        if hero_profile and hero_profile.get("title")
        else "UNYRA System"
        if current_dir == REPO_ROOT
        else humanize_surface_name(current_dir.name)
    )
    surface_pill = get_doc_card_surface_pill(current_dir, path, doc_kind)
    primary_cta = (
        "Open UNYRA System"
        if current_dir == REPO_ROOT
        else str(hero_profile.get("cta", "")).strip()
        if hero_profile and hero_profile.get("cta")
        else f"Open {surface_title}"
    )
    top_cta = "Open System Top" if current_dir == REPO_ROOT else f"Open {surface_title} Top"
    source_cta = get_doc_card_source_cta(doc_kind)
    source_href = path.name
    readable_layers = sum(
        1
        for child in current_dir.iterdir()
        if child.is_file()
        and child.suffix.lower() == ".md"
        and child.name not in {"README.md", "AGENTS.md", path.name}
    )
    focus_summary = get_standard_doc_focus_summary(meta, subtitle) or surface_title
    extra_meta = get_standard_doc_extra_meta_row(meta)
    status_value = str(meta_map.get("Status", "")).strip()

    items = [
        {
            "label": "Status" if status_value else "Surface Type",
            "value": status_value or surface_pill or doc_kind,
            "href": top_href,
            "cta": top_cta,
            "modifier": "layer",
        },
        {
            "label": "Primary Surface",
            "value": surface_title,
            "href": base_href,
            "cta": primary_cta,
            "modifier": "subject",
        },
        {
            "label": "Operating Focus",
            "value": focus_summary,
            "href": "#doc-reading-surface",
            "cta": "Open Reading",
            "modifier": "focus",
        },
    ]

    if extra_meta:
        extra_label, extra_value = extra_meta
        normalized = normalize_heading(extra_label)
        if "source" in normalized:
            extra_href = f"{base_href}#visual-system"
            extra_cta = "Open Source Integrity"
            extra_modifier = "surface"
        else:
            extra_href = "#doc-reading-surface"
            extra_cta = "Open Reading"
            extra_modifier = "docs"
        items.append(
            {
                "label": extra_label,
                "value": extra_value,
                "href": extra_href,
                "cta": extra_cta,
                "modifier": extra_modifier,
            }
        )
    else:
        items.append(
            {
                "label": "Readable Layers",
                "value": str(readable_layers),
                "href": f"{base_href}#supporting-files" if readable_layers else source_href,
                "cta": (
                    "Open Readable Layer"
                    if readable_layers == 1
                    else "Open Readable Layers"
                    if readable_layers > 1
                    else source_cta
                ),
                "modifier": "docs",
            }
        )

    items.extend(
        [
            {
                "label": "Source Route",
                "value": "Source Integrity",
                "href": f"{base_href}#visual-system",
                "cta": "Open Source Integrity",
                "modifier": "surface",
            },
            {
                "label": "Updated",
                "value": datetime.fromtimestamp(path.stat().st_mtime).strftime("%B %d, %Y"),
                "href": source_href,
                "cta": source_cta,
                "modifier": "source",
            },
        ]
    )
    return items


def render_meta_cards(path: Path, doc_kind: str, meta: list[tuple[str, str]], subtitle: str) -> str:
    if doc_kind == "Overview":
        return render_brief_header_meta_cards(build_overview_meta_items(path))
    if doc_kind not in {"Executive Brief"}:
        return render_brief_header_meta_cards(build_standard_doc_meta_items(path, doc_kind, meta, subtitle))
    else:
        fallback_meta = [
            ("Document Type", doc_kind),
            ("Source File", path.name),
            ("Area", AREA_LABELS.get(path.parts[len(REPO_ROOT.parts)], "System")),
            ("Last Updated", datetime.fromtimestamp(path.stat().st_mtime).strftime("%B %d, %Y")),
        ]
        rows = meta[:8] if meta else fallback_meta
    cards: list[str] = []
    for chunk in split_chunks(rows, 4):
        row_html = []
        for key, value in chunk:
            row_html.append(
                "<div class=\"meta-row\">"
                f"<span class=\"meta-label\">{html.escape(key)}</span>"
                f"<span class=\"meta-value\">{html.escape(value)}</span>"
                "</div>"
            )
        cards.append(f'<div class="meta-card">{"".join(row_html)}</div>')
    return "".join(cards)


def build_brief_header_meta_rows(current_dir: Path, path: Path, meta: list[tuple[str, str]]) -> list[tuple[str, str]]:
    meta_map = meta_to_dict(meta)
    sequence_local, sequence_external = get_decision_sequence_scope_counts(current_dir)
    outcome_local, outcome_external = get_outcome_path_scope_counts(current_dir)
    route_posture = get_route_posture(
        sequence_local,
        sequence_external,
        outcome_local,
        outcome_external,
    )
    if meta_map.get("Counterparty"):
        subject_label = "Counterparty"
        subject_value = meta_map["Counterparty"]
    elif meta_map.get("Route"):
        subject_label = "Route"
        subject_value = meta_map["Route"]
    else:
        subject_label = "Live Subject"
        subject_value = humanize_slug(current_dir.name)

    sequence_summary = get_scope_summary_override(current_dir, "sequence") or format_scope_summary(sequence_local, sequence_external)
    outcome_summary = get_scope_summary_override(current_dir, "outcomes") or format_scope_summary(outcome_local, outcome_external)

    return [
        ("Room Type", meta_map.get("Room Type", "Executive War Room")),
        (subject_label, subject_value),
        ("Route Logic", str(route_posture["label"])),
        ("Sequence", sequence_summary),
        ("Outcomes", outcome_summary),
        ("Updated", datetime.fromtimestamp(path.stat().st_mtime).strftime("%B %d, %Y")),
    ]


def build_brief_header_meta_items(
    current_dir: Path,
    path: Path,
    meta: list[tuple[str, str]],
    *,
    reading_ready: bool,
    focus_ready: bool,
    decision_ready: bool,
    support_ready: bool,
    related_ready: bool,
    source_ready: bool,
) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    active_deal_room_return = get_active_deal_room_return_context(current_dir)
    active_shipment_room_return = get_active_shipment_room_return_context(current_dir)
    active_account_room_return = get_active_account_room_return_context(current_dir)
    active_claim_room_return = get_active_claim_room_return_context(current_dir)
    fda_readiness_room_return = get_fda_readiness_room_return_context(current_dir)
    supplier_approval_room_return = get_supplier_approval_room_return_context(current_dir)
    outcome_href = (
        "#decision-support-links"
        if support_ready
        else "#related-rooms"
        if related_ready
        else "#brief-source-layer"
        if source_ready
        else ""
    )
    for label, value in build_brief_header_meta_rows(current_dir, path, meta):
        href = ""
        cta = ""
        modifier = "neutral"
        if label == "Room Type":
            href = "#brief-distribution"
            cta = "Open Distribution"
            modifier = "distribution"
        elif label in {"Counterparty", "Route", "Live Subject"}:
            href = "#current-reading" if reading_ready else "#brief-distribution"
            cta = "Open Reading" if reading_ready else "Open Distribution"
            modifier = "subject"
        elif label == "Route Logic":
            href = "#executive-focus" if focus_ready else "#brief-distribution"
            cta = "Open Focus" if focus_ready else "Open Distribution"
            modifier = "route"
        elif label == "Sequence":
            href = "#decision-agenda" if decision_ready else "#executive-focus" if focus_ready else ""
            cta = "Open Decision" if decision_ready else "Open Focus" if focus_ready else ""
            modifier = "sequence"
        elif label == "Outcomes":
            href = outcome_href
            cta = (
                "Open Support"
                if support_ready
                else "Open Related Rooms"
                if related_ready
                else "Open Deal Return"
                if active_deal_room_return and source_ready
                else "Open Shipment Return"
                if active_shipment_room_return and source_ready
                else "Open Account Return"
                if active_account_room_return and source_ready
                else "Open Claim Return"
                if active_claim_room_return and source_ready
                else "Open Readiness Return"
                if fda_readiness_room_return and source_ready
                else "Open Supplier Return"
                if supplier_approval_room_return and source_ready
                else "Open Source"
                if source_ready
                else ""
            )
            modifier = "outcomes"
        elif label == "Updated":
            href = "#brief-source-layer" if source_ready else "README.md"
            cta = (
                "Open Deal Return"
                if active_deal_room_return and source_ready
                else "Open Shipment Return"
                if active_shipment_room_return and source_ready
                else "Open Account Return"
                if active_account_room_return and source_ready
                else "Open Claim Return"
                if active_claim_room_return and source_ready
                else "Open Readiness Return"
                if fda_readiness_room_return and source_ready
                else "Open Supplier Return"
                if supplier_approval_room_return and source_ready
                else "Open Source Layer"
                if source_ready
                else "Open Brief Source"
            )
            modifier = "source"
        items.append(
            {
                "label": label,
                "value": value,
                "href": href,
                "cta": cta,
                "modifier": modifier,
            }
        )
    return items


def render_brief_header_meta_cards(items: list[dict[str, str]]) -> str:
    if not items:
        return ""
    cards = []
    for chunk in split_chunks(items, 3):
        row_html = []
        for item in chunk:
            label = str(item["label"])
            value = str(item["value"])
            href = str(item.get("href", "") or "")
            cta = str(item.get("cta", "") or "")
            modifier = str(item.get("modifier", "neutral") or "neutral")
            row_class = f"meta-row meta-row--brief meta-row--{modifier}"
            if href:
                row_class += " meta-row--link"
                row_html.append(
                    f'<a class="{html.escape(row_class, quote=True)}" href="{html.escape(href, quote=True)}">'
                    f'<span class="meta-label">{html.escape(label)}</span>'
                    f'<span class="meta-value">{html.escape(value)}</span>'
                    f'<span class="meta-row-cta">{html.escape(cta)}</span>'
                    "</a>"
                )
            else:
                row_html.append(
                    f'<div class="{html.escape(row_class, quote=True)}">'
                    f'<span class="meta-label">{html.escape(label)}</span>'
                    f'<span class="meta-value">{html.escape(value)}</span>'
                    "</div>"
                )
        cards.append(f'<div class="meta-card meta-card--brief">{"".join(row_html)}</div>')
    return "".join(cards)


def render_brief_header_identity(items: list[dict[str, str]]) -> str:
    if not items:
        return ""
    pills: list[str] = []
    for item in items:
        label = str(item["label"])
        if label == "Updated":
            continue
        value = str(item["value"])
        href = str(item.get("href", "") or "")
        modifier = str(item.get("modifier", "neutral") or "neutral")
        pill_text = value if label in {"Room Type", "Counterparty", "Route", "Live Subject", "Route Logic"} else f"{label} {value}"
        pill_class = "meta-pill"
        if modifier == "distribution":
            pill_class += " meta-pill--brief-hero-room"
        elif modifier == "subject":
            pill_class += " meta-pill--brief-hero-subject"
        elif modifier == "route":
            if value == "In-Room Throughline":
                pill_class += " meta-pill--route-local"
            elif value == "Mixed Exit Logic":
                pill_class += " meta-pill--route-mixed"
            elif value == "Board-Led Route":
                pill_class += " meta-pill--route-external"
            else:
                pill_class += " meta-pill--brief-hero-route"
        elif modifier == "sequence":
            pill_class += " meta-pill--brief-hero-sequence"
        elif modifier == "outcomes":
            pill_class += " meta-pill--brief-hero-outcomes"
        else:
            pill_class += " meta-pill--brief-hero-route"
        if href:
            pill_class += " meta-pill--link"
            pills.append(
                f'<a class="{html.escape(pill_class, quote=True)}" href="{html.escape(href, quote=True)}">{html.escape(pill_text)}</a>'
            )
        else:
            pills.append(f'<span class="{html.escape(pill_class, quote=True)}">{html.escape(pill_text)}</span>')
    if not pills:
        return ""
    return f'<div class="doc-header-identity">{"".join(pills)}</div>'


def render_brief_distribution_panel(meta: list[tuple[str, str]], current_dir: Path) -> str:
    meta_map = meta_to_dict(meta)
    subject = (
        meta_map.get("Counterparty")
        or meta_map.get("Route")
        or meta_map.get("Customer")
        or "Linked live matter"
    )
    rows = [
        ("Audience", "Founder and executive room owners"),
        ("Room Type", meta_map.get("Room Type", "Executive War Room")),
        ("Live Subject", subject),
        ("Handling", "Internal executive brief for live decision support. Do not use as an external release packet."),
    ]

    lineup_labels = {
        "Audience": "Audience",
        "Room Type": "Room",
        "Live Subject": "Subject",
        "Handling": "Handling",
    }
    lineup_entries: list[tuple[str, str, str]] = []
    cards: list[str] = []
    for index, (label, value) in enumerate(rows, start=1):
        anchor_id = get_brief_distribution_anchor_id(label)
        lineup_entries.append(
            (
                str(lineup_labels.get(label, label)),
                f"#{anchor_id}",
                "meta-pill--brief-lineup-distribution",
            )
        )
        cards.append(
            f'<article class="brief-distribution-card" id="{html.escape(anchor_id, quote=True)}">'
            "<div class=\"brief-distribution-meta\">"
            '<span class="meta-pill meta-pill--brief-distribution-point">Distribution Point</span>'
            f'<span class="meta-pill meta-pill--brief-distribution-index">{index:02d}</span>'
            "</div>"
            f"<p class=\"brief-distribution-label\">{html.escape(label)}</p>"
            f"<p class=\"brief-distribution-value\">{render_inline(value, current_dir)}</p>"
            "</article>"
        )

    meta_html = (
        '<div class="brief-panel-meta">'
        f'<span class="meta-pill meta-pill--brief-distribution-count">{len(rows)} Distribution Points</span>'
        '<span class="meta-pill meta-pill--brief-distribution-route">Audience / Subject / Handling</span>'
        "</div>"
    )
    return (
        '<section class="brief-distribution-panel" id="brief-distribution">'
        "<div class=\"brief-distribution-head\">"
        "<p class=\"eyebrow\">Brief Distribution</p>"
        "<h2 class=\"section-title-sm\">Set the room's audience, subject, and handling before using it in live decisions.</h2>"
        "<p class=\"section-copy\">This strip frames the memo as a controlled internal executive brief rather than a generic repository file.</p>"
        f"{meta_html}"
        f"{render_brief_panel_lineup(lineup_entries)}"
        "</div>"
        f"<div class=\"brief-distribution-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def render_brief_focus_panel(
    meta: list[tuple[str, str]], current_dir: Path, *, source_layer_ready: bool = False
) -> str:
    meta_map = meta_to_dict(meta)
    active_deal_room_return = get_active_deal_room_return_context(current_dir)
    active_shipment_room_return = get_active_shipment_room_return_context(current_dir)
    active_account_room_return = get_active_account_room_return_context(current_dir)
    active_claim_room_return = get_active_claim_room_return_context(current_dir)
    fda_readiness_room_return = get_fda_readiness_room_return_context(current_dir)
    supplier_approval_room_return = get_supplier_approval_room_return_context(current_dir)
    focus_rows = [
        ("Primary Lens", meta_map.get("Primary Lens", "")),
        ("Decision Now", meta_map.get("Decision Now", "")),
        ("Escalation Rhythm", meta_map.get("Escalation Rhythm", "")),
        ("Record Status", meta_map.get("Record Status", "")),
    ]
    populated_rows = [(label, value) for label, value in focus_rows if value]
    if not populated_rows:
        return ""

    room_profile = build_portal_hero_context(current_dir)
    lens_target = str(room_profile.get("lens_target", "")).strip() if room_profile else ""
    decision_target = str(room_profile.get("decision_target", "")).strip() if room_profile else ""
    has_watch = brief_has_escalation_triggers(current_dir / "README.md")
    room_open_here_href = relative_url(current_dir, current_dir / "OPEN-HERE.html")
    focus_targets: dict[str, tuple[str, str, str] | None] = {
        "Primary Lens": (
            (
                relative_url(current_dir, REPO_ROOT / lens_target),
                "Open Live Lens",
                "brief-focus-card--module",
            )
            if lens_target and not lens_target.startswith("#")
            else None
        ),
        "Decision Now": (
            (
                f"{room_open_here_href}{decision_target}"
                if decision_target.startswith("#")
                else relative_url(current_dir, REPO_ROOT / decision_target),
                "Open Room Decision" if decision_target.startswith("#") else "Open Decision Control",
                "brief-focus-card--decision",
            )
            if decision_target
            else None
        ),
        "Escalation Rhythm": (
            (f"{room_open_here_href}#escalation-trigger-01", "Open Room Trigger", "brief-focus-card--watch")
            if has_watch
            else None
        ),
        "Record Status": (
            (
                "#brief-source-layer" if source_layer_ready else "README.md",
                "Open Deal Return"
                if active_deal_room_return and source_layer_ready
                else "Open Shipment Return"
                if active_shipment_room_return and source_layer_ready
                else "Open Account Return"
                if active_account_room_return and source_layer_ready
                else "Open Claim Return"
                if active_claim_room_return and source_layer_ready
                else "Open Readiness Return"
                if fda_readiness_room_return and source_layer_ready
                else "Open Supplier Return"
                if supplier_approval_room_return and source_layer_ready
                else "Open Source Layer"
                if source_layer_ready
                else "Open Brief Source",
                "brief-focus-card--source",
            )
        ),
    }

    lineup_labels = {
        "Primary Lens": "Lens",
        "Decision Now": "Decision",
        "Escalation Rhythm": "Escalation",
        "Record Status": "Status",
    }
    lineup_entries: list[tuple[str, str, str]] = []
    cards: list[str] = []
    live_link_count = 0
    source_link_count = 0
    for label, value in populated_rows:
        anchor_id = get_brief_focus_anchor_id(label)
        lineup_entries.append(
            (
                str(lineup_labels.get(label, label)),
                f"#{anchor_id}",
                "meta-pill--brief-lineup-focus",
            )
        )
        target = focus_targets.get(label)
        if target:
            href, cta, modifier = target
            if modifier == "brief-focus-card--source":
                source_link_count += 1
            else:
                live_link_count += 1
            cards.append(
                f'<a class="brief-focus-card brief-focus-card--link {html.escape(modifier, quote=True)}" id="{html.escape(anchor_id, quote=True)}" href="{html.escape(href, quote=True)}">'
                f"<p class=\"brief-focus-label\">{html.escape(label)}</p>"
                f"<p class=\"brief-focus-value\">{render_inline(value, current_dir)}</p>"
                f"<span class=\"brief-focus-cta\">{html.escape(cta)}</span>"
                "</a>"
            )
        else:
            cards.append(
                f'<article class="brief-focus-card" id="{html.escape(anchor_id, quote=True)}">'
                f"<p class=\"brief-focus-label\">{html.escape(label)}</p>"
                f"<p class=\"brief-focus-value\">{render_inline(value, current_dir)}</p>"
                "</article>"
            )

    route_label = (
        f"{live_link_count} Live Links / {source_link_count} Return Link"
        if (active_deal_room_return or active_shipment_room_return or active_account_room_return or active_claim_room_return or fda_readiness_room_return or supplier_approval_room_return) and source_link_count
        else f"{live_link_count} Live Links / {source_link_count} Source Link"
        if source_link_count
        else f"{live_link_count} Live Links"
        if live_link_count
        else "Executive Frame"
    )
    meta_html = (
        '<div class="brief-panel-meta">'
        f'<span class="meta-pill meta-pill--brief-focus-count">{len(populated_rows)} Focus Lanes</span>'
        f'<span class="meta-pill meta-pill--brief-focus-route">{html.escape(route_label)}</span>'
        "</div>"
    )
    return (
        '<section class="brief-focus-panel" id="executive-focus">'
        "<div class=\"brief-focus-head\">"
        "<p class=\"eyebrow\">Executive Focus</p>"
        "<h2 class=\"section-title-sm\">Anchor the room on the decision logic before reading the full brief.</h2>"
        "<p class=\"section-copy\">This strip promotes the live decision frame the founder should carry through the rest of the room.</p>"
        f"{meta_html}"
        f"{render_brief_panel_lineup(lineup_entries)}"
        "</div>"
        f"<div class=\"brief-focus-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def render_brief_action_panel(items: list[str], current_dir: Path) -> str:
    if not items:
        return ""

    visible_items = items[:4]
    module_lookup = build_brief_module_lookup(current_dir)
    lineup_entries: list[tuple[str, str, str]] = []
    cards = []
    linked_module_total = 0
    for index, item in enumerate(visible_items, start=1):
        anchor_id = get_brief_action_anchor_id(index)
        lineup_entries.append(
            (summarize_brief_action_label(item, index), f"#{anchor_id}", "meta-pill--brief-lineup-action")
        )
        linked_modules = []
        for code_title in extract_inline_code_titles(item):
            matched = resolve_brief_module_match(module_lookup, code_title)
            if matched and matched not in linked_modules:
                linked_modules.append(matched)
        linked_module_total += len(linked_modules)
        module_html = ""
        if linked_modules:
            module_html = (
                '<div class="brief-action-modules">'
                + "".join(
                    f'<a class="meta-pill meta-pill--link meta-pill--brief-module" href="{html.escape(module["href"], quote=True)}">{html.escape(strip_module_suffix(module["title"]))}</a>'
                    for module in linked_modules
                )
                + "</div>"
            )
        cards.append(
            f'<article class="brief-action-card" id="{html.escape(anchor_id, quote=True)}">'
            f"<span class=\"brief-action-index\">{index:02d}</span>"
            f"<p class=\"brief-action-copy\">{render_inline(item, current_dir)}</p>"
            f"{module_html}"
            "</article>"
        )

    meta_html = (
        '<div class="brief-panel-meta">'
        f'<span class="meta-pill meta-pill--brief-action">{len(visible_items)} Founder Actions</span>'
        + (
            f'<span class="meta-pill meta-pill--brief-linked">{linked_module_total} Live Module Links</span>'
            if linked_module_total
            else '<span class="meta-pill meta-pill--brief-linked">Narrative Sequence</span>'
        )
        + "</div>"
    )
    return (
        '<section class="brief-action-panel" id="immediate-founder-actions">'
        "<div class=\"brief-action-head\">"
        "<p class=\"eyebrow\">Immediate Founder Actions</p>"
        "<h2 class=\"section-title-sm\">Start with the next moves before scanning the full room.</h2>"
        "<p class=\"section-copy\">This strip is lifted directly from the source brief so the founder sees the immediate operating sequence at the top of the document view.</p>"
        f"{meta_html}"
        f"{render_brief_panel_lineup(lineup_entries)}"
        "</div>"
        f"<div class=\"brief-action-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def render_brief_reading_panel(rows: list[tuple[str, str]], current_dir: Path) -> str:
    if not rows:
        return ""

    visible_rows = rows[:6]
    lineup_entries: list[tuple[str, str, str]] = []
    decision_signal_count = 0
    cards = []
    for index, (signal, reading) in enumerate(visible_rows, start=1):
        anchor_id = get_brief_reading_anchor_id(signal, index)
        signal_pill, modifier, signal_pill_class = get_brief_reading_signal_profile(signal)
        if modifier == "brief-reading-card--decision":
            decision_signal_count += 1
        lineup_entries.append(
            (summarize_brief_signal_label(signal), f"#{anchor_id}", "meta-pill--brief-lineup-reading")
        )
        cards.append(
            f'<article class="brief-reading-card {html.escape(modifier, quote=True)}" id="{html.escape(anchor_id, quote=True)}">'
            "<div class=\"brief-reading-meta\">"
            f'<span class="meta-pill {html.escape(signal_pill_class, quote=True)}">{html.escape(signal_pill)}</span>'
            f'<span class="meta-pill meta-pill--brief-reading-index">{index:02d}</span>'
            "</div>"
            f"<p class=\"brief-reading-label\">{html.escape(signal)}</p>"
            f"<p class=\"brief-reading-value\">{render_inline(reading, current_dir)}</p>"
            "</article>"
        )

    meta_html = (
        '<div class="brief-panel-meta">'
        f'<span class="meta-pill meta-pill--brief-reading">{len(visible_rows)} Live Signals</span>'
        + (
            f'<span class="meta-pill meta-pill--brief-reading-decision">{decision_signal_count} Decision Signals</span>'
            if decision_signal_count
            else '<span class="meta-pill meta-pill--brief-reading-decision">Signal Lineup</span>'
        )
        + "</div>"
    )
    return (
        '<section class="brief-reading-panel" id="current-reading">'
        "<div class=\"brief-reading-head\">"
        "<p class=\"eyebrow\">Current Reading</p>"
        "<h2 class=\"section-title-sm\">Read the live signals before going deeper into the room.</h2>"
        "<p class=\"section-copy\">These cards are generated from the source brief table so the founder sees the current posture in one clean executive strip.</p>"
        f"{meta_html}"
        f"{render_brief_panel_lineup(lineup_entries)}"
        "</div>"
        f"<div class=\"brief-reading-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def render_brief_decision_panel(items: list[str], current_dir: Path) -> str:
    if not items:
        return ""

    visible_items = items[:4]
    module_lookup = build_brief_module_lookup(current_dir)
    room_sequence_href = f'{relative_url(current_dir, current_dir / "OPEN-HERE.html")}#decision-sequence'
    lineup_entries: list[tuple[str, str, str]] = []
    cards = []
    linked_module_total = 0
    for index, item in enumerate(visible_items, start=1):
        anchor_id = get_brief_decision_anchor_id(index)
        lineup_entries.append(
            (summarize_brief_decision_label(item, index), f"#{anchor_id}", "meta-pill--brief-lineup-decision")
        )
        linked_modules = []
        for code_title in extract_inline_code_titles(item):
            matched = resolve_brief_module_match(module_lookup, code_title)
            if matched and matched not in linked_modules:
                linked_modules.append(matched)
        linked_module_total += len(linked_modules)
        module_html = ""
        if linked_modules:
            module_html = (
                '<div class="brief-action-modules">'
                + "".join(
                    f'<a class="meta-pill meta-pill--link meta-pill--brief-module" href="{html.escape(module["href"], quote=True)}">{html.escape(strip_module_suffix(module["title"]))}</a>'
                    for module in linked_modules
                )
                + "</div>"
            )
        cards.append(
            f'<article class="brief-decision-card" id="{html.escape(anchor_id, quote=True)}">'
            '<div class="brief-decision-meta">'
            '<span class="meta-pill meta-pill--brief-decision-step">Decision Step</span>'
            f'<span class="meta-pill meta-pill--brief-decision-index">{index:02d}</span>'
            "</div>"
            f"<p class=\"brief-decision-copy\">{render_inline(item, current_dir)}</p>"
            f"{module_html}"
            f'<div class="brief-decision-links"><a class="button-secondary" href="{html.escape(room_sequence_href, quote=True)}">Open Room Sequence</a></div>'
            "</article>"
        )

    meta_html = (
        '<div class="brief-panel-meta">'
        f'<span class="meta-pill meta-pill--brief-decision">{len(visible_items)} Decision Steps</span>'
        + (
            f'<span class="meta-pill meta-pill--brief-linked">{linked_module_total} Live Module Links</span>'
            if linked_module_total
            else '<span class="meta-pill meta-pill--brief-linked">Room Sequence Ready</span>'
        )
        + "</div>"
    )
    return (
        '<section class="brief-decision-panel" id="decision-agenda">'
        "<div class=\"brief-decision-head\">"
        "<p class=\"eyebrow\">Decision Agenda</p>"
        "<h2 class=\"section-title-sm\">Frame the founder decision path before moving into live controls.</h2>"
        "<p class=\"section-copy\">This strip promotes the agenda into a sequence the founder can scan, anchor, and then carry into the room-level decision layer.</p>"
        f"{meta_html}"
        f"{render_brief_panel_lineup(lineup_entries)}"
        "</div>"
        f"<div class=\"brief-decision-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def render_brief_trigger_panel(items: list[str], current_dir: Path) -> str:
    if not items:
        return ""

    visible_items = items[:4]
    room_open_here_href = relative_url(current_dir, current_dir / "OPEN-HERE.html")
    lineup_entries: list[tuple[str, str, str]] = []
    cards = []
    for index, item in enumerate(visible_items, start=1):
        anchor_id = get_brief_trigger_anchor_id(index)
        room_trigger_href = f"{room_open_here_href}#escalation-trigger-{index:02d}"
        lineup_entries.append(
            (summarize_brief_trigger_label(item, index), f"#{anchor_id}", "meta-pill--brief-lineup-trigger")
        )
        cards.append(
            f'<article class="brief-trigger-card" id="{html.escape(anchor_id, quote=True)}">'
            '<div class="brief-trigger-meta">'
            '<span class="meta-pill meta-pill--brief-trigger-type">Watch Trigger</span>'
            f'<span class="meta-pill meta-pill--brief-trigger-index">{index:02d}</span>'
            "</div>"
            f"<p class=\"brief-trigger-copy\">{render_inline(item, current_dir)}</p>"
            f'<div class="brief-trigger-links"><a class="button-secondary" href="{html.escape(room_trigger_href, quote=True)}">Open Room Trigger</a></div>'
            "</article>"
        )

    meta_html = (
        '<div class="brief-panel-meta">'
        f'<span class="meta-pill meta-pill--brief-trigger">{len(visible_items)} Escalation Triggers</span>'
        '<span class="meta-pill meta-pill--brief-trigger-room">Room Watch Linked</span>'
        "</div>"
    )
    return (
        '<section class="brief-trigger-panel" id="escalation-triggers">'
        "<div class=\"brief-trigger-head\">"
        "<p class=\"eyebrow\">Escalation Triggers</p>"
        "<h2 class=\"section-title-sm\">Scan the trigger stack before the room posture drifts unnoticed.</h2>"
        "<p class=\"section-copy\">Each trigger in this brief now maps back to the live watch inside the room so the founder can move from the memo into the exact escalation lane.</p>"
        f"{meta_html}"
        f"{render_brief_panel_lineup(lineup_entries)}"
        "</div>"
        f"<div class=\"brief-trigger-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def render_brief_usage_panel(items: list[str], current_dir: Path) -> str:
    if not items:
        return ""

    visible_items = items[:4]
    module_lookup = build_brief_module_lookup(current_dir)
    lineup_entries: list[tuple[str, str, str]] = []
    cards = []
    linked_module_total = 0
    for index, item in enumerate(visible_items, start=1):
        anchor_id = get_brief_usage_anchor_id(index)
        lineup_entries.append(
            (summarize_brief_operating_label(item, index, "Route"), f"#{anchor_id}", "meta-pill--brief-lineup-usage")
        )
        linked_modules = []
        for code_title in extract_inline_code_titles(item):
            matched = resolve_brief_module_match(module_lookup, code_title)
            if matched and matched not in linked_modules:
                linked_modules.append(matched)
        linked_module_total += len(linked_modules)
        module_html = ""
        if linked_modules:
            module_html = (
                '<div class="brief-action-modules">'
                + "".join(
                    f'<a class="meta-pill meta-pill--link meta-pill--brief-module" href="{html.escape(module["href"], quote=True)}">{html.escape(strip_module_suffix(module["title"]))}</a>'
                    for module in linked_modules
                )
                + "</div>"
            )
        cards.append(
            f'<article class="brief-usage-card" id="{html.escape(anchor_id, quote=True)}">'
            '<div class="brief-usage-meta">'
            '<span class="meta-pill meta-pill--brief-usage-route">Usage Route</span>'
            f'<span class="meta-pill meta-pill--brief-usage-index">{index:02d}</span>'
            "</div>"
            f"<p class=\"brief-usage-copy\">{render_inline(item, current_dir)}</p>"
            f"{module_html}"
            "</article>"
        )

    meta_html = (
        '<div class="brief-panel-meta">'
        f'<span class="meta-pill meta-pill--brief-usage">{len(visible_items)} Usage Routes</span>'
        + (
            f'<span class="meta-pill meta-pill--brief-linked">{linked_module_total} Live Module Links</span>'
            if linked_module_total
            else '<span class="meta-pill meta-pill--brief-linked">Narrative Standard</span>'
        )
        + "</div>"
    )
    return (
        '<section class="brief-usage-panel" id="founder-usage-standard">'
        "<div class=\"brief-usage-head\">"
        "<p class=\"eyebrow\">Founder Usage Standard</p>"
        "<h2 class=\"section-title-sm\">Close the brief on the operating rhythm the founder should actually follow.</h2>"
        "<p class=\"section-copy\">This strip turns the usage standard into a route layer so the founder can scan where to start, where to move next, and when the brief itself is the right reading surface.</p>"
        f"{meta_html}"
        f"{render_brief_panel_lineup(lineup_entries)}"
        "</div>"
        f"<div class=\"brief-usage-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def build_brief_module_lookup(current_dir: Path) -> dict[str, dict[str, str]]:
    child_directories = order_child_directories(
        current_dir,
        [path for path in current_dir.iterdir() if path.is_dir() and path.name not in SKIP_DIR_NAMES],
    )
    by_title: dict[str, dict[str, str]] = {}
    for child_dir in child_directories:
        profile = build_folder_card_profile(current_dir, child_dir)
        if not profile:
            continue
        title = str(profile["title"])
        entry = {
            "title": title,
            "pill": str(profile["pill"]),
            "cta": str(profile["cta"]),
            "href": relative_url(current_dir, child_dir / "OPEN-HERE.html"),
        }
        aliases = {
            normalize_heading(title),
            normalize_heading(strip_module_suffix(title)),
        }
        for alias in aliases:
            if alias:
                by_title[alias] = entry
    return by_title


def resolve_brief_module_match(
    module_lookup: dict[str, dict[str, str]], module_title: str
) -> dict[str, str] | None:
    normalized = normalize_heading(module_title)
    if not normalized:
        return None

    direct_match = module_lookup.get(normalized)
    if direct_match:
        return direct_match

    partial_matches: list[dict[str, str]] = []
    seen_hrefs: set[str] = set()
    for alias, entry in module_lookup.items():
        if alias.startswith(f"{normalized} ") or normalized.startswith(f"{alias} "):
            href = entry["href"]
            if href not in seen_hrefs:
                seen_hrefs.add(href)
                partial_matches.append(entry)
    if len(partial_matches) == 1:
        return partial_matches[0]
    return None


def collect_brief_modules(current_dir: Path, module_titles: list[str]) -> list[dict[str, str]]:
    by_title = build_brief_module_lookup(current_dir)

    modules: list[dict[str, str]] = []
    for module_title in module_titles:
        matched = resolve_brief_module_match(by_title, module_title)
        if matched:
            modules.append(matched)
    return modules


def collect_brief_module_profiles(current_dir: Path, lines: list[str]) -> list[dict[str, str]]:
    module_lookup = build_brief_module_lookup(current_dir)
    module_items = extract_section_list_items(lines, "Core Modules In This Room")
    modules: list[dict[str, str]] = []
    modules_by_href: dict[str, dict[str, str]] = {}
    for item in module_items:
        description = item.split(":", 1)[1].strip() if ":" in item else ""
        code_titles = extract_inline_code_titles(item)
        candidates = code_titles or [item.split(":", 1)[0].strip()]
        for candidate in candidates:
            matched = resolve_brief_module_match(module_lookup, candidate)
            if not matched:
                continue
            href = matched["href"]
            existing = modules_by_href.get(href)
            if existing:
                if description and not existing.get("copy"):
                    existing["copy"] = description
                continue
            entry = dict(matched)
            if description:
                entry["copy"] = description
            modules.append(entry)
            modules_by_href[href] = entry
    return modules


def render_brief_panel_lineup(entries: list[tuple[str, str, str]]) -> str:
    if not entries:
        return ""
    links = []
    for label, href, modifier in entries:
        classes = "meta-pill meta-pill--link"
        if modifier:
            classes += f" {modifier}"
        links.append(
            f'<a class="{html.escape(classes, quote=True)}" href="{html.escape(href, quote=True)}">{html.escape(label)}</a>'
        )
    return f'<div class="brief-panel-lineup">{"".join(links)}</div>'


def render_brief_module_panel(modules: list[dict[str, str]]) -> str:
    if not modules:
        return ""

    lineup_entries: list[tuple[str, str, str]] = []
    role_note_count = 0
    cards = []
    for index, module in enumerate(modules, start=1):
        anchor_id = get_brief_module_anchor_id(index, module["title"])
        lineup_entries.append(
            (strip_module_suffix(module["title"]), f"#{anchor_id}", "meta-pill--brief-lineup-module")
        )
        copy_html = ""
        if module.get("copy"):
            role_note_count += 1
            copy_html = f'<span class="brief-module-copy">{html.escape(module["copy"])}</span>'
        cards.append(
            "<a class=\"brief-module-card\" "
            f'id="{html.escape(anchor_id, quote=True)}" '
            f"href=\"{html.escape(module['href'], quote=True)}\">"
            "<div class=\"brief-module-meta\">"
            f"<span class=\"brief-module-pill\">{html.escape(module['pill'])}</span>"
            f'<span class="meta-pill meta-pill--brief-module-index">{index:02d}</span>'
            "</div>"
            f"<span class=\"brief-module-title\">{html.escape(module['title'])}</span>"
            f"{copy_html}"
            f"<span class=\"brief-module-cta\">{html.escape(module['cta'])}</span>"
            "</a>"
        )

    meta_html = (
        '<div class="brief-panel-meta">'
        f'<span class="meta-pill meta-pill--brief-module-count">{len(modules)} Live Modules</span>'
        + (
            f'<span class="meta-pill meta-pill--brief-module-role">{role_note_count} Role Notes</span>'
            if role_note_count
            else '<span class="meta-pill meta-pill--brief-module-role">Open Module Stack</span>'
        )
        + "</div>"
    )
    return (
        '<section class="brief-module-panel" id="quick-open-modules">'
        "<div class=\"brief-module-head\">"
        "<p class=\"eyebrow\">Quick Open Modules</p>"
        "<h2 class=\"section-title-sm\">Jump straight from the brief into the live module that carries the answer.</h2>"
        "<p class=\"section-copy\">These cards now carry both the live open path and the operating role each module plays inside the room, so the founder can move from narrative to control without reading a duplicate module list below.</p>"
        f"{meta_html}"
        f"{render_brief_panel_lineup(lineup_entries)}"
        "</div>"
        f"<div class=\"brief-module-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def collect_related_rooms(current_dir: Path, resolve_dir: Path | None = None) -> list[dict[str, str]]:
    relative_parent = current_dir.relative_to(REPO_ROOT).as_posix()
    href_dir = resolve_dir or current_dir
    profiles = {
        "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution": [
            {
                "title": "Atlantic Foods Garlic Deal Room",
                "pill": "Deal Room",
                "cta": "Open Deal Room",
                "copy": "Jump into the live deal room when trust posture has to be translated into commitment, pricing, or outbound control.",
                "target": REPO_ROOT / "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/OPEN-HERE.html",
            },
            {
                "title": "China to USA Shipment Room",
                "pill": "Shipment Room",
                "cta": "Open Shipment Room",
                "copy": "Open the shipment room when the account question has already become a release, packet, or funding-movement question.",
                "target": REPO_ROOT / "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/OPEN-HERE.html",
            },
            {
                "title": "Atlantic Foods Claim Room",
                "pill": "Claim Room",
                "cta": "Open Claim Room",
                "copy": "Move into the claim room when relationship confidence is being shaped by containment, recovery, or complaint proof.",
                "target": REPO_ROOT / "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/OPEN-HERE.html",
            },
        ],
        "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic": [
            {
                "title": "Atlantic Foods Account Room",
                "pill": "Customer Room",
                "cta": "Open Account Room",
                "copy": "Jump into the customer room when the live deal answer depends on trust, exposure, collections, or account weight.",
                "target": REPO_ROOT / "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/OPEN-HERE.html",
            },
            {
                "title": "China to USA Shipment Room",
                "pill": "Shipment Room",
                "cta": "Open Shipment Room",
                "copy": "Open the shipment room when the commercial answer is now constrained by release gates, packet proof, or funding timing.",
                "target": REPO_ROOT / "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/OPEN-HERE.html",
            },
            {
                "title": "Atlantic Foods Claim Room",
                "pill": "Claim Room",
                "cta": "Open Claim Room",
                "copy": "Move into the claim room when complaint consequence, recovery, or CAPA posture is affecting the same counterparty relationship.",
                "target": REPO_ROOT / "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/OPEN-HERE.html",
            },
        ],
        "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA": [
            {
                "title": "Atlantic Foods Account Room",
                "pill": "Customer Room",
                "cta": "Open Account Room",
                "copy": "Jump into the customer room when shipment release has to be read against trust posture, exposure, or collections confidence.",
                "target": REPO_ROOT / "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/OPEN-HERE.html",
            },
            {
                "title": "Atlantic Foods Garlic Deal Room",
                "pill": "Deal Room",
                "cta": "Open Deal Room",
                "copy": "Open the deal room when shipment movement has to stay synchronized with executable checks, founder decisions, or outbound commitments.",
                "target": REPO_ROOT / "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/OPEN-HERE.html",
            },
            {
                "title": "Atlantic Foods Claim Room",
                "pill": "Claim Room",
                "cta": "Open Claim Room",
                "copy": "Move into the claim room when shipment execution is being influenced by containment, recovery, or proof questions after the fact.",
                "target": REPO_ROOT / "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/OPEN-HERE.html",
            },
        ],
        "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim": [
            {
                "title": "Atlantic Foods Account Room",
                "pill": "Customer Room",
                "cta": "Open Account Room",
                "copy": "Jump into the customer room when complaint consequence needs to be weighed against trust, exposure, or account growth posture.",
                "target": REPO_ROOT / "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/OPEN-HERE.html",
            },
            {
                "title": "Atlantic Foods Garlic Deal Room",
                "pill": "Deal Room",
                "cta": "Open Deal Room",
                "copy": "Open the deal room when recovery consequence or complaint friction changes the commitment logic on the live commercial matter.",
                "target": REPO_ROOT / "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/OPEN-HERE.html",
            },
            {
                "title": "China to USA Shipment Room",
                "pill": "Shipment Room",
                "cta": "Open Shipment Room",
                "copy": "Move into the shipment room when the claim is tied to movement proof, packet quality, or release-stage operating facts.",
                "target": REPO_ROOT / "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/OPEN-HERE.html",
            },
        ],
    }
    related_rooms = []
    for item in profiles.get(relative_parent, []):
        related_rooms.append(
            {
                "title": str(item["title"]),
                "pill": str(item["pill"]),
                "cta": str(item["cta"]),
                "copy": str(item["copy"]),
                "href": relative_url(href_dir, Path(item["target"])),
            }
        )
    return related_rooms


def render_brief_related_panel(related_rooms: list[dict[str, str]]) -> str:
    if not related_rooms:
        return ""

    lineup_entries: list[tuple[str, str, str]] = []
    cards = []
    for index, room in enumerate(related_rooms, start=1):
        anchor_id = get_brief_related_anchor_id(index, room["title"])
        lineup_entries.append(
            (strip_open_prefix(room["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-related")
        )
        cards.append(
            "<a class=\"brief-related-card\" "
            f'id="{html.escape(anchor_id, quote=True)}" '
            f"href=\"{html.escape(room['href'], quote=True)}\">"
            "<div class=\"brief-related-meta\">"
            f"<span class=\"brief-related-pill\">{html.escape(room['pill'])}</span>"
            f"<span class=\"meta-pill meta-pill--brief-related-index\">{index:02d}</span>"
            "</div>"
            f"<span class=\"brief-related-title\">{html.escape(room['title'])}</span>"
            f"<span class=\"brief-related-copy\">{html.escape(room['copy'])}</span>"
            f"<span class=\"brief-related-cta\">{html.escape(room['cta'])}</span>"
            "</a>"
        )

    meta_html = (
        '<div class="brief-panel-meta">'
        f'<span class="meta-pill meta-pill--brief-related-count">{len(related_rooms)} Connected Rooms</span>'
        '<span class="meta-pill meta-pill--brief-related-route">Lateral Room Route</span>'
        "</div>"
    )
    return (
        '<section class="brief-related-panel" id="related-rooms">'
        "<div class=\"brief-related-head\">"
        "<p class=\"eyebrow\">Related Rooms</p>"
        "<h2 class=\"section-title-sm\">Move laterally across connected rooms when the founder answer spans more than one case.</h2>"
        "<p class=\"section-copy\">These links connect the live brief to the other war rooms most likely to change or confirm the same executive answer.</p>"
        f"{meta_html}"
        f"{render_brief_panel_lineup(lineup_entries)}"
        "</div>"
        f"<div class=\"brief-related-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def collect_decision_support_links(current_dir: Path, resolve_dir: Path | None = None) -> list[dict[str, str]]:
    relative_parent = current_dir.relative_to(REPO_ROOT).as_posix()
    href_dir = resolve_dir or current_dir
    profiles = {
        "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution": [
            {
                "title": "Customer Account Review Board",
                "pill": "Customer Board",
                "cta": "Open Customer Board",
                "copy": "Use the live customer board when the account answer needs to be compared against the broader customer portfolio.",
                "target": REPO_ROOT / "06_dashboard/08_customer-accounts/Customer-Account-Review-Board.html",
            },
            {
                "title": "Credit and Release Control Board",
                "pill": "Credit Board",
                "cta": "Open Credit Board",
                "copy": "Jump here when trust posture has to be converted into exposure logic, release limits, and override discipline.",
                "target": REPO_ROOT / "06_dashboard/09_credit-risk/Credit-and-Release-Control-Board.html",
            },
            {
                "title": "Strategic Counterparty Trust Review",
                "pill": "Trust Board",
                "cta": "Open Trust Board",
                "copy": "Use the trust board when response quality and institutional confidence need to be judged across counterparties, not only this account.",
                "target": REPO_ROOT / "06_dashboard/38_counterparty-trust/Strategic-Counterparty-Trust-and-Response-Review.html",
            },
            {
                "title": "Trust Posture Matrix",
                "pill": "Posture Matrix",
                "cta": "Open Trust Matrix",
                "copy": "Open the matrix when the founder needs the cross-counterparty rule that translates trust tier into release consequence.",
                "target": REPO_ROOT / "06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.html",
            },
        ],
        "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic": [
            {
                "title": "Active Matter Control Board",
                "pill": "Matter Board",
                "cta": "Open Matter Board",
                "copy": "Use the live matter board when this deal's control answer needs to be compared with other active matters.",
                "target": REPO_ROOT / "06_dashboard/10_matter-control/Active-Matter-Control-Board.html",
            },
            {
                "title": "Executive Decision Board",
                "pill": "Decision Board",
                "cta": "Open Decision Board",
                "copy": "Jump here when the deal is turning into a founder decision or override question rather than just an operating question.",
                "target": REPO_ROOT / "06_dashboard/13_founder-decisions/Executive-Decision-Board.html",
            },
            {
                "title": "Capital Allocation Review",
                "pill": "Capital Board",
                "cta": "Open Capital Board",
                "copy": "Use the capital board when this deal is competing with other matters for release confidence and capital priority.",
                "target": REPO_ROOT / "06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.html",
            },
            {
                "title": "Communication Control Board",
                "pill": "Communication Board",
                "cta": "Open Communication Board",
                "copy": "Open the communication board when the founder needs the institutional outbound answer beyond this one deal room.",
                "target": REPO_ROOT / "06_dashboard/36_external-communications/Counterparty-Communication-Control-Board.html",
            },
        ],
        "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA": [
            {
                "title": "Daily Shipment Control Tower",
                "pill": "Shipment Board",
                "cta": "Open Shipment Board",
                "copy": "Use the control tower when this shipment needs to be judged against the broader live movement queue.",
                "target": REPO_ROOT / "06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html",
            },
            {
                "title": "Daily Operations Command Center",
                "pill": "Operations Board",
                "cta": "Open Operations Board",
                "copy": "Jump here when shipment movement has to be read inside the full same-day operating picture.",
                "target": REPO_ROOT / "06_dashboard/03_operations/Daily-Operations-Command-Center.html",
            },
            {
                "title": "Funding and Payables Review",
                "pill": "Funding Board",
                "cta": "Open Funding Board",
                "copy": "Use the funding board when the release answer depends on cash movement, supplier payment timing, or payables discipline.",
                "target": REPO_ROOT / "06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.html",
            },
            {
                "title": "Executable Check Control Board",
                "pill": "Check Board",
                "cta": "Open Check Board",
                "copy": "Open the executable-check board when shipment movement is still constrained by live closure proof or control sync.",
                "target": REPO_ROOT / "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html",
            },
        ],
        "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim": [
            {
                "title": "CAPA and Preventive Action Review",
                "pill": "CAPA Board",
                "cta": "Open CAPA Board",
                "copy": "Use the CAPA board when containment quality needs to be read across complaint and corrective-action governance, not only inside this case.",
                "target": REPO_ROOT / "06_dashboard/31_capa-governance/CAPA-and-Preventive-Action-Review.html",
            },
            {
                "title": "Claims and Recovery Review",
                "pill": "Recovery Board",
                "cta": "Open Recovery Board",
                "copy": "Jump here when financial consequence and recovery posture need to be weighed against other active claims and credits.",
                "target": REPO_ROOT / "06_dashboard/30_claims-recovery/Claims-Credits-and-Recovery-Review.html",
            },
            {
                "title": "Executive Risk Register",
                "pill": "Risk Board",
                "cta": "Open Risk Board",
                "copy": "Use the executive risk register when the claim is now affecting the founder's formal risk picture.",
                "target": REPO_ROOT / "06_dashboard/18_executive-risk-register/Executive-Risk-Register.html",
            },
            {
                "title": "Weekly Executive Review",
                "pill": "Weekly Board",
                "cta": "Open Weekly Review",
                "copy": "Open the weekly executive review when this complaint needs to be read in cadence with the rest of the operating week.",
                "target": REPO_ROOT / "06_dashboard/14_weekly-executive-review/Weekly-Executive-Operating-Review.html",
            },
        ],
    }
    support_links = []
    for item in profiles.get(relative_parent, []):
        support_links.append(
            {
                "title": str(item["title"]),
                "pill": str(item["pill"]),
                "cta": str(item["cta"]),
                "copy": str(item["copy"]),
                "href": relative_url(href_dir, Path(item["target"])),
            }
        )
    return support_links


def render_brief_support_panel(links: list[dict[str, str]]) -> str:
    if not links:
        return ""

    lineup_entries: list[tuple[str, str, str]] = []
    cards = []
    for index, link in enumerate(links, start=1):
        anchor_id = get_brief_support_anchor_id(index, link["title"])
        lineup_entries.append(
            (strip_open_prefix(link["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-support")
        )
        cards.append(
            "<a class=\"brief-support-card\" "
            f'id="{html.escape(anchor_id, quote=True)}" '
            f"href=\"{html.escape(link['href'], quote=True)}\">"
            "<div class=\"brief-support-meta\">"
            f"<span class=\"brief-support-pill\">{html.escape(link['pill'])}</span>"
            f"<span class=\"meta-pill meta-pill--brief-support-index\">{index:02d}</span>"
            "</div>"
            f"<span class=\"brief-support-title\">{html.escape(link['title'])}</span>"
            f"<span class=\"brief-support-copy\">{html.escape(link['copy'])}</span>"
            f"<span class=\"brief-support-cta\">{html.escape(link['cta'])}</span>"
            "</a>"
        )

    meta_html = (
        '<div class="brief-panel-meta">'
        f'<span class="meta-pill meta-pill--brief-support-count">{len(links)} Executive Boards</span>'
        '<span class="meta-pill meta-pill--brief-support-route">Decision Carry</span>'
        "</div>"
    )
    return (
        '<section class="brief-support-panel" id="decision-support-links">'
        "<div class=\"brief-support-head\">"
        "<p class=\"eyebrow\">Decision Support Links</p>"
        "<h2 class=\"section-title-sm\">Open the executive board that usually carries the same decision beyond this one room.</h2>"
        "<p class=\"section-copy\">These links connect the brief to the dashboards most likely to confirm, widen, or govern the same founder answer.</p>"
        f"{meta_html}"
        f"{render_brief_panel_lineup(lineup_entries)}"
        "</div>"
        f"<div class=\"brief-support-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def render_brief_source_panel(current_dir: Path, *, has_residual_body: bool = False) -> str:
    active_deal_room_return = get_active_deal_room_return_context(current_dir)
    active_shipment_room_return = get_active_shipment_room_return_context(current_dir)
    active_account_room_return = get_active_account_room_return_context(current_dir)
    active_claim_room_return = get_active_claim_room_return_context(current_dir)
    fda_readiness_room_return = get_fda_readiness_room_return_context(current_dir)
    supplier_approval_room_return = get_supplier_approval_room_return_context(current_dir)
    if active_deal_room_return:
        source_routes = [
            {
                "title": "Live Room View",
                "pill": "Room Layer",
                "copy": "Return to the live room when the founder needs the full navigation mesh, module stack, outcomes, and watch layers instead of the memo abstraction.",
                "cta": str(active_deal_room_return["room_view_cta"]),
                "href": str(active_deal_room_return["room_view_href"]),
            },
            {
                "title": "Active Deals",
                "pill": "Deal Flow Lane",
                "copy": "Move back into active deals when the founder needs the broader live commercial lane and current pressure behind this room.",
                "cta": str(active_deal_room_return["lane_cta"]),
                "href": str(active_deal_room_return["lane_href"]),
            },
            {
                "title": "Deals",
                "pill": "Commercial Map",
                "copy": "Return to the deals hub when the founder needs the wider commercial map across live, won, and lost posture instead of one active room.",
                "cta": str(active_deal_room_return["hub_cta"]),
                "href": str(active_deal_room_return["hub_href"]),
            },
            {
                "title": "Preview Docs",
                "pill": "Brand Surface",
                "copy": "Move into preview docs when the next decision depends on branded outbound, benchmark surfaces, or institutional release presentation.",
                "cta": str(active_deal_room_return["preview_cta"]),
                "href": str(active_deal_room_return["preview_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(source_routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="brief-source-layer">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Deal Return</p>"
            "<h2 class=\"section-title-sm\">Close the brief on the routes that reconnect the live room, the commercial lane, and outward benchmark review.</h2>"
            "<p class=\"section-copy\">This return layer closes the brief on the live room, active deals, the wider deals hub, or preview docs instead of falling back to generic source framing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Room / Lane / Hub / Preview</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if active_shipment_room_return:
        source_routes = [
            {
                "title": "Live Room View",
                "pill": "Room Layer",
                "copy": "Return to the live shipment room when the founder needs the full navigation mesh, module stack, movement paths, and watch layers instead of the memo abstraction.",
                "cta": str(active_shipment_room_return["room_view_cta"]),
                "href": str(active_shipment_room_return["room_view_href"]),
            },
            {
                "title": "Active Shipments",
                "pill": "Movement Lane",
                "copy": "Move back into active shipments when the founder needs the broader live movement lane and the other contained shipment answers around this room.",
                "cta": str(active_shipment_room_return["lane_cta"]),
                "href": str(active_shipment_room_return["lane_href"]),
            },
            {
                "title": "Shipments",
                "pill": "Operations Hub",
                "copy": "Return to the shipments hub when the founder needs the wider movement map, shipment pathways, and operating navigation beyond this one room.",
                "cta": str(active_shipment_room_return["hub_cta"]),
                "href": str(active_shipment_room_return["hub_href"]),
            },
            {
                "title": "Shipment Control Tower",
                "pill": "Control Board",
                "copy": "Move into the shipment control tower when the next decision depends on the broader executive board that governs daily shipment movement across the queue.",
                "cta": str(active_shipment_room_return["board_cta"]),
                "href": str(active_shipment_room_return["board_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(source_routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="brief-source-layer">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Shipment Return</p>"
            "<h2 class=\"section-title-sm\">Close the brief on the routes that reconnect the live room, the movement lane, and the governing board.</h2>"
            "<p class=\"section-copy\">This return layer closes the brief on the live shipment room, active shipments, the wider shipments hub, or the shipment control tower instead of falling back to generic source framing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Room / Lane / Hub / Board</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if active_account_room_return:
        source_routes = [
            {
                "title": "Live Room View",
                "pill": "Room Layer",
                "copy": "Return to the live account room when the founder needs the full navigation mesh, module stack, account paths, and watch layers instead of the memo abstraction.",
                "cta": str(active_account_room_return["room_view_cta"]),
                "href": str(active_account_room_return["room_view_href"]),
            },
            {
                "title": "Customers",
                "pill": "Counterparty Lane",
                "copy": "Move back into customers when the founder needs the broader customer lane and the other counterparty answers around this room.",
                "cta": str(active_account_room_return["lane_cta"]),
                "href": str(active_account_room_return["lane_href"]),
            },
            {
                "title": "CRM",
                "pill": "Commercial Hub",
                "copy": "Return to CRM when the founder needs the wider commercial map across counterparties, deals, and execution posture beyond this one account room.",
                "cta": str(active_account_room_return["hub_cta"]),
                "href": str(active_account_room_return["hub_href"]),
            },
            {
                "title": "Customer Account Review Board",
                "pill": "Control Board",
                "copy": "Move into the customer account review board when the next decision depends on the broader executive board that governs account posture and release weight.",
                "cta": str(active_account_room_return["board_cta"]),
                "href": str(active_account_room_return["board_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(source_routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="brief-source-layer">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Account Return</p>"
            "<h2 class=\"section-title-sm\">Close the brief on the routes that reconnect the live room, the counterparty lane, and the governing board.</h2>"
            "<p class=\"section-copy\">This return layer closes the brief on the live account room, customers, the wider CRM hub, or the customer account review board instead of falling back to generic source framing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Room / Lane / Hub / Board</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if active_claim_room_return:
        source_routes = [
            {
                "title": "Live Room View",
                "pill": "Room Layer",
                "copy": "Return to the live claim room when the founder needs the full navigation mesh, module stack, outcome paths, and watch layers instead of the memo abstraction.",
                "cta": str(active_claim_room_return["room_view_cta"]),
                "href": str(active_claim_room_return["room_view_href"]),
            },
            {
                "title": "Inspection Cases",
                "pill": "Case Lane",
                "copy": "Move back into inspection cases when the founder needs the broader governed case lane around complaint, readiness, and inspection posture.",
                "cta": str(active_claim_room_return["lane_cta"]),
                "href": str(active_claim_room_return["lane_href"]),
            },
            {
                "title": "Compliance",
                "pill": "Governance Hub",
                "copy": "Return to compliance when the founder needs the wider proof, supplier-control, and governed-case map beyond this one claim room.",
                "cta": str(active_claim_room_return["hub_cta"]),
                "href": str(active_claim_room_return["hub_href"]),
            },
            {
                "title": "Claims Recovery",
                "pill": "Recovery Board",
                "copy": "Move into claims recovery when the next decision depends on the broader executive board that governs credits, recovery, and financial consequence across cases.",
                "cta": str(active_claim_room_return["board_cta"]),
                "href": str(active_claim_room_return["board_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(source_routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="brief-source-layer">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Claim Return</p>"
            "<h2 class=\"section-title-sm\">Close the brief on the routes that reconnect the live room, the governed case lane, and recovery consequence.</h2>"
            "<p class=\"section-copy\">This return layer closes the brief on the live claim room, inspection cases, the wider compliance hub, or claims recovery instead of falling back to generic source framing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Room / Lane / Hub / Board</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if fda_readiness_room_return:
        source_routes = [
            {
                "title": "Live Room View",
                "pill": "Room Layer",
                "copy": "Return to the live readiness room when the founder needs the full navigation mesh, readiness context, and proof posture instead of the memo abstraction.",
                "cta": str(fda_readiness_room_return["room_view_cta"]),
                "href": str(fda_readiness_room_return["room_view_href"]),
            },
            {
                "title": "Inspection Cases",
                "pill": "Case Lane",
                "copy": "Move back into inspection cases when the founder needs the broader readiness and case lane around this one FDA-readiness surface.",
                "cta": str(fda_readiness_room_return["lane_cta"]),
                "href": str(fda_readiness_room_return["lane_href"]),
            },
            {
                "title": "Compliance",
                "pill": "Governance Hub",
                "copy": "Return to compliance when the founder needs the wider governed map across inspections, supplier control, and retained proof beyond this one readiness room.",
                "cta": str(fda_readiness_room_return["hub_cta"]),
                "href": str(fda_readiness_room_return["hub_href"]),
            },
            {
                "title": "Compliance Control",
                "pill": "Control Board",
                "copy": "Move into compliance control when the next answer depends on the broader founder board that governs readiness posture, open proof gaps, and live response discipline.",
                "cta": str(fda_readiness_room_return["board_cta"]),
                "href": str(fda_readiness_room_return["board_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(source_routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="brief-source-layer">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Readiness Return</p>"
            "<h2 class=\"section-title-sm\">Close the brief on the routes that reconnect the live readiness room, the inspection lane, and founder control.</h2>"
            "<p class=\"section-copy\">This return layer closes the brief on the live readiness room, inspection cases, the wider compliance hub, or compliance control instead of falling back to generic source framing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Room / Lane / Hub / Board</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if supplier_approval_room_return:
        source_routes = [
            {
                "title": "Live Room View",
                "pill": "Room Layer",
                "copy": "Return to the live supplier room when the founder needs the full governance surface across approval posture, performance control, and backup-sourcing resilience instead of the memo abstraction.",
                "cta": str(supplier_approval_room_return["room_view_cta"]),
                "href": str(supplier_approval_room_return["room_view_href"]),
            },
            {
                "title": "Supplier Approval",
                "pill": "Governance Lane",
                "copy": "Move back into supplier approval when the founder needs the wider governed supplier lane rather than one supplier room.",
                "cta": str(supplier_approval_room_return["lane_cta"]),
                "href": str(supplier_approval_room_return["lane_href"]),
            },
            {
                "title": "Compliance",
                "pill": "Governance Hub",
                "copy": "Return to compliance when the founder needs the wider proof, inspection, and supplier-governance map beyond this one supplier room.",
                "cta": str(supplier_approval_room_return["hub_cta"]),
                "href": str(supplier_approval_room_return["hub_href"]),
            },
            {
                "title": "Supplier Performance Board",
                "pill": "Control Board",
                "copy": "Move into the supplier performance board when the next answer depends on quarterly scorecard posture, response quality, and approval-with-controls discipline.",
                "cta": str(supplier_approval_room_return["board_cta"]),
                "href": str(supplier_approval_room_return["board_href"]),
            },
            {
                "title": "Supply Resilience Board",
                "pill": "Resilience Board",
                "copy": "Open supply resilience when backup coverage, capacity confidence, and contingency depth matter as much as current supplier performance.",
                "cta": str(supplier_approval_room_return["resilience_cta"]),
                "href": str(supplier_approval_room_return["resilience_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(source_routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="brief-source-layer">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Supplier Return</p>"
            "<h2 class=\"section-title-sm\">Close the brief on the routes that reconnect supplier governance, performance control, and resilience review.</h2>"
            "<p class=\"section-copy\">This return layer closes the brief on the live supplier room, supplier approval, the wider compliance hub, or the supplier performance and resilience boards instead of falling back to generic source framing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">5 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Room / Lane / Hub / Boards</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )

    room_href = relative_url(current_dir, current_dir / "OPEN-HERE.html")
    preview_hub_href = relative_url(current_dir, PREVIEW_HUB_PATH)
    source_routes = [
        {
            "title": "Live Room View",
            "pill": "Room Layer",
            "copy": "Return to the live room when the founder needs the full navigation mesh, module stack, outcomes, and watch layers instead of the memo abstraction.",
            "cta": "Open Room View",
            "href": room_href,
        },
        {
            "title": "Brief Source",
            "pill": "Repository Source",
            "copy": "Open the raw brief source only when the founder needs the exact repository wording rather than the branded executive reading surface.",
            "cta": "Open Brief Source",
            "href": "README.md",
        },
        {
            "title": "Preview Docs",
            "pill": "Brand Surface",
            "copy": "Move into preview docs when the decision now depends on branded outbound, benchmark surfaces, or institutional release presentation.",
            "cta": "Open Preview Docs",
            "href": preview_hub_href,
        },
    ]

    lineup_entries: list[tuple[str, str, str]] = []
    cards = []
    for index, route in enumerate(source_routes, start=1):
        anchor_id = get_brief_source_anchor_id(index, route["title"])
        lineup_entries.append(
            (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
        )
        cards.append(
            "<a class=\"brief-source-card\" "
            f'id="{html.escape(anchor_id, quote=True)}" '
            f'href="{html.escape(route["href"], quote=True)}">'
            "<div class=\"brief-source-meta\">"
            f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
            f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
            "</div>"
            f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
            f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
            f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
            "</a>"
        )

    meta_html = (
        '<div class="brief-panel-meta">'
        f'<span class="meta-pill meta-pill--brief-source-count">{len(source_routes)} Source Routes</span>'
        + (
            '<span class="meta-pill meta-pill--brief-source-state">Room / Source / Preview</span>'
            if has_residual_body
            else '<span class="meta-pill meta-pill--brief-source-state">Panels Fully Promoted</span>'
        )
        + "</div>"
    )
    section_copy = (
        "This layer now closes the brief after the remaining reading body, so the founder exits through the live room, the brief source, or preview docs on purpose."
        if has_residual_body
        else "This layer now closes the brief after the executive panels have absorbed the reading body, so the founder exits through the live room, the brief source, or preview docs on purpose."
    )
    return (
        '<section class="brief-source-panel" id="brief-source-layer">'
        "<div class=\"brief-source-head\">"
        "<p class=\"eyebrow\">Source Layer</p>"
        "<h2 class=\"section-title-sm\">Close the brief on the exact system surfaces that still matter after the executive abstraction.</h2>"
        f"<p class=\"section-copy\">{html.escape(section_copy)}</p>"
        f"{meta_html}"
        f"{render_brief_panel_lineup(lineup_entries)}"
        "</div>"
        f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def build_brief_nav_links(links: list[tuple[str, str, str]]) -> str:
    return "".join(
        f'<a class="brief-nav-link{" brief-nav-link--top" if style == "top" else ""}" href="{html.escape(href, quote=True)}">{html.escape(label)}</a>'
        for label, href, style in links
    )


def build_brief_nav_link_groups(
    groups: list[tuple[str, list[tuple[str, str, str]], str | None, str | None]]
) -> str:
    rendered_groups: list[str] = []
    for label, links, modifier, summary in groups:
        filtered_links = [
            (link_label, href, style)
            for link_label, href, style in links
            if link_label and href
        ]
        if not filtered_links:
            continue
        count = len(filtered_links)
        count_label = f"{count} Link" if count == 1 else f"{count} Links"
        group_class = "brief-nav-group"
        if modifier:
            group_class += f" brief-nav-group--{modifier}"
        header_meta = [
            f'<span class="{html.escape(get_room_nav_count_pill_class(modifier), quote=True)}">{html.escape(count_label)}</span>'
        ]
        if summary:
            header_meta.insert(
                0,
                f'<span class="{html.escape(get_room_nav_summary_pill_class(summary, modifier), quote=True)}">{html.escape(summary)}</span>',
            )
        rendered_groups.append(
            f"""
            <div class="{html.escape(group_class, quote=True)}">
              <div class="brief-nav-group-header">
                <p class="brief-nav-group-label">{html.escape(label)}</p>
                <div class="brief-nav-group-meta">{''.join(header_meta)}</div>
              </div>
              <div class="brief-nav-links">
                {build_brief_nav_links(filtered_links)}
              </div>
            </div>
            """
        )
    if not rendered_groups:
        return ""
    return '<div class="brief-nav-groups">' + "".join(rendered_groups) + "</div>"


def render_brief_nav_panel(current_dir: Path, items: list[tuple[str, str]]) -> str:
    if not items:
        return ""

    active_deal_room_return = get_active_deal_room_return_context(current_dir)
    active_shipment_room_return = get_active_shipment_room_return_context(current_dir)
    active_account_room_return = get_active_account_room_return_context(current_dir)
    active_claim_room_return = get_active_claim_room_return_context(current_dir)
    fda_readiness_room_return = get_fda_readiness_room_return_context(current_dir)
    supplier_approval_room_return = get_supplier_approval_room_return_context(current_dir)
    active_room_return = active_deal_room_return or active_shipment_room_return or active_account_room_return or active_claim_room_return or fda_readiness_room_return or supplier_approval_room_return
    labels = {
        "Brief Top": "Top",
        "Brief Distribution": "Distribution",
        "Executive Focus": "Focus",
        "Immediate Founder Actions": "Actions",
        "Current Reading": "Reading",
        "Quick Open Modules": "Modules",
        "Decision Support Links": "Support Links",
        "Related Rooms": "Related Rooms",
        "Decision Agenda": "Decision",
        "Escalation Triggers": "Escalation",
        "Core Modules In This Room": "Core Modules",
        "Founder Usage Standard": "Usage",
        "Source Layer": "Return" if active_room_return else "Source",
    }
    read_links: list[tuple[str, str, str]] = []
    surface_links: list[tuple[str, str, str]] = []
    decision_links: list[tuple[str, str, str]] = []
    standard_links: list[tuple[str, str, str]] = []
    for label, anchor in items:
        short_label = labels.get(label, label)
        entry = (short_label, f"#{anchor}", "top" if anchor == "brief-top" else "")
        if anchor in {"brief-top", "brief-distribution", "executive-focus", "immediate-founder-actions", "current-reading"}:
            read_links.append(entry)
        elif anchor in {"quick-open-modules", "decision-support-links", "related-rooms"}:
            surface_links.append(entry)
        elif anchor in {"decision-agenda", "escalation-triggers"}:
            decision_links.append(entry)
        else:
            standard_links.append(entry)

    return (
        '<section class="brief-nav-panel">'
        '<div class="card-meta"><span class="meta-pill">Brief Navigation</span><span class="meta-pill">Founder Use</span></div>'
        + build_brief_nav_link_groups(
            [
                ("Read First", read_links, "module", "Brief / Focus / Actions"),
                ("Room Surface", surface_links, "module-surface", "Modules / Support / Rooms"),
                ("Decision Layer", decision_links, "controls", "Decision / Escalation"),
                (
                    "Return Layer" if active_room_return else "Source Integrity",
                    standard_links,
                    "surface",
                    "Usage / Return" if active_room_return else "Usage / Source",
                ),
            ]
        )
        +
        "</section>"
    )


def render_document_closeout_panel(path: Path, doc_kind: str, *, has_residual_body: bool = False) -> str:
    current_dir = path.parent
    relative = current_dir.relative_to(REPO_ROOT).as_posix() if current_dir != REPO_ROOT else ""
    guideline_doc = get_brand_guideline_doc_context(path)
    if guideline_doc:
        routes = list(guideline_doc.get("closeout_routes", []))
        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            route_title = str(route["title"])
            route_cta = str(route["cta"])
            anchor_id = get_brief_source_anchor_id(index, route_title)
            lineup_entries.append(
                (strip_open_prefix(route_cta), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(str(route["href"]), quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(str(route["pill"]))}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route_title)}</span>'
                f'<span class="brief-source-copy">{html.escape(str(route["copy"]))}</span>'
                f'<span class="brief-source-cta">{html.escape(route_cta)}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            f'<p class="eyebrow">{html.escape(str(guideline_doc["closeout_eyebrow"]))}</p>'
            f'<h2 class="section-title-sm">{html.escape(str(guideline_doc["closeout_title"]))}</h2>'
            f'<p class="section-copy">{html.escape(str(guideline_doc["closeout_copy"]))}</p>'
            '<div class="brief-panel-meta">'
            f'<span class="meta-pill meta-pill--brief-source-count">{len(routes)} Exit Routes</span>'
            f'<span class="meta-pill meta-pill--brief-source-state">{html.escape(str(guideline_doc["closeout_state"]))}</span>'
            "</div>"
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    master_template_doc = get_master_template_doc_context(path)
    if master_template_doc:
        routes = [
            {
                "title": str(master_template_doc["domain_title"]),
                "pill": "Domain Surface",
                "copy": "Return to the template domain when the founder needs the full approved pack around this master instead of one drafting source alone.",
                "cta": str(master_template_doc["domain_cta"]),
                "href": str(master_template_doc["domain_href"]),
            },
            {
                "title": str(master_template_doc["hub_title"]),
                "pill": "Template Hub",
                "copy": "Move into the wider templates hub when the next answer depends on cross-domain drafting structure, not just one protected pack.",
                "cta": str(master_template_doc["hub_cta"]),
                "href": str(master_template_doc["hub_href"]),
            },
            {
                "title": str(master_template_doc["routes_title"]),
                "pill": "Drafting Route",
                "copy": "Open the fast-route layer when the founder wants the shortest path into founder control, outbound release, or contained-movement drafting stacks.",
                "cta": str(master_template_doc["routes_cta"]),
                "href": str(master_template_doc["routes_href"]),
            },
            {
                "title": str(master_template_doc["related_title"]),
                "pill": str(master_template_doc["related_pill"]),
                "copy": "Use the linked template route when the next answer belongs on a related protected pack rather than staying inside one template family.",
                "cta": str(master_template_doc["related_cta"]),
                "href": str(master_template_doc["related_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, str(route["title"]))
            lineup_entries.append(
                (strip_open_prefix(str(route["cta"])), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(str(route["href"]), quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(str(route["pill"]))}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(str(route["title"]))}</span>'
                f'<span class="brief-source-copy">{html.escape(str(route["copy"]))}</span>'
                f'<span class="brief-source-cta">{html.escape(str(route["cta"]))}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Master Return</p>"
            "<h2 class=\"section-title-sm\">Close this master on the routes that reconnect the protected pack, the wider template system, and the right drafting spine.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the domain pack, the templates hub, fast drafting routes, and the linked protected pack instead of defaulting to readable layers or source-integrity language.</p>"
            '<div class="brief-panel-meta">'
            f'<span class="meta-pill meta-pill--brief-source-count">{len(routes)} Exit Routes</span>'
            f'<span class="meta-pill meta-pill--brief-source-state">{html.escape(str(master_template_doc["return_state"]))}</span>'
            "</div>"
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    sop_doc = get_sop_doc_context(path)
    if sop_doc:
        routes = [
            {
                "title": str(sop_doc["domain_title"]),
                "pill": "Procedure Domain",
                "copy": "Return to the procedure domain when the founder needs the full governed SOP pack around this standard instead of one policy surface alone.",
                "cta": str(sop_doc["domain_cta"]),
                "href": str(sop_doc["domain_href"]),
            },
            {
                "title": str(sop_doc["hub_title"]),
                "pill": "Procedure Hub",
                "copy": "Move into the wider SOP hub when the next answer depends on cross-domain operating standards, not just one governed procedure pack.",
                "cta": str(sop_doc["hub_cta"]),
                "href": str(sop_doc["hub_href"]),
            },
            {
                "title": str(sop_doc["routes_title"]),
                "pill": "Procedure Route",
                "copy": "Open the fast-route layer when the founder wants the shortest path into founder cadence, commercial lifecycle, archive discipline, or communication standards.",
                "cta": str(sop_doc["routes_cta"]),
                "href": str(sop_doc["routes_href"]),
            },
            {
                "title": str(sop_doc["related_title"]),
                "pill": str(sop_doc["related_pill"]),
                "copy": "Use the linked control route when the next answer belongs on the live operating surface behind this procedure, not inside the SOP layer alone.",
                "cta": str(sop_doc["related_cta"]),
                "href": str(sop_doc["related_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, str(route["title"]))
            lineup_entries.append(
                (strip_open_prefix(str(route["cta"])), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(str(route["href"]), quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(str(route["pill"]))}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(str(route["title"]))}</span>'
                f'<span class="brief-source-copy">{html.escape(str(route["copy"]))}</span>'
                f'<span class="brief-source-cta">{html.escape(str(route["cta"]))}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Procedure Return</p>"
            "<h2 class=\"section-title-sm\">Close this procedure on the routes that reconnect the governed pack, the SOP hub, and the live operating spine.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the procedure domain, the SOP hub, fast procedure routes, and the linked live control surface instead of defaulting to readable layers or source-integrity language.</p>"
            '<div class="brief-panel-meta">'
            f'<span class="meta-pill meta-pill--brief-source-count">{len(routes)} Exit Routes</span>'
            f'<span class="meta-pill meta-pill--brief-source-state">{html.escape(str(sop_doc["return_state"]))}</span>'
            "</div>"
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    dashboard_doc = get_dashboard_doc_context(path)
    if dashboard_doc:
        routes = [
            {
                "title": str(dashboard_doc["board_title"]),
                "pill": "Control Surface",
                "copy": "Return to the live board surface when the founder needs the full control frame, board navigation, and governed context around this reading layer.",
                "cta": str(dashboard_doc["board_cta"]),
                "href": str(dashboard_doc["board_href"]),
            },
            {
                "title": str(dashboard_doc["routes_title"]),
                "pill": "Route Layer",
                "copy": "Open the board routes when the founder wants the curated path through related dashboard surfaces instead of re-entering the board cold.",
                "cta": str(dashboard_doc["routes_cta"]),
                "href": str(dashboard_doc["routes_href"]),
            },
            {
                "title": str(dashboard_doc["hub_title"]),
                "pill": "Dashboard Hub",
                "copy": "Move into the dashboard hub when the founder needs the wider control system across cadence, execution watch, and cross-functional boards.",
                "cta": str(dashboard_doc["hub_cta"]),
                "href": str(dashboard_doc["hub_href"]),
            },
            {
                "title": str(dashboard_doc["related_title"]),
                "pill": str(dashboard_doc["related_pill"]),
                "copy": "Use the linked founder route when the next answer belongs on the wider control spine instead of staying inside one board family.",
                "cta": str(dashboard_doc["related_cta"]),
                "href": str(dashboard_doc["related_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, str(route["title"]))
            lineup_entries.append(
                (strip_open_prefix(str(route["cta"])), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(str(route["href"]), quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(str(route["pill"]))}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(str(route["title"]))}</span>'
                f'<span class="brief-source-copy">{html.escape(str(route["copy"]))}</span>'
                f'<span class="brief-source-cta">{html.escape(str(route["cta"]))}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Board Return</p>"
            "<h2 class=\"section-title-sm\">Close this dashboard on the routes that reconnect the live board, dashboard hub, and founder control spine.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the board surface, its curated routes, the dashboard hub, and the linked control route instead of defaulting to readable layers or source-integrity language.</p>"
            '<div class="brief-panel-meta">'
            f'<span class="meta-pill meta-pill--brief-source-count">{len(routes)} Exit Routes</span>'
            f'<span class="meta-pill meta-pill--brief-source-state">{html.escape(str(dashboard_doc["return_state"]))}</span>'
            "</div>"
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Executive Brief":
        return render_brief_source_panel(current_dir, has_residual_body=has_residual_body)

    if doc_kind == "Overview" and current_dir == REPO_ROOT:
        routes = [
            {
                "title": "Founder Dashboard",
                "pill": "Daily Control",
                "copy": "Return to the daily founder dashboard when the next move depends on same-day posture across revenue, execution, compliance, cash, and approvals.",
                "cta": "Open Founder Dashboard",
                "href": "06_dashboard/01_executive/Daily-Founder-Dashboard.html",
            },
            {
                "title": "Control Routing",
                "pill": "Decision Route",
                "copy": "Move into control routing when a founder issue needs the right layer before anyone treats it as sales, operations, compliance, or finance by default.",
                "cta": "Open Control Routing",
                "href": "06_dashboard/33_control-routing/Founder-Control-Routing-Matrix.html",
            },
            {
                "title": "Executable Checks",
                "pill": "Execution Watch",
                "copy": "Open executable checks when a trust-linked override, same-day gate, or fragmented proof chain needs one founder-ready control surface.",
                "cta": "Open Executable Checks",
                "href": "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded system memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">System Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect founder control, routing discipline, and live execution watch.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the daily dashboard, control routing, executable checks, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Daily / Routing / Watch</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == "00_brand/01_assets/04_signatures":
        routes = [
            {
                "title": "Brand Signatures",
                "pill": "Signature Reference",
                "copy": "Return to brand signatures when the founder needs the full approved signature surface rather than this memo abstraction.",
                "cta": "Open Brand Signatures",
                "href": "OPEN-HERE.html",
            },
            {
                "title": "Assets",
                "pill": "Asset Hub",
                "copy": "Move back into assets when the founder needs the wider protected brand source map around signatures and compositions.",
                "cta": "Open Assets",
                "href": "../OPEN-HERE.html",
            },
            {
                "title": "Approved Compositions",
                "pill": "Composition Surface",
                "copy": "Open approved compositions when the next answer depends on lockups, seals, and branded header treatments adjacent to signature use.",
                "cta": "Open Approved Compositions",
                "href": "../05_approved-compositions/OPEN-HERE.html",
            },
            {
                "title": "Visual Standard",
                "pill": "Governance Surface",
                "copy": "Widen into the visual standard when the founder needs the governing styling rules behind signature usage rather than one asset reference surface.",
                "cta": "Open Visual Standard",
                "href": "../../03_exports/01_visual-standard/OPEN-HERE.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Signature Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect approved signatures, asset governance, and document styling.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to brand signatures, assets, approved compositions, or the visual standard instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Reference / Assets / Standard</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == "00_brand/01_assets/05_approved-compositions":
        routes = [
            {
                "title": "Approved Compositions",
                "pill": "Composition Reference",
                "copy": "Return to approved compositions when the founder needs the full lockup and seal surface rather than this memo abstraction.",
                "cta": "Open Approved Compositions",
                "href": "OPEN-HERE.html",
            },
            {
                "title": "Assets",
                "pill": "Asset Hub",
                "copy": "Move back into assets when the founder needs the wider protected brand source map around signatures, lockups, and approved visual source sets.",
                "cta": "Open Assets",
                "href": "../OPEN-HERE.html",
            },
            {
                "title": "Brand Signatures",
                "pill": "Signature Surface",
                "copy": "Open brand signatures when the next answer depends on outbound closure treatments that sit next to the approved composition system.",
                "cta": "Open Brand Signatures",
                "href": "../04_signatures/OPEN-HERE.html",
            },
            {
                "title": "Visual Standard",
                "pill": "Governance Surface",
                "copy": "Widen into the visual standard when the founder needs the governing styling rules behind lockup and seal usage rather than one asset reference surface.",
                "cta": "Open Visual Standard",
                "href": "../../03_exports/01_visual-standard/OPEN-HERE.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Composition Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect approved lockups, asset governance, and signature use.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to approved compositions, assets, brand signatures, or the visual standard instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Reference / Assets / Standard</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == "02_crm/04_deals/won":
        routes = [
            {
                "title": "Won Deals",
                "pill": "Retained Win Lane",
                "copy": "Return to won deals when the founder needs the retained commercial win lane, precedent framing, and preserved room in one governed reference surface.",
                "cta": "Open Won Deals",
                "href": "OPEN-HERE.html",
            },
            {
                "title": "Harbor Fresh Won Deal",
                "pill": "Reference Room",
                "copy": "Open the Harbor Fresh win when the next answer depends on the preserved commercial narrative, packet trail, and reusable pattern behind a closed success.",
                "cta": "Open Harbor Fresh Won Deal",
                "href": "DEAL-2026-003_HarborFresh_Garlic/OPEN-HERE.html",
            },
            {
                "title": "Active Deals",
                "pill": "Live Deal Lane",
                "copy": "Move into active deals when the founder needs current commercial pressure instead of retained precedent and reference wins.",
                "cta": "Open Active Deals",
                "href": "../active/OPEN-HERE.html",
            },
            {
                "title": "Deals Hub",
                "pill": "Commercial Map",
                "copy": "Return to the deal hub when the founder needs the wider lane map across live, won, and lost commercial posture instead of one retained win.",
                "cta": "Open Deals",
                "href": "../OPEN-HERE.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Win Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect retained precedent, live pressure, and the wider deal map.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to won deals, the Harbor Fresh reference room, active deals, or the wider deal hub instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Retained / Live / Hub</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == "02_crm/04_deals/lost":
        routes = [
            {
                "title": "Lost Deals",
                "pill": "Recovery Learning Lane",
                "copy": "Return to lost deals when the founder needs the retained miss, learning posture, and decision record in one governed recovery surface.",
                "cta": "Open Lost Deals",
                "href": "OPEN-HERE.html",
            },
            {
                "title": "Crescent Market Lost Deal",
                "pill": "Learning Room",
                "copy": "Open the Crescent Market miss when the next answer depends on the recorded commercial loss, reset logic, and learning trail behind a failed deal.",
                "cta": "Open Crescent Market Lost Deal",
                "href": "DEAL-2026-002_CrescentMarket_Ginger/OPEN-HERE.html",
            },
            {
                "title": "Active Deals",
                "pill": "Live Deal Lane",
                "copy": "Move into active deals when the founder needs current commercial pressure instead of recovery learning and retained misses.",
                "cta": "Open Active Deals",
                "href": "../active/OPEN-HERE.html",
            },
            {
                "title": "Deals Hub",
                "pill": "Commercial Map",
                "copy": "Return to the deal hub when the founder needs the wider lane map across live, won, and lost commercial posture instead of one retained miss.",
                "cta": "Open Deals",
                "href": "../OPEN-HERE.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Loss Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect recovery learning, live pressure, and the wider deal map.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to lost deals, the Crescent Market learning room, active deals, or the wider deal hub instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Learning / Live / Hub</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == "02_crm/04_deals/won/DEAL-2026-003_HarborFresh_Garlic":
        routes = [
            {
                "title": "Harbor Fresh Garlic Won Deal Room",
                "pill": "Reference Win Room",
                "copy": "Return to the room when the founder needs the preserved commercial narrative, handoff logic, and institutional context in one retained surface.",
                "cta": "Open Harbor Fresh Garlic Won Deal Room",
                "href": "OPEN-HERE.html",
            },
            {
                "title": "Harbor Fresh Garlic Trade Review",
                "pill": "Reference Module",
                "copy": "Open the trade review when the next answer depends on execution handoff, closed deal economics, and reusable release precedent.",
                "cta": "Open Trade Review",
                "href": "PROFIT-2026-001_HarborFresh-Garlic-Trade-Review/OPEN-HERE.html",
            },
            {
                "title": "Won Deals",
                "pill": "Retained Win Lane",
                "copy": "Return to won deals when the founder needs the broader retained-win lane instead of one reference room.",
                "cta": "Open Won Deals",
                "href": "../OPEN-HERE.html",
            },
            {
                "title": "Active Deals",
                "pill": "Live Deal Lane",
                "copy": "Move into active deals when the next answer depends on current commercial pressure instead of retained precedent and reference wins.",
                "cta": "Open Active Deals",
                "href": "../../active/OPEN-HERE.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Reference Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect retained precedent, execution handoff, and live pressure.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the Harbor Fresh room, its trade review, won deals, or active deals instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Retained / Handoff / Live</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == "02_crm/04_deals/lost/DEAL-2026-002_CrescentMarket_Ginger":
        routes = [
            {
                "title": "Crescent Market Ginger Lost Deal Room",
                "pill": "Recovery Learning Room",
                "copy": "Return to the room when the founder needs the retained miss record, reset logic, and accountability trail in one governed learning surface.",
                "cta": "Open Crescent Market Ginger Lost Deal Room",
                "href": "OPEN-HERE.html",
            },
            {
                "title": "Lost Deals",
                "pill": "Recovery Learning Lane",
                "copy": "Return to lost deals when the founder needs the wider recovery-learning lane instead of one preserved miss.",
                "cta": "Open Lost Deals",
                "href": "../OPEN-HERE.html",
            },
            {
                "title": "Active Deals",
                "pill": "Live Deal Lane",
                "copy": "Move into active deals when the next answer depends on current commercial pressure instead of retrospective loss learning.",
                "cta": "Open Active Deals",
                "href": "../../active/OPEN-HERE.html",
            },
            {
                "title": "Deals Hub",
                "pill": "Commercial Map",
                "copy": "Return to the deal hub when the founder needs the wider lane map across live, won, and lost commercial posture instead of one recorded miss.",
                "cta": "Open Deals",
                "href": "../../OPEN-HERE.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Learning Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect recovery learning, live pressure, and the wider deal map.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the Crescent Market room, lost deals, active deals, or the wider deal hub instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Learning / Live / Hub</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == "02_crm/04_deals/won/DEAL-2026-003_HarborFresh_Garlic/PROFIT-2026-001_HarborFresh-Garlic-Trade-Review":
        routes = [
            {
                "title": "Harbor Fresh Garlic Trade Review",
                "pill": "Trade Review Module",
                "copy": "Return to the trade review when the founder needs the focused margin-variance readout and handoff logic in one retained module.",
                "cta": "Open Harbor Fresh Garlic Trade Review",
                "href": "OPEN-HERE.html",
            },
            {
                "title": "Harbor Fresh Garlic Won Deal Room",
                "pill": "Reference Win Room",
                "copy": "Return to the room when the next answer depends on the broader retained narrative around the win rather than on the variance module alone.",
                "cta": "Open Won Deal Room",
                "href": "../OPEN-HERE.html",
            },
            {
                "title": "Won Deals",
                "pill": "Retained Win Lane",
                "copy": "Return to won deals when the founder needs precedent across retained wins instead of one trade review.",
                "cta": "Open Won Deals",
                "href": "../../OPEN-HERE.html",
            },
            {
                "title": "Active Deals",
                "pill": "Live Deal Lane",
                "copy": "Move into active deals when the next answer depends on current commercial pressure instead of retained win economics.",
                "cta": "Open Active Deals",
                "href": "../../../active/OPEN-HERE.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Trade Review Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect retained economics, precedent, and live pressure.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the trade review, the Harbor Fresh room, won deals, or active deals instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Variance / Retained / Live</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    active_deal_module = get_active_deal_module_context(current_dir)
    if doc_kind == "Overview" and active_deal_module:
        next_title = strip_open_prefix(str(active_deal_module["next_action_label"])) or "Next Route"
        next_pill = str(active_deal_module["next_pill"]).replace("Next ", "", 1).strip() or "Next Route"
        routes = [
            {
                "title": str(active_deal_module["room_title"]),
                "pill": "Live Deal Room",
                "copy": f"Return to {str(active_deal_module['room_title'])} when the founder needs the full live-deal answer across control, commitment, communication, and linked support instead of a single module view.",
                "cta": str(active_deal_module["room_entry_label"]),
                "href": str(active_deal_module["room_entry_href"]),
            },
            {
                "title": next_title,
                "pill": next_pill,
                "copy": f"Follow the next route when {str(active_deal_module['module_title']).lower()} has already done its job and the deal now depends on the next move inside the live commercial sequence.",
                "cta": str(active_deal_module["next_action_label"]),
                "href": str(active_deal_module["next_action_href"]),
            },
            {
                "title": "Active Deals",
                "pill": "Deal Flow Lane",
                "copy": "Move back into active deals when the founder needs the broader live commercial lane, current pressure, and room-level posture beyond this one module.",
                "cta": "Open Active Deals",
                "href": str(active_deal_module["active_deals_href"]),
            },
            {
                "title": "Deals",
                "pill": "Commercial Map",
                "copy": "Return to the deals hub when the founder needs the wider commercial map across active, won, and lost posture instead of one live module.",
                "cta": "Open Deals",
                "href": str(active_deal_module["deals_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Deal Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect the live room, the next move, and the wider commercial lane.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the live deal room, the next module move, active deals, or the wider deals hub instead of defaulting to source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Room / Next / Lane</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    active_shipment_module = get_active_shipment_module_context(current_dir)
    if doc_kind == "Overview" and active_shipment_module:
        next_title = strip_open_prefix(str(active_shipment_module["next_action_label"])) or "Next Route"
        next_pill = str(active_shipment_module["next_pill"]).replace("Next ", "", 1).strip() or "Next Route"
        routes = [
            {
                "title": str(active_shipment_module["room_title"]),
                "pill": "Live Shipment Room",
                "copy": f"Return to {str(active_shipment_module['room_title'])} when the founder needs the full live-shipment answer across release, funding, packet proof, and movement review instead of a single module view.",
                "cta": str(active_shipment_module["room_entry_label"]),
                "href": str(active_shipment_module["room_entry_href"]),
            },
            {
                "title": next_title,
                "pill": next_pill,
                "copy": f"Follow the next route when {str(active_shipment_module['module_title']).lower()} has already done its job and the shipment now depends on the next move inside the live movement sequence.",
                "cta": str(active_shipment_module["next_action_label"]),
                "href": str(active_shipment_module["next_action_href"]),
            },
            {
                "title": "Active Shipments",
                "pill": "Movement Lane",
                "copy": "Move back into active shipments when the founder needs the broader live movement lane, current shipment queue, and room-level posture beyond this one module.",
                "cta": "Open Active Shipments",
                "href": str(active_shipment_module["active_shipments_href"]),
            },
            {
                "title": "Shipments",
                "pill": "Operations Hub",
                "copy": "Return to the shipments hub when the founder needs the wider movement map, route lanes, and operating navigation beyond one live module.",
                "cta": "Open Shipments",
                "href": str(active_shipment_module["shipments_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Shipment Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect the live shipment room, the next move, and the wider movement lane.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the live shipment room, the next module move, active shipments, or the wider shipments hub instead of defaulting to source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Room / Next / Lane</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    active_account_module = get_active_account_module_context(current_dir)
    if doc_kind == "Overview" and active_account_module:
        next_title = strip_open_prefix(str(active_account_module["next_action_label"])) or "Next Route"
        next_pill = str(active_account_module["next_pill"]).replace("Next ", "", 1).strip() or "Next Route"
        routes = [
            {
                "title": str(active_account_module["room_title"]),
                "pill": "Live Account Room",
                "copy": f"Return to {str(active_account_module['room_title'])} when the founder needs the full live account answer across trust, release, cash, collections, and posture instead of a single module view.",
                "cta": str(active_account_module["room_entry_label"]),
                "href": str(active_account_module["room_entry_href"]),
            },
            {
                "title": next_title,
                "pill": next_pill,
                "copy": f"Follow the next route when {str(active_account_module['module_title']).lower()} has already done its job and the account now depends on the next move inside the live counterparty sequence.",
                "cta": str(active_account_module["next_action_label"]),
                "href": str(active_account_module["next_action_href"]),
            },
            {
                "title": "Customers",
                "pill": "Counterparty Lane",
                "copy": "Move back into customers when the founder needs the broader customer lane, current account posture, and room-level pressure beyond this one module.",
                "cta": "Open Customers",
                "href": str(active_account_module["customers_href"]),
            },
            {
                "title": "CRM",
                "pill": "Commercial Hub",
                "copy": "Return to CRM when the founder needs the wider commercial map across customers, deals, and execution posture beyond one live account module.",
                "cta": "Open CRM",
                "href": str(active_account_module["crm_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Account Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect the live account room, the next move, and the wider counterparty lane.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the live account room, the next module move, customers, or the wider CRM hub instead of defaulting to source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Room / Next / Lane</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    active_claim_module = get_active_claim_module_context(current_dir)
    if doc_kind == "Overview" and active_claim_module:
        next_title = strip_open_prefix(str(active_claim_module["next_action_label"])) or "Next Route"
        next_pill = str(active_claim_module["next_pill"]).replace("Next ", "", 1).strip() or "Next Route"
        routes = [
            {
                "title": str(active_claim_module["room_title"]),
                "pill": "Live Claim Room",
                "copy": f"Return to {str(active_claim_module['room_title'])} when the founder needs the full live claim answer across containment, recovery, proof, and escalation instead of a single module view.",
                "cta": str(active_claim_module["room_entry_label"]),
                "href": str(active_claim_module["room_entry_href"]),
            },
            {
                "title": next_title,
                "pill": next_pill,
                "copy": f"Follow the next route when {str(active_claim_module['module_title']).lower()} has already done its job and the claim now depends on the next move inside the governed case sequence.",
                "cta": str(active_claim_module["next_action_label"]),
                "href": str(active_claim_module["next_action_href"]),
            },
            {
                "title": "Inspection Cases",
                "pill": "Case Lane",
                "copy": "Move back into inspection cases when the founder needs the broader governed case lane, adjacent complaint posture, and inspection context beyond this one module.",
                "cta": "Open Inspection Cases",
                "href": str(active_claim_module["inspection_cases_href"]),
            },
            {
                "title": "Compliance",
                "pill": "Governance Hub",
                "copy": "Return to compliance when the founder needs the wider proof, supplier-control, and governed-case map beyond one live claim module.",
                "cta": "Open Compliance",
                "href": str(active_claim_module["compliance_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Claim Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect the live room, the next move, and the wider governed case lane.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the live claim room, the next module move, inspection cases, or the wider compliance hub instead of defaulting to source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Room / Next / Lane</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    supplier_approval_module = get_supplier_approval_module_context(current_dir)
    if doc_kind == "Overview" and supplier_approval_module:
        next_title = strip_open_prefix(str(supplier_approval_module["next_action_label"])) or "Next Route"
        next_pill = str(supplier_approval_module["next_pill"]).replace("Next ", "", 1).strip() or "Next Route"
        routes = [
            {
                "title": str(supplier_approval_module["room_title"]),
                "pill": "Supplier Governance Room",
                "copy": f"Return to {str(supplier_approval_module['room_title'])} when the founder needs the full approval answer across performance, resilience, and dependence posture instead of a single module view.",
                "cta": str(supplier_approval_module["room_entry_label"]),
                "href": str(supplier_approval_module["room_entry_href"]),
            },
            {
                "title": next_title,
                "pill": next_pill,
                "copy": f"Follow the next route when {str(supplier_approval_module['module_title']).lower()} has already done its job and supplier governance now depends on the next performance or resilience surface.",
                "cta": str(supplier_approval_module["next_action_label"]),
                "href": str(supplier_approval_module["next_action_href"]),
            },
            {
                "title": "Supplier Approval",
                "pill": "Governance Lane",
                "copy": "Move back into supplier approval when the founder needs the wider governed supplier lane instead of one module.",
                "cta": "Open Supplier Approval",
                "href": str(supplier_approval_module["supplier_approval_href"]),
            },
            {
                "title": "Compliance",
                "pill": "Governance Hub",
                "copy": "Return to compliance when the founder needs the wider proof, inspection, and supplier-governance map beyond one module.",
                "cta": "Open Compliance",
                "href": str(supplier_approval_module["compliance_href"]),
            },
            {
                "title": strip_open_prefix(str(supplier_approval_module["board_cta"])),
                "pill": "Control Board",
                "copy": "Open the linked board when the next answer depends on the wider founder dashboard rather than the room module alone.",
                "cta": str(supplier_approval_module["board_cta"]),
                "href": str(supplier_approval_module["board_href"]),
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Supplier Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect the supplier room, the next review track, and the wider governance lane.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the live supplier room, the next review move, supplier approval, compliance, or the linked board instead of defaulting to source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">5 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Room / Next / Lane / Board</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == "02_crm/04_deals":
        routes = [
            {
                "title": "Active Deals",
                "pill": "Live Deal Lane",
                "copy": "Return to active deals when the founder needs the current commercial room, founder routes, and outbound commitment surfaces that still carry live pressure.",
                "cta": "Open Active Deals",
                "href": "active/OPEN-HERE.html",
            },
            {
                "title": "Won Deals",
                "pill": "Reference Wins",
                "copy": "Open won deals when the founder wants retained commercial wins for replication, precedent, and narrative continuity rather than live commitment calls.",
                "cta": "Open Won Deals",
                "href": "won/OPEN-HERE.html",
            },
            {
                "title": "Lost Deals",
                "pill": "Recovery Learning",
                "copy": "Move into lost deals when the next answer depends on missed commercial patterns, accountability, and recovery learning instead of active movement.",
                "cta": "Open Lost Deals",
                "href": "lost/OPEN-HERE.html",
            },
            {
                "title": "CRM Hub",
                "pill": "Commercial System",
                "copy": "Return to CRM when the founder needs the wider counterparty and task map around deal posture, not only the deal hub itself.",
                "cta": "Open CRM",
                "href": "../OPEN-HERE.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Deal Hub Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the lanes that reconnect live posture, retained wins, and recovery learning.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to active deals, won deals, lost deals, or the wider CRM hub instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Live / Won / Lost / CRM</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == "03_operations/03_shipments/active":
        routes = [
            {
                "title": "Active Shipments",
                "pill": "Movement Lane",
                "copy": "Return to active shipments when the founder needs the live brief, route lanes, and current movement room in one governed shipment layer.",
                "cta": "Open Active Shipments",
                "href": "OPEN-HERE.html",
            },
            {
                "title": "Release Gate",
                "pill": "Release Control",
                "copy": "Move into the live release gate when the next decision depends on whether packet completeness and shipment readiness truly authorize movement.",
                "cta": "Open Release Gate",
                "href": "SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/OPEN-HERE.html",
            },
            {
                "title": "Packet Proof",
                "pill": "Document Spine",
                "copy": "Open packet proof when the founder needs the document spine, supplier release packet, and shipment review trail behind the move.",
                "cta": "Open Packet Proof",
                "href": "SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/OPEN-HERE.html",
            },
            {
                "title": "Shipment Control Tower",
                "pill": "Founder Control",
                "copy": "Jump to the shipment control tower when the live move needs executive visibility, escalation rhythm, or same-day intervention.",
                "cta": "Open Shipment Control Tower",
                "href": "../../../06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Shipment Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect live movement, release readiness, and packet proof.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to active shipments, the release gate, packet proof, or the shipment control tower instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Movement / Release / Proof</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == "02_crm/04_deals/active":
        routes = [
            {
                "title": "Active Deals",
                "pill": "Deal Flow Lane",
                "copy": "Return to active deals when the founder needs the lane brief, founder routes, and current live deal room in one governed commercial surface.",
                "cta": "Open Active Deals",
                "href": "OPEN-HERE.html",
            },
            {
                "title": "Matter Control",
                "pill": "Control Route",
                "copy": "Open matter control when the next answer depends on live deal discipline, executable closure, and the exact control spine behind the active commercial room.",
                "cta": "Open Matter Control",
                "href": "DEAL-2026-001_AtlanticFoods_Garlic/MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control/OPEN-HERE.html",
            },
            {
                "title": "Capital Allocation",
                "pill": "Commitment Route",
                "copy": "Move into capital allocation when release priority, commercial confidence, or commitment weight has to be judged before the deal widens.",
                "cta": "Open Capital Allocation",
                "href": "../../../06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.html",
            },
            {
                "title": "Formal Offer Packet",
                "pill": "Outbound Route",
                "copy": "Open the formal offer packet when the founder needs the send-ready commercial surface that carries live deal posture into institutional outbound language.",
                "cta": "Open Formal Offer Packet",
                "href": "DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/OPEN-HERE.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Deal Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect deal control, commitment weight, and outbound readiness.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to active deals, matter control, capital allocation, or the formal offer packet instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Control / Commit / Outbound</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and is_archive_directory(current_dir):
        routes = [
            {
                "title": "Archived CRM",
                "pill": "Retained Commercial",
                "copy": "Return to archived CRM when the founder needs the retained commercial stack, closed deal trail, and retrieval posture instead of the wider archive overview.",
                "cta": "Open Archived CRM",
                "href": "03_crm/OPEN-HERE.html",
            },
            {
                "title": "Archive Closeout SOP",
                "pill": "Closeout Control",
                "copy": "Move into archive closeout standards when the question is whether a matter is truly complete enough to leave the active operating layer.",
                "cta": "Open Archive Closeout SOP",
                "href": "../05_sops/07_archive/Archive-Closeout-SOP.html",
            },
            {
                "title": "Closed Deal Memo",
                "pill": "Retained Matter",
                "copy": "Open the closed deal memo when the founder needs one concrete retained matter with final references, historical context, and archived record links.",
                "cta": "Open Closed Deal Memo",
                "href": "03_crm/DEAL-2026-001_AtlanticFoods_Garlic-CLOSED/README.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded archive memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Archive Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect retained history, closeout control, and concrete retrieval.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to archived CRM, archive closeout standards, one retained matter, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">History / Closeout / Retrieval</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and is_sops_directory(current_dir):
        routes = [
            {
                "title": "Founder Cadence SOP",
                "pill": "Founder Rhythm",
                "copy": "Return to founder cadence when the next move depends on daily, weekly, and monthly operating rhythm rather than the wider SOP layer.",
                "cta": "Open Founder Cadence SOP",
                "href": "06_dashboard/Founder-Operating-Cadence-SOP.html",
            },
            {
                "title": "Commercial Lifecycle SOP",
                "pill": "Lifecycle Control",
                "copy": "Move into the commercial lifecycle SOP when stage transitions, deal discipline, and customer conversion rules need to stay explicit.",
                "cta": "Open Commercial Lifecycle SOP",
                "href": "04_crm/Commercial-Execution-Lifecycle-SOP.html",
            },
            {
                "title": "Communication Standard SOP",
                "pill": "Outbound Discipline",
                "copy": "Open the communication standard when the founder needs institutional wording, response discipline, and controlled release logic for counterparties.",
                "cta": "Open Communication Standard SOP",
                "href": "08_external-communications/Counterparty-Communication-Standard-SOP.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded SOP memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">SOP Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect founder rhythm, lifecycle control, and communication discipline.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to founder cadence, commercial lifecycle, communication standards, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Rhythm / Lifecycle / Outbound</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and is_dashboard_directory(current_dir):
        routes = [
            {
                "title": "Founder Dashboard",
                "pill": "Daily Control",
                "copy": "Return to the founder dashboard when the next move depends on same-day posture across revenue, execution, compliance, cash, and pending approvals.",
                "cta": "Open Founder Dashboard",
                "href": "01_executive/Daily-Founder-Dashboard.html",
            },
            {
                "title": "Weekly Review",
                "pill": "Cadence Review",
                "copy": "Move into the weekly executive review when leadership cadence, cross-functional drift, and next-week priorities matter more than the wider dashboard layer.",
                "cta": "Open Weekly Review",
                "href": "14_weekly-executive-review/Weekly-Executive-Operating-Review.html",
            },
            {
                "title": "Executable Checks",
                "pill": "Execution Watch",
                "copy": "Open executable checks when the founder needs one board for trust overrides, live evidence state, same-day cutoff pressure, and blocked gates.",
                "cta": "Open Executable Checks",
                "href": "40_executable-checks/Trust-Override-Executable-Check-Control-Board.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded dashboard memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Dashboard Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect founder control, cadence review, and executable checks.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the daily dashboard, weekly review, executable checks, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Daily / Weekly / Watch</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and is_compliance_directory(current_dir):
        routes = [
            {
                "title": "Inspection Cases",
                "pill": "Governed Cases",
                "copy": "Return to inspection cases when the founder needs complaint recovery, readiness reviews, and CAPA posture rather than the wider compliance overview.",
                "cta": "Open Inspection Cases",
                "href": "05_inspections/OPEN-HERE.html",
            },
            {
                "title": "Supplier Approval",
                "pill": "Supplier Control",
                "copy": "Move into supplier approval when continuity, approval posture, and fallback governance matter more than complaint or proof review.",
                "cta": "Open Supplier Approval",
                "href": "06_supplier-approval/OPEN-HERE.html",
            },
            {
                "title": "Traceability",
                "pill": "Proof Chain",
                "copy": "Open traceability when the founder needs lot-path proof, audit readiness, and retained evidence across a governed case.",
                "cta": "Open Traceability",
                "href": "04_traceability/OPEN-HERE.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded compliance memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Compliance Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect governed cases, supplier control, and proof.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to inspection cases, supplier approval, traceability, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Cases / Suppliers / Proof</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and is_operations_directory(current_dir):
        routes = [
            {
                "title": "Active Shipments",
                "pill": "Live Execution",
                "copy": "Return to active shipments when the founder needs the live movement rooms, release gates, and shipment modules rather than the wider operations overview.",
                "cta": "Open Active Shipments",
                "href": "03_shipments/active/OPEN-HERE.html",
            },
            {
                "title": "Operations Command",
                "pill": "Founder Control",
                "copy": "Move into the operations command center when live gates, escalation rhythm, and same-day interventions need one executive control surface.",
                "cta": "Open Operations Command",
                "href": "../06_dashboard/03_operations/Daily-Operations-Command-Center.html",
            },
            {
                "title": "Working Files",
                "pill": "Support Surface",
                "copy": "Open working files when execution depends on temporary trackers, spreadsheets, and support records that still need final placement.",
                "cta": "Open Working Files",
                "href": "05_working-files/OPEN-HERE.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded operations memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Operations Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect live execution, founder control, and support files.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to active shipments, operations command, working files, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Execution / Command / Support</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and is_crm_directory(current_dir):
        routes = [
            {
                "title": "Customer Accounts",
                "pill": "Counterparty Layer",
                "copy": "Return to customer accounts when the founder needs trust posture, collections, and release exposure across active commercial relationships.",
                "cta": "Open Customer Accounts",
                "href": "02_customers/OPEN-HERE.html",
            },
            {
                "title": "Active Deals",
                "pill": "Deal Posture",
                "copy": "Move into active deals when the founder needs the live commercial matter stack instead of the wider CRM overview.",
                "cta": "Open Active Deals",
                "href": "04_deals/active/OPEN-HERE.html",
            },
            {
                "title": "Founder Queue",
                "pill": "Execution Queue",
                "copy": "Open the founder execution queue when deal pressure needs explicit task ownership, executable checks, and follow-through discipline.",
                "cta": "Open Founder Queue",
                "href": "05_tasks/TASK-2026-001_Founder-Execution-Queue/README.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded CRM memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">CRM Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect counterparties, deal posture, and founder follow-through.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to customer accounts, active deals, founder queue, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Counterparties / Deals / Queue</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and is_templates_directory(current_dir):
        routes = [
            {
                "title": "Template Domains",
                "pill": "Protected Masters",
                "copy": "Return to the full template domain grid when the founder needs the governed master landscape instead of a single route or memo view.",
                "cta": "Open Template Domains",
                "href": "OPEN-HERE.html#room-modules",
            },
            {
                "title": "Template Fast Routes",
                "pill": "Route Stack",
                "copy": "Open the fast-route layer when the founder needs the shortest path into contained movement, outbound release, or founder-governance templates.",
                "cta": "Open Fast Routes",
                "href": "OPEN-HERE.html#featured-routes",
            },
            {
                "title": "Founder Control Templates",
                "pill": "Governance Route",
                "copy": "Move into the governance template surface when a matter needs founder control, executable checks, and exception discipline before drafting widens.",
                "cta": "Open Founder Control Templates",
                "href": "10_governance/OPEN-HERE.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded templates memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Template Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect protected masters to the right drafting path.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to template domains, fast routes, founder-control templates, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Masters / Routes / Governance</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and is_brand_assets_directory(current_dir):
        routes = [
            {
                "title": "Brand",
                "pill": "Brand Hub",
                "copy": "Return to the parent brand layer when the founder needs assets, guidelines, and exports in one governed navigation surface.",
                "cta": "Open Brand",
                "href": "../OPEN-HERE.html",
            },
            {
                "title": "Brand Signatures",
                "pill": "Review Surface",
                "copy": "Move into brand signatures when the founder needs approved outbound identity closures rather than the broader asset map.",
                "cta": "Open Brand Signatures",
                "href": "04_signatures/OPEN-HERE.html",
            },
            {
                "title": "Approved Compositions",
                "pill": "Review Surface",
                "copy": "Open approved compositions when the founder needs governed lockups, layout treatments, and presentation-ready compositions.",
                "cta": "Open Approved Compositions",
                "href": "05_approved-compositions/OPEN-HERE.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded asset memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Asset Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect asset custody to review-ready brand surfaces.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the parent brand hub, the two review surfaces, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Brand / Review / Source</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and is_brand_directory(current_dir):
        routes = [
            {
                "title": "Assets",
                "pill": "Approved Assets",
                "copy": "Return to the approved asset layer when the founder needs signatures, compositions, and protected brand materials rather than written governance.",
                "cta": "Open Assets",
                "href": "01_assets/OPEN-HERE.html",
            },
            {
                "title": "Brand Guidelines",
                "pill": "Guidance Hub",
                "copy": "Move into brand guidelines when the founder needs the written rule set that governs identity, document standard, and voice discipline.",
                "cta": "Open Brand Guidelines",
                "href": "02_guidelines/OPEN-HERE.html",
            },
            {
                "title": "Exports",
                "pill": "Export Hub",
                "copy": "Open exports when the founder needs preview docs, domain lanes, and the visual standard that carry brand governance into founder-facing review.",
                "cta": "Open Exports",
                "href": "03_exports/OPEN-HERE.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded brand memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Brand Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect brand governance to approved assets, rules, and exports.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to assets, brand guidelines, exports, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Assets / Guidance / Exports</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and is_preview_docs_directory(current_dir):
        routes = [
            {
                "title": "Founder Pathways",
                "pill": "Hub Route",
                "copy": "Return to the fast-entry pathways when the founder wants the right decision route before reopening the full benchmark library.",
                "cta": "Open Founder Pathways",
                "href": "index.html#founder-pathways",
            },
            {
                "title": "Domain Lanes",
                "pill": "Benchmark Library",
                "copy": "Open the domain lanes when the founder wants the benchmark library segmented by operating theme instead of re-entering a single preview.",
                "cta": "Open Domain Lanes",
                "href": "index.html#full-catalog",
            },
            {
                "title": "Brand Anchors",
                "pill": "Reference Surface",
                "copy": "Move into the approved anchor layer when the founder needs the controlled visual lineage behind preview benchmarks and outward-facing surfaces.",
                "cta": "Open Brand Anchors",
                "href": "index.html#brand-anchors",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded preview memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        meta_html = (
            '<div class="brief-panel-meta">'
            f'<span class="meta-pill meta-pill--brief-source-count">{len(routes)} Exit Routes</span>'
            '<span class="meta-pill meta-pill--brief-source-state">Founder / Lanes / Reference</span>'
            "</div>"
        )
        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Preview Hub Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the route that gets the founder back into the right preview architecture.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the hub pathways, benchmark lanes, approved anchors, or the memo source instead of falling back to generic source routing.</p>"
            f"{meta_html}"
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and is_brand_guidelines_directory(current_dir):
        routes = [
            {
                "title": "Guidance Standards",
                "pill": "Brand Guidance",
                "copy": "Return to the guidance standards when the founder needs the full rule set behind identity, document design, and institutional voice.",
                "cta": "Open Guidance Standards",
                "href": "OPEN-HERE.html#supporting-files",
            },
            {
                "title": "Visual Standard",
                "pill": "Governance Surface",
                "copy": "Move into visual standard when the founder needs the governed styling system that carries these rules into branded previews and exports.",
                "cta": "Open Visual Standard",
                "href": "../03_exports/01_visual-standard/OPEN-HERE.html",
            },
            {
                "title": "Exports",
                "pill": "Reference Layer",
                "copy": "Open exports when the founder needs the parent hub that connects guidance rules to preview docs and outbound benchmark surfaces.",
                "cta": "Open Exports",
                "href": "../03_exports/OPEN-HERE.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded guidance memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Guidance Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect brand rules to visual governance and export routing.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to the guidance standards, visual standard, exports, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Rules / Governance / Exports</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and is_exports_directory(current_dir):
        routes = [
            {
                "title": "Preview Docs",
                "pill": "Benchmark Hub",
                "copy": "Return to preview docs when the founder needs the governed entry surface into benchmark review rather than the export-layer overview.",
                "cta": "Open Preview Docs",
                "href": "02_preview-docs/OPEN-HERE.html",
            },
            {
                "title": "Domain Lanes",
                "pill": "Benchmark Library",
                "copy": "Open the domain lanes when the founder wants the preview library segmented by operating theme inside the full benchmark hub.",
                "cta": "Open Domain Lanes",
                "href": "02_preview-docs/index.html#full-catalog",
            },
            {
                "title": "Visual Standard",
                "pill": "Governance Surface",
                "copy": "Move into visual standard when the founder needs the styling discipline that governs branded previews and exports.",
                "cta": "Open Visual Standard",
                "href": "01_visual-standard/OPEN-HERE.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded export memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Export Hub Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reopen benchmark routing and visual governance.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to preview docs, domain lanes, visual standard, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Hub / Lanes / Governance</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and is_visual_standard_directory(current_dir):
        routes = [
            {
                "title": "Exports",
                "pill": "Export Hub",
                "copy": "Return to exports when the founder needs the parent route that connects visual governance to preview docs and benchmark routing.",
                "cta": "Open Exports",
                "href": "../OPEN-HERE.html",
            },
            {
                "title": "Preview Docs",
                "pill": "Benchmark Surface",
                "copy": "Move into preview docs when the founder wants to see how this visual standard governs the live benchmark library and domain lanes.",
                "cta": "Open Preview Docs",
                "href": "../02_preview-docs/OPEN-HERE.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded standard memo surface.",
                "cta": "Open Memo Source",
                "href": path.name,
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append(
                (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
            )
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Standard Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that keep visual governance connected to the live benchmark system.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to exports, preview docs, or the memo source instead of falling back to generic source-integrity language.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">3 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Hub / Benchmark / Source</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == LEAD_ROOM_RELATIVE:
        routes = [
            {
                "title": "Leads",
                "pill": "Lead Lane",
                "copy": "Return to leads when the founder needs the wider prospect lane around qualification, stage discipline, and advancement timing.",
                "cta": "Open Leads",
                "href": "../OPEN-HERE.html",
            },
            {
                "title": "Sales Pipeline",
                "pill": "Control Board",
                "copy": "Move into sales pipeline when qualification priority, conversion posture, and next commercial sequencing need comparative founder review.",
                "cta": "Open Sales Pipeline",
                "href": "../../../06_dashboard/02_sales-pipeline/Daily-Sales-Pipeline-Command-Center.html",
            },
            {
                "title": "Founder Queue",
                "pill": "Execution Surface",
                "copy": "Open the founder queue when the next commercial move needs owned follow-through, explicit closure, or a bounded founder override path.",
                "cta": "Open Founder Queue",
                "href": "../../05_tasks/TASK-2026-001_Founder-Execution-Queue/OPEN-HERE.html",
            },
            {
                "title": "CRM",
                "pill": "Commercial Hub",
                "copy": "Return to CRM when the founder needs the wider commercial lane map around leads, counterparties, deals, and tasks.",
                "cta": "Open CRM",
                "href": "../../OPEN-HERE.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append((strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source"))
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Lead Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect qualification, pipeline control, and explicit follow-through.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to leads, the sales pipeline board, founder follow-through, or the wider CRM hub instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Lane / Pipeline / Queue</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == SUPPLIER_ROOM_RELATIVE:
        routes = [
            {
                "title": "Suppliers",
                "pill": "Supplier Lane",
                "copy": "Return to suppliers when the founder needs the wider sourcing lane around continuity risk, counterparty confidence, and next sourcing moves.",
                "cta": "Open Suppliers",
                "href": "../OPEN-HERE.html",
            },
            {
                "title": "Supplier Approval",
                "pill": "Approval Surface",
                "copy": "Move into supplier approval when the sourcing answer now needs the governed compliance handoff rather than staying only in CRM supplier posture.",
                "cta": "Open Supplier Approval",
                "href": "../../../04_compliance/06_supplier-approval/OPEN-HERE.html",
            },
            {
                "title": "Supplier Performance",
                "pill": "Control Board",
                "copy": "Open the supplier performance board when current sourcing confidence needs a wider scorecard and watch-item read beyond one room.",
                "cta": "Open Supplier Performance",
                "href": "../../../06_dashboard/07_supplier-performance/Supplier-Performance-Review-Board.html",
            },
            {
                "title": "CRM",
                "pill": "Commercial Hub",
                "copy": "Return to CRM when the founder needs the wider commercial lane map around suppliers, customers, deals, and tasks.",
                "cta": "Open CRM",
                "href": "../../OPEN-HERE.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append((strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source"))
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Supplier Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect sourcing posture, approval governance, and supplier performance.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to suppliers, supplier approval, supplier performance, or the wider CRM hub instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Lane / Approval / Performance</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == TASK_ROOM_RELATIVE:
        routes = [
            {
                "title": "Tasks",
                "pill": "Task Lane",
                "copy": "Return to tasks when the founder needs the wider execution queue around live ownership, pending action, and closure discipline.",
                "cta": "Open Tasks",
                "href": "../OPEN-HERE.html",
            },
            {
                "title": "Executable Checks",
                "pill": "Gate Control",
                "copy": "Move into executable checks when this queue item needs formal live-gate closure rather than only narrative task review.",
                "cta": "Open Executable Checks",
                "href": "../../../06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html",
            },
            {
                "title": "Owner Accountability",
                "pill": "Control Board",
                "copy": "Open owner accountability when the founder needs the wider board that tests whether follow-through is holding beyond one queue item.",
                "cta": "Open Owner Accountability",
                "href": "../../../06_dashboard/28_owner-accountability/Executive-Owner-Accountability-and-Follow-Through-Review.html",
            },
            {
                "title": "CRM",
                "pill": "Commercial Hub",
                "copy": "Return to CRM when the founder needs the wider commercial lane map around tasks, deals, counterparties, and current execution pressure.",
                "cta": "Open CRM",
                "href": "../../OPEN-HERE.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append((strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source"))
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Execution Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect live queue pressure, gate control, and owner follow-through.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to tasks, executable checks, owner accountability, or the wider CRM hub instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Queue / Gates / Follow-Through</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == TRACEABILITY_ROOM_RELATIVE:
        routes = [
            {
                "title": "Traceability",
                "pill": "Proof Lane",
                "copy": "Return to traceability when the founder needs the wider proof-chain lane around lot lineage, retrieval discipline, and audit readiness.",
                "cta": "Open Traceability",
                "href": "../OPEN-HERE.html",
            },
            {
                "title": "Compliance Control",
                "pill": "Control Board",
                "copy": "Move into compliance control when the proof answer needs the wider board that governs same-day exception handling and regulator readiness.",
                "cta": "Open Compliance Control",
                "href": "../../../06_dashboard/04_compliance/Daily-Compliance-Control-Center.html",
            },
            {
                "title": "Claims Recovery",
                "pill": "Recovery Board",
                "copy": "Open claims recovery when the founder needs the wider board that translates proof into credit, recovery, or complaint consequence.",
                "cta": "Open Claims Recovery",
                "href": "../../../06_dashboard/30_claims-recovery/Claims-Credits-and-Recovery-Review.html",
            },
            {
                "title": "Compliance",
                "pill": "Governance Hub",
                "copy": "Return to Compliance when the founder needs the wider map across traceability, inspection cases, supplier approval, and proof governance.",
                "cta": "Open Compliance",
                "href": "../../OPEN-HERE.html",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append((strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source"))
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Traceability Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that reconnect lot proof, compliance control, and recovery consequence.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to traceability, compliance control, claims recovery, or the wider compliance hub instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Proof / Control / Recovery</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == ARCHIVED_CLOSED_DEAL_RELATIVE:
        routes = [
            {
                "title": "Archived CRM",
                "pill": "Retained Lane",
                "copy": "Return to archived CRM when the founder needs the wider retained commercial lane around this closed matter.",
                "cta": "Open Archived CRM",
                "href": "../OPEN-HERE.html",
            },
            {
                "title": "Archive",
                "pill": "Archive Hub",
                "copy": "Move into Archive when the founder needs the wider retained-history map beyond this one commercial record.",
                "cta": "Open Archive",
                "href": "../../OPEN-HERE.html",
            },
            {
                "title": "Archive Closeout SOP",
                "pill": "Closeout Standard",
                "copy": "Open archive closeout standards when the question is whether this matter was complete enough to stay closed.",
                "cta": "Open Archive Closeout SOP",
                "href": "../../../05_sops/07_archive/Archive-Closeout-SOP.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact retained-record wording matters more than the branded reading surface.",
                "cta": "Open Memo Source",
                "href": "README.md",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append((strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source"))
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Archive Return</p>"
            "<h2 class=\"section-title-sm\">Close this retained matter on the routes that keep archive memory, closeout discipline, and commercial context coherent.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to archived CRM, the archive hub, closeout standards, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Retained / Closeout / Source</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )
    if doc_kind == "Overview" and relative == WORKING_FILES_RELATIVE:
        routes = [
            {
                "title": "Operations",
                "pill": "Operating Hub",
                "copy": "Return to Operations when the staged record needs the wider live execution context before relocation.",
                "cta": "Open Operations",
                "href": "../OPEN-HERE.html",
            },
            {
                "title": "Active Shipments",
                "pill": "Movement Lane",
                "copy": "Move into Active Shipments when the support file belongs to a live shipment room, release gate, packet, or funding proof.",
                "cta": "Open Active Shipments",
                "href": "../03_shipments/active/OPEN-HERE.html",
            },
            {
                "title": "Operations Command",
                "pill": "Control Board",
                "copy": "Open Operations Command when the staged item affects same-day execution posture, ownership, or decision control.",
                "cta": "Open Operations Command",
                "href": "../../06_dashboard/03_operations/Daily-Operations-Command-Center.html",
            },
            {
                "title": "Memo Source",
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact staging wording matters more than the branded reading surface.",
                "cta": "Open Memo Source",
                "href": "README.md",
            },
        ]

        lineup_entries: list[tuple[str, str, str]] = []
        cards = []
        for index, route in enumerate(routes, start=1):
            anchor_id = get_brief_source_anchor_id(index, route["title"])
            lineup_entries.append((strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source"))
            cards.append(
                "<a class=\"brief-source-card\" "
                f'id="{html.escape(anchor_id, quote=True)}" '
                f'href="{html.escape(route["href"], quote=True)}">'
                "<div class=\"brief-source-meta\">"
                f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
                f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
                "</div>"
                f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
                f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
                f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
                "</a>"
            )

        return (
            '<section class="brief-source-panel" id="doc-source-route">'
            "<div class=\"brief-source-head\">"
            "<p class=\"eyebrow\">Staging Return</p>"
            "<h2 class=\"section-title-sm\">Close this memo on the routes that move temporary work back into governed operations.</h2>"
            "<p class=\"section-copy\">This closing layer returns the founder to Operations, Active Shipments, Operations Command, or the memo source instead of defaulting to generic source routing.</p>"
            '<div class="brief-panel-meta"><span class="meta-pill meta-pill--brief-source-count">4 Exit Routes</span><span class="meta-pill meta-pill--brief-source-state">Stage / Route / Control</span></div>'
            f"{render_brief_panel_lineup(lineup_entries)}"
            "</div>"
            f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
            "</section>"
        )

    hero_profile = build_portal_hero_context(current_dir)
    base_href = (
        relative_url(current_dir, ROOT_INDEX_PATH)
        if current_dir == REPO_ROOT
        else relative_url(current_dir, current_dir / "OPEN-HERE.html")
    )
    surface_title = (
        str(hero_profile.get("title", "")).strip()
        if hero_profile and hero_profile.get("title")
        else "UNYRA System"
        if current_dir == REPO_ROOT
        else humanize_surface_name(current_dir.name)
    )
    surface_pill = get_doc_card_surface_pill(current_dir, path, doc_kind)
    primary_cta = (
        "Open System Layer"
        if current_dir == REPO_ROOT
        else str(hero_profile.get("cta", "")).strip()
        if hero_profile and hero_profile.get("cta")
        else f"Open {surface_title}"
    )
    readable_layers = sum(
        1
        for child in current_dir.iterdir()
        if child.is_file()
        and child.suffix.lower() == ".md"
        and child.name not in {"README.md", "AGENTS.md", path.name}
    )
    source_cta = get_doc_card_source_cta(doc_kind)
    source_title = get_doc_card_source_label(doc_kind, path.name).split(" / ", 1)[0]
    routes = [
        {
            "title": surface_title,
            "pill": surface_pill if surface_pill and surface_pill != "Readable Layer" else "Live Surface",
            "copy": "Return to the live surface when the founder needs the full navigation mesh, linked layers, and operating context around this reading view.",
            "cta": primary_cta,
            "href": base_href,
        }
    ]
    if readable_layers:
        readable_title = "Readable Layer" if readable_layers == 1 else "Readable Layers"
        readable_cta = "Open Readable Layer" if readable_layers == 1 else "Open Readable Layers"
        routes.append(
            {
                "title": readable_title,
                "pill": "Support Surface",
                "copy": "Move into sibling readable layers when the next answer depends on adjacent notes, procedures, or supporting records in the same operating surface.",
                "cta": readable_cta,
                "href": f"{base_href}#supporting-files",
            }
        )
    routes.extend(
        [
            {
                "title": "Source Integrity",
                "pill": "Governed Route",
                "copy": "Use the protected source route when the founder needs to confirm how this branded document maps back to repository control and synchronized surfaces.",
                "cta": "Open Source Integrity",
                "href": f"{base_href}#visual-system",
            },
            {
                "title": source_title,
                "pill": "Repository Source",
                "copy": "Open the raw Markdown only when exact repository wording matters more than the branded reading surface.",
                "cta": source_cta,
                "href": path.name,
            },
        ]
    )

    lineup_entries: list[tuple[str, str, str]] = []
    cards = []
    for index, route in enumerate(routes, start=1):
        anchor_id = get_brief_source_anchor_id(index, route["title"])
        lineup_entries.append(
            (strip_open_prefix(route["cta"]), f"#{anchor_id}", "meta-pill--brief-lineup-source")
        )
        cards.append(
            "<a class=\"brief-source-card\" "
            f'id="{html.escape(anchor_id, quote=True)}" '
            f'href="{html.escape(route["href"], quote=True)}">'
            "<div class=\"brief-source-meta\">"
            f'<span class="brief-source-pill">{html.escape(route["pill"])}</span>'
            f'<span class="meta-pill meta-pill--brief-source-index">{index:02d}</span>'
            "</div>"
            f'<span class="brief-source-title">{html.escape(route["title"])}</span>'
            f'<span class="brief-source-copy">{html.escape(route["copy"])}</span>'
            f'<span class="brief-source-cta">{html.escape(route["cta"])}</span>'
            "</a>"
        )

    route_summary = "Surface / Support / Source" if readable_layers else "Surface / Source"
    meta_html = (
        '<div class="brief-panel-meta">'
        f'<span class="meta-pill meta-pill--brief-source-count">{len(routes)} Exit Routes</span>'
        f'<span class="meta-pill meta-pill--brief-source-state">{route_summary}</span>'
        "</div>"
    )
    summary_copy = (
        "This closing layer replaces the generic generated footer, so the founder exits the branded document through the live surface, adjacent readable notes, or the governed source route on purpose."
        if readable_layers
        else "This closing layer replaces the generic generated footer, so the founder exits the branded document through the live surface or exact source route on purpose."
    )
    return (
        '<section class="brief-source-panel" id="doc-source-route">'
        "<div class=\"brief-source-head\">"
        "<p class=\"eyebrow\">Source Route</p>"
        "<h2 class=\"section-title-sm\">Close this branded document on the exact layer or source route that still matters.</h2>"
        f"<p class=\"section-copy\">{html.escape(summary_copy)}</p>"
        f"{meta_html}"
        f"{render_brief_panel_lineup(lineup_entries)}"
        "</div>"
        f"<div class=\"brief-source-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def wrap_document_html(path: Path, title: str, subtitle: str, doc_kind: str, brief_header_identity_html: str, meta_cards: str, nav_panel_html: str, distribution_panel_html: str, focus_panel_html: str, action_panel_html: str, reading_panel_html: str, decision_panel_html: str, trigger_panel_html: str, module_panel_html: str, usage_panel_html: str, support_panel_html: str, related_panel_html: str, source_panel_html: str, body_html: str) -> str:
    current_dir = path.parent
    css_href = relative_url(current_dir, CSS_PATH)
    lockup_href = relative_url(current_dir, LOCKUP_PATH)
    seal_href = relative_url(current_dir, SEAL_PATH)
    root_href = relative_url(current_dir, ROOT_INDEX_PATH)
    folder_href = relative_url(current_dir, current_dir / "OPEN-HERE.html")
    source_href = path.name
    preview_hub_href = relative_url(current_dir, PREVIEW_HUB_PATH)
    overview_profile = build_portal_hero_context(current_dir) if doc_kind == "Overview" else None
    overview_surface_pill = get_doc_card_surface_pill(current_dir, path, doc_kind) if doc_kind == "Overview" else ""
    overview_title = (
        str(overview_profile.get("title", "")).strip()
        if overview_profile and overview_profile.get("title")
        else "UNYRA System"
        if current_dir == REPO_ROOT
        else humanize_surface_name(current_dir.name)
    )
    subtitle_text = (
        (clamp_summary(clean_markdown_summary(str(overview_profile.get("note", "")).strip())) if overview_profile else "")
        if doc_kind == "Overview"
        else ""
    ) or subtitle or "Branded visual reading view for founder-friendly navigation across the UNYRA operating system."
    breadcrumbs = (
        build_brief_breadcrumbs(path, current_dir)
        if doc_kind == "Executive Brief"
        else build_overview_breadcrumbs(path, current_dir)
        if doc_kind == "Overview"
        else build_document_breadcrumbs(path, current_dir, title)
    )
    display_doc_kind = get_doc_header_eyebrow(doc_kind, current_dir, path)
    room_profile = build_portal_hero_context(current_dir) if doc_kind == "Executive Brief" else None
    decision_target = str(room_profile.get("decision_target", "")).strip() if room_profile else ""
    has_watch = brief_has_escalation_triggers(current_dir / "README.md") if doc_kind == "Executive Brief" else False
    room_decision_href = ""
    room_decision_label = ""
    if decision_target:
        room_decision_href = (
            f"{folder_href}{decision_target}"
            if decision_target.startswith("#")
            else relative_url(current_dir, REPO_ROOT / decision_target)
        )
        room_decision_label = "Open Room Decision" if decision_target.startswith("#") else "Open Decision Control"
    room_trigger_href = f"{folder_href}#escalation-trigger-01" if has_watch else ""
    source_surface_href = "#brief-source-layer" if doc_kind == "Executive Brief" else source_href
    source_surface_label = "Open Source Layer" if doc_kind == "Executive Brief" else "Open Source Markdown"
    if doc_kind == "Executive Brief":
        active_deal_room_return = get_active_deal_room_return_context(current_dir)
        active_shipment_room_return = get_active_shipment_room_return_context(current_dir)
        active_account_room_return = get_active_account_room_return_context(current_dir)
        active_claim_room_return = get_active_claim_room_return_context(current_dir)
        fda_readiness_room_return = get_fda_readiness_room_return_context(current_dir)
        supplier_approval_room_return = get_supplier_approval_room_return_context(current_dir)
        if active_deal_room_return:
            viewer_actions = [
                ("button-primary", folder_href, "Open Room View"),
                (
                    "button-secondary",
                    room_decision_href or str(active_deal_room_return["lane_href"]),
                    room_decision_label or str(active_deal_room_return["lane_cta"]),
                ),
                (
                    "button-secondary",
                    room_trigger_href or source_surface_href,
                    "Open Room Trigger" if room_trigger_href else "Open Deal Return",
                ),
                ("button-secondary", str(active_deal_room_return["lane_href"]), str(active_deal_room_return["lane_cta"])),
            ]
        elif active_shipment_room_return:
            viewer_actions = [
                ("button-primary", folder_href, "Open Room View"),
                (
                    "button-secondary",
                    room_decision_href or str(active_shipment_room_return["lane_href"]),
                    room_decision_label or str(active_shipment_room_return["lane_cta"]),
                ),
                (
                    "button-secondary",
                    room_trigger_href or source_surface_href,
                    "Open Room Trigger" if room_trigger_href else "Open Shipment Return",
                ),
                ("button-secondary", str(active_shipment_room_return["lane_href"]), str(active_shipment_room_return["lane_cta"])),
            ]
        elif active_account_room_return:
            viewer_actions = [
                ("button-primary", folder_href, "Open Room View"),
                (
                    "button-secondary",
                    room_decision_href or str(active_account_room_return["lane_href"]),
                    room_decision_label or str(active_account_room_return["lane_cta"]),
                ),
                (
                    "button-secondary",
                    room_trigger_href or source_surface_href,
                    "Open Room Trigger" if room_trigger_href else "Open Account Return",
                ),
                ("button-secondary", str(active_account_room_return["lane_href"]), str(active_account_room_return["lane_cta"])),
            ]
        elif active_claim_room_return:
            viewer_actions = [
                ("button-primary", folder_href, "Open Room View"),
                (
                    "button-secondary",
                    room_decision_href or str(active_claim_room_return["lane_href"]),
                    room_decision_label or str(active_claim_room_return["lane_cta"]),
                ),
                (
                    "button-secondary",
                    room_trigger_href or source_surface_href,
                    "Open Room Trigger" if room_trigger_href else "Open Claim Return",
                ),
                ("button-secondary", str(active_claim_room_return["lane_href"]), str(active_claim_room_return["lane_cta"])),
            ]
        elif fda_readiness_room_return:
            viewer_actions = [
                ("button-primary", folder_href, "Open Room View"),
                (
                    "button-secondary",
                    room_decision_href or str(fda_readiness_room_return["lane_href"]),
                    room_decision_label or str(fda_readiness_room_return["lane_cta"]),
                ),
                (
                    "button-secondary",
                    room_trigger_href or source_surface_href,
                    "Open Room Trigger" if room_trigger_href else "Open Readiness Return",
                ),
                ("button-secondary", str(fda_readiness_room_return["board_href"]), str(fda_readiness_room_return["board_cta"])),
            ]
        elif supplier_approval_room_return:
            viewer_actions = [
                ("button-primary", folder_href, "Open Room View"),
                (
                    "button-secondary",
                    room_decision_href or str(supplier_approval_room_return["lane_href"]),
                    room_decision_label or str(supplier_approval_room_return["lane_cta"]),
                ),
                (
                    "button-secondary",
                    room_trigger_href or source_surface_href,
                    "Open Room Trigger" if room_trigger_href else "Open Supplier Return",
                ),
                ("button-secondary", str(supplier_approval_room_return["board_href"]), str(supplier_approval_room_return["board_cta"])),
            ]
        else:
            viewer_actions = [
                ("button-secondary", folder_href, "Open Room View"),
                (
                    "button-secondary",
                    room_decision_href or preview_hub_href,
                    room_decision_label or "Open Preview Docs",
                ),
                (
                    "button-secondary",
                    room_trigger_href or preview_hub_href,
                    "Open Room Trigger" if room_trigger_href else "Open Preview Docs",
                ),
                ("button-primary", source_surface_href, source_surface_label),
            ]
    elif doc_kind == "Overview":
        viewer_actions = build_overview_viewer_actions(
            path,
            current_dir,
            root_href,
            folder_href,
            source_href,
            overview_profile,
            overview_title,
        )
    else:
        viewer_actions = build_standard_viewer_actions(
            path,
            current_dir,
            root_href,
            folder_href,
            source_href,
            doc_kind,
            title,
        )
    viewer_actions_html = "".join(
        f'<a class="{html.escape(css_class, quote=True)}" href="{html.escape(href, quote=True)}">{html.escape(label)}</a>'
        for css_class, href, label in viewer_actions
    )
    render_body_section = not (doc_kind == "Executive Brief" and body_html == EMPTY_MARKDOWN_STATE_HTML)
    header_identity_html = (
        brief_header_identity_html
        if doc_kind == "Executive Brief" and brief_header_identity_html
        else f'<span class="doc-kind">{html.escape(overview_surface_pill)}</span><p class="doc-path">{html.escape(get_overview_memo_label(current_dir, overview_title))} / README.md</p>'
        if doc_kind == "Overview" and overview_surface_pill
        else f'<span class="doc-kind">{html.escape(doc_kind)}</span><p class="doc-path">{html.escape(get_doc_card_source_label(doc_kind, path.name))}</p>'
    )
    body_section_html = (
        f"""
      <div class="doc-body">
        <section class="section" id="doc-reading-surface">
          <div class="markdown-view">
            {body_html}
          </div>
        </section>
      </div>"""
        if render_body_section
        else ""
    )
    closeout_panel_html = (
        ""
        if doc_kind == "Executive Brief" and source_panel_html
        else render_document_closeout_panel(path, doc_kind, has_residual_body=render_body_section)
    )

    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{html.escape(title)} | UNYRA Visual View</title>
    {GENERATED_MARKER}
    <link rel="stylesheet" href="{css_href}" />
  </head>
  <body class="preview-shell">
    <article class="doc-sheet" id="brief-top">
      <div class="doc-rail"></div>
      <div class="viewer-toolbar">
        <div class="breadcrumbs">{breadcrumbs}</div>
        <div class="viewer-actions">
          {viewer_actions_html}
        </div>
      </div>
      <header class="doc-header">
        <div class="dashboard-hero">
          <div class="brand-header">
            <img
              class="brand-lockup"
              src="{lockup_href}"
              alt="UNYRA GROUP LLC approved lockup"
            />
            <div class="doc-header-copy">
              <p class="eyebrow">{html.escape(display_doc_kind)}</p>
              <h1 class="doc-title">{html.escape(title)}</h1>
              <p class="doc-subtitle">{html.escape(subtitle_text)}</p>
              {header_identity_html}
            </div>
          </div>
          <img
            class="dashboard-seal"
            src="{seal_href}"
            alt="UNYRA circular seal"
          />
        </div>
        <div class="doc-meta">
          {meta_cards}
        </div>
      </header>
      {nav_panel_html}
      {distribution_panel_html}
      {focus_panel_html}
      {action_panel_html}
      {reading_panel_html}
      {decision_panel_html}
      {trigger_panel_html}
      {module_panel_html}
      {usage_panel_html}
      {support_panel_html}
      {related_panel_html}
      {source_panel_html}
      {body_section_html}
      {closeout_panel_html}
    </article>
  </body>
</html>
"""


def build_path_role_note(path_context: dict[str, str] | None, has_room_paths: bool, *, current_module: bool = False) -> str:
    if path_context:
        lead = "This is the live" if current_module else "This module carries the live"
        return (
            '<p class="viewer-card-path-note">'
            f"{lead} <strong>{html.escape(str(path_context['pill']))} Path</strong> for the room, "
            "so the founder can treat it as the active operating answer instead of a supporting check."
            "</p>"
        )
    if has_room_paths:
        return (
            '<p class="viewer-card-path-note">'
            "Use this module as a supporting control to test, confirm, or tighten the live room path before the founder changes the case answer."
            "</p>"
        )
    return ""


def build_module_group_panel(
    eyebrow: str,
    title: str,
    copy: str,
    cards: list[str],
    *,
    anchor_id: str | None = None,
    summary_pills: list[tuple[str, str | None]] | None = None,
    current_path: bool = False,
) -> str:
    if not cards:
        return ""
    modifier = " viewer-subsection--current-path" if current_path else " viewer-subsection--supporting"
    anchor_attr = f' id="{html.escape(anchor_id, quote=True)}"' if anchor_id else ""
    summary_html = ""
    if summary_pills:
        summary_html = (
            '<div class="card-meta">'
            + "".join(
                (
                    f'<a class="meta-pill meta-pill--link" href="{html.escape(target, quote=True)}">{html.escape(pill)}</a>'
                    if target
                    else f'<span class="meta-pill">{html.escape(pill)}</span>'
                )
                for pill, target in summary_pills
            )
            + "</div>"
        )
    return f"""
          <div class="viewer-subsection{modifier}"{anchor_attr}>
            <div class="section-heading">
              <p class="eyebrow">{html.escape(eyebrow)}</p>
              <h3 class="section-title-sm">{html.escape(title)}</h3>
              <p class="section-copy">{html.escape(copy)}</p>
              {summary_html}
            </div>
            <div class="viewer-grid">
              {"".join(cards)}
            </div>
          </div>
"""


def get_folder_card_surface_pill(profile: dict[str, str] | None, portal_profile: dict[str, object] | None) -> str:
    source_area = (
        str(profile["area"])
        if profile and profile.get("area")
        else str(portal_profile["area"])
        if portal_profile and portal_profile.get("area")
        else ""
    )
    if "Archive" in source_area:
        return "Archive Surface"
    if "Retained Deal" in source_area:
        return "Retained Deal Surface"
    if "Task" in source_area:
        return "Task Surface"
    if "Customer" in source_area:
        return "Customer Surface"
    if "Won Deal" in source_area:
        return "Won Deal Surface"
    if "Lost Deal" in source_area:
        return "Lost Deal Surface"
    if "Deal" in source_area:
        return "Deal Surface"
    if "Supplier Approval" in source_area:
        return "Supplier Approval Surface"
    if "Traceability" in source_area:
        return "Traceability Surface"
    if "Inspection" in source_area:
        return "Inspection Surface"
    if "Signature" in source_area:
        return "Signature Surface"
    if "Composition" in source_area:
        return "Composition Surface"
    if "Asset" in source_area:
        return "Asset Surface"
    if "Export" in source_area:
        return "Export Surface"
    if "Visual Standard" in source_area:
        return "Visual Standard Surface"
    if "Preview" in source_area:
        return "Preview Surface"
    if "Lead" in source_area:
        return "Lead Surface"
    if "Supplier" in source_area:
        return "Supplier Surface"
    if "War Room" in source_area:
        return "War Room Surface"
    if "Room" in source_area:
        return "Room Surface"
    if "Board" in source_area:
        return "Board Surface"
    if "Procedure" in source_area or "SOP" in source_area:
        return "Procedure Surface"
    if "Guidance" in source_area:
        return "Guidance Surface"
    if "Template" in source_area:
        return "Template Surface"
    if "Module" in source_area:
        return "Module Surface"
    if "Brand" in source_area:
        return "Brand Surface"
    if "CRM" in source_area or "Commercial" in source_area:
        return "Commercial Surface"
    if "Operations" in source_area or "Shipment" in source_area or "Execution" in source_area or "Working File" in source_area:
        return "Execution Surface"
    if "Compliance" in source_area:
        return "Compliance Surface"
    if "Control" in source_area or "Dashboard" in source_area:
        return "Control Surface"
    if "Layer" in source_area:
        return "Layer Surface"
    return "Current Surface"


def get_folder_card_stat_profile(card_surface_pill: str, title: str) -> dict[str, str]:
    context = f"{card_surface_pill} {title}".lower()
    profile = {
        "docs_label": "Readable Layers",
        "child_label": "Linked Surfaces",
        "status_value": "Ready",
        "status_label": "Current Surface",
    }
    if "guidance" in context:
        profile.update(
            {
                "docs_label": "Guidance Notes",
                "child_label": "Guidance Paths",
                "status_value": "Guided",
                "status_label": "Guidance Surface",
            }
        )
    elif "template" in context:
        profile.update(
            {
                "docs_label": "Template Files",
                "child_label": "Template Sets",
                "status_value": "Protected",
                "status_label": "Template Surface",
            }
        )
    elif "procedure" in context or "sop" in context:
        profile.update(
            {
                "docs_label": "Procedure Notes",
                "child_label": "Procedure Paths",
                "status_value": "Governed",
                "status_label": "Procedure Surface",
            }
        )
    elif "board" in context or "dashboard" in context:
        profile.update(
            {
                "docs_label": "Board Notes",
                "child_label": "Linked Boards",
                "status_value": "Live",
                "status_label": "Board Surface",
            }
        )
    elif "task" in context:
        profile.update(
            {
                "docs_label": "Action Notes",
                "child_label": "Action Queues",
                "status_value": "Active",
                "status_label": "Task Surface",
            }
        )
    elif "archive" in context:
        profile.update(
            {
                "docs_label": "Archive Notes",
                "child_label": "Retained Layers",
                "status_value": "Retained",
                "status_label": "Archive Surface",
            }
        )
    elif "customer" in context:
        profile.update(
            {
                "docs_label": "Account Notes",
                "child_label": "Account Rooms",
                "status_value": "Active",
                "status_label": "Customer Surface",
            }
        )
    elif "won deal" in context:
        profile.update(
            {
                "docs_label": "Retained Notes",
                "child_label": "Reference Layers",
                "status_value": "Retained",
                "status_label": "Won Deal Surface",
            }
        )
    elif "lost deal" in context:
        profile.update(
            {
                "docs_label": "Recovery Notes",
                "child_label": "Learning Layers",
                "status_value": "Recorded",
                "status_label": "Lost Deal Surface",
            }
        )
    elif "retained deal" in context:
        profile.update(
            {
                "docs_label": "Closed Deal Memo",
                "child_label": "Archive Routes",
                "status_value": "Retained",
                "status_label": "Retained Deal Surface",
            }
        )
    elif "deal" in context:
        profile.update(
            {
                "docs_label": "Deal Notes",
                "child_label": "Deal Layers",
                "status_value": "Active",
                "status_label": "Deal Surface",
            }
        )
    elif "module" in context or "control" in context:
        profile.update(
            {
                "docs_label": "Control Notes",
                "child_label": "Linked Controls",
                "status_value": "Ready",
                "status_label": "Control Surface",
            }
        )
    elif "war room" in context:
        profile.update(
            {
                "docs_label": "War Room Notes",
                "child_label": "Live Controls",
                "status_value": "Live",
                "status_label": "War Room Surface",
            }
        )
    elif "traceability" in context:
        profile.update(
            {
                "docs_label": "Proof Notes",
                "child_label": "Proof Rooms",
                "status_value": "Governed",
                "status_label": "Traceability Surface",
            }
        )
    elif "inspection" in context:
        profile.update(
            {
                "docs_label": "Review Notes",
                "child_label": "Recovery Paths",
                "status_value": "Governed",
                "status_label": "Inspection Surface",
            }
        )
    elif "supplier approval" in context:
        profile.update(
            {
                "docs_label": "Approval Notes",
                "child_label": "Linked Reviews",
                "status_value": "Governed",
                "status_label": "Supplier Approval Surface",
            }
        )
    elif "lead" in context:
        profile.update(
            {
                "docs_label": "Lead Notes",
                "child_label": "Linked Moves",
                "status_value": "Active",
                "status_label": "Lead Surface",
            }
        )
    elif "supplier" in context:
        profile.update(
            {
                "docs_label": "Supplier Notes",
                "child_label": "Linked Reviews",
                "status_value": "Active",
                "status_label": "Supplier Surface",
            }
        )
    elif "room" in context:
        profile.update(
            {
                "docs_label": "Room Notes",
                "child_label": "Linked Controls",
                "status_value": "Live",
                "status_label": "Room Surface",
            }
        )
    elif "signature" in context:
        profile.update(
            {
                "docs_label": "Signature Notes",
                "child_label": "Signature Sets",
                "status_value": "Approved",
                "status_label": "Signature Surface",
            }
        )
    elif "composition" in context:
        profile.update(
            {
                "docs_label": "Composition Notes",
                "child_label": "Composition Sets",
                "status_value": "Approved",
                "status_label": "Composition Surface",
            }
        )
    elif "asset" in context:
        profile.update(
            {
                "docs_label": "Asset Notes",
                "child_label": "Asset Sets",
                "status_value": "Approved",
                "status_label": "Asset Surface",
            }
        )
    elif "export" in context:
        profile.update(
            {
                "docs_label": "Export Notes",
                "child_label": "Output Layers",
                "status_value": "Ready",
                "status_label": "Export Surface",
            }
        )
    elif "visual standard" in context:
        profile.update(
            {
                "docs_label": "Standard Notes",
                "child_label": "Standard Layers",
                "status_value": "Approved",
                "status_label": "Visual Standard Surface",
            }
        )
    elif "preview" in context:
        profile.update(
            {
                "docs_label": "Preview Notes",
                "child_label": "Preview Layers",
                "status_value": "Ready",
                "status_label": "Preview Surface",
            }
        )
    elif "brand" in context:
        profile.update(
            {
                "docs_label": "Brand Notes",
                "child_label": "Brand Layers",
                "status_value": "Approved",
                "status_label": "Brand Surface",
            }
        )
    elif "crm" in context or "commercial" in context:
        profile.update(
            {
                "docs_label": "Commercial Notes",
                "child_label": "Commercial Layers",
                "status_value": "Active",
                "status_label": "Commercial Surface",
            }
        )
    elif "operations" in context or "shipment" in context or "execution" in context or "working file" in context:
        profile.update(
            {
                "docs_label": "Execution Notes",
                "child_label": "Execution Layers",
                "status_value": "Active",
                "status_label": "Execution Surface",
            }
        )
    elif "compliance" in context:
        profile.update(
            {
                "docs_label": "Compliance Notes",
                "child_label": "Governed Layers",
                "status_value": "Governed",
                "status_label": "Compliance Surface",
            }
        )
    elif "layer" in context:
        profile.update(
            {
                "docs_label": "Readable Layers",
                "child_label": "Linked Layers",
                "status_value": "Ready",
                "status_label": "Layer Surface",
            }
        )
    return profile


def build_folder_card(directory: Path, current_dir: Path, markdown_files: list[Path], child_directories: list[Path], *, anchor_id: str | None = None) -> str:
    child_portal = directory / "OPEN-HERE.html"
    relative_dir = directory.relative_to(REPO_ROOT)
    area_key = relative_dir.parts[0] if relative_dir.parts else ""
    profile = build_folder_card_profile(current_dir, directory)
    portal_profile = build_portal_hero_context(directory)
    copy = (
        str(profile["copy"])
        if profile and profile.get("copy")
        else str(portal_profile["copy"])
        if portal_profile and portal_profile.get("copy")
        else TOP_LEVEL_COPY.get(directory.name, f"Use this operating surface to review {humanize_surface_name(directory.name)} in the branded layer.")
    )
    title = (
        str(profile["title"])
        if profile and profile.get("title")
        else str(portal_profile["title"])
        if portal_profile and portal_profile.get("title")
        else humanize_surface_name(directory.name)
    )
    pill = (
        str(profile["pill"])
        if profile and profile.get("pill")
        else str(portal_profile["area"])
        if portal_profile and portal_profile.get("area")
        else AREA_LABELS.get(area_key, humanize_slug(directory.name))
    )
    card_surface_pill = get_folder_card_surface_pill(profile, portal_profile)
    cta = (
        str(profile["cta"])
        if profile and profile.get("cta")
        else str(portal_profile["cta"])
        if portal_profile and portal_profile.get("cta")
        else f"Open {str(portal_profile['area'])}"
        if portal_profile and portal_profile.get("area")
        else f"Open {humanize_surface_name(directory.name)}"
    )
    md_count = len(markdown_files)
    child_count = len(child_directories)
    stat_profile = get_folder_card_stat_profile(card_surface_pill, title)
    docs_value: object = md_count
    docs_label = str(stat_profile["docs_label"])
    child_value: object = child_count
    child_label = str(stat_profile["child_label"])
    status_value: object = stat_profile["status_value"]
    status_label = str(stat_profile["status_label"])
    if is_archive_directory(directory):
        archive_metrics = get_archive_layer_metrics(directory)
        card_surface_pill = "Archive Hub"
        pill = "Retained History + Closeout"
        docs_value = archive_metrics["archived_matter_count"]
        docs_label = count_label(archive_metrics["archived_matter_count"], "Archived Matter")
        child_value = archive_metrics["archive_function_count"]
        child_label = count_label(archive_metrics["archive_function_count"], "Archive Function")
        status_value = archive_metrics["fast_route_count"]
        status_label = count_label(archive_metrics["fast_route_count"], "Fast Route")
    if is_sops_directory(directory):
        sop_metrics = get_sop_layer_metrics(directory)
        card_surface_pill = "SOP Hub"
        pill = "Standards + Control"
        docs_value = sop_metrics["sop_surface_count"]
        docs_label = count_label(sop_metrics["sop_surface_count"], "SOP Surface")
        child_value = sop_metrics["founder_standard_count"]
        child_label = count_label(sop_metrics["founder_standard_count"], "Founder Standard")
        status_value = sop_metrics["fast_route_count"]
        status_label = count_label(sop_metrics["fast_route_count"], "Fast Route")
    if is_dashboard_directory(directory):
        dashboard_metrics = get_dashboard_layer_metrics(directory)
        card_surface_pill = "Dashboard Hub"
        pill = "Founder Control + Cadence"
        docs_value = dashboard_metrics["dashboard_surface_count"]
        docs_label = count_label(dashboard_metrics["dashboard_surface_count"], "Dashboard Surface")
        child_value = dashboard_metrics["founder_cadence_count"]
        child_label = count_label(dashboard_metrics["founder_cadence_count"], "Founder Cadence")
        status_value = dashboard_metrics["fast_route_count"]
        status_label = count_label(dashboard_metrics["fast_route_count"], "Fast Route")
    if is_compliance_directory(directory):
        compliance_metrics = get_compliance_layer_metrics(directory)
        card_surface_pill = "Compliance Hub"
        pill = "Cases + Proof"
        docs_value = compliance_metrics["governed_case_count"]
        docs_label = count_label(compliance_metrics["governed_case_count"], "Governed Case")
        child_value = compliance_metrics["compliance_domain_count"]
        child_label = count_label(compliance_metrics["compliance_domain_count"], "Compliance Domain")
        status_value = compliance_metrics["fast_route_count"]
        status_label = count_label(compliance_metrics["fast_route_count"], "Fast Route")
    if is_operations_directory(directory):
        operations_metrics = get_operations_layer_metrics(directory)
        card_surface_pill = "Operations Hub"
        pill = "Live Execution + Gates"
        docs_value = operations_metrics["active_shipment_count"]
        docs_label = count_label(operations_metrics["active_shipment_count"], "Active Shipment")
        child_value = operations_metrics["execution_domain_count"]
        child_label = count_label(operations_metrics["execution_domain_count"], "Execution Domain")
        status_value = operations_metrics["fast_route_count"]
        status_label = count_label(operations_metrics["fast_route_count"], "Fast Route")
    if is_crm_directory(directory):
        crm_metrics = get_crm_layer_metrics(directory)
        card_surface_pill = "CRM Hub"
        pill = "Counterparties + Deal Posture"
        docs_value = crm_metrics["counterparty_layer_count"]
        docs_label = count_label(crm_metrics["counterparty_layer_count"], "Counterparty Layer")
        child_value = crm_metrics["deal_posture_count"]
        child_label = count_label(crm_metrics["deal_posture_count"], "Deal Posture")
        status_value = crm_metrics["execution_queue_count"]
        status_label = count_label(crm_metrics["execution_queue_count"], "Execution Queue")
    if is_templates_directory(directory):
        template_metrics = get_template_layer_metrics(directory)
        card_surface_pill = "Template Hub"
        pill = "Masters + Routes"
        docs_value = template_metrics["master_template_count"]
        docs_label = count_label(template_metrics["master_template_count"], "Master Template")
        child_value = template_metrics["template_domain_count"]
        child_label = count_label(template_metrics["template_domain_count"], "Template Domain")
        status_value = template_metrics["fast_route_count"]
        status_label = count_label(template_metrics["fast_route_count"], "Fast Route")
    if is_brand_assets_directory(directory):
        asset_metrics = get_brand_assets_metrics(directory)
        card_surface_pill = "Asset Hub"
        pill = "Review + Protected Sets"
        docs_value = asset_metrics["asset_set_count"]
        docs_label = count_label(asset_metrics["asset_set_count"], "Asset Set")
        child_value = asset_metrics["review_surface_count"]
        child_label = count_label(asset_metrics["review_surface_count"], "Review Surface")
        status_value = asset_metrics["protected_set_count"]
        status_label = count_label(asset_metrics["protected_set_count"], "Protected Set")
    if is_brand_directory(directory):
        brand_metrics = get_brand_layer_metrics(directory)
        card_surface_pill = "Brand Hub"
        pill = "Assets + Governance"
        docs_value = brand_metrics["asset_set_count"]
        docs_label = count_label(brand_metrics["asset_set_count"], "Asset Set")
        child_value = brand_metrics["guidance_count"]
        child_label = count_label(brand_metrics["guidance_count"], "Guidance Standard")
        status_value = brand_metrics["preview_benchmark_count"]
        status_label = count_label(brand_metrics["preview_benchmark_count"], "Preview Benchmark")
    if is_brand_guidelines_directory(directory):
        guidance_metrics = get_brand_guidelines_metrics(directory)
        card_surface_pill = "Guidance Hub"
        pill = "Rules + Voice"
        docs_value = guidance_metrics["guidance_count"]
        docs_label = count_label(guidance_metrics["guidance_count"], "Guidance Standard")
        child_value = guidance_metrics["governance_surface_count"]
        child_label = count_label(guidance_metrics["governance_surface_count"], "Governance Surface")
        status_value = "Exports"
        status_label = "Reference Layer"
    if is_visual_standard_directory(directory):
        preview_metrics = get_preview_hub_metrics(REPO_ROOT / PREVIEW_DOCS_RELATIVE)
        card_surface_pill = "Standard Governance"
        pill = "Visual Standard"
        docs_value = 1
        docs_label = "Standard Memo"
        child_value = preview_metrics["benchmark_count"]
        child_label = count_label(preview_metrics["benchmark_count"], "Preview Benchmark")
        status_value = "Exports"
        status_label = "Export Hub"
    if is_exports_directory(directory):
        export_metrics = get_exports_metrics(directory)
        card_surface_pill = "Export Hub"
        pill = "Preview Docs + Standard"
        docs_value = export_metrics["benchmark_count"]
        docs_label = count_label(export_metrics["benchmark_count"], "Preview Benchmark")
        child_value = export_metrics["domain_lane_count"]
        child_label = count_label(export_metrics["domain_lane_count"], "Domain Lane")
        status_value = export_metrics["reference_surface_count"]
        status_label = count_label(export_metrics["reference_surface_count"], "Reference Surface")
    if is_preview_docs_directory(directory):
        preview_metrics = get_preview_hub_metrics(directory)
        card_surface_pill = "Preview Hub"
        pill = title
        docs_value = preview_metrics["benchmark_count"]
        docs_label = count_label(preview_metrics["benchmark_count"], "Preview Benchmark")
        child_value = preview_metrics["domain_lane_count"]
        child_label = count_label(preview_metrics["domain_lane_count"], "Domain Lane")
        status_value = preview_metrics["brand_anchor_count"]
        status_label = count_label(preview_metrics["brand_anchor_count"], "Brand Anchor")
    href = relative_url(current_dir, child_portal)
    relative_parent = current_dir.relative_to(REPO_ROOT).as_posix() if current_dir != REPO_ROOT else ""
    has_room_paths = bool(relative_parent and get_outcome_paths_profile(relative_parent))
    path_context = get_module_room_path_context(current_dir, directory) if has_room_paths else None
    path_sequence = get_outcome_path_sequence(relative_parent, str(path_context["pill"])) if path_context and relative_parent else None
    card_class = "viewer-card viewer-card--current-path" if path_context else "viewer-card viewer-card--supporting-control" if has_room_paths else "viewer-card"
    if path_context:
        cta = f"Open {str(path_context['pill'])} Path"
    path_pill_html = (
        (
            f'<span class="meta-pill">Path {path_sequence[0]:02d} of {path_sequence[1]:02d}</span>'
            f'<span class="meta-pill meta-pill--path-current">Current Path</span>'
        )
        if path_context
        else '<span class="meta-pill meta-pill--path-supporting">Supporting Control</span>' if has_room_paths else ""
    )
    path_role_note = build_path_role_note(path_context, has_room_paths)
    anchor_attr = f' id="{html.escape(anchor_id, quote=True)}"' if anchor_id else ""
    room_path_stat_html = (
        f"""
              <div class="stat-mini">
                <p class="stat-mini-value">{html.escape(str(path_context['pill']) if path_context else 'Support')}</p>
                <p class="stat-mini-label">Room Path</p>
              </div>"""
        if has_room_paths
        else ""
    )
    path_order_stat_html = (
        f"""
              <div class="stat-mini">
                <p class="stat-mini-value">{path_sequence[0]:02d}/{path_sequence[1]:02d}</p>
                <p class="stat-mini-label">Path Order</p>
              </div>"""
        if path_sequence
        else ""
    )
    secondary_pill_html = (
        f'<span class="meta-pill">{html.escape(pill)}</span>'
        if pill and pill != card_surface_pill
        else ""
    )

    return f"""
          <article class="{card_class}"{anchor_attr}>
            <div class="card-meta">
              <span class="meta-pill">{html.escape(card_surface_pill)}</span>
              {secondary_pill_html}
              {path_pill_html}
            </div>
            <h3 class="viewer-card-title">{html.escape(title)}</h3>
            <p class="viewer-card-copy">{html.escape(copy)}</p>
            {path_role_note}
            <div class="hero-stats">
              <div class="stat-mini">
                <p class="stat-mini-value">{html.escape(str(docs_value))}</p>
                <p class="stat-mini-label">{html.escape(docs_label)}</p>
              </div>
              <div class="stat-mini">
                <p class="stat-mini-value">{html.escape(str(child_value))}</p>
                <p class="stat-mini-label">{html.escape(child_label)}</p>
              </div>
              <div class="stat-mini">
                <p class="stat-mini-value">{html.escape(str(status_value))}</p>
                <p class="stat-mini-label">{html.escape(status_label)}</p>
              </div>
              {path_order_stat_html}
              {room_path_stat_html}
            </div>
            <div class="viewer-card-links">
              <a class="button-primary" href="{href}">{html.escape(cta)}</a>
            </div>
          </article>
"""


def build_doc_card(markdown_path: Path, current_dir: Path, title: str, subtitle: str, doc_kind: str) -> str:
    profile = build_doc_card_profile(current_dir, markdown_path)
    html_href = relative_url(current_dir, markdown_path.with_suffix(".html"))
    source_href = relative_url(current_dir, markdown_path)
    kind = str(profile["kind"]) if profile and profile.get("kind") else doc_kind
    surface_pill = get_doc_card_surface_pill(current_dir, markdown_path, kind)
    card_title = (
        str(profile["title_override"])
        if profile and profile.get("title_override")
        else get_doc_card_title(current_dir, markdown_path, title, kind, surface_pill)
    )
    copy = (
        str(profile["copy_override"])
        if profile and profile.get("copy_override")
        else get_doc_card_copy(subtitle, kind)
    )
    primary_cta = str(profile["cta"]) if profile and profile.get("cta") else get_doc_card_primary_cta(kind, surface_pill)
    source_cta = str(profile["source_cta"]) if profile and profile.get("source_cta") else get_doc_card_source_cta(kind)
    source_label = get_doc_card_source_label(kind, markdown_path.name)
    kind_label = get_doc_card_kind_label(kind, current_dir)
    priority_pill = str(profile["priority_pill"]) if profile and profile.get("priority_pill") else ""
    kind_pill_html = (
        f'<span class="meta-pill">{html.escape(kind_label)}</span>'
        if kind_label and kind_label != surface_pill
        else ""
    )
    priority_pill_html = f'<span class="meta-pill">{html.escape(priority_pill)}</span>' if priority_pill else ""
    return f"""
          <article class="viewer-card">
            <div class="card-meta">
              <span class="meta-pill">{html.escape(surface_pill)}</span>
              {kind_pill_html}
              {priority_pill_html}
            </div>
            <h3 class="viewer-card-title">{html.escape(card_title)}</h3>
            <p class="viewer-card-copy">{html.escape(copy)}</p>
            <p class="doc-path">{html.escape(source_label)}</p>
            <div class="viewer-card-links">
              <a class="button-primary" href="{html_href}">{html.escape(primary_cta)}</a>
              <a class="button-secondary" href="{source_href}">{html.escape(source_cta)}</a>
            </div>
          </article>
"""


def build_priority_brief_section(directory: Path, docs_for_dir: list[dict[str, str]]) -> str:
    brief_doc = next(
        (
            doc
            for doc in docs_for_dir
            if (build_doc_card_profile(directory, Path(str(doc["path"]))) or {}).get("kind") == "Executive Brief"
        ),
        None,
    )
    if not brief_doc:
        return ""

    markdown_path = Path(str(brief_doc["path"]))
    profile = build_doc_card_profile(directory, markdown_path) or {}
    title, subtitle, meta, body_lines = extract_document_parts(
        markdown_path.read_text(encoding="utf-8"),
        humanize_slug(markdown_path.stem),
    )
    meta_map = meta_to_dict(meta)
    brief_href = relative_url(directory, markdown_path.with_suffix(".html"))
    source_href = relative_url(directory, markdown_path)
    primary_cta = str(profile.get("cta") or "Open Executive Brief")
    summary = subtitle or "Use this executive brief as the first reading layer before opening modules or live boards."
    sequence_local, sequence_external = get_decision_sequence_scope_counts(directory)
    outcome_local, outcome_external = get_outcome_path_scope_counts(directory)
    sequence_summary_override = get_scope_summary_override(directory, "sequence")
    outcome_summary_override = get_scope_summary_override(directory, "outcomes")
    route_posture = get_route_posture(sequence_local, sequence_external, outcome_local, outcome_external)
    child_dirs = [
        path
        for path in directory.iterdir()
        if path.is_dir() and path.name not in SKIP_DIR_NAMES
    ]
    has_module_outcomes = bool(build_module_outcome_paths_section(directory))
    has_folder_section = bool(
        [
            child
            for child in order_child_directories(directory, child_dirs)
            if build_folder_card_profile(directory, child)
        ]
    )
    sequence_links = [("Open Sequence", "#decision-sequence")]
    if sequence_local and sequence_external:
        sequence_links.extend(
            [
                ("Open Seq In", "#decision-sequence-in-room"),
                ("Open Seq Out", "#decision-sequence-external"),
            ]
        )
    outcome_links = [("Open Outcomes", "#outcome-paths")]
    if sequence_external or outcome_external:
        if outcome_local and outcome_external:
            outcome_links.extend(
                [
                    ("Open In-Room", "#outcome-room-paths"),
                    ("Open External", "#outcome-external-controls"),
                ]
            )
    module_surface_links: list[tuple[str, str]] = []
    if has_folder_section:
        module_surface_links.append(("Open Modules", "#room-modules"))
    path_surface_links: list[tuple[str, str]] = []
    if bool(get_outcome_paths_profile(directory.relative_to(REPO_ROOT).as_posix())) and has_folder_section:
        path_surface_links.extend(
            [
                ("Open Live Path", "#room-live-path-modules"),
                ("Open Controls", "#room-supporting-controls"),
            ]
        )
    oversight_links: list[tuple[str, str]] = []
    if extract_section_list_items(body_lines, "Escalation Triggers"):
        oversight_links.append(("Open Watch", "#escalation-watch"))
    active_deal_room_return = get_active_deal_room_return_context(directory)
    active_shipment_room_return = get_active_shipment_room_return_context(directory)
    active_account_room_return = get_active_account_room_return_context(directory)
    active_claim_room_return = get_active_claim_room_return_context(directory)
    fda_readiness_room_return = get_fda_readiness_room_return_context(directory)
    supplier_approval_room_return = get_supplier_approval_room_return_context(directory)
    system_surface_links: list[tuple[str, str]] = []
    has_supporting_files = any(
        (build_doc_card_profile(directory, Path(str(doc["path"]))) or {}).get("kind") != "Executive Brief"
        for doc in docs_for_dir
    )
    if active_deal_room_return:
        system_surface_links.extend(
            [
                (str(active_deal_room_return["brief_cta"]), str(active_deal_room_return["brief_href"])),
                (str(active_deal_room_return["lane_cta"]), str(active_deal_room_return["lane_href"])),
                (str(active_deal_room_return["hub_cta"]), str(active_deal_room_return["hub_href"])),
                (str(active_deal_room_return["preview_cta"]), str(active_deal_room_return["preview_href"])),
            ]
        )
    elif active_shipment_room_return:
        system_surface_links.extend(
            [
                (str(active_shipment_room_return["brief_cta"]), str(active_shipment_room_return["brief_href"])),
                (str(active_shipment_room_return["lane_cta"]), str(active_shipment_room_return["lane_href"])),
                (str(active_shipment_room_return["hub_cta"]), str(active_shipment_room_return["hub_href"])),
                (str(active_shipment_room_return["board_cta"]), str(active_shipment_room_return["board_href"])),
            ]
        )
    elif active_account_room_return:
        system_surface_links.extend(
            [
                (str(active_account_room_return["brief_cta"]), str(active_account_room_return["brief_href"])),
                (str(active_account_room_return["lane_cta"]), str(active_account_room_return["lane_href"])),
                (str(active_account_room_return["hub_cta"]), str(active_account_room_return["hub_href"])),
                (str(active_account_room_return["board_cta"]), str(active_account_room_return["board_href"])),
            ]
        )
    elif active_claim_room_return:
        system_surface_links.extend(
            [
                (str(active_claim_room_return["brief_cta"]), str(active_claim_room_return["brief_href"])),
                (str(active_claim_room_return["lane_cta"]), str(active_claim_room_return["lane_href"])),
                (str(active_claim_room_return["hub_cta"]), str(active_claim_room_return["hub_href"])),
                (str(active_claim_room_return["board_cta"]), str(active_claim_room_return["board_href"])),
            ]
        )
    elif fda_readiness_room_return:
        system_surface_links.extend(
            [
                (str(fda_readiness_room_return["brief_cta"]), str(fda_readiness_room_return["brief_href"])),
                (str(fda_readiness_room_return["lane_cta"]), str(fda_readiness_room_return["lane_href"])),
                (str(fda_readiness_room_return["hub_cta"]), str(fda_readiness_room_return["hub_href"])),
                (str(fda_readiness_room_return["board_cta"]), str(fda_readiness_room_return["board_href"])),
            ]
        )
    elif supplier_approval_room_return:
        system_surface_links.extend(
            [
                (str(supplier_approval_room_return["brief_cta"]), str(supplier_approval_room_return["brief_href"])),
                (str(supplier_approval_room_return["lane_cta"]), str(supplier_approval_room_return["lane_href"])),
                (str(supplier_approval_room_return["hub_cta"]), str(supplier_approval_room_return["hub_href"])),
                (str(supplier_approval_room_return["board_cta"]), str(supplier_approval_room_return["board_href"])),
                (str(supplier_approval_room_return["resilience_cta"]), str(supplier_approval_room_return["resilience_href"])),
            ]
        )
    else:
        if has_supporting_files:
            system_surface_links.append(("Open Readable Layers", "#supporting-files"))
        system_surface_links.append(("Open Source Integrity", "#visual-system"))
    sequence_scope_summary = get_scope_summary_override(directory, "sequence") or format_scope_summary(sequence_local, sequence_external)
    outcome_scope_summary = get_scope_summary_override(directory, "outcomes") or format_scope_summary(outcome_local, outcome_external)
    sequence_scope_pill = get_route_scope_pill_override(directory, "Sequence") or format_route_scope_pill("Sequence", sequence_local, sequence_external)
    outcome_scope_pill = get_route_scope_pill_override(directory, "Outcomes") or format_route_scope_pill("Outcomes", outcome_local, outcome_external)
    route_links_html = build_route_posture_link_groups(
        [
            ("Sequence", sequence_links, "sequence", sequence_scope_summary),
            ("Outcomes", outcome_links, "outcomes", outcome_scope_summary),
            ("Oversight Layer", oversight_links, "support", "Escalation Watch" if oversight_links else None),
            ("Module Surface", module_surface_links, "module-surface", "Module Access" if module_surface_links else None),
            ("Path Surface", path_surface_links, "path-surface", "Live / Controls" if path_surface_links else None),
            (
                "Return Layer" if active_deal_room_return or active_shipment_room_return or active_account_room_return or active_claim_room_return or fda_readiness_room_return or supplier_approval_room_return else "Source Integrity",
                system_surface_links,
                "surface",
                "Brief / Lane / Hub / Preview"
                if active_deal_room_return
                else "Brief / Lane / Hub / Board"
                if active_shipment_room_return
                else "Brief / Lane / Hub / Board"
                if active_account_room_return
                else "Brief / Lane / Hub / Board"
                if active_claim_room_return
                else "Brief / Lane / Hub / Board"
                if fda_readiness_room_return
                else "Brief / Lane / Hub / Boards"
                if supplier_approval_room_return
                else "Readable / Source"
                if has_supporting_files
                else "Source Integrity",
            ),
        ]
    )

    signal_rows = [
        ("Primary Lens", meta_map.get("Primary Lens", "")),
        ("Decision Now", meta_map.get("Decision Now", "")),
        ("Escalation Rhythm", meta_map.get("Escalation Rhythm", "")),
    ]
    signal_cards = "".join(
        "<article class=\"priority-brief-signal\">"
        f"<p class=\"priority-brief-label\">{html.escape(label)}</p>"
        f"<p class=\"priority-brief-value\">{render_inline(value, directory)}</p>"
        "</article>"
        for label, value in signal_rows
        if value
    )

    return f"""
        <section class="home-section priority-brief-panel" id="founder-start-here">
          <div class="section-heading">
            <p class="eyebrow">Founder Start Here</p>
            <h2 class="section-title">Read the executive brief before opening modules.</h2>
            <p class="section-copy">
              This room's memo is the controlled starting point for the founder answer, so the case logic stays coherent before anyone jumps into individual modules.
            </p>
          </div>
          <div class="priority-brief-grid">
            <article class="priority-brief-card">
              <div class="card-meta">
                <span class="meta-pill">Read First</span>
                <span class="meta-pill">Executive Brief</span>
              </div>
              <h3 class="viewer-card-title">{html.escape(title)}</h3>
              <p class="viewer-card-copy">{html.escape(summary)}</p>
              <div class="card-meta priority-brief-route-meta">
                <span class="{html.escape(str(route_posture['pill_class']), quote=True)}">{html.escape(str(route_posture['label']))}</span>
                <span class="meta-pill">{html.escape(sequence_scope_pill)}</span>
                <span class="meta-pill">{html.escape(outcome_scope_pill)}</span>
              </div>
              <p class="{html.escape(str(route_posture['note_class']), quote=True)}">{html.escape(str(route_posture['note']))}</p>
              {route_links_html}
              <p class="doc-path">{html.escape(get_doc_card_source_label("Executive Brief", markdown_path.name))}</p>
              <div class="viewer-card-links">
                <a class="button-primary" href="{brief_href}">{html.escape(primary_cta)}</a>
                <a class="button-secondary" href="{brief_href}#executive-focus">Open Focus</a>
                <a class="button-secondary" href="{brief_href}#immediate-founder-actions">Open Actions</a>
                <a class="button-secondary" href="{brief_href}#decision-agenda">Open Decision</a>
                <a class="button-secondary" href="{source_href}">Open Brief Source</a>
              </div>
            </article>
            <div class="priority-brief-signals">
              {signal_cards}
            </div>
          </div>
        </section>
"""


def build_module_brief_snapshot_section(directory: Path) -> str:
    parent = directory.parent
    if parent == REPO_ROOT:
        return ""
    try:
        parent.relative_to(REPO_ROOT)
    except ValueError:
        return ""

    room_profile = build_portal_hero_context(parent)
    current_profile = build_folder_card_profile(parent, directory)
    brief_path = parent / "README.md"
    brief_profile = build_doc_card_profile(parent, brief_path) if brief_path.exists() else None
    if not room_profile or not current_profile or not brief_profile:
        return ""

    title, subtitle, meta, body_lines = extract_document_parts(
        brief_path.read_text(encoding="utf-8"),
        humanize_slug(brief_path.stem),
    )
    meta_map = meta_to_dict(meta)
    summary = subtitle or "Use the room brief as the controlled founder narrative before relying on a single module answer."
    brief_href = relative_url(directory, brief_path.with_suffix(".html"))
    source_href = relative_url(directory, brief_path)
    shipment_stack_override = get_shipment_stack_navigation_override(directory)
    room_title = str(room_profile["title"])
    module_title = str(current_profile["title"])
    sequence_local, sequence_external = get_decision_sequence_scope_counts(parent)
    outcome_local, outcome_external = get_outcome_path_scope_counts(parent)
    route_posture = get_route_posture(sequence_local, sequence_external, outcome_local, outcome_external)
    sequence_jump_links = get_module_sequence_jump_links(directory)
    stack_jump_links = get_module_stack_jump_links(directory)
    room_open_href = relative_url(directory, parent / "OPEN-HERE.html")
    room_entry_links: list[tuple[str, str]] = [
        ("Open Top", f"{room_open_href}#room-top"),
        ("Open Room", room_open_href),
        (get_room_entry_label(parent, "Open Brief", "Open Entry"), get_room_entry_href(directory, parent)),
    ]
    if shipment_stack_override and shipment_stack_override.get("room_entry_label") and shipment_stack_override.get("room_entry_href"):
        room_entry_links[-1] = (
            f"Open {str(shipment_stack_override['room_entry_label'])}",
            str(shipment_stack_override["room_entry_href"]),
        )
    child_dirs = [
        path
        for path in directory.iterdir()
        if path.is_dir() and path.name not in SKIP_DIR_NAMES
    ]
    has_module_outcomes = bool(build_module_outcome_paths_section(directory))
    has_folder_section = bool(
        [
            child
            for child in order_child_directories(directory, child_dirs)
            if build_folder_card_profile(directory, child)
        ]
    )
    docs_for_current = list(directory.glob("*.md"))
    priority_brief_docs = [
        doc for doc in docs_for_current
        if (build_doc_card_profile(directory, doc) or {}).get("kind") == "Executive Brief"
    ]
    docs_for_cards = [
        doc for doc in docs_for_current
        if (build_doc_card_profile(directory, doc) or {}).get("kind") != "Executive Brief"
    ] if priority_brief_docs else docs_for_current
    has_docs_section = bool(docs_for_cards)
    sequence_links = [("Open Sequence", "#module-sequence-context")]
    if sequence_jump_links:
        sequence_links.extend(list(sequence_jump_links["full_links"]))
    stack_links = list(stack_jump_links["full_links"]) if stack_jump_links else []
    stack_surface_links: list[tuple[str, str]] = []
    if bool(get_outcome_paths_profile(parent.relative_to(REPO_ROOT).as_posix())):
        stack_surface_links.extend(
            [
                ("Open Live Path", "#stack-live-path-modules"),
                ("Open Controls", "#stack-supporting-controls"),
            ]
        )
    room_sequence_label = "Room Sequence"
    room_sequence_summary = format_scope_summary(sequence_local, sequence_external)
    room_links: list[tuple[str, str]] = [
        ("Open Room Sequence", f"{room_open_href}#decision-sequence"),
    ]
    if sequence_local and sequence_external:
        room_links.extend(
            [
                ("Open Room Seq In", f"{room_open_href}#decision-sequence-in-room"),
                ("Open Room Seq Out", f"{room_open_href}#decision-sequence-external"),
            ]
        )
    if shipment_stack_override:
        room_sequence_label = str(shipment_stack_override["route_label"])
        room_sequence_summary = str(shipment_stack_override["route_summary"])
        room_links = list(shipment_stack_override["route_links_cta"])
    room_outcome_label = "Room Outcomes"
    room_outcome_summary = format_scope_summary(outcome_local, outcome_external)
    room_outcome_links: list[tuple[str, str]] = [
        ("Open Room Outcomes", f"{room_open_href}#outcome-paths"),
    ]
    if outcome_local and outcome_external:
        room_outcome_links.extend(
            [
                ("Open Room In", f"{room_open_href}#outcome-room-paths"),
                ("Open Room Out", f"{room_open_href}#outcome-external-controls"),
            ]
        )
    if shipment_stack_override:
        room_outcome_label = str(shipment_stack_override["outcome_label"])
        room_outcome_summary = str(shipment_stack_override["outcome_summary"])
        room_outcome_links = list(shipment_stack_override["outcome_links_cta"])
    outcome_links: list[tuple[str, str]] = []
    if has_module_outcomes:
        outcome_links.append(("Open Paths", "#module-outcome-paths"))
        if sequence_external or outcome_external:
            if outcome_local and outcome_external:
                outcome_links.extend(
                    [
                        ("Open In-Room", "#module-outcome-room-paths"),
                        ("Open External", "#module-outcome-external-controls"),
                    ]
                )
    oversight_links: list[tuple[str, str]] = []
    if extract_section_list_items(body_lines, "Escalation Triggers"):
        oversight_links.append(("Open Watch", "#module-escalation-watch"))
    if collect_decision_support_links(parent):
        oversight_links.append(("Open Support", "#module-decision-support"))
    if collect_related_rooms(parent):
        oversight_links.append(("Open Rooms", "#module-related-rooms"))
    active_deal_module = get_active_deal_module_context(directory)
    active_shipment_module = get_active_shipment_module_context(directory)
    active_account_module = get_active_account_module_context(directory)
    active_claim_module = get_active_claim_module_context(directory)
    supplier_approval_module = get_supplier_approval_module_context(directory)
    system_surface_links: list[tuple[str, str]] = []
    if active_deal_module:
        system_surface_links.extend(
            [
                ("Open Module Memo", str(active_deal_module["module_memo_href"])),
                (str(active_deal_module["room_entry_label"]), str(active_deal_module["room_entry_href"])),
                ("Open Active Deals", str(active_deal_module["active_deals_href"])),
                ("Open Deals", str(active_deal_module["deals_href"])),
            ]
        )
    elif active_shipment_module:
        system_surface_links.extend(
            [
                ("Open Module Memo", str(active_shipment_module["module_memo_href"])),
                (str(active_shipment_module["room_entry_label"]), str(active_shipment_module["room_entry_href"])),
                ("Open Active Shipments", str(active_shipment_module["active_shipments_href"])),
                ("Open Shipments", str(active_shipment_module["shipments_href"])),
            ]
        )
    elif active_account_module:
        system_surface_links.extend(
            [
                ("Open Module Memo", str(active_account_module["module_memo_href"])),
                (str(active_account_module["room_entry_label"]), str(active_account_module["room_entry_href"])),
                ("Open Customers", str(active_account_module["customers_href"])),
                ("Open CRM", str(active_account_module["crm_href"])),
            ]
        )
    elif active_claim_module:
        system_surface_links.extend(
            [
                ("Open Module Memo", str(active_claim_module["module_memo_href"])),
                (str(active_claim_module["room_entry_label"]), str(active_claim_module["room_entry_href"])),
                ("Open Inspection Cases", str(active_claim_module["inspection_cases_href"])),
                ("Open Compliance", str(active_claim_module["compliance_href"])),
            ]
        )
    elif supplier_approval_module:
        system_surface_links.extend(
            [
                ("Open Module Memo", str(supplier_approval_module["module_memo_href"])),
                (str(supplier_approval_module["room_entry_label"]), str(supplier_approval_module["room_entry_href"])),
                ("Open Supplier Approval", str(supplier_approval_module["supplier_approval_href"])),
                ("Open Compliance", str(supplier_approval_module["compliance_href"])),
                (str(supplier_approval_module["board_cta"]), str(supplier_approval_module["board_href"])),
            ]
        )
    elif shipment_stack_override:
        system_surface_links.extend(list(shipment_stack_override["return_links_cta"]))
    else:
        if has_folder_section:
            system_surface_links.append(("Open Modules", "#room-modules"))
        if has_docs_section:
            system_surface_links.append(("Open Readable Layers", "#supporting-files"))
            system_surface_links.append(("Open Source Integrity", "#visual-system"))
    module_sequence_summary = None
    if sequence_jump_links:
        module_sequence_summary = str(sequence_jump_links.get("position_pill") or "").strip() or None
    stack_summary = None
    if stack_jump_links:
        stack_count = len(stack_jump_links.get("nav_links", []))
        stack_summary = f"{stack_count} sequence stops" if stack_count else None
    stack_surface_summary = "Live / Controls" if stack_surface_links else None
    oversight_summary_parts: list[str] = []
    if extract_section_list_items(body_lines, "Escalation Triggers"):
        oversight_summary_parts.append("Watch")
    if collect_decision_support_links(parent):
        oversight_summary_parts.append("Support")
    if collect_related_rooms(parent):
        oversight_summary_parts.append("Rooms")
    oversight_summary = " / ".join(oversight_summary_parts) if oversight_summary_parts else None
    if shipment_stack_override:
        system_group_label = str(shipment_stack_override["return_label"])
        system_surface_summary = str(shipment_stack_override["return_summary"])
    elif active_deal_module or active_shipment_module or active_account_module or active_claim_module or supplier_approval_module:
        system_group_label = "Return Layer"
        system_surface_summary = (
            "Memo / Room / Lane / Board"
            if supplier_approval_module
            else "Memo / Room / Lane / Hub"
        )
    else:
        system_group_label = "System Surface" if has_folder_section else "Source Integrity"
        if has_folder_section and has_docs_section:
            system_surface_summary = "Modules / Readable / Source"
        elif has_folder_section:
            system_surface_summary = "Modules / Source"
        elif has_docs_section:
            system_surface_summary = "Readable / Source"
        else:
            system_surface_summary = "Source Integrity"
    route_links_html = build_route_posture_link_groups(
        [
            ("Room Entry", room_entry_links, "module-surface", "Room Access"),
            ("Module Sequence", sequence_links, "sequence", module_sequence_summary),
            ("Stack Route", stack_links, "stack", stack_summary),
            ("Stack Surface", stack_surface_links, "path-surface", stack_surface_summary),
            (room_sequence_label, room_links, "room", room_sequence_summary),
            (room_outcome_label, room_outcome_links, "outcomes", room_outcome_summary),
            ("Module Outcomes", outcome_links, "outcomes", format_scope_summary(outcome_local, outcome_external)),
            ("Oversight Layer", oversight_links, "support", oversight_summary),
            (system_group_label, system_surface_links, "surface", system_surface_summary),
        ]
    )
    sequence_scope_pill = (
        f"Routes: {str(shipment_stack_override['route_summary'])}"
        if shipment_stack_override
        else format_route_scope_pill("Sequence", sequence_local, sequence_external)
    )
    outcome_scope_pill = (
        f"Outcomes: {str(shipment_stack_override['outcome_summary'])}"
        if shipment_stack_override
        else format_route_scope_pill("Outcomes", outcome_local, outcome_external)
    )
    snapshot_eyebrow = str(shipment_stack_override["snapshot_eyebrow"]) if shipment_stack_override else "Room Brief Snapshot"
    snapshot_pill = str(shipment_stack_override["snapshot_pill"]) if shipment_stack_override else "Read First"
    brief_pill = str(shipment_stack_override["brief_pill"]) if shipment_stack_override else "Room Brief"

    current_reading_rows = extract_section_table_rows(body_lines, "Current Reading")
    signal_rows = current_reading_rows[:3] if current_reading_rows else [
        ("Primary Lens", meta_map.get("Primary Lens", "")),
        ("Decision Now", meta_map.get("Decision Now", "")),
        ("Escalation Rhythm", meta_map.get("Escalation Rhythm", "")),
    ]
    signal_cards = "".join(
        "<article class=\"priority-brief-signal\">"
        f"<p class=\"priority-brief-label\">{html.escape(label)}</p>"
        f"<p class=\"priority-brief-value\">{render_inline(value, directory)}</p>"
        "</article>"
        for label, value in signal_rows
        if value
    )

    immediate_actions = extract_section_list_items(body_lines, "Immediate Founder Actions")
    action_cards = "".join(
        "<article class=\"brief-action-card\">"
        f"<span class=\"brief-action-index\">{index:02d}</span>"
        f"<p class=\"brief-action-copy\">{render_inline(item, directory)}</p>"
        "</article>"
        for index, item in enumerate(immediate_actions[:3], start=1)
    )
    action_grid_html = f'<div class="brief-action-grid">{action_cards}</div>' if action_cards else ""

    return f"""
        <section class="home-section priority-brief-panel" id="module-brief-snapshot">
          <div class="section-heading">
            <p class="eyebrow">{html.escape(snapshot_eyebrow)}</p>
            <h2 class="section-title">Carry the room brief into {html.escape(module_title)}.</h2>
            <p class="section-copy">
              This snapshot keeps the founder anchored on {html.escape(room_title)}'s narrative, live signals, and immediate actions while reading a single module in depth.
            </p>
          </div>
          <div class="priority-brief-grid">
            <article class="priority-brief-card">
              <div class="card-meta">
                <span class="meta-pill">{html.escape(snapshot_pill)}</span>
                <span class="meta-pill">{html.escape(brief_pill)}</span>
              </div>
              <h3 class="viewer-card-title">{html.escape(title)}</h3>
              <p class="viewer-card-copy">{html.escape(summary)}</p>
              <div class="card-meta priority-brief-route-meta">
                <span class="{html.escape(str(route_posture['pill_class']), quote=True)}">{html.escape(str(route_posture['label']))}</span>
                <span class="meta-pill">{html.escape(sequence_scope_pill)}</span>
                <span class="meta-pill">{html.escape(outcome_scope_pill)}</span>
              </div>
              <p class="{html.escape(str(route_posture['note_class']), quote=True)}">{html.escape(str(route_posture['note']))}</p>
              {route_links_html}
              <p class="doc-path">{html.escape(get_doc_card_source_label("Executive Brief", brief_path.name))}</p>
              <div class="viewer-card-links">
                <a class="button-primary" href="{brief_href}">{html.escape(str(brief_profile.get("cta") or "Open Room Brief"))}</a>
                <a class="button-secondary" href="{brief_href}#executive-focus">Open Focus</a>
                <a class="button-secondary" href="{brief_href}#immediate-founder-actions">Open Actions</a>
                <a class="button-secondary" href="{source_href}">Open Brief Source</a>
              </div>
            </article>
            <div class="priority-brief-signals">
              {signal_cards}
            </div>
          </div>
          {action_grid_html}
        </section>
"""


def build_decision_sequence_group_panel(
    eyebrow: str,
    title: str,
    copy: str,
    cards: list[str],
    *,
    anchor_id: str | None = None,
    summary_pills: list[tuple[str, str | None]] | None = None,
    local: bool,
) -> str:
    if not cards:
        return ""
    modifier = " viewer-subsection--current-path" if local else " viewer-subsection--supporting"
    anchor_attr = f' id="{html.escape(anchor_id, quote=True)}"' if anchor_id else ""
    summary_html = ""
    if summary_pills:
        summary_html = (
            '<div class="card-meta">'
            + "".join(
                (
                    f'<a class="meta-pill meta-pill--link" href="{html.escape(target, quote=True)}">{html.escape(pill)}</a>'
                    if target
                    else f'<span class="meta-pill">{html.escape(pill)}</span>'
                )
                for pill, target in summary_pills
            )
            + "</div>"
        )
    return f"""
          <div class="viewer-subsection{modifier}"{anchor_attr}>
            <div class="section-heading">
              <p class="eyebrow">{html.escape(eyebrow)}</p>
              <h3 class="section-title-sm">{html.escape(title)}</h3>
              <p class="section-copy">{html.escape(copy)}</p>
              {summary_html}
            </div>
            <div class="decision-sequence-grid">
              {"".join(cards)}
            </div>
          </div>
"""


def get_decision_sequence_profile(relative: str) -> dict[str, object] | None:
    sequences: dict[str, dict[str, object]] = {
        "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution": {
            "title": "Use this account room in order.",
            "copy": "Move from founder narrative to trust posture, then pressure-test exposure and only then decide whether Atlantic Foods should carry more strategic weight.",
            "steps": [
                (
                    "01",
                    "Read the account brief",
                    "Start with the controlled founder memo so release, trust, and growth weight begin from one account answer.",
                    "Open Account Brief",
                    "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/README.html",
                ),
                (
                    "02",
                    "Confirm trust and release posture",
                    "Use the trust review and release-control answer before assuming the relationship supports wider commercial movement.",
                    "Open Trust Review",
                    "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CTRUST-2026-Q2_AtlanticFoods-Relationship-Trust-Review/OPEN-HERE.html",
                ),
                (
                    "03",
                    "Pressure-test cash and collections",
                    "Check whether receivable behavior and exposure timing still support the same release answer under real cash pressure.",
                    "Open Cash Module",
                    "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CASH-2026-005_AtlanticFoods-Cash-Outlook/OPEN-HERE.html",
                ),
                (
                    "04",
                    "Decide growth weight",
                    "Only after trust and cash logic hold together should the founder widen strategic weight, concentration tolerance, or quarter commitment.",
                    "Open Monthly Review",
                    "06_dashboard/15_monthly-strategic-review/Monthly-Strategic-Business-Review.html",
                ),
            ],
        },
        "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic": {
            "title": "Use this deal room in order.",
            "copy": "Keep the garlic deal disciplined by confirming control first, then testing commitment logic, and only then shaping what can be communicated outwardly.",
            "steps": [
                (
                    "01",
                    "Read the deal brief",
                    "Start with the live-deal memo so the founder reads control, commitment, and outbound posture as one answer.",
                    "Open Deal Brief",
                    "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/README.html",
                ),
                (
                    "02",
                    "Confirm matter control",
                    "Use matter control and executable-check logic before treating the deal as commercially ready.",
                    "Open Matter Control",
                    "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control/OPEN-HERE.html",
                ),
                (
                    "03",
                    "Test commitment logic",
                    "Pressure-test price, allocation, and recovery assumptions before widening commercial promise or founder urgency.",
                    "Open Release Priority",
                    "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/ALLOC-2026-Q2_AtlanticFoods-Release-Priority/OPEN-HERE.html",
                ),
                (
                    "04",
                    "Release the outbound layer",
                    "Only after control and commitment hold should the founder move into offer packet, communication control, and response discipline.",
                    "Open Formal Offer Packet",
                    "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/OPEN-HERE.html",
                ),
            ],
        },
        "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA": {
            "title": "Use this shipment room in order.",
            "copy": "Keep movement disciplined by reading the shipment narrative first, then confirming release, then packet and payment proof, and only then deciding whether contained movement can widen.",
            "steps": [
                (
                    "01",
                    "Read the shipment brief",
                    "Start with the founder memo so release, payment, packet, and containment posture stay synchronized from the first click.",
                    "Open Shipment Brief",
                    "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/README.html",
                ),
                (
                    "02",
                    "Confirm the live release gate",
                    "Use the live release answer before assuming the shipment is ready just because paperwork looks complete.",
                    "Open Release Gate",
                    "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/OPEN-HERE.html",
                ),
                (
                    "03",
                    "Verify packet and payment proof",
                    "Check export packet completeness and funding posture so movement is supported by both document proof and cash discipline.",
                    "Open Funding Module",
                    "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/OPEN-HERE.html",
                ),
                (
                    "04",
                    "Escalate contained movement if needed",
                    "If any live gate is still constrained, move into the containment stack before authorizing wider shipment movement.",
                    "Open Executable Checks",
                    "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html",
                ),
            ],
        },
        "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim": {
            "title": "Use this claim room in order.",
            "copy": "Treat the claim as a controlled executive case by reading the narrative first, confirming containment, then quantifying consequence, and only then closing the proof trail.",
            "steps": [
                (
                    "01",
                    "Read the claim brief",
                    "Start with the founder memo so containment, recovery, and proof are read as one complaint answer.",
                    "Open Claim Brief",
                    "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/README.html",
                ),
                (
                    "02",
                    "Confirm CAPA containment",
                    "Use the corrective-action layer before treating the claim as stabilized or externally manageable.",
                    "Open CAPA Module",
                    "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/CAPA-2026-001_AtlanticFoods-Garlic-Containment-and-Prevention/OPEN-HERE.html",
                ),
                (
                    "03",
                    "Quantify recovery consequence",
                    "Translate the complaint into credit, recovery, and executive consequence before closing posture or customer confidence assumptions.",
                    "Open Recovery Module",
                    "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/RECOV-2026-001_AtlanticFoods-Claim-Recovery/OPEN-HERE.html",
                ),
                (
                    "04",
                    "Lock the proof trail",
                    "Close with the archive-ready proof chain so the case can withstand later dispute, audit, or founder review.",
                    "Open Claims Recovery",
                    "06_dashboard/30_claims-recovery/Claims-Credits-and-Recovery-Review.html",
                ),
            ],
        },
        "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce": {
            "title": "Use this supplier room in order.",
            "copy": "Read the supplier narrative first, confirm quarterly performance, then test backup sourcing resilience, and only then widen the answer into founder-level supplier governance.",
            "steps": [
                (
                    "01",
                    "Read the supplier brief",
                    "Start with the founder memo so approval posture, scorecard discipline, and resilience logic are read as one governed supplier answer.",
                    "Open Supplier Brief",
                    "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce/README.html",
                ),
                (
                    "02",
                    "Confirm quarterly performance posture",
                    "Use the supplier-performance module before assuming Golden Harvest still deserves approved-with-controls status.",
                    "Open Performance Module",
                    "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce/PERF-2026-Q2_GoldenHarvest-Supplier-Performance/OPEN-HERE.html",
                ),
                (
                    "03",
                    "Test backup sourcing resilience",
                    "Pressure-test contingency depth and capacity confidence before treating supplier dependence as founder-safe.",
                    "Open Resilience Module",
                    "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce/CAPACITY-2026-Q2_GoldenHarvest-Backup-Sourcing-Review/OPEN-HERE.html",
                ),
                (
                    "04",
                    "Widen the governance answer",
                    "Only after performance and resilience hold together should the founder widen into the executive board that compares supplier posture beyond one room.",
                    "Open Supplier Performance Board",
                    "06_dashboard/07_supplier-performance/Supplier-Performance-Review-Board.html",
                ),
            ],
        },
        LEAD_ROOM_RELATIVE: {
            "title": "Use this lead room in order.",
            "copy": "Read the qualification narrative first, reconfirm the live prospect posture, then pressure-test pipeline priority before assigning explicit founder follow-through.",
            "steps": [
                (
                    "01",
                    "Read the lead brief",
                    "Start with the lead brief so qualification posture, next move, and founder caution all begin from one governed prospect answer.",
                    "Open Lead Brief",
                    f"{LEAD_ROOM_RELATIVE}/README.html",
                ),
                (
                    "02",
                    "Reconfirm the live prospect posture",
                    "Stay inside the room long enough to test whether the room surface still reflects the real qualification state before widening into a board.",
                    "Open Lead Room",
                    f"{LEAD_ROOM_RELATIVE}/OPEN-HERE.html",
                ),
                (
                    "03",
                    "Pressure-test pipeline priority",
                    "Use the sales pipeline board before treating the lead as founder-ready, because stage confidence and sequencing still need comparative review.",
                    "Open Sales Pipeline",
                    SALES_PIPELINE_BOARD_RELATIVE,
                ),
                (
                    "04",
                    "Assign explicit follow-through",
                    "Only after priority is clear should the founder push the next commercial move into an owned queue with accountable follow-through.",
                    "Open Founder Queue",
                    f"{TASK_ROOM_RELATIVE}/OPEN-HERE.html",
                ),
            ],
        },
        SUPPLIER_ROOM_RELATIVE: {
            "title": "Use this supplier room in order.",
            "copy": "Read the sourcing narrative first, reconfirm the live supplier posture, then hand off into approval discipline and only then widen into performance review.",
            "steps": [
                (
                    "01",
                    "Read the supplier brief",
                    "Start with the supplier brief so continuity risk, approval posture, and dependency confidence begin from one governed sourcing answer.",
                    "Open Supplier Brief",
                    f"{SUPPLIER_ROOM_RELATIVE}/README.html",
                ),
                (
                    "02",
                    "Reconfirm the live supplier posture",
                    "Stay inside the room long enough to confirm whether the sourcing answer still holds before widening into compliance or board-level review.",
                    "Open Supplier Room",
                    f"{SUPPLIER_ROOM_RELATIVE}/OPEN-HERE.html",
                ),
                (
                    "03",
                    "Hand off into supplier approval",
                    "Use the supplier-approval hub before treating this source as founder-safe, because compliance readiness and continuity proof still matter.",
                    "Open Supplier Approval",
                    f"{SUPPLIER_APPROVAL_RELATIVE}/OPEN-HERE.html",
                ),
                (
                    "04",
                    "Widen into performance control",
                    "Only after approval posture is clean should the founder widen into the board that compares supplier performance beyond one room.",
                    "Open Supplier Performance Board",
                    SUPPLIER_PERFORMANCE_BOARD_RELATIVE,
                ),
            ],
        },
        TASK_ROOM_RELATIVE: {
            "title": "Use this execution queue in order.",
            "copy": "Read the execution narrative first, reconfirm the live queue posture, then close the executable gate and only then widen into owner-accountability review.",
            "steps": [
                (
                    "01",
                    "Read the execution brief",
                    "Start with the execution brief so the live gate, proof requirement, and founder override context begin from one governed action answer.",
                    "Open Execution Brief",
                    f"{TASK_ROOM_RELATIVE}/README.html",
                ),
                (
                    "02",
                    "Reconfirm the live queue posture",
                    "Stay inside the queue long enough to confirm whether the task surface still reflects the true blocker, owner, and closure basis.",
                    "Open Founder Queue",
                    f"{TASK_ROOM_RELATIVE}/OPEN-HERE.html",
                ),
                (
                    "03",
                    "Close the executable gate",
                    "Use the executable-check control board before calling the task safe, because gate closure still depends on explicit proof and cutoff discipline.",
                    "Open Executable Checks",
                    EXECUTABLE_CHECKS_BOARD_RELATIVE,
                ),
                (
                    "04",
                    "Confirm owner follow-through",
                    "Only after gate logic is clean should the founder widen into the board that tests whether follow-through is actually holding.",
                    "Open Owner Accountability",
                    OWNER_ACCOUNTABILITY_BOARD_RELATIVE,
                ),
            ],
        },
        TRACEABILITY_ROOM_RELATIVE: {
            "title": "Use this traceability room in order.",
            "copy": "Read the traceability narrative first, reconfirm the live lot-path proof, then pressure-test compliance control before widening into recovery and challenge response.",
            "steps": [
                (
                    "01",
                    "Read the traceability brief",
                    "Start with the traceability brief so lot lineage, retrieval discipline, and audit-readiness posture begin from one governed founder answer.",
                    "Open Traceability Brief",
                    f"{TRACEABILITY_ROOM_RELATIVE}/README.html",
                ),
                (
                    "02",
                    "Reconfirm the live proof chain",
                    "Stay inside the room long enough to verify whether the current lot-path answer still holds before widening into a broader control surface.",
                    "Open Traceability Room",
                    f"{TRACEABILITY_ROOM_RELATIVE}/OPEN-HERE.html",
                ),
                (
                    "03",
                    "Pressure-test compliance control",
                    "Use the daily compliance board before treating the proof chain as founder-safe, because exception handling and regulator-readiness still matter.",
                    "Open Compliance Control",
                    COMPLIANCE_CONTROL_CENTER_RELATIVE,
                ),
                (
                    "04",
                    "Widen into recovery posture",
                    "Only after proof and control hold together should the founder widen into the board that converts traceability evidence into complaint or recovery consequence.",
                    "Open Claims Recovery",
                    CLAIMS_RECOVERY_BOARD_RELATIVE,
                ),
            ],
        },
    }
    return sequences.get(relative)


def build_decision_sequence_section(directory: Path) -> str:
    relative = directory.relative_to(REPO_ROOT).as_posix()
    profile = get_decision_sequence_profile(relative)
    if not profile:
        return ""

    all_steps: list[str] = []
    local_steps: list[str] = []
    external_steps: list[str] = []
    local_count = 0
    external_count = 0
    step_pills: list[tuple[str, str]] = []
    local_step_pills: list[tuple[str, str]] = []
    external_step_pills: list[tuple[str, str]] = []
    for order, title, copy, cta, target in profile["steps"]:
        step_context = get_sequence_step_target_context(directory, directory, str(target))
        if step_context["scope"] == "local":
            local_count += 1
        else:
            external_count += 1
        step_anchor = f"#decision-step-{str(order)}"
        pill_item = (get_sequence_step_pill_label(str(order), str(title)), step_anchor)
        step_pills.append(pill_item)
        card_html = f"""
          <article class="decision-sequence-card decision-sequence-card--{html.escape(str(step_context["scope"]), quote=True)}" id="decision-step-{html.escape(str(order), quote=True)}">
            <div class="card-meta decision-sequence-meta">
              <p class="decision-sequence-order">{html.escape(str(order))}</p>
              {build_meta_pills(list(step_context["meta_items"]))}
            </div>
            <h3 class="decision-sequence-title">{html.escape(str(title))}</h3>
            <p class="decision-sequence-copy">{html.escape(str(copy))}</p>
            <p class="decision-sequence-route-note decision-sequence-route-note--{html.escape(str(step_context["scope"]), quote=True)}">{html.escape(str(step_context["route_note"]))}</p>
            <a class="decision-sequence-cta" href="{html.escape(str(step_context["href"]), quote=True)}">{html.escape(str(cta))}</a>
          </article>
"""
        all_steps.append(card_html)
        if step_context["scope"] == "local":
            local_steps.append(card_html)
            local_step_pills.append(pill_item)
        else:
            external_steps.append(card_html)
            external_step_pills.append(pill_item)

    summary_html = (
        '<div class="card-meta">'
        f'<span class="meta-pill">{html.escape(format_count_label(len(profile["steps"]), "Sequence Step"))}</span>'
        + (
            f'<span class="meta-pill">{html.escape(format_count_label(local_count, "In-Room Step", "In-Room Steps"))}</span>'
            if local_count
            else ""
        )
        + (
            f'<span class="meta-pill">{html.escape(format_count_label(external_count, "External Control"))}</span>'
            if external_count
            else ""
        )
        + "".join(
            f'<a class="meta-pill meta-pill--link" href="{html.escape(target, quote=True)}">{html.escape(label)}</a>'
            for label, target in step_pills
        )
        + "</div>"
    )
    grouped_steps_html = (
        build_decision_sequence_group_panel(
            "In-Room Steps",
            "Stay inside the room while the sequence still belongs to the local stack.",
            "Use these steps when the founder should continue through the brief and live modules without leaving the room for a wider board yet.",
            local_steps,
            anchor_id="decision-sequence-in-room",
            summary_pills=[(format_count_label(local_count, "In-Room Step", "In-Room Steps"), None), *local_step_pills],
            local=True,
        )
        + build_decision_sequence_group_panel(
            "External Controls",
            "Leave the room only when the sequence escalates beyond the local stack.",
            "Use these steps when the founder should move from the room into a broader board or executive control layer to finish the sequence.",
            external_steps,
            anchor_id="decision-sequence-external",
            summary_pills=[(format_count_label(external_count, "External Control"), None), *external_step_pills],
            local=False,
        )
    ) if local_steps and external_steps else f"""
          <div class="decision-sequence-grid">
            {"".join(all_steps)}
          </div>
"""

    return f"""
        <section class="home-section decision-sequence-panel" id="decision-sequence">
          <div class="section-heading">
            <p class="eyebrow">Decision Sequence</p>
            <h2 class="section-title">{html.escape(str(profile["title"]))}</h2>
            <p class="section-copy">
              {html.escape(str(profile["copy"]))}
            </p>
            {summary_html}
          </div>
          {grouped_steps_html}
        </section>
"""


def get_outcome_paths_profile(relative: str) -> dict[str, object] | None:
    profiles: dict[str, dict[str, object]] = {
        "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution": {
            "title": "Choose the next account path after the read.",
            "copy": "Once the founder finishes the account narrative, use one of these three routes so the next move is explicit instead of implied.",
            "paths": [
                (
                    "Widen",
                    "Widen strategic weight",
                    "Use this path when trust, release, and cash behavior hold together strongly enough to justify more account weight.",
                    "Open Monthly Review",
                    "06_dashboard/15_monthly-strategic-review/Monthly-Strategic-Business-Review.html",
                ),
                (
                    "Hold",
                    "Hold exposure discipline",
                    "Use this path when Atlantic Foods should remain active but current release confidence or credit posture should not widen yet.",
                    "Open Credit Control",
                    "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/OPEN-HERE.html",
                ),
                (
                    "Escalate",
                    "Escalate relationship risk",
                    "Use this path when trust quality, response posture, or collections behavior weaken enough to change the account answer.",
                    "Open Trust Review",
                    "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CTRUST-2026-Q2_AtlanticFoods-Relationship-Trust-Review/OPEN-HERE.html",
                ),
            ],
        },
        "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic": {
            "title": "Choose the next deal path after the read.",
            "copy": "Use these outcome routes to keep the live deal moving with discipline after the founder decides whether commitment should widen, hold, or escalate.",
            "paths": [
                (
                    "Advance",
                    "Advance outward commitment",
                    "Use this path when control is clean enough to move from internal posture into a tighter external commitment or send-ready packet.",
                    "Open Formal Offer Packet",
                    "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/OPEN-HERE.html",
                ),
                (
                    "Hold",
                    "Hold under matter control",
                    "Use this path when the deal remains viable but still needs founder discipline, executable closure, or exception control before widening.",
                    "Open Matter Control",
                    "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control/OPEN-HERE.html",
                ),
                (
                    "Escalate",
                    "Escalate downside response",
                    "Use this path when commercial drift, assumptions, or recovery pressure make the deal answer unstable enough to require formal downside handling.",
                    "Open Scenario Response",
                    "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/SCEN-2026-Q2_AtlanticFoods-Cash-Stress-Response/OPEN-HERE.html",
                ),
            ],
        },
        "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA": {
            "title": "Choose the next shipment path after the read.",
            "copy": "Use one of these routes to make the movement answer explicit once the founder knows whether the shipment should move, hold, or escalate.",
            "paths": [
                (
                    "Move",
                    "Authorize controlled movement",
                    "Use this path when release, packet proof, and payment posture are aligned strongly enough for controlled shipment movement.",
                    "Open Release Gate",
                    "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/OPEN-HERE.html",
                ),
                (
                    "Hold",
                    "Keep the shipment contained",
                    "Use this path when movement should remain possible in principle but live gates still require executable-check discipline or contained posture.",
                    "Open Executable Checks",
                    "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html",
                ),
                (
                    "Escalate",
                    "Escalate funding or packet risk",
                    "Use this path when the shipment is blocked by payment exposure, packet incompleteness, or the risk of moving faster than proof allows.",
                    "Open Funding Review",
                    "06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.html",
                ),
            ],
        },
        "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim": {
            "title": "Choose the next claim path after the read.",
            "copy": "Use these routes so the founder can move from the complaint narrative into the right next action without blending containment, recovery, and escalation logic.",
            "paths": [
                (
                    "Contain",
                    "Continue containment discipline",
                    "Use this path when the case is still operationally live and corrective action remains the priority over closure language.",
                    "Open CAPA Module",
                    "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/CAPA-2026-001_AtlanticFoods-Garlic-Containment-and-Prevention/OPEN-HERE.html",
                ),
                (
                    "Recover",
                    "Translate into recovery consequence",
                    "Use this path when the operational answer is stable enough that the founder can quantify credit, cash, and commercial consequence.",
                    "Open Recovery Module",
                    "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/RECOV-2026-001_AtlanticFoods-Claim-Recovery/OPEN-HERE.html",
                ),
                (
                    "Escalate",
                    "Escalate executive exposure",
                    "Use this path when the complaint answer now affects customer confidence, executive risk, or founder-level recovery posture.",
                    "Open Risk Register",
                    "06_dashboard/18_executive-risk-register/Executive-Risk-Register.html",
                ),
            ],
        },
        "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce": {
            "title": "Choose the next supplier path after the read.",
            "copy": "Use these routes to make the supplier answer explicit once the founder knows whether Golden Harvest should stay approved, fortify resilience, or widen into a broader governance review.",
            "paths": [
                (
                    "Maintain",
                    "Maintain approved-with-controls posture",
                    "Use this path when supplier confidence remains intact enough that the founder should stay anchored in the quarterly performance track.",
                    "Open Performance Module",
                    "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce/PERF-2026-Q2_GoldenHarvest-Supplier-Performance/OPEN-HERE.html",
                ),
                (
                    "Fortify",
                    "Fortify backup sourcing coverage",
                    "Use this path when approval can continue only if contingency depth, fallback timing, and capacity resilience are strengthened immediately.",
                    "Open Resilience Module",
                    "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce/CAPACITY-2026-Q2_GoldenHarvest-Backup-Sourcing-Review/OPEN-HERE.html",
                ),
                (
                    "Escalate",
                    "Escalate supplier dependence risk",
                    "Use this path when the room answer now depends on a wider resilience view across concentration pressure, backup coverage, and founder-level supply risk.",
                    "Open Supply Resilience Board",
                    "06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.html",
                ),
            ],
        },
        LEAD_ROOM_RELATIVE: {
            "title": "Choose the next lead path after the read.",
            "copy": "Use these routes so the founder can advance, hold, or escalate the prospect without letting the next move stay implied.",
            "paths": [
                (
                    "Advance",
                    "Advance into live deal posture",
                    "Use this path when qualification is clean enough that the next answer belongs in the active-deals lane rather than the lead stack.",
                    "Open Active Deals",
                    f"{ACTIVE_DEALS_RELATIVE}/OPEN-HERE.html",
                ),
                (
                    "Hold",
                    "Hold under explicit follow-through",
                    "Use this path when the prospect is still viable but the next move needs owned follow-through before any wider commercial promise is made.",
                    "Open Founder Queue",
                    f"{TASK_ROOM_RELATIVE}/OPEN-HERE.html",
                ),
                (
                    "Escalate",
                    "Escalate response discipline",
                    "Use this path when silence, drift, or weak counterparty behavior changes the prospect answer enough to require formal response escalation.",
                    "Open Response Escalation",
                    RESPONSE_ESCALATION_BOARD_RELATIVE,
                ),
            ],
        },
        SUPPLIER_ROOM_RELATIVE: {
            "title": "Choose the next supplier path after the read.",
            "copy": "Use these routes to make the supplier answer explicit once the founder knows whether this source should advance, fortify, or escalate.",
            "paths": [
                (
                    "Advance",
                    "Advance into approval control",
                    "Use this path when the supplier answer is strong enough that the next move belongs in the governed approval lane.",
                    "Open Supplier Approval",
                    f"{SUPPLIER_APPROVAL_RELATIVE}/OPEN-HERE.html",
                ),
                (
                    "Fortify",
                    "Fortify resilience coverage",
                    "Use this path when sourcing can continue only if contingency depth and fallback readiness are strengthened immediately.",
                    "Open Supply Resilience Board",
                    SUPPLY_RESILIENCE_BOARD_RELATIVE,
                ),
                (
                    "Escalate",
                    "Escalate supplier dependence risk",
                    "Use this path when the source answer now depends on a wider founder-level risk read across supplier concentration and continuity.",
                    "Open Executive Risk Register",
                    "06_dashboard/18_executive-risk-register/Executive-Risk-Register.html",
                ),
            ],
        },
        TASK_ROOM_RELATIVE: {
            "title": "Choose the next execution path after the read.",
            "copy": "Use these routes to make the queue answer explicit once the founder knows whether the gate should close, hold, or escalate.",
            "paths": [
                (
                    "Close",
                    "Close the live executable gate",
                    "Use this path when the task has enough proof to move into explicit executable-check closure instead of staying in narrative review.",
                    "Open Executable Checks",
                    EXECUTABLE_CHECKS_BOARD_RELATIVE,
                ),
                (
                    "Hold",
                    "Hold under owner follow-through",
                    "Use this path when the task remains active but the right next answer is stronger owner discipline rather than immediate closure.",
                    "Open Owner Accountability",
                    OWNER_ACCOUNTABILITY_BOARD_RELATIVE,
                ),
                (
                    "Escalate",
                    "Escalate founder decision pressure",
                    "Use this path when the queue item now needs a directional founder call rather than more passive monitoring.",
                    "Open Founder Decisions",
                    "06_dashboard/13_founder-decisions/Executive-Decision-Board.html",
                ),
            ],
        },
        TRACEABILITY_ROOM_RELATIVE: {
            "title": "Choose the next traceability path after the read.",
            "copy": "Use these routes to make the proof answer explicit once the founder knows whether the lot path should defend, hold, or escalate.",
            "paths": [
                (
                    "Defend",
                    "Defend with governed proof",
                    "Use this path when the lot-path answer is strong enough to support live challenge defense through the daily compliance control surface.",
                    "Open Compliance Control",
                    COMPLIANCE_CONTROL_CENTER_RELATIVE,
                ),
                (
                    "Hold",
                    "Hold inside the traceability lane",
                    "Use this path when the proof chain remains viable but should stay inside the traceability lane until the remaining evidence gap is fully closed.",
                    "Open Traceability",
                    f"{TRACEABILITY_RELATIVE}/OPEN-HERE.html",
                ),
                (
                    "Escalate",
                    "Escalate recovery consequence",
                    "Use this path when the proof answer now depends on complaint handling, credit recovery, or wider executive exposure rather than only traceability control.",
                    "Open Claims Recovery",
                    CLAIMS_RECOVERY_BOARD_RELATIVE,
                ),
            ],
        },
    }
    return profiles.get(relative)


def get_outcome_path_order_map(relative: str) -> dict[str, int]:
    profile = get_outcome_paths_profile(relative)
    if not profile:
        return {}
    return {
        str(pill): index
        for index, (pill, _title, _copy, _cta, _target) in enumerate(profile["paths"])
    }


def get_outcome_path_sequence(relative: str, pill: str) -> tuple[int, int] | None:
    profile = get_outcome_paths_profile(relative)
    if not profile:
        return None
    order_map = get_outcome_path_order_map(relative)
    if pill not in order_map:
        return None
    return (order_map[pill] + 1, len(profile["paths"]))


def get_module_room_path_context(parent: Path, child: Path) -> dict[str, str] | None:
    if parent == REPO_ROOT:
        return None
    try:
        relative_parent = parent.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return None

    profile = get_outcome_paths_profile(relative_parent)
    if not profile:
        return None

    current_path = child / "OPEN-HERE.html"
    for pill, title, copy, cta, target in profile["paths"]:
        target_path = REPO_ROOT / str(target)
        if target_path == current_path:
            return {
                "pill": str(pill),
                "title": str(title),
                "copy": str(copy),
                "cta": str(cta),
            }
    return None


def get_outcome_path_target_label(target_path: Path) -> str:
    try:
        relative = target_path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return "Linked Route"

    if relative.startswith("06_dashboard/"):
        return "Decision Board"
    if target_path.name == "OPEN-HERE.html":
        return "Linked Module"
    return "Linked Record"


def get_sequence_step_target_context(
    room_directory: Path,
    current_directory: Path,
    target: str,
) -> dict[str, object]:
    target_path = REPO_ROOT / str(target)
    href = relative_url(current_directory, target_path)
    try:
        room_relative = target_path.relative_to(room_directory)
    except ValueError:
        room_relative = None

    if room_relative is not None:
        if room_relative.parts == ("README.html",):
            return {
                "scope": "local",
                "href": href,
                "meta_items": [
                    ("In Room", "meta-pill meta-pill--outcome-local"),
                    ("Executive Brief", "meta-pill"),
                ],
                "route_note": "Stay inside this case room and begin from the founder brief before widening movement.",
            }
        if target_path.name == "OPEN-HERE.html" and len(room_relative.parts) >= 2:
            return {
                "scope": "local",
                "href": href,
                "meta_items": [
                    ("In Room", "meta-pill meta-pill--outcome-local"),
                    ("Live Module", "meta-pill"),
                ],
                "route_note": "Stay inside this case room and move directly into the linked live module.",
            }
        return {
            "scope": "local",
            "href": href,
            "meta_items": [
                ("In Room", "meta-pill meta-pill--outcome-local"),
                ("Linked Record", "meta-pill"),
            ],
            "route_note": "Stay inside this case room and keep the sequence moving through the local record stack.",
        }

    return {
        "scope": "external",
        "href": href,
        "meta_items": [
            ("External Control", "meta-pill meta-pill--outcome-external"),
            (get_outcome_path_target_label(target_path), "meta-pill"),
        ],
        "route_note": "Step out of this case room when the sequence now belongs on a wider board or executive control layer.",
    }


def get_sequence_step_pill_label(order: str, title: str) -> str:
    tokens = re.findall(r"[A-Za-z0-9]+", title)
    keyword = tokens[0] if tokens else "Step"
    return f"{order} {keyword}"


def get_decision_sequence_scope_counts(directory: Path) -> tuple[int, int]:
    try:
        relative = directory.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return (0, 0)
    profile = get_decision_sequence_profile(relative)
    if not profile:
        return (0, 0)
    local_count = 0
    external_count = 0
    for order, title, copy, cta, target in profile["steps"]:
        step_context = get_sequence_step_target_context(directory, directory, str(target))
        if step_context["scope"] == "local":
            local_count += 1
        else:
            external_count += 1
    return (local_count, external_count)


def format_route_scope_pill(label: str, local_count: int, external_count: int) -> str:
    parts: list[str] = []
    if local_count:
        parts.append(f"{local_count} in-room")
    if external_count:
        parts.append(f"{external_count} external")
    if not parts:
        parts.append("no route data")
    return f"{label}: {' / '.join(parts)}"


def get_scope_summary_override(directory: Path, category: str) -> str | None:
    if is_fda_readiness_room(directory):
        if category == "sequence":
            return "Readiness / Response"
        if category == "outcomes":
            return "Lane / Hub / Board"
    return None


def get_route_scope_pill_override(directory: Path, label: str) -> str | None:
    normalized = label.lower()
    summary = get_scope_summary_override(
        directory,
        "sequence" if normalized == "sequence" else "outcomes" if normalized == "outcomes" else normalized,
    )
    if not summary:
        return None
    return f"{label}: {summary.lower()}"


def get_shipment_stack_navigation_override(directory: Path) -> dict[str, object] | None:
    try:
        relative = directory.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return None

    shipment_room_open = relative_url(directory, REPO_ROOT / ACTIVE_SHIPMENT_ROOM_RELATIVE / "OPEN-HERE.html")
    release_gate_open = relative_url(
        directory,
        REPO_ROOT / ACTIVE_SHIPMENT_ROOM_RELATIVE / "REL-2026-001_Pre-Shipment-Release/OPEN-HERE.html",
    )
    packet_proof_open = relative_url(
        directory,
        REPO_ROOT / ACTIVE_SHIPMENT_ROOM_RELATIVE / "DOCCTRL-2026-001_Garlic-Export-Packet/OPEN-HERE.html",
    )
    shipment_control_tower_open = relative_url(directory, REPO_ROOT / SHIPMENT_CONTROL_TOWER_RELATIVE)
    operations_open = relative_url(directory, REPO_ROOT / "03_operations/OPEN-HERE.html")
    operations_memo_open = relative_url(directory, REPO_ROOT / "03_operations/README.html")
    shipments_open = relative_url(directory, REPO_ROOT / SHIPMENTS_RELATIVE / "OPEN-HERE.html")
    active_shipments_open = relative_url(directory, REPO_ROOT / ACTIVE_SHIPMENTS_RELATIVE / "OPEN-HERE.html")
    active_shipments_brief_open = relative_url(directory, REPO_ROOT / ACTIVE_SHIPMENTS_RELATIVE / "README.html")

    if relative == SHIPMENTS_RELATIVE:
        return {
            "panel_label": "Shipment Hub Navigation",
            "snapshot_eyebrow": "Operations Brief Snapshot",
            "snapshot_pill": "Stack Entry",
            "brief_pill": "Operations Brief",
            "route_label": "Shipment Routes",
            "route_summary": "Release / Proof / Founder",
            "route_links_nav": [
                ("Shipment Routes", "#featured-routes", ""),
                ("Active Shipments", active_shipments_open, ""),
                ("Shipment Room", shipment_room_open, ""),
            ],
            "route_links_cta": [
                ("Open Shipment Routes", "#featured-routes"),
                ("Open Active Shipments", active_shipments_open),
                ("Open Shipment Room", shipment_room_open),
            ],
            "outcome_label": "Shipment Outcomes",
            "outcome_summary": "Gate / Packet / Tower",
            "outcome_links_nav": [
                ("Release Gate", release_gate_open, ""),
                ("Packet Proof", packet_proof_open, ""),
                ("Control Tower", shipment_control_tower_open, ""),
            ],
            "outcome_links_cta": [
                ("Open Release Gate", release_gate_open),
                ("Open Packet Proof", packet_proof_open),
                ("Open Control Tower", shipment_control_tower_open),
            ],
            "return_label": "Return Layer",
            "return_summary": "Operations / Lane / Board",
            "return_links_nav": [
                ("Operations", operations_open, ""),
                ("Operations Memo", operations_memo_open, ""),
                ("Active Shipments", active_shipments_open, ""),
                ("Shipment Control Tower", shipment_control_tower_open, ""),
            ],
            "return_links_cta": [
                ("Open Operations", operations_open),
                ("Open Operations Memo", operations_memo_open),
                ("Open Active Shipments", active_shipments_open),
                ("Open Shipment Control Tower", shipment_control_tower_open),
            ],
        }

    if relative == ACTIVE_SHIPMENTS_RELATIVE:
        return {
            "panel_label": "Shipment Lane Navigation",
            "snapshot_eyebrow": "Shipment Brief Snapshot",
            "snapshot_pill": "Lane Entry",
            "brief_pill": "Shipment Brief",
            "room_entry_label": "Routes",
            "room_entry_href": f"{shipments_open}#featured-routes",
            "route_label": "Shipment Routes",
            "route_summary": "Release / Proof / Contained",
            "route_links_nav": [
                ("Shipment Routes", f"{shipments_open}#featured-routes", ""),
                ("Active Routes", "#featured-routes", ""),
                ("Shipment Room", shipment_room_open, ""),
            ],
            "route_links_cta": [
                ("Open Shipment Routes", f"{shipments_open}#featured-routes"),
                ("Open Active Routes", "#featured-routes"),
                ("Open Shipment Room", shipment_room_open),
            ],
            "outcome_label": "Shipment Outcomes",
            "outcome_summary": "Move / Proof / Tower",
            "outcome_links_nav": [
                ("Release Gate", release_gate_open, ""),
                ("Packet Proof", packet_proof_open, ""),
                ("Control Tower", shipment_control_tower_open, ""),
            ],
            "outcome_links_cta": [
                ("Open Release Gate", release_gate_open),
                ("Open Packet Proof", packet_proof_open),
                ("Open Control Tower", shipment_control_tower_open),
            ],
            "return_label": "Return Layer",
            "return_summary": "Brief / Lane / Hub / Board",
            "return_links_nav": [
                ("Shipment Brief", active_shipments_brief_open, ""),
                ("Shipments", shipments_open, ""),
                ("Operations", operations_open, ""),
                ("Shipment Control Tower", shipment_control_tower_open, ""),
            ],
            "return_links_cta": [
                ("Open Shipment Brief", active_shipments_brief_open),
                ("Open Shipments", shipments_open),
                ("Open Operations", operations_open),
                ("Open Shipment Control Tower", shipment_control_tower_open),
            ],
        }

    return None


def get_route_posture(
    sequence_local: int,
    sequence_external: int,
    outcome_local: int,
    outcome_external: int,
) -> dict[str, str]:
    if sequence_external == 0 and outcome_external == 0:
        return {
            "label": "In-Room Throughline",
            "pill_class": "meta-pill meta-pill--route-local",
            "note_class": "priority-brief-route-note priority-brief-route-note--local",
            "note": "This case stays inside the room from the brief through the next outcome, so the founder can read and act without leaving the local stack.",
        }
    if sequence_local or outcome_local:
        return {
            "label": "Mixed Exit Logic",
            "pill_class": "meta-pill meta-pill--route-mixed",
            "note_class": "priority-brief-route-note priority-brief-route-note--mixed",
            "note": "Most moves stay inside the room, but this case still exits to a wider board when the sequence or outcome stack explicitly calls for it.",
        }
    return {
        "label": "Board-Led Route",
        "pill_class": "meta-pill meta-pill--route-external",
        "note_class": "priority-brief-route-note priority-brief-route-note--external",
        "note": "This case quickly leaves the room for wider boards, so the founder should expect an external control layer early.",
        }


def build_route_posture_links(links: list[tuple[str, str]]) -> str:
    if not links:
        return ""
    return (
        '<div class="card-meta priority-brief-route-links">'
        + "".join(
            f'<a class="meta-pill meta-pill--link" href="{html.escape(href, quote=True)}">{html.escape(label)}</a>'
            for label, href in links
        )
        + "</div>"
    )


def get_priority_brief_group_summary_pill_class(summary: str | None, modifier: str | None) -> str:
    if not summary:
        return "meta-pill"
    normalized = summary.lower()
    if modifier == "sequence":
        return "meta-pill meta-pill--nav-sequence"
    if modifier == "module-surface":
        return "meta-pill meta-pill--nav-module-surface"
    if modifier == "stack":
        return "meta-pill meta-pill--nav-stack"
    if modifier == "path-surface":
        return "meta-pill meta-pill--nav-path-surface"
    if modifier == "support":
        return "meta-pill meta-pill--nav-oversight"
    if modifier == "surface":
        return "meta-pill meta-pill--nav-surface"
    if modifier in {"room", "outcomes"}:
        if "in-room" in normalized and "external" in normalized:
            return "meta-pill meta-pill--route-mixed"
        if "in-room" in normalized:
            return "meta-pill meta-pill--route-local"
        if "external" in normalized:
            return "meta-pill meta-pill--route-external"
        return "meta-pill meta-pill--nav-room-route" if modifier == "room" else "meta-pill meta-pill--nav-outcome"
    return "meta-pill"


def get_priority_brief_group_count_pill_class(modifier: str | None) -> str:
    if modifier == "sequence":
        return "meta-pill meta-pill--nav-sequence"
    if modifier == "module-surface":
        return "meta-pill meta-pill--nav-module-surface"
    if modifier == "stack":
        return "meta-pill meta-pill--nav-stack"
    if modifier == "path-surface":
        return "meta-pill meta-pill--nav-path-surface"
    if modifier == "room":
        return "meta-pill meta-pill--nav-room-route"
    if modifier == "outcomes":
        return "meta-pill meta-pill--nav-outcome"
    if modifier == "support":
        return "meta-pill meta-pill--nav-oversight"
    if modifier == "surface":
        return "meta-pill meta-pill--nav-surface"
    return "meta-pill"


def build_route_posture_link_groups(
    groups: list[tuple[str, list[tuple[str, str]], str | None, str | None]]
) -> str:
    rendered_groups: list[str] = []
    for label, links, modifier, summary in groups:
        filtered_links = [(group_label, href) for group_label, href in links if group_label and href]
        if not filtered_links:
            continue
        count = len(filtered_links)
        count_label = f"{count} Link" if count == 1 else f"{count} Links"
        group_class = "priority-brief-route-group"
        if modifier:
            group_class += f" priority-brief-route-group--{modifier}"
        summary_html = (
            f'<span class="{html.escape(get_priority_brief_group_summary_pill_class(summary, modifier), quote=True)}">{html.escape(summary)}</span>'
            if summary
            else ""
        )
        count_html = (
            f'<span class="{html.escape(get_priority_brief_group_count_pill_class(modifier), quote=True)}">{html.escape(count_label)}</span>'
        )
        rendered_groups.append(
            f"""
            <div class="{html.escape(group_class, quote=True)}">
              <div class="priority-brief-route-group-header">
                <p class="priority-brief-route-group-label">{html.escape(label)}</p>
                <div class="priority-brief-route-group-meta">{summary_html}{count_html}</div>
              </div>
              {build_route_posture_links(filtered_links)}
            </div>
            """
        )
    if not rendered_groups:
        return ""
    return '<div class="priority-brief-route-groups">' + "".join(rendered_groups) + "</div>"


def build_room_nav_links(links: list[tuple[str, str, str]]) -> str:
    return "".join(
        f'<a class="room-nav-link{" room-nav-link--top" if style == "top" else ""}" href="{html.escape(href, quote=True)}">{html.escape(label)}</a>'
        for label, href, style in links
    )


def get_room_nav_summary_pill_class(summary: str | None, modifier: str | None) -> str:
    if not summary:
        return "meta-pill"
    normalized = summary.lower()
    if "mixed exit logic" in normalized:
        return "meta-pill meta-pill--route-mixed"
    if "in-room throughline" in normalized:
        return "meta-pill meta-pill--route-local"
    if "board-led route" in normalized:
        return "meta-pill meta-pill--route-external"
    if modifier == "module":
        return "meta-pill meta-pill--nav-sequence"
    if modifier == "stack":
        return "meta-pill meta-pill--nav-stack"
    if modifier == "module-surface":
        return "meta-pill meta-pill--nav-module-surface"
    if modifier == "path-surface":
        return "meta-pill meta-pill--nav-path-surface"
    if modifier == "controls":
        if "in-room" in normalized and "external" in normalized:
            return "meta-pill meta-pill--route-mixed"
        if "in-room" in normalized:
            return "meta-pill meta-pill--route-local"
        if "external" in normalized:
            return "meta-pill meta-pill--route-external"
        return "meta-pill meta-pill--nav-outcome"
    if modifier == "support":
        return "meta-pill meta-pill--nav-oversight"
    if modifier == "surface":
        return "meta-pill meta-pill--nav-surface"
    return "meta-pill"


def get_room_nav_count_pill_class(modifier: str | None) -> str:
    if modifier == "module":
        return "meta-pill meta-pill--nav-sequence"
    if modifier == "stack":
        return "meta-pill meta-pill--nav-stack"
    if modifier == "module-surface":
        return "meta-pill meta-pill--nav-module-surface"
    if modifier == "path-surface":
        return "meta-pill meta-pill--nav-path-surface"
    if modifier == "route":
        return "meta-pill meta-pill--nav-room-route"
    if modifier == "controls":
        return "meta-pill meta-pill--nav-outcome"
    if modifier == "support":
        return "meta-pill meta-pill--nav-oversight"
    if modifier == "surface":
        return "meta-pill meta-pill--nav-surface"
    return "meta-pill"


def build_room_nav_link_groups(
    groups: list[tuple[str, list[tuple[str, str, str]], str | None, str | None]]
) -> str:
    rendered_groups: list[str] = []
    for label, links, modifier, summary in groups:
        filtered_links = [
            (link_label, href, style)
            for link_label, href, style in links
            if link_label and href
        ]
        if not filtered_links:
            continue
        count = len(filtered_links)
        count_label = f"{count} Link" if count == 1 else f"{count} Links"
        group_class = "room-nav-group"
        if modifier:
            group_class += f" room-nav-group--{modifier}"
        header_meta = [
            f'<span class="{html.escape(get_room_nav_count_pill_class(modifier), quote=True)}">{html.escape(count_label)}</span>'
        ]
        if summary:
            header_meta.insert(
                0,
                f'<span class="{html.escape(get_room_nav_summary_pill_class(summary, modifier), quote=True)}">{html.escape(summary)}</span>',
            )
        rendered_groups.append(
            f"""
            <div class="{html.escape(group_class, quote=True)}">
              <div class="room-nav-group-header">
                <p class="room-nav-group-label">{html.escape(label)}</p>
                <div class="room-nav-group-meta">{''.join(header_meta)}</div>
              </div>
              <div class="room-nav-links">
                {build_room_nav_links(filtered_links)}
              </div>
            </div>
            """
        )
    if not rendered_groups:
        return ""
    return '<div class="room-nav-groups">' + "".join(rendered_groups) + "</div>"


def is_outcome_path_room_module(room_directory: Path, target: str) -> bool:
    target_path = REPO_ROOT / str(target)
    return target_path.name == "OPEN-HERE.html" and target_path.parent.parent == room_directory


def get_outcome_path_scope_counts(room_directory: Path) -> tuple[int, int]:
    try:
        relative = room_directory.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return (0, 0)
    profile = get_outcome_paths_profile(relative)
    if not profile:
        return (0, 0)
    local_count = 0
    external_count = 0
    for pill, title, copy, cta, target in profile["paths"]:
        if is_outcome_path_room_module(room_directory, str(target)):
            local_count += 1
        else:
            external_count += 1
    return (local_count, external_count)


def format_scope_summary(local_count: int, external_count: int) -> str:
    parts: list[str] = []
    if local_count:
        parts.append(f"{local_count} in-room")
    if external_count:
        parts.append(f"{external_count} external")
    if not parts:
        return "No route data"
    return " / ".join(parts)


def brief_has_escalation_triggers(brief_path: Path) -> bool:
    if not brief_path.exists():
        return False
    _title, _subtitle, _meta, body_lines = extract_document_parts(
        brief_path.read_text(encoding="utf-8"),
        humanize_slug(brief_path.stem),
    )
    return bool(extract_section_list_items(body_lines, "Escalation Triggers"))


def get_escalation_trigger_pill_label(trigger: str, index: int) -> str:
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", trigger)
    plain = re.sub(r"[*_`>#-]+", " ", plain)
    words = re.findall(r"[A-Za-z0-9]+", plain)
    stopwords = {
        "if",
        "when",
        "the",
        "a",
        "an",
        "and",
        "or",
        "to",
        "of",
        "for",
        "on",
        "in",
        "is",
        "are",
        "be",
        "any",
        "this",
        "that",
        "with",
        "from",
        "at",
        "by",
        "as",
        "it",
        "its",
        "into",
        "your",
        "their",
        "our",
        "should",
        "must",
        "can",
        "still",
        "now",
    }
    filtered = [word for word in words if word.lower() not in stopwords][:2]
    if not filtered:
        filtered = words[:2]
    label = " ".join(filtered) if filtered else "Trigger"
    return f"{index:02d} {label}"


def get_outcome_path_target_context(
    room_directory: Path,
    current_directory: Path,
    pill: str,
    target: str,
    *,
    anchor_prefix: str,
    jump_label: str,
) -> dict[str, object]:
    target_path = REPO_ROOT / str(target)
    href = relative_url(current_directory, target_path)
    is_room_module = is_outcome_path_room_module(room_directory, str(target))
    if is_room_module:
        return {
            "scope": "local",
            "href": href,
            "meta_items": [
                ("In Room", "meta-pill meta-pill--outcome-local"),
                ("Live Module", "meta-pill"),
            ],
            "jump_href": f"#{anchor_prefix}-{slugify_heading(pill)}",
            "jump_label": jump_label,
        }
    return {
        "scope": "external",
        "href": href,
        "meta_items": [
            ("External Control", "meta-pill meta-pill--outcome-external"),
            (get_outcome_path_target_label(target_path), "meta-pill"),
        ],
        "jump_href": None,
        "jump_label": None,
    }


def build_meta_pills(items: list[tuple[str, str]]) -> str:
    return "".join(
        f'<span class="{html.escape(class_name, quote=True)}">{html.escape(label)}</span>'
        for label, class_name in items
    )


def build_outcome_path_route_note(scope: str, *, module_context: bool = False) -> str:
    if scope == "local":
        text = (
            "Stay inside the current room stack and move directly into the linked live module."
            if module_context
            else "Stay inside this case room and move directly into the linked live module."
        )
        modifier = "local"
    else:
        text = (
            "Step out of the current room stack and validate the answer on a wider board."
            if module_context
            else "Step out of this case room and validate the answer on a wider board."
        )
        modifier = "external"
    return f'<p class="outcome-path-route-note outcome-path-route-note--{modifier}">{html.escape(text)}</p>'


def build_outcome_path_group_panel(
    eyebrow: str,
    title: str,
    copy: str,
    cards: list[str],
    *,
    anchor_id: str | None = None,
    summary_pills: list[tuple[str, str | None]] | None = None,
    local: bool,
) -> str:
    if not cards:
        return ""
    modifier = " viewer-subsection--current-path" if local else " viewer-subsection--supporting"
    anchor_attr = f' id="{html.escape(anchor_id, quote=True)}"' if anchor_id else ""
    summary_html = ""
    if summary_pills:
        summary_html = (
            '<div class="card-meta">'
            + "".join(
                (
                    f'<a class="meta-pill meta-pill--link" href="{html.escape(target, quote=True)}">{html.escape(pill)}</a>'
                    if target
                    else f'<span class="meta-pill">{html.escape(pill)}</span>'
                )
                for pill, target in summary_pills
            )
            + "</div>"
        )
    return f"""
          <div class="viewer-subsection{modifier}"{anchor_attr}>
            <div class="section-heading">
              <p class="eyebrow">{html.escape(eyebrow)}</p>
              <h3 class="section-title-sm">{html.escape(title)}</h3>
              <p class="section-copy">{html.escape(copy)}</p>
              {summary_html}
            </div>
            <div class="outcome-paths-grid">
              {"".join(cards)}
            </div>
          </div>
"""


def build_outcome_paths_section(directory: Path) -> str:
    relative = directory.relative_to(REPO_ROOT).as_posix()
    profile = get_outcome_paths_profile(relative)
    if not profile:
        return ""

    total_paths = len(profile["paths"])
    local_count = 0
    external_count = 0
    summary_pills: list[tuple[str, str | None]] = []
    local_cards: list[str] = []
    external_cards: list[str] = []
    local_pills: list[tuple[str, str | None]] = []
    external_pills: list[tuple[str, str | None]] = []
    for index, (pill, title, copy, cta, target) in enumerate(profile["paths"], start=1):
        target_context = get_outcome_path_target_context(
            directory,
            directory,
            str(pill),
            str(target),
            anchor_prefix="room-path",
            jump_label="Jump to Live Module",
        )
        anchor_id = f"room-outcome-path-{slugify_heading(str(pill))}"
        if target_context["jump_href"]:
            local_count += 1
        else:
            external_count += 1
        summary_pills.append((f"{index:02d} {str(pill)} Path", f"#{anchor_id}"))
        action_links = [
            f'<a class="outcome-path-cta" href="{html.escape(str(target_context["href"]), quote=True)}">{html.escape(str(cta))}</a>'
        ]
        if target_context["jump_href"] and target_context["jump_label"]:
            action_links.append(
                f'<a class="outcome-path-cta outcome-path-cta--secondary" href="{html.escape(str(target_context["jump_href"]), quote=True)}">{html.escape(str(target_context["jump_label"]))}</a>'
            )
        card_html = f"""
          <article class="outcome-path-card outcome-path-card--{html.escape(str(target_context['scope']), quote=True)}" id="{html.escape(anchor_id, quote=True)}">
            <div class="card-meta outcome-path-meta">
              <span class="meta-pill">{index:02d} of {total_paths:02d}</span>
              <span class="outcome-path-pill">{html.escape(str(pill))}</span>
              {build_meta_pills(list(target_context["meta_items"]))}
            </div>
            <h3 class="outcome-path-title">{html.escape(str(title))}</h3>
            <p class="outcome-path-copy">{html.escape(str(copy))}</p>
            {build_outcome_path_route_note(str(target_context["scope"]))}
            <div class="viewer-card-links outcome-path-links">
              {"".join(action_links)}
            </div>
          </article>
"""
        pill_item = (f"{index:02d} {str(pill)} Path", f"#{anchor_id}")
        if target_context["jump_href"]:
            local_cards.append(card_html)
            local_pills.append(pill_item)
        else:
            external_cards.append(card_html)
            external_pills.append(pill_item)

    summary_html = (
        '<div class="card-meta">'
        f'<span class="meta-pill">{html.escape(format_count_label(total_paths, "Outcome Path"))}</span>'
        + (
            f'<span class="meta-pill">{html.escape(format_count_label(local_count, "In-Room Path", "In-Room Paths"))}</span>'
            if local_count
            else ""
        )
        + (
            f'<span class="meta-pill">{html.escape(format_count_label(external_count, "External Control"))}</span>'
            if external_count
            else ""
        )
        + "".join(
            f'<a class="meta-pill meta-pill--link" href="{html.escape(target, quote=True)}">{html.escape(label)}</a>'
            for label, target in summary_pills
        )
        + "</div>"
    )
    grouped_cards_html = (
        build_outcome_path_group_panel(
            "In-Room Paths",
            "Continue inside the live case room before leaving the stack.",
            "Use these paths when the next answer stays inside the room and the founder can move directly into a live module without stepping out to a broader board.",
            local_cards,
            anchor_id="outcome-room-paths",
            summary_pills=[(format_count_label(local_count, "In-Room Path", "In-Room Paths"), None), *local_pills],
            local=True,
        )
        + build_outcome_path_group_panel(
            "External Controls",
            "Leave the room only when the next answer belongs on a wider board.",
            "Use these paths when the founder needs a dashboard, executive board, or broader release lens rather than another module inside the same room.",
            external_cards,
            anchor_id="outcome-external-controls",
            summary_pills=[(format_count_label(external_count, "External Control"), None), *external_pills],
            local=False,
        )
    ) if local_cards and external_cards else f"""
          <div class="outcome-paths-grid">
            {"".join(local_cards + external_cards)}
          </div>
"""

    return f"""
        <section class="home-section outcome-paths-panel" id="outcome-paths">
          <div class="section-heading">
            <p class="eyebrow">Outcome Paths</p>
            <h2 class="section-title">{html.escape(str(profile["title"]))}</h2>
            <p class="section-copy">
              {html.escape(str(profile["copy"]))}
            </p>
            {summary_html}
          </div>
          {grouped_cards_html}
        </section>
"""


def build_module_outcome_paths_section(directory: Path) -> str:
    parent = directory.parent
    if parent == REPO_ROOT:
        return ""
    try:
        parent.relative_to(REPO_ROOT)
    except ValueError:
        return ""

    room_profile = build_portal_hero_context(parent)
    current_profile = build_folder_card_profile(parent, directory)
    outcome_profile = get_outcome_paths_profile(parent.relative_to(REPO_ROOT).as_posix())
    if not room_profile or not current_profile or not outcome_profile:
        return ""

    total_paths = len(outcome_profile["paths"])
    local_count = 0
    external_count = 0
    summary_pills: list[tuple[str, str | None]] = []
    local_cards: list[str] = []
    external_cards: list[str] = []
    local_pills: list[tuple[str, str | None]] = []
    external_pills: list[tuple[str, str | None]] = []
    current_target = relative_url(directory, directory / "OPEN-HERE.html")
    for index, (pill, title, copy, cta, target) in enumerate(outcome_profile["paths"], start=1):
        target_context = get_outcome_path_target_context(
            parent,
            directory,
            str(pill),
            str(target),
            anchor_prefix="stack-path",
            jump_label="Jump to Stack Module",
        )
        anchor_id = f"module-outcome-path-{slugify_heading(str(pill))}"
        if target_context["jump_href"]:
            local_count += 1
        else:
            external_count += 1
        summary_pills.append((f"{index:02d} {str(pill)} Path", f"#{anchor_id}"))
        is_current_path = str(target_context["href"]) == current_target
        meta_items = list(target_context["meta_items"])
        if is_current_path:
            meta_items.append(("Current Path", "meta-pill meta-pill--path-current"))
        path_cta = "Current Path" if is_current_path else str(cta)
        action_links = []
        if is_current_path:
            action_links.append(f'<span class="outcome-path-cta outcome-path-cta--current">{html.escape(path_cta)}</span>')
        else:
            action_links.append(
                f'<a class="outcome-path-cta" href="{html.escape(str(target_context["href"]), quote=True)}">{html.escape(path_cta)}</a>'
            )
        if target_context["jump_href"] and target_context["jump_label"]:
            action_links.append(
                f'<a class="outcome-path-cta outcome-path-cta--secondary" href="{html.escape(str(target_context["jump_href"]), quote=True)}">{html.escape(str(target_context["jump_label"]))}</a>'
            )
        card_html = f"""
          <article class="outcome-path-card outcome-path-card--{html.escape(str(target_context['scope']), quote=True)}" id="{html.escape(anchor_id, quote=True)}">
            <div class="card-meta outcome-path-meta">
              <span class="meta-pill">{index:02d} of {total_paths:02d}</span>
              <span class="outcome-path-pill">{html.escape(str(pill))}</span>
              {build_meta_pills(meta_items)}
            </div>
            <h3 class="outcome-path-title">{html.escape(str(title))}</h3>
            <p class="outcome-path-copy">{html.escape(str(copy))}</p>
            {build_outcome_path_route_note(str(target_context["scope"]), module_context=True)}
            <div class="viewer-card-links outcome-path-links">
              {"".join(action_links)}
            </div>
          </article>
"""
        pill_item = (f"{index:02d} {str(pill)} Path", f"#{anchor_id}")
        if target_context["jump_href"]:
            local_cards.append(card_html)
            local_pills.append(pill_item)
        else:
            external_cards.append(card_html)
            external_pills.append(pill_item)

    room_title = str(room_profile["title"])
    module_title = str(current_profile["title"])
    summary_html = (
        '<div class="card-meta">'
        f'<span class="meta-pill">{html.escape(format_count_label(total_paths, "Outcome Path"))}</span>'
        + (
            f'<span class="meta-pill">{html.escape(format_count_label(local_count, "In-Room Path", "In-Room Paths"))}</span>'
            if local_count
            else ""
        )
        + (
            f'<span class="meta-pill">{html.escape(format_count_label(external_count, "External Control"))}</span>'
            if external_count
            else ""
        )
        + "".join(
            f'<a class="meta-pill meta-pill--link" href="{html.escape(target, quote=True)}">{html.escape(label)}</a>'
            for label, target in summary_pills
        )
        + "</div>"
    )
    grouped_cards_html = (
        build_outcome_path_group_panel(
            "In-Room Paths",
            "Stay inside the room when the next answer is still module-level.",
            "Use these paths when the founder can stay inside the same case stack and move directly from the current module into another live module without widening to an outside board.",
            local_cards,
            anchor_id="module-outcome-room-paths",
            summary_pills=[(format_count_label(local_count, "In-Room Path", "In-Room Paths"), None), *local_pills],
            local=True,
        )
        + build_outcome_path_group_panel(
            "External Controls",
            "Step out only when the current module is no longer enough.",
            "Use these paths when the founder should leave the room stack and validate the answer on a broader board, dashboard, or executive release layer.",
            external_cards,
            anchor_id="module-outcome-external-controls",
            summary_pills=[(format_count_label(external_count, "External Control"), None), *external_pills],
            local=False,
        )
    ) if local_cards and external_cards else f"""
          <div class="outcome-paths-grid">
            {"".join(local_cards + external_cards)}
          </div>
"""
    return f"""
        <section class="home-section outcome-paths-panel" id="module-outcome-paths">
          <div class="section-heading">
            <p class="eyebrow">Module Exit Paths</p>
            <h2 class="section-title">Choose the next room-level path without leaving {html.escape(module_title)}.</h2>
            <p class="section-copy">
              These are the same outcome routes carried by {html.escape(room_title)}, now pulled into the module so the founder can advance, hold, or escalate the case from the current control layer.
            </p>
            {summary_html}
          </div>
          {grouped_cards_html}
        </section>
"""


def build_module_related_rooms_section(directory: Path) -> str:
    parent = directory.parent
    if parent == REPO_ROOT:
        return ""
    try:
        parent.relative_to(REPO_ROOT)
    except ValueError:
        return ""

    room_profile = build_portal_hero_context(parent)
    current_profile = build_folder_card_profile(parent, directory)
    if not room_profile or not current_profile:
        return ""

    related_rooms = collect_related_rooms(parent, resolve_dir=directory)
    if not related_rooms:
        return ""

    cards = []
    for room in related_rooms:
        cards.append(
            "<a class=\"brief-related-card\" "
            f"href=\"{html.escape(room['href'], quote=True)}\">"
            f"<span class=\"brief-related-pill\">{html.escape(room['pill'])}</span>"
            f"<span class=\"brief-related-title\">{html.escape(room['title'])}</span>"
            f"<span class=\"brief-related-copy\">{html.escape(room['copy'])}</span>"
            f"<span class=\"brief-related-cta\">{html.escape(room['cta'])}</span>"
            "</a>"
        )

    room_title = str(room_profile["title"])
    module_title = str(current_profile["title"])
    return (
        '<section class="brief-related-panel" id="module-related-rooms">'
        "<div class=\"brief-related-head\">"
        "<p class=\"eyebrow\">Module Related Rooms</p>"
        f"<h2 class=\"section-title-sm\">Jump laterally into the connected war rooms without leaving {html.escape(module_title)}.</h2>"
        f"<p class=\"section-copy\">Use these links when the founder needs to test {html.escape(room_title)}'s module answer against the other live rooms most likely to confirm or change the same case posture.</p>"
        "</div>"
        f"<div class=\"brief-related-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def build_escalation_watch_section(directory: Path, docs_for_dir: list[dict[str, str]]) -> str:
    brief_doc = next(
        (
            doc
            for doc in docs_for_dir
            if (build_doc_card_profile(directory, Path(str(doc["path"]))) or {}).get("kind") == "Executive Brief"
        ),
        None,
    )
    if not brief_doc:
        return ""

    markdown_path = Path(str(brief_doc["path"]))
    _title, _subtitle, _meta, body_lines = extract_document_parts(
        markdown_path.read_text(encoding="utf-8"),
        humanize_slug(markdown_path.stem),
    )
    triggers = extract_section_list_items(body_lines, "Escalation Triggers")
    if not triggers:
        return ""

    cards: list[str] = []
    summary_pills: list[tuple[str, str]] = []
    for index, trigger in enumerate(triggers, start=1):
        anchor_id = f"escalation-trigger-{index:02d}"
        summary_pills.append((get_escalation_trigger_pill_label(trigger, index), f"#{anchor_id}"))
        cards.append(
            "<article class=\"escalation-watch-card\" "
            f"id=\"{html.escape(anchor_id, quote=True)}\">"
            f"<span class=\"escalation-watch-pill\">Escalate {index:02d}</span>"
            f"<p class=\"escalation-watch-copy\">{render_inline(trigger, directory)}</p>"
            "</article>"
        )
    summary_html = (
        '<div class="card-meta">'
        f'<span class="meta-pill">{html.escape(format_count_label(len(triggers), "Escalation Trigger"))}</span>'
        + "".join(
            f'<a class="meta-pill meta-pill--link" href="{html.escape(target, quote=True)}">{html.escape(label)}</a>'
            for label, target in summary_pills
        )
        + "</div>"
    )

    return f"""
        <section class="home-section escalation-watch-panel" id="escalation-watch">
          <div class="section-heading">
            <p class="eyebrow">Escalation Watch</p>
            <h2 class="section-title">Know what breaks the normal answer.</h2>
            <p class="section-copy">
              These are the founder-level triggers that mean the room should move out of its normal path and into stronger executive control.
            </p>
            {summary_html}
          </div>
          <div class="escalation-watch-grid">
            {"".join(cards)}
          </div>
        </section>
"""


def get_module_stack_sequence_relations(directory: Path) -> dict[str, Path | None] | None:
    parent = directory.parent
    if parent == REPO_ROOT:
        return None
    try:
        parent.relative_to(REPO_ROOT)
    except ValueError:
        return None

    ordered_children = [
        child
        for child in order_child_directories(
            parent,
            [path for path in parent.iterdir() if path.is_dir() and path.name not in SKIP_DIR_NAMES],
        )
        if build_folder_card_profile(parent, child)
    ]
    if not ordered_children or directory not in ordered_children:
        return None

    relations: dict[str, Path | None] = {
        "previous_dir": None,
        "current_dir": directory,
        "next_dir": None,
    }

    relative_parent = parent.relative_to(REPO_ROOT).as_posix()
    sequence_profile = get_decision_sequence_profile(relative_parent)
    current_target_path = directory / "OPEN-HERE.html"
    if sequence_profile:
        sequence_steps = list(sequence_profile["steps"])
        current_sequence_index = next(
            (
                index
                for index, (_order, _title, _copy, _cta, target) in enumerate(sequence_steps)
                if REPO_ROOT / str(target) == current_target_path
            ),
            None,
        )
        if current_sequence_index is not None:
            if current_sequence_index > 0:
                prev_target = REPO_ROOT / str(sequence_steps[current_sequence_index - 1][4])
                try:
                    prev_relative = prev_target.relative_to(parent)
                except ValueError:
                    prev_relative = None
                if prev_relative is not None and prev_target.name == "OPEN-HERE.html" and len(prev_relative.parts) >= 2:
                    relations["previous_dir"] = prev_target.parent
            if current_sequence_index + 1 < len(sequence_steps):
                next_target = REPO_ROOT / str(sequence_steps[current_sequence_index + 1][4])
                try:
                    next_relative = next_target.relative_to(parent)
                except ValueError:
                    next_relative = None
                if next_relative is not None and next_target.name == "OPEN-HERE.html" and len(next_relative.parts) >= 2:
                    relations["next_dir"] = next_target.parent
            return relations

    current_index = ordered_children.index(directory)
    if current_index > 0:
        relations["previous_dir"] = ordered_children[current_index - 1]
    if current_index + 1 < len(ordered_children):
        relations["next_dir"] = ordered_children[current_index + 1]
    return relations


def build_room_module_stack_lineup(
    directory: Path,
    anchor_lookup: dict[Path, str],
    sequence_relations: dict[str, Path | None],
) -> list[tuple[str, str, bool]]:
    parent = directory.parent
    if parent == REPO_ROOT:
        return []

    current_profile = build_folder_card_profile(parent, directory)
    if not current_profile:
        return []

    previous_dir = sequence_relations.get("previous_dir")
    current_dir = sequence_relations.get("current_dir") or directory
    next_dir = sequence_relations.get("next_dir")
    sequence_jump_links = get_module_sequence_jump_links(directory) or {}
    previous_action = sequence_jump_links.get(
        "previous_action",
        (
            get_room_entry_label(parent, "Open Entry Brief", "Open Room Entry"),
            get_room_entry_href(directory, parent),
        ),
    )
    next_action = sequence_jump_links.get("next_action", ("Open Room Outcomes", f"{relative_url(directory, parent / 'OPEN-HERE.html')}#outcome-paths"))
    full_links = list(sequence_jump_links.get("full_links", []))
    current_action_label = str(full_links[1][0]) if len(full_links) >= 2 else str(current_profile.get("cta") or current_profile["title"])

    def build_label(source_label: str, *, current: bool = False) -> str:
        base = strip_open_prefix(source_label)
        if current and not base.lower().startswith("current "):
            base = f"Current {base}"
        return base

    lineup: list[tuple[str, str, bool]] = []

    previous_label = build_label(str(previous_action[0]))
    previous_href = f"#{anchor_lookup[previous_dir]}" if previous_dir and previous_dir in anchor_lookup else str(previous_action[1])
    lineup.append((f"01 {previous_label}", previous_href, previous_dir is not None and previous_dir in anchor_lookup))

    current_label = build_label(current_action_label, current=True)
    current_href = f"#{anchor_lookup[current_dir]}" if current_dir in anchor_lookup else "#room-module-stack"
    lineup.append((f"02 {current_label}", current_href, current_dir in anchor_lookup))

    next_label = build_label(str(next_action[0]))
    next_href = f"#{anchor_lookup[next_dir]}" if next_dir and next_dir in anchor_lookup else str(next_action[1])
    lineup.append((f"03 {next_label}", next_href, next_dir is not None and next_dir in anchor_lookup))

    return lineup


def get_module_stack_jump_links(directory: Path) -> dict[str, list[tuple[str, str]]] | None:
    parent = directory.parent
    if parent == REPO_ROOT:
        return None
    try:
        parent.relative_to(REPO_ROOT)
    except ValueError:
        return None

    sequence_relations = get_module_stack_sequence_relations(directory)
    if not sequence_relations:
        return None

    previous_dir = sequence_relations.get("previous_dir")
    next_dir = sequence_relations.get("next_dir")
    sequence_jump_links = get_module_sequence_jump_links(directory) or {}
    previous_action = sequence_jump_links.get(
        "previous_action",
        (
            get_room_entry_label(parent, "Open Entry Brief", "Open Room Entry"),
            get_room_entry_href(directory, parent),
        ),
    )
    next_action = sequence_jump_links.get("next_action", ("Open Room Outcomes", f"{relative_url(directory, parent / 'OPEN-HERE.html')}#outcome-paths"))
    full_links = list(sequence_jump_links.get("full_links", []))
    current_action_label = str(full_links[1][0]) if len(full_links) >= 2 else "Open Current Module"

    def current_stack_label(label: str) -> str:
        cleaned = strip_open_prefix(label)
        if not cleaned.lower().startswith("current "):
            cleaned = f"Current {cleaned}"
        return cleaned

    def stack_label(label: str) -> str:
        return strip_open_prefix(label)

    if previous_dir is not None:
        previous_href = f"#{get_stack_module_anchor_id(previous_dir)}"
        previous_nav = f"Stack {stack_label(str(previous_action[0]))}"
        previous_full = f"Open Stack {stack_label(str(previous_action[0]))}"
    else:
        previous_href = str(previous_action[1])
        previous_nav = f"Stack {stack_label(str(previous_action[0]))}"
        previous_full = f"Open Stack {stack_label(str(previous_action[0]))}"

    current_href = f"#{get_stack_module_anchor_id(directory)}"
    current_nav = f"Stack {current_stack_label(current_action_label)}"
    current_full = f"Open Stack {current_stack_label(current_action_label)}"

    if next_dir is not None:
        next_href = f"#{get_stack_module_anchor_id(next_dir)}"
        next_nav = f"Stack {stack_label(str(next_action[0]))}"
        next_full = f"Open Stack {stack_label(str(next_action[0]))}"
    else:
        next_href = str(next_action[1])
        next_nav = f"Stack {stack_label(str(next_action[0]))}"
        next_full = f"Open Stack {stack_label(str(next_action[0]))}"

    return {
        "nav_links": [
            (previous_nav, previous_href),
            (current_nav, current_href),
            (next_nav, next_href),
        ],
        "full_links": [
            (previous_full, previous_href),
            (current_full, current_href),
            (next_full, next_href),
        ],
    }


def build_room_module_stack_section(directory: Path) -> str:
    parent = directory.parent
    if parent == REPO_ROOT:
        return ""
    try:
        parent.relative_to(REPO_ROOT)
    except ValueError:
        return ""

    room_profile = build_portal_hero_context(parent)
    current_profile = build_folder_card_profile(parent, directory)
    if not room_profile or not current_profile:
        return ""

    path_entries: list[tuple[int, str, str, tuple[str, str | None]]] = []
    support_cards: list[str] = []
    relative_parent = parent.relative_to(REPO_ROOT).as_posix()
    has_room_paths = bool(get_outcome_paths_profile(relative_parent))
    path_order = get_outcome_path_order_map(relative_parent)
    sequence_relations = get_module_stack_sequence_relations(directory) or {}
    previous_dir = sequence_relations.get("previous_dir")
    current_dir = sequence_relations.get("current_dir")
    next_dir = sequence_relations.get("next_dir")
    card_anchor_lookup: dict[Path, str] = {}
    for child in order_child_directories(
        parent,
        [path for path in parent.iterdir() if path.is_dir() and path.name not in SKIP_DIR_NAMES],
    ):
        profile = build_folder_card_profile(parent, child)
        if not profile:
            continue
        href = relative_url(directory, child / "OPEN-HERE.html")
        current_pill = '<span class="meta-pill">Current</span>' if child == directory else ""
        path_context = get_module_room_path_context(parent, child) if has_room_paths else None
        path_sequence = get_outcome_path_sequence(relative_parent, str(path_context["pill"])) if path_context else None
        card_classes = ["viewer-card"]
        if path_context:
            card_classes.append("viewer-card--current-path")
        elif has_room_paths:
            card_classes.append("viewer-card--supporting-control")

        sequence_relation_pill = ""
        sequence_relation_note = ""
        if child == current_dir:
            card_classes.append("viewer-card--sequence-current-step")
            sequence_relation_pill = '<span class="meta-pill meta-pill--sequence-current">Current Step</span>'
            sequence_relation_note = '<p class="viewer-card-sequence-note viewer-card-sequence-note--current">This is the module currently open in the room sequence.</p>'
        elif previous_dir is not None and child == previous_dir:
            card_classes.append("viewer-card--sequence-previous-step")
            sequence_relation_pill = '<span class="meta-pill meta-pill--sequence-previous">Previous Step</span>'
            sequence_relation_note = '<p class="viewer-card-sequence-note viewer-card-sequence-note--previous">This module is the immediate previous step before the current module.</p>'
        elif next_dir is not None and child == next_dir:
            card_classes.append("viewer-card--sequence-next-step")
            sequence_relation_pill = '<span class="meta-pill meta-pill--sequence-next">Next Step</span>'
            sequence_relation_note = '<p class="viewer-card-sequence-note viewer-card-sequence-note--next">This module is the immediate next step after the current module.</p>'

        card_class = " ".join(card_classes)
        path_pill = (
            (
                f'<span class="meta-pill">Path {path_sequence[0]:02d} of {path_sequence[1]:02d}</span>'
                f'<span class="meta-pill meta-pill--path-current">Current Path</span>'
            )
            if path_context
            else '<span class="meta-pill meta-pill--path-supporting">Supporting Control</span>' if has_room_paths else ""
        )
        path_role_note = build_path_role_note(path_context, has_room_paths, current_module=child == directory)
        if child == directory:
            cta = "Current Path Module" if path_context else "Current Module"
        else:
            cta = f"Open {str(path_context['pill'])} Path" if path_context else str(profile["cta"])
        card_anchor_id = get_stack_module_anchor_id(child)
        card_anchor_lookup[child] = card_anchor_id
        anchor_attr = f' id="{html.escape(card_anchor_id, quote=True)}"'
        card_html = f"""
          <article class="{card_class}"{anchor_attr}>
            <div class="card-meta">
              <span class="meta-pill">Room Module</span>
              <span class="meta-pill">{html.escape(str(profile["pill"]))}</span>
              {path_pill}
              {sequence_relation_pill}
              {current_pill}
            </div>
            <h3 class="viewer-card-title">{html.escape(str(profile["title"]))}</h3>
            <p class="viewer-card-copy">{html.escape(str(profile["copy"]))}</p>
            {sequence_relation_note}
            {path_role_note}
            <div class="viewer-card-links">
              <a class="button-primary" href="{href}">{html.escape(cta)}</a>
            </div>
          </article>
"""
        if path_context:
            pill_name = str(path_context["pill"])
            path_entries.append(
                (
                    path_order.get(pill_name, len(path_order)),
                    pill_name,
                    card_html,
                    (f"{path_sequence[0]:02d} {pill_name} Path", f"#{card_anchor_id}"),
                )
            )
        else:
            support_cards.append(card_html)

    path_cards = [entry[2] for entry in sorted(path_entries, key=lambda item: (item[0], item[1]))]
    path_pills = [entry[3] for entry in sorted(path_entries, key=lambda item: (item[0], item[1]))]

    if not path_cards and not support_cards:
        return ""

    room_title = str(room_profile["title"])
    stack_lineup = build_room_module_stack_lineup(directory, card_anchor_lookup, sequence_relations)
    in_stack_count = sum(1 for _label, _href, in_stack in stack_lineup if in_stack)
    transition_count = len(stack_lineup) - in_stack_count
    stack_summary_html = ""
    if stack_lineup:
        stack_summary_html = (
            '<div class="card-meta">'
            f'<span class="meta-pill">{html.escape(format_count_label(len(stack_lineup), "Sequence Stop"))}</span>'
            + (
                f'<span class="meta-pill">{html.escape(format_count_label(in_stack_count, "In-Stack Module"))}</span>'
                if in_stack_count
                else ""
            )
            + (
                f'<span class="meta-pill">{html.escape(format_count_label(transition_count, "Room Transition"))}</span>'
                if transition_count
                else ""
            )
            + "".join(
                f'<a class="meta-pill meta-pill--link" href="{html.escape(href, quote=True)}">{html.escape(label)}</a>'
                for label, href, _in_stack in stack_lineup
            )
            + "</div>"
        )
    if has_room_paths and path_cards:
        grouped_cards = (
            build_module_group_panel(
                "Live Path Modules",
                "Start with the modules that currently carry the room answer.",
                "These modules hold the active advance, hold, contain, recover, move, or escalate answer inside the room, so they deserve first reading priority.",
                path_cards,
                anchor_id="stack-live-path-modules",
                summary_pills=[(format_count_label(len(path_cards), "Active Path"), None), *list(dict.fromkeys(path_pills))],
                current_path=True,
            )
            + build_module_group_panel(
                "Supporting Controls",
                "Use supporting controls to pressure-test the live room path.",
                "These modules help the founder confirm, tighten, or challenge the active room answer before changing the case direction.",
                support_cards,
                anchor_id="stack-supporting-controls",
                summary_pills=[(format_count_label(len(support_cards), "Supporting Control"), None), ("Pressure-Test Layer", None)] if support_cards else None,
                current_path=False,
            )
        )
    else:
        grouped_cards = f"""
          <div class="viewer-grid">
            {"".join(path_cards + support_cards)}
          </div>
"""
    return f"""
        <section class="home-section" id="room-module-stack">
          <div class="section-heading">
            <p class="eyebrow">Room Module Stack</p>
            <h2 class="section-title">Move across the modules that belong to {html.escape(room_title)}.</h2>
            <p class="section-copy">
              Use this stack when the founder is already inside one module but needs to compare it against the sibling controls that make up the same room answer, then jump directly to the exact previous, current, next, entry, or outcomes stop.
            </p>
            {stack_summary_html}
          </div>
          {grouped_cards}
        </section>
"""


def build_module_sequence_context_section(directory: Path) -> str:
    parent = directory.parent
    if parent == REPO_ROOT:
        return ""
    try:
        parent.relative_to(REPO_ROOT)
    except ValueError:
        return ""

    room_profile = build_portal_hero_context(parent)
    current_profile = build_folder_card_profile(parent, directory)
    if not room_profile or not current_profile:
        return ""
    sequence_jump_links = get_module_sequence_jump_links(directory) or {}
    sequence_action_links = list(sequence_jump_links.get("full_links", []))

    cards: list[dict[str, object]] = []

    def sequence_summary_label(index: int, fallback: str) -> str:
        if 0 <= index < len(sequence_action_links):
            label = strip_open_prefix(str(sequence_action_links[index][0]))
            if label:
                return f"{index + 1:02d} {label}"
        return fallback

    def current_sequence_label() -> str:
        if len(sequence_action_links) >= 2:
            label = strip_open_prefix(str(sequence_action_links[1][0]))
            if label:
                if not label.lower().startswith("current "):
                    label = f"Current {label}"
                return label
        fallback = str(current_profile.get("pill") or current_profile["title"])
        if fallback.lower().startswith("current "):
            return fallback
        return f"Current {fallback}"

    def register_sequence_card(
        kind: str,
        title: str,
        copy: str,
        href: str,
        cta: str,
        step_label: str,
        anchor_id: str,
        summary_label: str,
        meta_items: list[tuple[str, str]] | None = None,
        route_note: str | None = None,
        current: bool = False,
        stack_href: str | None = None,
        stack_cta: str | None = None,
    ) -> None:
        cards.append(
            {
                "kind": kind,
                "title": title,
                "copy": copy,
                "href": href,
                "cta": cta,
                "step_label": step_label,
                "anchor_id": anchor_id,
                "summary_label": summary_label,
                "meta_items": list(meta_items or []),
                "route_note": route_note,
                "current": current,
                "stack_href": stack_href,
                "stack_cta": stack_cta,
                "external": any(label == "External Control" for label, _ in (meta_items or [])),
            }
        )

    def render_sequence_card(card: dict[str, object]) -> str:
        meta_items = list(card["meta_items"])
        meta_html = build_meta_pills(meta_items)
        route_html = (
            f'<p class="decision-sequence-route-note decision-sequence-route-note--{"external" if card["external"] else "local"}">{html.escape(str(card["route_note"]))}</p>'
            if card["route_note"]
            else ""
        )
        card_classes = ["viewer-card", "module-sequence-card"]
        if card["current"]:
            card_classes.append("module-sequence-card--current")
        if card["external"]:
            card_classes.append("module-sequence-card--external")
        primary_href = str(card["href"])
        primary_cta = str(card["cta"])
        stack_link_html = (
            f'<a class="button-secondary" href="{html.escape(str(card["stack_href"]), quote=True)}">{html.escape(str(card["stack_cta"]))}</a>'
            if card["stack_href"] and card["stack_cta"]
            else ""
        )
        if card["current"] and card["stack_href"] and card["stack_cta"]:
            primary_href = str(card["stack_href"])
            primary_cta = str(card["stack_cta"])
            stack_link_html = ""
        return f"""
          <article class="{' '.join(card_classes)}" id="{html.escape(str(card["anchor_id"]), quote=True)}">
            <div class="card-meta">
              <span class="meta-pill">{html.escape(str(card["kind"]))}</span>
              <span class="meta-pill">{html.escape(str(card["step_label"]))}</span>
              {meta_html}
            </div>
            <h3 class="viewer-card-title">{html.escape(str(card["title"]))}</h3>
            <p class="viewer-card-copy">{html.escape(str(card["copy"]))}</p>
            {route_html}
            <div class="viewer-card-links">
              <a class="button-primary" href="{html.escape(primary_href, quote=True)}">{html.escape(primary_cta)}</a>
              {stack_link_html}
            </div>
          </article>
"""

    relative_parent = parent.relative_to(REPO_ROOT).as_posix()
    sequence_profile = get_decision_sequence_profile(relative_parent)
    current_target_path = directory / "OPEN-HERE.html"
    ordered_children = [
        child
        for child in order_child_directories(
            parent,
            [path for path in parent.iterdir() if path.is_dir() and path.name not in SKIP_DIR_NAMES],
        )
        if build_folder_card_profile(parent, child)
    ]
    if not ordered_children or directory not in ordered_children:
        return ""

    current_index = ordered_children.index(directory)
    total = len(ordered_children)
    shipment_stack_override = get_shipment_stack_navigation_override(directory)
    room_title = str(room_profile["title"])
    room_short = " ".join(room_title.split()[-2:])
    if sequence_profile:
        sequence_steps = list(sequence_profile["steps"])
        current_sequence_index = next(
            (
                index
                for index, (_order, _title, _copy, _cta, target) in enumerate(sequence_steps)
                if REPO_ROOT / str(target) == current_target_path
            ),
            None,
        )
        if current_sequence_index is not None:
            total_steps = len(sequence_steps)
            if current_sequence_index > 0:
                prev_order, prev_title, prev_copy, prev_cta, prev_target = sequence_steps[current_sequence_index - 1]
                prev_context = get_sequence_step_target_context(parent, directory, str(prev_target))
                prev_stack_href = get_room_module_stack_href(parent, REPO_ROOT / str(prev_target))
                register_sequence_card(
                    "Previous Step",
                    str(prev_title),
                    str(prev_copy),
                    str(prev_context["href"]),
                    str(prev_cta),
                    f"Step {prev_order} of {total_steps:02d}",
                    "module-sequence-previous",
                    sequence_summary_label(0, "01 Previous"),
                    list(prev_context["meta_items"]),
                    str(prev_context["route_note"]),
                    stack_href=prev_stack_href,
                    stack_cta="Jump to Stack Module" if prev_stack_href else None,
                )
            else:
                register_sequence_card(
                    "Room Entry",
                    room_title,
                    "This module sits at the start of the room decision sequence. Return to the brief when the founder needs the full case framing before moving deeper.",
                    get_room_entry_href(directory, parent),
                    get_room_entry_label(parent, "Open Room Brief", "Open Room Entry"),
                    f"Step 01 of {total_steps:02d}",
                    "module-sequence-entry",
                    sequence_summary_label(0, "01 Entry Brief"),
                    [("In Room", "meta-pill meta-pill--outcome-local"), ("Executive Brief", "meta-pill")],
                    "Stay inside the current room stack and begin from the founder brief before widening movement.",
                )

            current_order, current_step_title, current_step_copy, _current_cta, _current_target = sequence_steps[current_sequence_index]
            current_context = get_sequence_step_target_context(parent, directory, str(_current_target))
            current_meta = [("Current Step", "meta-pill")] + list(current_context["meta_items"])
            register_sequence_card(
                "Current",
                str(current_profile["title"]),
                f"This is the active module in the room decision sequence. {str(current_step_copy)}",
                relative_url(directory, directory / "OPEN-HERE.html"),
                current_sequence_label(),
                f"Step {current_order} of {total_steps:02d}",
                "module-sequence-current",
                sequence_summary_label(1, "02 Current"),
                current_meta,
                str(current_context["route_note"]),
                current=True,
                stack_href=f"#{get_stack_module_anchor_id(directory)}",
                stack_cta="Jump to Stack Module",
            )

            if current_sequence_index + 1 < total_steps:
                next_order, next_title, next_copy, next_cta, next_target = sequence_steps[current_sequence_index + 1]
                next_context = get_sequence_step_target_context(parent, directory, str(next_target))
                next_stack_href = get_room_module_stack_href(parent, REPO_ROOT / str(next_target))
                register_sequence_card(
                    "Next Step",
                    str(next_title),
                    str(next_copy),
                    str(next_context["href"]),
                    str(next_cta),
                    f"Step {next_order} of {total_steps:02d}",
                    "module-sequence-next",
                    sequence_summary_label(2, "03 Next"),
                    list(next_context["meta_items"]),
                    str(next_context["route_note"]),
                    stack_href=next_stack_href,
                    stack_cta="Jump to Stack Module" if next_stack_href else None,
                )
            else:
                register_sequence_card(
                    "Room Outcomes",
                    f"Return to {room_short}",
                    "This module sits at the end of the room decision sequence. Return to the room outcomes when the founder needs to choose the next advance, hold, or escalate path.",
                    f"{relative_url(directory, parent / 'OPEN-HERE.html')}#outcome-paths",
                    f"Open {room_short} Outcomes",
                    f"Step {total_steps:02d} of {total_steps:02d}",
                    "module-sequence-outcomes",
                    sequence_summary_label(2, "03 Room Outcomes"),
                    [("Outcome Paths", "meta-pill"), ("Route Choice", "meta-pill")],
                    "Stay inside the current room stack until the founder is ready to choose the next route.",
                )
            local_count = sum(1 for card in cards if not bool(card["external"]))
            external_count = sum(1 for card in cards if bool(card["external"]))
            summary_html = (
                '<div class="card-meta">'
                f'<span class="meta-pill">{html.escape(format_count_label(len(cards), "Sequence Stop"))}</span>'
                + (
                    f'<span class="meta-pill">{html.escape(format_count_label(local_count, "In-Room Link", "In-Room Links"))}</span>'
                    if local_count
                    else ""
                )
                + (
                    f'<span class="meta-pill">{html.escape(format_count_label(external_count, "External Transition"))}</span>'
                    if external_count
                    else ""
                )
                + "".join(
                    f'<a class="meta-pill meta-pill--link" href="#{html.escape(str(card["anchor_id"]), quote=True)}">{html.escape(str(card["summary_label"]))}</a>'
                    for card in cards
                )
                + "</div>"
            )
            return f"""
        <section class="home-section module-sequence-panel" id="module-sequence-context">
          <div class="section-heading">
            <p class="eyebrow">Module Sequence Context</p>
            <h2 class="section-title">See where this module sits inside {html.escape(room_title)}.</h2>
            <p class="section-copy">
              Use this sequence strip when the founder is already inside one control and needs the fastest step backward or forward in the actual room decision sequence.
            </p>
            {summary_html}
          </div>
          <div class="viewer-grid module-sequence-grid">
            {"".join(render_sequence_card(card) for card in cards)}
          </div>
        </section>
"""

    if current_index > 0:
        previous_dir = ordered_children[current_index - 1]
        previous_profile = build_folder_card_profile(parent, previous_dir)
        if previous_profile:
            register_sequence_card(
                "Previous",
                str(previous_profile["title"]),
                str(previous_profile["copy"]),
                relative_url(directory, previous_dir / "OPEN-HERE.html"),
                str(previous_profile["cta"]),
                f"Step {current_index} of {total}",
                "module-sequence-previous",
                sequence_summary_label(0, "01 Previous"),
                stack_href=f"#{get_stack_module_anchor_id(previous_dir)}",
                stack_cta="Jump to Stack Module",
            )
    else:
        register_sequence_card(
            "Room Entry",
            room_title,
            "This module sits at the start of the curated case sequence. Return to the room brief when the founder needs the full room framing before moving deeper.",
            get_room_entry_href(directory, parent),
            get_room_entry_label(parent, "Open Room Brief", "Open Room Entry"),
            f"Step 1 of {total}",
            "module-sequence-entry",
            sequence_summary_label(0, "01 Entry Brief"),
        )

    register_sequence_card(
        "Current",
        str(current_profile["title"]),
        "This is the active module in the curated room sequence. Use the cards around it to move one layer backward or forward without losing the case answer.",
        relative_url(directory, directory / "OPEN-HERE.html"),
        current_sequence_label(),
        f"Step {current_index + 1} of {total}",
        "module-sequence-current",
        sequence_summary_label(1, "02 Current"),
        current=True,
        stack_href=f"#{get_stack_module_anchor_id(directory)}",
        stack_cta="Jump to Stack Module",
    )

    if current_index + 1 < total:
        next_dir = ordered_children[current_index + 1]
        next_profile = build_folder_card_profile(parent, next_dir)
        if next_profile:
            register_sequence_card(
                "Next",
                str(next_profile["title"]),
                str(next_profile["copy"]),
                relative_url(directory, next_dir / "OPEN-HERE.html"),
                str(next_profile["cta"]),
                f"Step {current_index + 2} of {total}",
                "module-sequence-next",
                sequence_summary_label(2, "03 Next"),
                stack_href=f"#{get_stack_module_anchor_id(next_dir)}",
                stack_cta="Jump to Stack Module",
            )
    else:
        register_sequence_card(
            "Room Outcomes",
            f"Return to {room_short}",
            "This module sits at the far end of the curated sequence. Return to the room outcomes when the founder needs to choose the right advance, hold, or escalate path.",
            f"{relative_url(directory, parent / 'OPEN-HERE.html')}#outcome-paths",
            f"Open {room_short} Outcomes",
            f"Step {total} of {total}",
            "module-sequence-outcomes",
            sequence_summary_label(2, "03 Room Outcomes"),
        )

    local_count = sum(1 for card in cards if not bool(card["external"]))
    external_count = sum(1 for card in cards if bool(card["external"]))
    summary_html = (
        '<div class="card-meta">'
        f'<span class="meta-pill">{html.escape(format_count_label(len(cards), "Sequence Stop"))}</span>'
        + (
            f'<span class="meta-pill">{html.escape(format_count_label(local_count, "In-Room Link", "In-Room Links"))}</span>'
            if local_count
            else ""
        )
        + (
            f'<span class="meta-pill">{html.escape(format_count_label(external_count, "External Transition"))}</span>'
            if external_count
            else ""
        )
        + "".join(
            f'<a class="meta-pill meta-pill--link" href="#{html.escape(str(card["anchor_id"]), quote=True)}">{html.escape(str(card["summary_label"]))}</a>'
            for card in cards
        )
        + "</div>"
    )

    return f"""
        <section class="home-section module-sequence-panel" id="module-sequence-context">
          <div class="section-heading">
            <p class="eyebrow">Module Sequence Context</p>
            <h2 class="section-title">See where this module sits inside {html.escape(room_title)}.</h2>
            <p class="section-copy">
              Use this sequence strip when the founder is already inside one control and needs the fastest step backward or forward in the same case stack.
            </p>
            {summary_html}
          </div>
          <div class="viewer-grid module-sequence-grid">
            {"".join(render_sequence_card(card) for card in cards)}
          </div>
        </section>
"""


def get_module_sequence_jump_links(directory: Path) -> dict[str, object] | None:
    parent = directory.parent
    if parent == REPO_ROOT:
        return None
    try:
        parent.relative_to(REPO_ROOT)
    except ValueError:
        return None

    ordered_children = [
        child
        for child in order_child_directories(
            parent,
            [path for path in parent.iterdir() if path.is_dir() and path.name not in SKIP_DIR_NAMES],
        )
        if build_folder_card_profile(parent, child)
    ]
    if not ordered_children or directory not in ordered_children:
        return None
    current_profile = build_folder_card_profile(parent, directory)
    current_nav_label = "Current"

    previous_label = "Prev"
    previous_href = "#module-sequence-previous"
    next_label = "Next"
    next_href = "#module-sequence-next"
    previous_action_label = "Open Prev"
    current_action_label = "Open Current Step"
    next_action_label = "Open Next"
    previous_action_href = get_room_entry_href(directory, parent)
    next_action_href = next_href
    previous_nav_label = previous_label
    next_nav_label = next_label

    relative_parent = parent.relative_to(REPO_ROOT).as_posix()
    sequence_profile = get_decision_sequence_profile(relative_parent)
    current_target_path = directory / "OPEN-HERE.html"
    if sequence_profile:
        sequence_steps = list(sequence_profile["steps"])
        current_sequence_index = next(
            (
                index
                for index, (_order, _title, _copy, _cta, target) in enumerate(sequence_steps)
                if REPO_ROOT / str(target) == current_target_path
            ),
            None,
        )
        if current_sequence_index is not None:
            total_steps = len(sequence_steps)
            current_order = str(sequence_steps[current_sequence_index][0]).zfill(2)
            next_scope_label = "In Room"
            note = "The next move stays inside the current room stack."
            _current_order, current_title, _current_copy, current_cta, _current_target = sequence_steps[current_sequence_index]
            current_action_label = str(current_cta) if str(current_cta).strip() else "Open Current Step"
            current_nav_label = current_action_label.replace("Open ", "", 1).strip()
            if current_sequence_index == 0:
                previous_label = "Entry"
                previous_href = "#module-sequence-entry"
                previous_action_label = get_room_entry_label(parent, "Open Entry Brief", "Open Room Entry")
                previous_nav_label = "Entry"
                previous_action_href = get_room_entry_href(directory, parent)
            else:
                _prev_order, _prev_title, _prev_copy, prev_cta, prev_target = sequence_steps[current_sequence_index - 1]
                prev_context = get_sequence_step_target_context(parent, directory, str(prev_target))
                previous_action_label = str(prev_cta) if str(prev_cta).strip() else "Open Prev"
                previous_nav_label = previous_action_label.replace("Open ", "", 1).strip()
                previous_action_href = str(prev_context["href"])
            if current_sequence_index + 1 >= len(sequence_steps):
                next_label = "Outcomes"
                next_href = "#module-sequence-outcomes"
                next_scope_label = "Outcomes"
                note = "This module closes the room sequence before the founder chooses the next room outcome."
                next_action_label = "Open Room Outcomes"
                next_nav_label = "Room Outcomes"
                next_action_href = f"{relative_url(directory, parent / 'OPEN-HERE.html')}#outcome-paths"
            else:
                _next_order, next_title, _next_copy, next_cta, next_target = sequence_steps[current_sequence_index + 1]
                next_context = get_sequence_step_target_context(parent, directory, str(next_target))
                next_action_label = str(next_cta) if str(next_cta).strip() else "Open Next"
                next_nav_label = next_action_label.replace("Open ", "", 1).strip()
                next_action_href = str(next_context["href"])
                if any(label == "External Control" for label, _style in list(next_context["meta_items"])):
                    next_scope_label = "External"
                    note = f"The next move exits this room through {str(next_title)}."
                else:
                    next_scope_label = "In Room"
                    note = f"The next move stays in room through {str(next_title)}."
            return {
                "nav_links": [
                    (previous_nav_label, previous_href),
                    (current_nav_label, "#module-sequence-current"),
                    (next_nav_label, next_href),
                ],
                "full_links": [
                    (previous_action_label, previous_href),
                    (current_action_label, "#module-sequence-current"),
                    (next_action_label, next_href),
                ],
                "position_value": f"{current_order} of {total_steps:02d}",
                "position_pill": f"Step {current_order}/{total_steps:02d}",
                "next_pill": f"Next {next_scope_label}",
                "note": note,
                "previous_action": (previous_action_label, previous_action_href),
                "next_action": (next_action_label, next_action_href),
            }

    current_index = ordered_children.index(directory)
    total = len(ordered_children)
    if current_profile and current_profile.get("cta"):
        current_action_label = f"Current {str(current_profile['pill']).replace(' Module', '')}".strip()
        current_nav_label = current_action_label
    if current_index == 0:
        previous_label = "Entry"
        previous_href = "#module-sequence-entry"
        previous_action_label = get_room_entry_label(parent, "Open Entry Brief", "Open Room Entry")
        previous_nav_label = "Entry"
        previous_action_href = get_room_entry_href(directory, parent)
    else:
        previous_profile = build_folder_card_profile(parent, ordered_children[current_index - 1])
        previous_action_label = str(previous_profile["cta"]) if previous_profile else "Open Prev"
        previous_nav_label = previous_action_label.replace("Open ", "", 1).strip()
        previous_action_href = relative_url(directory, ordered_children[current_index - 1] / "OPEN-HERE.html")
    if current_index + 1 >= len(ordered_children):
        next_label = "Outcomes"
        next_href = "#module-sequence-outcomes"
        next_action_label = "Open Room Outcomes"
        next_nav_label = "Room Outcomes"
        next_action_href = f"{relative_url(directory, parent / 'OPEN-HERE.html')}#outcome-paths"
    else:
        next_profile = build_folder_card_profile(parent, ordered_children[current_index + 1])
        next_action_label = str(next_profile["cta"]) if next_profile else "Open Next"
        next_nav_label = next_action_label.replace("Open ", "", 1).strip()
        next_action_href = relative_url(directory, ordered_children[current_index + 1] / "OPEN-HERE.html")

    note = (
        "This module closes the curated room sequence before the founder returns to room outcomes."
        if next_label == "Outcomes"
        else "The next move stays inside the current room stack."
    )

    return {
        "nav_links": [
            (previous_nav_label, previous_href),
            (current_nav_label, "#module-sequence-current"),
            (next_nav_label, next_href),
        ],
        "full_links": [
            (previous_action_label, previous_href),
            (current_action_label, "#module-sequence-current"),
            (next_action_label, next_href),
        ],
        "position_value": f"{current_index + 1:02d} of {total:02d}",
        "position_pill": f"Step {current_index + 1:02d}/{total:02d}",
        "next_pill": f"Next {'Outcomes' if next_label == 'Outcomes' else 'In Room'}",
        "note": note,
        "previous_action": (previous_action_label, previous_action_href),
        "next_action": (next_action_label, next_action_href),
    }


def build_module_decision_support_section(directory: Path) -> str:
    parent = directory.parent
    if parent == REPO_ROOT:
        return ""
    try:
        parent.relative_to(REPO_ROOT)
    except ValueError:
        return ""

    room_profile = build_portal_hero_context(parent)
    current_profile = build_folder_card_profile(parent, directory)
    if not room_profile or not current_profile:
        return ""

    links = collect_decision_support_links(parent, resolve_dir=directory)
    if not links:
        return ""

    cards = []
    for link in links:
        cards.append(
            "<a class=\"brief-support-card\" "
            f"href=\"{html.escape(link['href'], quote=True)}\">"
            f"<span class=\"brief-support-pill\">{html.escape(link['pill'])}</span>"
            f"<span class=\"brief-support-title\">{html.escape(link['title'])}</span>"
            f"<span class=\"brief-support-copy\">{html.escape(link['copy'])}</span>"
            f"<span class=\"brief-support-cta\">{html.escape(link['cta'])}</span>"
            "</a>"
        )

    room_title = str(room_profile["title"])
    module_title = str(current_profile["title"])
    return (
        '<section class="brief-support-panel" id="module-decision-support">'
        "<div class=\"brief-support-head\">"
        "<p class=\"eyebrow\">Module Decision Support</p>"
        f"<h2 class=\"section-title-sm\">Open the executive boards that usually confirm or widen the answer behind {html.escape(module_title)}.</h2>"
        f"<p class=\"section-copy\">Use these links when the founder needs to step out of {html.escape(room_title)}'s module layer and validate the same decision in the broader executive dashboard spine.</p>"
        "</div>"
        f"<div class=\"brief-support-grid\">{''.join(cards)}</div>"
        "</section>"
    )


def build_module_escalation_watch_section(directory: Path) -> str:
    parent = directory.parent
    if parent == REPO_ROOT:
        return ""
    try:
        parent.relative_to(REPO_ROOT)
    except ValueError:
        return ""

    room_profile = build_portal_hero_context(parent)
    current_profile = build_folder_card_profile(parent, directory)
    brief_path = parent / "README.md"
    if not room_profile or not current_profile or not brief_path.exists():
        return ""

    _title, _subtitle, _meta, body_lines = extract_document_parts(
        brief_path.read_text(encoding="utf-8"),
        humanize_slug(brief_path.stem),
    )
    triggers = extract_section_list_items(body_lines, "Escalation Triggers")
    if not triggers:
        return ""

    cards: list[str] = []
    summary_pills: list[tuple[str, str]] = []
    for index, trigger in enumerate(triggers, start=1):
        anchor_id = f"module-escalation-trigger-{index:02d}"
        summary_pills.append((get_escalation_trigger_pill_label(trigger, index), f"#{anchor_id}"))
        cards.append(
            "<article class=\"escalation-watch-card\" "
            f"id=\"{html.escape(anchor_id, quote=True)}\">"
            f"<span class=\"escalation-watch-pill\">Escalate {index:02d}</span>"
            f"<p class=\"escalation-watch-copy\">{render_inline(trigger, directory)}</p>"
            "</article>"
        )
    summary_html = (
        '<div class="card-meta">'
        f'<span class="meta-pill">{html.escape(format_count_label(len(triggers), "Escalation Trigger"))}</span>'
        + "".join(
            f'<a class="meta-pill meta-pill--link" href="{html.escape(target, quote=True)}">{html.escape(label)}</a>'
            for label, target in summary_pills
        )
        + "</div>"
    )

    room_title = str(room_profile["title"])
    module_title = str(current_profile["title"])
    return f"""
        <section class="home-section escalation-watch-panel" id="module-escalation-watch">
          <div class="section-heading">
            <p class="eyebrow">Module Escalation Watch</p>
            <h2 class="section-title">Keep the room-level escalation triggers visible while reading {html.escape(module_title)}.</h2>
            <p class="section-copy">
              These triggers are inherited from {html.escape(room_title)} so the founder can see what breaks the normal case answer without leaving the current module.
            </p>
            {summary_html}
          </div>
          <div class="escalation-watch-grid">
            {"".join(cards)}
          </div>
        </section>
"""


def build_portal_room_navigation(directory: Path, has_folder_section: bool, has_docs_section: bool, has_escalation_watch: bool) -> str:
    relative = directory.relative_to(REPO_ROOT).as_posix()
    supported_rooms = {
        "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution",
        "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic",
        "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA",
        TRACEABILITY_ROOM_RELATIVE,
        "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim",
        "04_compliance/05_inspections/INSP-2026-001_FDA-Readiness-Review",
        "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce",
    }
    if relative not in supported_rooms:
        return ""

    sequence_local, sequence_external = get_decision_sequence_scope_counts(directory)
    local_outcomes, external_outcomes = get_outcome_path_scope_counts(directory)
    start_links = [
        ("Top", "#room-top", "top"),
        ("Start Here", "#founder-start-here", ""),
    ]
    decision_links = [
        ("Sequence", "#decision-sequence", ""),
    ]
    if sequence_local and sequence_external:
        decision_links.append(("Seq In", "#decision-sequence-in-room", ""))
        decision_links.append(("Seq Out", "#decision-sequence-external", ""))
    decision_links.append(("Routes", "#featured-routes", ""))
    outcome_links = [
        ("Outcomes", "#outcome-paths", ""),
    ]
    if local_outcomes and external_outcomes:
        outcome_links.append(("In-Room", "#outcome-room-paths", ""))
        outcome_links.append(("External", "#outcome-external-controls", ""))
    sequence_summary_override = get_scope_summary_override(directory, "sequence")
    outcome_summary_override = get_scope_summary_override(directory, "outcomes")
    oversight_links: list[tuple[str, str, str]] = []
    if has_escalation_watch:
        oversight_links.append(("Watch", "#escalation-watch", ""))
    module_surface_links: list[tuple[str, str, str]] = []
    if has_folder_section:
        module_surface_links.append(("Modules", "#room-modules", ""))
    path_surface_links: list[tuple[str, str, str]] = []
    if bool(get_outcome_paths_profile(relative)) and has_folder_section:
        path_surface_links.append(("Live Path", "#room-live-path-modules", ""))
        path_surface_links.append(("Controls", "#room-supporting-controls", ""))
    active_deal_room_return = get_active_deal_room_return_context(directory)
    active_shipment_room_return = get_active_shipment_room_return_context(directory)
    active_account_room_return = get_active_account_room_return_context(directory)
    active_claim_room_return = get_active_claim_room_return_context(directory)
    fda_readiness_room_return = get_fda_readiness_room_return_context(directory)
    supplier_approval_room_return = get_supplier_approval_room_return_context(directory)
    lead_room_return = relative == LEAD_ROOM_RELATIVE
    supplier_room_return = relative == SUPPLIER_ROOM_RELATIVE
    task_room_return = relative == TASK_ROOM_RELATIVE
    traceability_room_return = relative == TRACEABILITY_ROOM_RELATIVE
    system_surface_links: list[tuple[str, str, str]] = []
    if active_deal_room_return:
        system_surface_links.extend(
            [
                ("Deal Brief", str(active_deal_room_return["brief_href"]), ""),
                ("Active Deals", str(active_deal_room_return["lane_href"]), ""),
                ("Deals", str(active_deal_room_return["hub_href"]), ""),
                ("Preview Docs", str(active_deal_room_return["preview_href"]), ""),
            ]
        )
    elif active_shipment_room_return:
        system_surface_links.extend(
            [
                ("Shipment Brief", str(active_shipment_room_return["brief_href"]), ""),
                ("Active Shipments", str(active_shipment_room_return["lane_href"]), ""),
                ("Shipments", str(active_shipment_room_return["hub_href"]), ""),
                ("Shipment Control Tower", str(active_shipment_room_return["board_href"]), ""),
            ]
        )
    elif active_account_room_return:
        system_surface_links.extend(
            [
                ("Account Brief", str(active_account_room_return["brief_href"]), ""),
                ("Customers", str(active_account_room_return["lane_href"]), ""),
                ("CRM", str(active_account_room_return["hub_href"]), ""),
                ("Customer Board", str(active_account_room_return["board_href"]), ""),
            ]
        )
    elif active_claim_room_return:
        system_surface_links.extend(
            [
                ("Claim Brief", str(active_claim_room_return["brief_href"]), ""),
                ("Inspection Cases", str(active_claim_room_return["lane_href"]), ""),
                ("Compliance", str(active_claim_room_return["hub_href"]), ""),
                ("Claims Recovery", str(active_claim_room_return["board_href"]), ""),
            ]
        )
    elif fda_readiness_room_return:
        system_surface_links.extend(
            [
                ("Readiness Brief", str(fda_readiness_room_return["brief_href"]), ""),
                ("Inspection Cases", str(fda_readiness_room_return["lane_href"]), ""),
                ("Compliance", str(fda_readiness_room_return["hub_href"]), ""),
                ("Compliance Control", str(fda_readiness_room_return["board_href"]), ""),
            ]
        )
    elif supplier_approval_room_return:
        system_surface_links.extend(
            [
                ("Supplier Brief", str(supplier_approval_room_return["brief_href"]), ""),
                ("Supplier Approval", str(supplier_approval_room_return["lane_href"]), ""),
                ("Compliance", str(supplier_approval_room_return["hub_href"]), ""),
                ("Supplier Performance", str(supplier_approval_room_return["board_href"]), ""),
                ("Supply Resilience", str(supplier_approval_room_return["resilience_href"]), ""),
            ]
        )
    elif lead_room_return:
        system_surface_links.extend(
            [
                ("Lead Brief", "README.html", ""),
                ("Leads", relative_url(directory, REPO_ROOT / LEADS_RELATIVE / "OPEN-HERE.html"), ""),
                ("CRM", relative_url(directory, REPO_ROOT / "02_crm/OPEN-HERE.html"), ""),
                ("Sales Pipeline", relative_url(directory, REPO_ROOT / SALES_PIPELINE_BOARD_RELATIVE), ""),
                ("Founder Queue", relative_url(directory, REPO_ROOT / TASK_ROOM_RELATIVE / "OPEN-HERE.html"), ""),
            ]
        )
    elif supplier_room_return:
        system_surface_links.extend(
            [
                ("Supplier Brief", "README.html", ""),
                ("Suppliers", relative_url(directory, REPO_ROOT / SUPPLIERS_RELATIVE / "OPEN-HERE.html"), ""),
                ("CRM", relative_url(directory, REPO_ROOT / "02_crm/OPEN-HERE.html"), ""),
                ("Supplier Approval", relative_url(directory, REPO_ROOT / SUPPLIER_APPROVAL_RELATIVE / "OPEN-HERE.html"), ""),
                ("Supplier Performance", relative_url(directory, REPO_ROOT / SUPPLIER_PERFORMANCE_BOARD_RELATIVE), ""),
            ]
        )
    elif task_room_return:
        system_surface_links.extend(
            [
                ("Execution Brief", "README.html", ""),
                ("Tasks", relative_url(directory, REPO_ROOT / TASKS_RELATIVE / "OPEN-HERE.html"), ""),
                ("CRM", relative_url(directory, REPO_ROOT / "02_crm/OPEN-HERE.html"), ""),
                ("Executable Checks", relative_url(directory, REPO_ROOT / EXECUTABLE_CHECKS_BOARD_RELATIVE), ""),
                ("Owner Accountability", relative_url(directory, REPO_ROOT / OWNER_ACCOUNTABILITY_BOARD_RELATIVE), ""),
            ]
        )
    elif traceability_room_return:
        system_surface_links.extend(
            [
                ("Traceability Brief", "README.html", ""),
                ("Traceability", relative_url(directory, REPO_ROOT / TRACEABILITY_RELATIVE / "OPEN-HERE.html"), ""),
                ("Compliance", relative_url(directory, REPO_ROOT / "04_compliance/OPEN-HERE.html"), ""),
                ("Compliance Control", relative_url(directory, REPO_ROOT / COMPLIANCE_CONTROL_CENTER_RELATIVE), ""),
                ("Claims Recovery", relative_url(directory, REPO_ROOT / CLAIMS_RECOVERY_BOARD_RELATIVE), ""),
            ]
        )
    else:
        if has_docs_section:
            system_surface_links.append(("Readable Layers", "#supporting-files", ""))
        system_surface_links.append(("Source Integrity", "#visual-system", ""))

    module_surface_summary = "Module Access" if has_folder_section else None
    path_surface_summary = "Live / Controls" if path_surface_links else None
    system_surface_summary = (
        "Brief / Lane / Hub / Preview"
        if active_deal_room_return
        else "Brief / Lane / Hub / Board"
        if active_shipment_room_return
        else "Brief / Lane / Hub / Board"
        if active_account_room_return
        else "Brief / Lane / Hub / Board"
        if active_claim_room_return
        else "Brief / Lane / Hub / Board"
        if fda_readiness_room_return
        else "Brief / Lane / Hub / Boards"
        if supplier_approval_room_return
        else "Brief / Lane / Hub / Boards"
        if lead_room_return or supplier_room_return or task_room_return or traceability_room_return
        else "Readable / Source"
        if has_docs_section
        else "Source Integrity"
    )

    group_html = build_room_nav_link_groups(
        [
            ("Start Layer", start_links, "room", "Read First"),
            ("Decision Flow", decision_links, "module", sequence_summary_override or format_scope_summary(sequence_local, sequence_external)),
            ("Outcome Layer", outcome_links, "controls", outcome_summary_override or format_scope_summary(local_outcomes, external_outcomes)),
            ("Oversight Layer", oversight_links, "support", "Escalation Watch" if has_escalation_watch else None),
            ("Module Surface", module_surface_links, "module-surface", module_surface_summary),
            ("Path Surface", path_surface_links, "path-surface", path_surface_summary),
            ("Return Layer" if active_deal_room_return or active_shipment_room_return or active_account_room_return or active_claim_room_return or fda_readiness_room_return or supplier_approval_room_return or lead_room_return or supplier_room_return or task_room_return or traceability_room_return else "Source Integrity", system_surface_links, "surface", system_surface_summary),
        ]
    )

    return f"""
        <section class="room-nav-panel" id="room-navigation">
          <div class="card-meta">
            <span class="meta-pill">Room Navigation</span>
            <span class="meta-pill">Founder Use</span>
          </div>
          {group_html}
        </section>
"""


def build_module_portal_navigation(
    directory: Path,
    has_folder_section: bool,
    has_docs_section: bool,
    has_module_snapshot: bool,
    has_module_sequence_context: bool,
    has_room_module_stack: bool,
    has_module_outcomes: bool,
    has_module_watch: bool,
    has_module_support: bool,
    has_module_related_rooms: bool,
) -> str:
    parent = directory.parent
    if parent == REPO_ROOT:
        return ""
    try:
        parent.relative_to(REPO_ROOT)
    except ValueError:
        return ""

    room_profile = build_portal_hero_context(parent)
    current_profile = build_folder_card_profile(parent, directory)
    if not room_profile or not current_profile:
        return ""

    shipment_stack_override = get_shipment_stack_navigation_override(directory)
    room_title = str(room_profile["title"])
    room_short = " ".join(room_title.split()[-2:])
    sequence_local, sequence_external = get_decision_sequence_scope_counts(parent)
    local_outcomes, external_outcomes = get_outcome_path_scope_counts(parent)
    sequence_jump_links = get_module_sequence_jump_links(directory)
    stack_jump_links = get_module_stack_jump_links(directory)
    room_entry_links = [
        ("Top", "#room-top", "top"),
        (room_short, relative_url(directory, parent / "OPEN-HERE.html"), ""),
        (get_room_entry_label(parent, "Brief", "Entry"), get_room_entry_href(directory, parent), ""),
    ]
    if shipment_stack_override and shipment_stack_override.get("room_entry_label") and shipment_stack_override.get("room_entry_href"):
        room_entry_links[-1] = (
            str(shipment_stack_override["room_entry_label"]),
            str(shipment_stack_override["room_entry_href"]),
            "",
        )
    room_sequence_label = "Room Sequence"
    room_sequence_summary = format_scope_summary(sequence_local, sequence_external)
    room_sequence_links = [
        ("Room Sequence", f"{relative_url(directory, parent / 'OPEN-HERE.html')}#decision-sequence", ""),
    ]
    if sequence_local and sequence_external:
        room_sequence_links.append(("Room Seq In", f"{relative_url(directory, parent / 'OPEN-HERE.html')}#decision-sequence-in-room", ""))
        room_sequence_links.append(("Room Seq Out", f"{relative_url(directory, parent / 'OPEN-HERE.html')}#decision-sequence-external", ""))
    if shipment_stack_override:
        room_sequence_label = str(shipment_stack_override["route_label"])
        room_sequence_summary = str(shipment_stack_override["route_summary"])
        room_sequence_links = list(shipment_stack_override["route_links_nav"])
    room_outcome_label = "Room Outcomes"
    room_outcome_summary = format_scope_summary(local_outcomes, external_outcomes)
    room_outcome_links = [
        ("Outcomes", f"{relative_url(directory, parent / 'OPEN-HERE.html')}#outcome-paths", ""),
    ]
    if local_outcomes and external_outcomes:
        room_outcome_links.append(("Room In", f"{relative_url(directory, parent / 'OPEN-HERE.html')}#outcome-room-paths", ""))
        room_outcome_links.append(("Room Out", f"{relative_url(directory, parent / 'OPEN-HERE.html')}#outcome-external-controls", ""))
    if shipment_stack_override:
        room_outcome_label = str(shipment_stack_override["outcome_label"])
        room_outcome_summary = str(shipment_stack_override["outcome_summary"])
        room_outcome_links = list(shipment_stack_override["outcome_links_nav"])
    module_links: list[tuple[str, str, str]] = []
    if has_module_snapshot:
        module_links.append(("Snapshot", "#module-brief-snapshot", ""))
    if has_module_sequence_context:
        module_links.append(("Sequence", "#module-sequence-context", ""))
        if sequence_jump_links:
            module_links.extend((label, href, "") for label, href in sequence_jump_links["nav_links"])
    stack_route_links: list[tuple[str, str, str]] = []
    stack_surface_links: list[tuple[str, str, str]] = []
    if has_room_module_stack:
        stack_route_links.append(("Stack", "#room-module-stack", ""))
        if stack_jump_links:
            stack_route_links.extend((label, href, "") for label, href in stack_jump_links["nav_links"])
        if bool(get_outcome_paths_profile(parent.relative_to(REPO_ROOT).as_posix())):
            stack_surface_links.append(("Live Path", "#stack-live-path-modules", ""))
            stack_surface_links.append(("Controls", "#stack-supporting-controls", ""))
    outcome_links: list[tuple[str, str, str]] = []
    if has_module_outcomes:
        outcome_links.append(("Paths", "#module-outcome-paths", ""))
        if local_outcomes and external_outcomes:
            outcome_links.append(("In-Room", "#module-outcome-room-paths", ""))
            outcome_links.append(("External", "#module-outcome-external-controls", ""))
    oversight_links: list[tuple[str, str, str]] = []
    if has_module_watch:
        oversight_links.append(("Watch", "#module-escalation-watch", ""))
    if has_module_support:
        oversight_links.append(("Support", "#module-decision-support", ""))
    if has_module_related_rooms:
        oversight_links.append(("Rooms", "#module-related-rooms", ""))
    active_deal_module = get_active_deal_module_context(directory)
    active_shipment_module = get_active_shipment_module_context(directory)
    active_account_module = get_active_account_module_context(directory)
    active_claim_module = get_active_claim_module_context(directory)
    supplier_approval_module = get_supplier_approval_module_context(directory)
    system_links: list[tuple[str, str, str]] = []
    if active_deal_module:
        system_links.extend(
            [
                ("Module Memo", str(active_deal_module["module_memo_href"]), ""),
                (strip_open_prefix(str(active_deal_module["room_entry_label"])), str(active_deal_module["room_entry_href"]), ""),
                ("Active Deals", str(active_deal_module["active_deals_href"]), ""),
                ("Deals", str(active_deal_module["deals_href"]), ""),
            ]
        )
    elif active_shipment_module:
        system_links.extend(
            [
                ("Module Memo", str(active_shipment_module["module_memo_href"]), ""),
                (strip_open_prefix(str(active_shipment_module["room_entry_label"])), str(active_shipment_module["room_entry_href"]), ""),
                ("Active Shipments", str(active_shipment_module["active_shipments_href"]), ""),
                ("Shipments", str(active_shipment_module["shipments_href"]), ""),
            ]
        )
    elif active_account_module:
        system_links.extend(
            [
                ("Module Memo", str(active_account_module["module_memo_href"]), ""),
                (strip_open_prefix(str(active_account_module["room_entry_label"])), str(active_account_module["room_entry_href"]), ""),
                ("Customers", str(active_account_module["customers_href"]), ""),
                ("CRM", str(active_account_module["crm_href"]), ""),
            ]
        )
    elif active_claim_module:
        system_links.extend(
            [
                ("Module Memo", str(active_claim_module["module_memo_href"]), ""),
                (strip_open_prefix(str(active_claim_module["room_entry_label"])), str(active_claim_module["room_entry_href"]), ""),
                ("Inspection Cases", str(active_claim_module["inspection_cases_href"]), ""),
                ("Compliance", str(active_claim_module["compliance_href"]), ""),
            ]
        )
    elif supplier_approval_module:
        system_links.extend(
            [
                ("Module Memo", str(supplier_approval_module["module_memo_href"]), ""),
                (strip_open_prefix(str(supplier_approval_module["room_entry_label"])), str(supplier_approval_module["room_entry_href"]), ""),
                ("Supplier Approval", str(supplier_approval_module["supplier_approval_href"]), ""),
                ("Compliance", str(supplier_approval_module["compliance_href"]), ""),
                (strip_open_prefix(str(supplier_approval_module["board_cta"])), str(supplier_approval_module["board_href"]), ""),
            ]
        )
    elif shipment_stack_override:
        system_links.extend(list(shipment_stack_override["return_links_nav"]))
    else:
        if has_docs_section:
            system_links.append(("Readable Layers", "#supporting-files", ""))
        system_links.append(("Source Integrity", "#visual-system", ""))

    route_posture = get_route_posture(sequence_local, sequence_external, local_outcomes, external_outcomes)
    module_position_summary = None
    if sequence_jump_links:
        module_position_summary = str(sequence_jump_links.get("position_pill") or "").strip() or None
    stack_summary = None
    if stack_jump_links:
        stack_count = len(stack_jump_links.get("nav_links", []))
        stack_summary = f"{stack_count} sequence stops" if stack_count else None
    stack_surface_summary = "Live / Controls" if stack_surface_links else None
    oversight_summary_parts: list[str] = []
    if has_module_watch:
        oversight_summary_parts.append("Watch")
    if has_module_support:
        oversight_summary_parts.append("Support")
    if has_module_related_rooms:
        oversight_summary_parts.append("Rooms")
    oversight_summary = " / ".join(oversight_summary_parts) if oversight_summary_parts else None
    active_module_return = (
        active_deal_module
        or active_shipment_module
        or active_account_module
        or active_claim_module
        or supplier_approval_module
    )
    if shipment_stack_override:
        system_label = str(shipment_stack_override["return_label"])
        system_summary = str(shipment_stack_override["return_summary"])
    else:
        system_label = "Return Layer" if active_module_return else "Source Integrity"
        system_summary = (
            "Memo / Room / Lane / Board"
            if supplier_approval_module
            else "Memo / Room / Lane / Hub"
            if active_module_return
            else "Readable / Source"
            if has_docs_section
            else "Source Integrity"
        )

    group_html = build_room_nav_link_groups(
        [
            ("Room Entry", room_entry_links, "room", "Room Access"),
            (room_sequence_label, room_sequence_links, "module", room_sequence_summary),
            (room_outcome_label, room_outcome_links, "route", room_outcome_summary),
            ("Module Flow", module_links, "module", module_position_summary),
            ("Stack Route", stack_route_links, "stack", stack_summary),
            ("Stack Surface", stack_surface_links, "path-surface", stack_surface_summary),
            ("Outcome Layer", outcome_links, "controls", format_scope_summary(local_outcomes, external_outcomes) if has_module_outcomes else None),
            ("Oversight Layer", oversight_links, "support", oversight_summary),
            (system_label, system_links, "surface", system_summary),
        ]
    )

    return f"""
        <section class="room-nav-panel" id="module-navigation">
          <div class="card-meta">
            <span class="meta-pill">{html.escape(str(shipment_stack_override["panel_label"])) if shipment_stack_override else "Module Navigation"}</span>
            <span class="meta-pill">{html.escape(str(current_profile["pill"]))}</span>
          </div>
          {group_html}
        </section>
"""


def build_route_card(current_dir: Path, pill_a: str, pill_b: str, title: str, copy: str, links: list[tuple[str, str]]) -> str:
    link_html = []
    for label, target in links:
        href = relative_url(current_dir, REPO_ROOT / target)
        link_html.append(f'<a class="button-secondary" href="{href}">{html.escape(label)}</a>')
    return f"""
          <article class="route-card">
            <div class="card-meta">
              <span class="meta-pill">{html.escape(pill_a)}</span>
              <span class="meta-pill">{html.escape(pill_b)}</span>
            </div>
            <h3 class="card-title">{html.escape(title)}</h3>
            <p class="card-copy">{html.escape(copy)}</p>
            <div class="route-links">
              {"".join(link_html)}
            </div>
          </article>
"""


def build_area_routes_section(directory: Path) -> str:
    relative = directory.relative_to(REPO_ROOT).as_posix()

    if relative == "01_templates":
        cards = [
            build_route_card(
                directory,
                "Templates",
                "Contained",
                "Contained Movement Template Stack",
                "Open the source templates that now carry movement posture, stop rules, next safe movement, and send-ready outward language for constrained matters.",
                [
                    ("Proforma", "01_templates/01_sales/Proforma-Invoice-MASTER.html"),
                    ("Purchase Order", "01_templates/02_purchasing/Purchase-Order-MASTER.html"),
                    ("Shipping Instructions", "01_templates/03_logistics/Shipping-Instructions-MASTER.html"),
                    ("Sales Contract", "01_templates/04_legal/Sales-Contract-MASTER.html"),
                ],
            ),
            build_route_card(
                directory,
                "External",
                "Release",
                "Institutional Outbound Pack",
                "Use this route when the founder wants to inspect the master packet layer that governs transmittal, correspondence, packet indexing, and release approval before anything leaves UNYRA.",
                [
                    ("Transmittal", "01_templates/11_external-communications/Official-Document-Transmittal-MASTER.html"),
                    ("Correspondence", "01_templates/11_external-communications/Institutional-Trade-Correspondence-MASTER.html"),
                    ("Packet Index", "01_templates/11_external-communications/Counterparty-Document-Packet-Index-MASTER.html"),
                    ("Release Checklist", "01_templates/11_external-communications/External-Communication-Release-Checklist-MASTER.html"),
                ],
            ),
            build_route_card(
                directory,
                "Governance",
                "Founder",
                "Founder Control Templates",
                "Open the master governance layer for decision routing, control integrity, executable checks, and founder exceptions when a matter needs executive discipline before movement widens.",
                [
                    ("Matter Control", "01_templates/10_governance/Matter-Control-Index-MASTER.html"),
                    ("Control Integrity", "01_templates/10_governance/Executive-Control-Integrity-and-Decision-Readiness-Review-MASTER.html"),
                    ("Executable Check Board", "01_templates/10_governance/Trust-Override-Executable-Check-Control-Board-MASTER.html"),
                    ("Exceptions Review", "01_templates/10_governance/Executive-Exceptions-and-Override-Review-MASTER.html"),
                ],
            ),
        ]
        title = "Template Fast Routes"
        copy = "Start with the template stack that matches the decision instead of browsing the full template tree first."
    elif relative == "02_crm/02_customers":
        cards = [
            build_route_card(
                directory,
                "Customers",
                "Trust",
                "Relationship Trust Stack",
                "Use this route when the founder wants to judge whether a customer account is institutionally strong enough to support more release, more urgency, and more commercial dependence.",
                [
                    ("Atlantic Foods Account Room", "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/OPEN-HERE.html"),
                    ("Customer Accounts", "06_dashboard/08_customer-accounts/Customer-Account-Review-Board.html"),
                    ("Trust Review", "06_dashboard/38_counterparty-trust/Strategic-Counterparty-Trust-and-Response-Review.html"),
                    ("Trust Matrix", "06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.html"),
                ],
            ),
            build_route_card(
                directory,
                "Customers",
                "Exposure",
                "Credit and Collections Stack",
                "Open this route when the founder needs one clean customer path from collections pressure to credit posture and release consequence.",
                [
                    ("Credit Control", "06_dashboard/09_credit-risk/Credit-and-Release-Control-Board.html"),
                    ("Collections Control", "06_dashboard/06_collections/Daily-Collections-Control-Center.html"),
                    ("Cash Forecast", "06_dashboard/19_cash-forecast/Cash-Forecast-and-Exposure-Outlook.html"),
                    ("Capital Allocation", "06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.html"),
                ],
            ),
            build_route_card(
                directory,
                "Customers",
                "Growth",
                "Revenue and Concentration Stack",
                "Start here when the founder wants to decide whether customer growth is still healthy once forecast quality, account concentration, and release confidence are viewed together.",
                [
                    ("Revenue Forecast", "06_dashboard/23_revenue-forecast/Revenue-Forecast-and-Commitments-Review.html"),
                    ("Concentration Review", "06_dashboard/20_concentration-risk/Portfolio-Concentration-Review.html"),
                    ("Quarterly Plan", "06_dashboard/22_quarterly-operating-plan/Quarterly-Operating-Plan.html"),
                    ("Monthly Review", "06_dashboard/15_monthly-strategic-review/Monthly-Strategic-Business-Review.html"),
                ],
            ),
        ]
        title = "Customer Fast Routes"
        copy = "Use these grouped routes when a customer issue is already real and the founder needs account, exposure, and growth posture without drilling through the whole CRM tree."
    elif relative == "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution":
        cards = [
            build_route_card(
                directory,
                "Atlantic Foods",
                "Trust",
                "Trust and Release War Room",
                "Use this route when the founder wants the live Atlantic Foods answer on trust quality, release posture, and whether the relationship still supports wider movement.",
                [
                    ("Trust Review", "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CTRUST-2026-Q2_AtlanticFoods-Relationship-Trust-Review/OPEN-HERE.html"),
                    ("Trust Posture", "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/TPST-2026-Q2_AtlanticFoods-Trust-Posture/OPEN-HERE.html"),
                    ("Credit Control", "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/OPEN-HERE.html"),
                    ("Customer Board", "06_dashboard/08_customer-accounts/Customer-Account-Review-Board.html"),
                ],
            ),
            build_route_card(
                directory,
                "Atlantic Foods",
                "Cash",
                "Cash and Collections War Room",
                "Open this route when the founder needs the same customer read through collections timing, cash exposure, and concentration pressure.",
                [
                    ("Receivable", "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/COLLECT-2026-001_April-Receivable/OPEN-HERE.html"),
                    ("Cash Outlook", "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CASH-2026-005_AtlanticFoods-Cash-Outlook/OPEN-HERE.html"),
                    ("Account Review", "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/ACCT-2026-Q2_AtlanticFoods-Account-Review/OPEN-HERE.html"),
                    ("Concentration Review", "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CONC-2026-Q2_AtlanticFoods-Revenue-Concentration/OPEN-HERE.html"),
                ],
            ),
            build_route_card(
                directory,
                "Atlantic Foods",
                "Growth",
                "Growth and Commitment War Room",
                "Start here when the founder wants to decide whether Atlantic Foods should receive more commercial weight in forecast, quarter planning, and capital priority.",
                [
                    ("Revenue Forecast", "06_dashboard/23_revenue-forecast/Revenue-Forecast-and-Commitments-Review.html"),
                    ("Quarterly Plan", "06_dashboard/22_quarterly-operating-plan/Quarterly-Operating-Plan.html"),
                    ("Capital Allocation", "06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.html"),
                    ("Monthly Review", "06_dashboard/15_monthly-strategic-review/Monthly-Strategic-Business-Review.html"),
                ],
            ),
        ]
        title = "Atlantic Foods Fast Routes"
        copy = "Use these curated war rooms when the founder is already inside the Atlantic Foods account and needs the right reading immediately."
    elif relative == LEADS_RELATIVE:
        cards = [
            build_route_card(
                directory,
                "Leads",
                "Qualify",
                "Qualification Route",
                "Open this route when the founder wants the shortest path from live lead posture into qualification priority and explicit next-step ownership.",
                [
                    ("Lead Room", LEAD_ROOM_RELATIVE + "/OPEN-HERE.html"),
                    ("Lead Brief", LEAD_ROOM_RELATIVE + "/README.html"),
                    ("Sales Pipeline", SALES_PIPELINE_BOARD_RELATIVE),
                    ("Founder Queue", TASK_ROOM_RELATIVE + "/OPEN-HERE.html"),
                ],
            ),
            build_route_card(
                directory,
                "Leads",
                "Advance",
                "Advancement Route",
                "Use this route when the founder wants to judge whether a qualified prospect should now advance into live commercial posture rather than stay in intake.",
                [
                    ("Lead Room", LEAD_ROOM_RELATIVE + "/OPEN-HERE.html"),
                    ("Active Deals", ACTIVE_DEALS_RELATIVE + "/OPEN-HERE.html"),
                    ("Deals", DEALS_RELATIVE + "/OPEN-HERE.html"),
                    ("Founder Dashboard", "06_dashboard/01_executive/Daily-Founder-Dashboard.html"),
                ],
            ),
            build_route_card(
                directory,
                "Leads",
                "Escalate",
                "Response Route",
                "Start here when silence, drift, or weak counterparty behavior changes the prospect answer enough to require a formal escalation read instead of passive waiting.",
                [
                    ("Response Escalation", RESPONSE_ESCALATION_BOARD_RELATIVE),
                    ("Founder Queue", TASK_ROOM_RELATIVE + "/OPEN-HERE.html"),
                    ("Founder Decisions", "06_dashboard/13_founder-decisions/Executive-Decision-Board.html"),
                    ("CRM", "02_crm/OPEN-HERE.html"),
                ],
            ),
        ]
        title = "Lead Routes"
        copy = "Use these grouped routes when the founder already knows the prospect question and needs the shortest path into qualification, advancement, or escalation."
    elif relative == SUPPLIERS_RELATIVE:
        cards = [
            build_route_card(
                directory,
                "Suppliers",
                "Approve",
                "Approval Route",
                "Open this route when the founder wants the shortest path from current sourcing posture into governed supplier approval.",
                [
                    ("Supplier Room", SUPPLIER_ROOM_RELATIVE + "/OPEN-HERE.html"),
                    ("Supplier Brief", SUPPLIER_ROOM_RELATIVE + "/README.html"),
                    ("Supplier Approval", SUPPLIER_APPROVAL_RELATIVE + "/OPEN-HERE.html"),
                    ("Compliance Control", "06_dashboard/04_compliance/Daily-Compliance-Control-Center.html"),
                ],
            ),
            build_route_card(
                directory,
                "Suppliers",
                "Perform",
                "Performance Route",
                "Use this route when the founder needs the wider scorecard and watch-item read behind current supplier confidence.",
                [
                    ("Supplier Room", SUPPLIER_ROOM_RELATIVE + "/OPEN-HERE.html"),
                    ("Supplier Performance", SUPPLIER_PERFORMANCE_BOARD_RELATIVE),
                    ("Supplier Approval", SUPPLIER_APPROVAL_RELATIVE + "/OPEN-HERE.html"),
                    ("CRM", "02_crm/OPEN-HERE.html"),
                ],
            ),
            build_route_card(
                directory,
                "Suppliers",
                "Fortify",
                "Continuity Route",
                "Start here when the supplier answer now depends on fallback sourcing, concentration pressure, and founder-level continuity risk.",
                [
                    ("Supply Resilience", SUPPLY_RESILIENCE_BOARD_RELATIVE),
                    ("Concentration Review", "06_dashboard/20_concentration-risk/Portfolio-Concentration-Review.html"),
                    ("Executive Risk Register", "06_dashboard/18_executive-risk-register/Executive-Risk-Register.html"),
                    ("Supplier Approval", SUPPLIER_APPROVAL_RELATIVE + "/OPEN-HERE.html"),
                ],
            ),
        ]
        title = "Supplier Routes"
        copy = "Use these grouped routes when the founder already knows the sourcing question and needs the shortest path into approval, performance, or continuity posture."
    elif relative == TASKS_RELATIVE:
        cards = [
            build_route_card(
                directory,
                "Tasks",
                "Close",
                "Gate Closure Route",
                "Open this route when the founder wants the shortest path from live task pressure into explicit executable-check closure.",
                [
                    ("Founder Queue", TASK_ROOM_RELATIVE + "/OPEN-HERE.html"),
                    ("Execution Brief", TASK_ROOM_RELATIVE + "/README.html"),
                    ("Executable Checks", EXECUTABLE_CHECKS_BOARD_RELATIVE),
                    ("Control Integrity", "06_dashboard/34_control-integrity/Executive-Control-Integrity-and-Decision-Readiness-Review.html"),
                ],
            ),
            build_route_card(
                directory,
                "Tasks",
                "Follow Through",
                "Follow-Through Route",
                "Use this route when the founder needs the wider accountability spine behind a still-open queue item.",
                [
                    ("Owner Accountability", OWNER_ACCOUNTABILITY_BOARD_RELATIVE),
                    ("Founder Decisions", "06_dashboard/13_founder-decisions/Executive-Decision-Board.html"),
                    ("Founder Dashboard", "06_dashboard/01_executive/Daily-Founder-Dashboard.html"),
                    ("CRM", "02_crm/OPEN-HERE.html"),
                ],
            ),
            build_route_card(
                directory,
                "Tasks",
                "Sync",
                "Commercial Sync Route",
                "Start here when task pressure now depends on keeping the linked commercial and execution lanes synchronized.",
                [
                    ("Active Deals", ACTIVE_DEALS_RELATIVE + "/OPEN-HERE.html"),
                    ("Operations Command", "06_dashboard/03_operations/Daily-Operations-Command-Center.html"),
                    ("CRM", "02_crm/OPEN-HERE.html"),
                    ("Founder Queue", TASK_ROOM_RELATIVE + "/OPEN-HERE.html"),
                ],
            ),
        ]
        title = "Execution Routes"
        copy = "Use these grouped routes when the founder already knows the queue question and needs the shortest path into gate closure, follow-through, or cross-lane synchronization."
    elif relative == TRACEABILITY_RELATIVE:
        cards = [
            build_route_card(
                directory,
                "Traceability",
                "Proof",
                "Lot Proof Route",
                "Open this route when the founder wants the shortest path from live lot-path proof into the room, the brief, and the compliance board that confirms whether the evidence is challenge-ready.",
                [
                    ("Traceability Room", f"{TRACEABILITY_ROOM_RELATIVE}/OPEN-HERE.html"),
                    ("Traceability Brief", f"{TRACEABILITY_ROOM_RELATIVE}/README.html"),
                    ("Compliance Control", COMPLIANCE_CONTROL_CENTER_RELATIVE),
                    ("Claims Recovery", CLAIMS_RECOVERY_BOARD_RELATIVE),
                ],
            ),
            build_route_card(
                directory,
                "Traceability",
                "Audit",
                "Audit Defense Route",
                "Use this route when the founder needs to pressure-test whether retrieval proof, control posture, and audit readiness still hold together under scrutiny.",
                [
                    ("Traceability Brief", f"{TRACEABILITY_ROOM_RELATIVE}/README.html"),
                    ("Compliance Control", COMPLIANCE_CONTROL_CENTER_RELATIVE),
                    ("Inspection Cases", f"{INSPECTIONS_RELATIVE}/OPEN-HERE.html"),
                    ("Compliance", "04_compliance/OPEN-HERE.html"),
                ],
            ),
            build_route_card(
                directory,
                "Traceability",
                "Recovery",
                "Recovery Consequence Route",
                "Start here when the proof answer now needs to widen into complaint consequence, recovery logic, or broader compliance escalation rather than staying only in the traceability lane.",
                [
                    ("Claims Recovery", CLAIMS_RECOVERY_BOARD_RELATIVE),
                    ("Complaint Case", f"{CLAIM_ROOM_RELATIVE}/OPEN-HERE.html"),
                    ("Compliance", "04_compliance/OPEN-HERE.html"),
                    ("Traceability Room", f"{TRACEABILITY_ROOM_RELATIVE}/OPEN-HERE.html"),
                ],
            ),
        ]
        title = "Traceability Routes"
        copy = "Use these grouped routes when the founder already knows the proof question and needs the shortest path into lot defense, audit posture, or recovery consequence."
    elif relative == "02_crm":
        cards = [
            build_route_card(
                directory,
                "CRM",
                "Customers",
                "Customer Trust and Credit Stack",
                "Open this route when the founder wants to judge whether a customer relationship can support more exposure, collections pressure, and release confidence without relying on gut feel.",
                [
                    ("Customer Accounts", "06_dashboard/08_customer-accounts/Customer-Account-Review-Board.html"),
                    ("Credit Control", "06_dashboard/09_credit-risk/Credit-and-Release-Control-Board.html"),
                    ("Trust Review", "06_dashboard/38_counterparty-trust/Strategic-Counterparty-Trust-and-Response-Review.html"),
                    ("Trust Matrix", "06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.html"),
                ],
            ),
            build_route_card(
                directory,
                "CRM",
                "Deals",
                "Active Deal and Communication Stack",
                "Use this route when the founder wants one clean path from active deal posture to forecast, outbound control, and response discipline before widening a commercial commitment.",
                [
                    ("Active Deals", "02_crm/04_deals/active/OPEN-HERE.html"),
                    ("Revenue Forecast", "06_dashboard/23_revenue-forecast/Revenue-Forecast-and-Commitments-Review.html"),
                    ("Communication Control", "06_dashboard/36_external-communications/Counterparty-Communication-Control-Board.html"),
                    ("Response Escalation", "06_dashboard/37_response-escalation/Counterparty-Response-SLA-and-Escalation-Board.html"),
                ],
            ),
            build_route_card(
                directory,
                "CRM",
                "Founder",
                "Founder Execution Queue",
                "Start here when the founder needs to convert deal pressure into explicit task ownership, executable checks, and matter control instead of chasing follow-up by memory.",
                [
                    ("Task Queue", "02_crm/05_tasks/TASK-2026-001_Founder-Execution-Queue/README.html"),
                    ("Owner Accountability", "06_dashboard/28_owner-accountability/Executive-Owner-Accountability-and-Follow-Through-Review.html"),
                    ("Matter Control", "06_dashboard/10_matter-control/Active-Matter-Control-Board.html"),
                    ("Executable Checks", "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html"),
                ],
            ),
        ]
        title = "CRM Fast Routes"
        copy = "Start with the CRM stack that matches the counterparty problem instead of browsing leads, customers, suppliers, deals, and tasks one folder at a time."
    elif relative == "02_crm/04_deals/active":
        cards = [
            build_route_card(
                directory,
                "Deals",
                "Control",
                "Deal Control Route",
                "Use this route when the founder wants the active deal control spine in one place, from matter control and executable checks to founder decision logic.",
                [
                    ("Atlantic Foods Deal", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/OPEN-HERE.html"),
                    ("Matter Control", "06_dashboard/10_matter-control/Active-Matter-Control-Board.html"),
                    ("Executable Checks", "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html"),
                    ("Decision Board", "06_dashboard/13_founder-decisions/Executive-Decision-Board.html"),
                ],
            ),
            build_route_card(
                directory,
                "Deals",
                "Commercial",
                "Commitment Route",
                "Open this route when the founder needs to test whether an active deal deserves more pricing confidence, revenue weight, or capital priority before widening commitment.",
                [
                    ("Pricing Governance", "06_dashboard/12_pricing-governance/Pricing-Governance-Board.html"),
                    ("Revenue Forecast", "06_dashboard/23_revenue-forecast/Revenue-Forecast-and-Commitments-Review.html"),
                    ("Capital Allocation", "06_dashboard/24_capital-allocation/Capital-Allocation-and-Release-Priority-Review.html"),
                    ("Plan Variance", "06_dashboard/27_plan-variance/Executive-Plan-Variance-and-Recovery-Review.html"),
                ],
            ),
            build_route_card(
                directory,
                "Deals",
                "Outbound",
                "Outbound Route",
                "Start here when the founder wants to move from active deal posture into send-ready communication without overpromising what the live gate still constrains.",
                [
                    ("Formal Offer Packet", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/OPEN-HERE.html"),
                    ("Communication Control", "06_dashboard/36_external-communications/Counterparty-Communication-Control-Board.html"),
                    ("Response Escalation", "06_dashboard/37_response-escalation/Counterparty-Response-SLA-and-Escalation-Board.html"),
                    ("Communication SOP", "05_sops/08_external-communications/Counterparty-Communication-Standard-SOP.html"),
                ],
            ),
        ]
        title = "Founder Deal Routes"
        copy = "Start with the founder route that matches the live deal question instead of opening the lane and scanning control, commitment, and outbound surfaces manually."
    elif relative == "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic":
        cards = [
            build_route_card(
                directory,
                "Atlantic Foods Deal",
                "Control",
                "Deal Control War Room",
                "Use this route when the founder wants the governing spine of the live deal in one place, from matter control to executable check closure.",
                [
                    ("Matter Control", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control/OPEN-HERE.html"),
                    ("Executable Check", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXECCHK-2026-001_AtlanticFoods-Override-Closure/OPEN-HERE.html"),
                    ("Founder Decisions", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/DEC-2026-001_AtlanticFoods-Founder-Decisions/OPEN-HERE.html"),
                    ("Exception Review", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/EXC-2026-Q2_AtlanticFoods-Exception-Review/OPEN-HERE.html"),
                ],
            ),
            build_route_card(
                directory,
                "Atlantic Foods Deal",
                "Commercial",
                "Deal Commitment War Room",
                "Open this route when the founder needs the commercial answer on price, forecast, release priority, and recovery path before widening commitment.",
                [
                    ("Pricing Review", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/PRICE-2026-001_AtlanticFoods-Garlic-Pricing-Review/OPEN-HERE.html"),
                    ("Release Priority", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/ALLOC-2026-Q2_AtlanticFoods-Release-Priority/OPEN-HERE.html"),
                    ("Recovery Path", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/PVAR-2026-Q3_AtlanticFoods-Recovery-Path/OPEN-HERE.html"),
                    ("Assumptions", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/ASSUMP-2026-Q2_AtlanticFoods-Q3-Assumptions/OPEN-HERE.html"),
                ],
            ),
            build_route_card(
                directory,
                "Atlantic Foods Deal",
                "Outbound",
                "Deal Communication War Room",
                "Start here when the founder needs the institutional outbound layer for this live deal without losing response discipline or scenario context.",
                [
                    ("Formal Offer Packet", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/OPEN-HERE.html"),
                    ("Communication Control", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMCTRL-2026-Q2_AtlanticFoods-Communication-Control/OPEN-HERE.html"),
                    ("Language Reference", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMMSTYLE-2026-Q2_AtlanticFoods-Institutional-Language-Reference/OPEN-HERE.html"),
                    ("Response SLA", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/RESP-2026-Q2_AtlanticFoods-Response-SLA/OPEN-HERE.html"),
                ],
            ),
        ]
        title = "Atlantic Foods Deal Fast Routes"
        copy = "Use these curated war rooms when the founder is already inside the live Atlantic Foods deal and needs the right control or commitment stack immediately."
    elif relative == "03_operations":
        cards = [
            build_route_card(
                directory,
                "Operations",
                "Contained",
                "Contained Movement Execution Trail",
                "Use this route when the matter is already in live execution and the founder needs one clean path from contained movement logic to shipment, funding, and outward packet handling.",
                [
                    ("Shipment Control Tower", "06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html"),
                    ("Funding Review", "06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.html"),
                    ("Pre-Shipment Release", "01_templates/03_logistics/Pre-Shipment-Release-Review-MASTER.html"),
                    ("Supplier Release Packet", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/README.html"),
                ],
            ),
            build_route_card(
                directory,
                "Operations",
                "Core Docs",
                "Core Execution Documents",
                "Open the source documents that operational teams, suppliers, brokers, and forwarders depend on when live execution begins.",
                [
                    ("Purchase Order", "01_templates/02_purchasing/Purchase-Order-MASTER.html"),
                    ("Shipping Instructions", "01_templates/03_logistics/Shipping-Instructions-MASTER.html"),
                    ("Document Control", "01_templates/03_logistics/Document-Control-Register-MASTER.html"),
                    ("Shipment Review", "01_templates/03_logistics/Shipment-Review-Log-MASTER.html"),
                ],
            ),
            build_route_card(
                directory,
                "Operations",
                "Founder",
                "Founder Same-Day Ops Stack",
                "Use this route when the founder needs to intervene in a live gate without losing linkage between operations, executable checks, risk, and scenario response.",
                [
                    ("Operations Command Center", "06_dashboard/03_operations/Daily-Operations-Command-Center.html"),
                    ("Executable Checks", "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html"),
                    ("Scenario Response", "06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.html"),
                    ("Risk Register", "06_dashboard/18_executive-risk-register/Executive-Risk-Register.html"),
                ],
            ),
        ]
        title = "Operations Fast Routes"
        copy = "Start with the live execution stack that matches the founder problem instead of scanning every shipment and working file first."
    elif relative == "03_operations/03_shipments":
        cards = [
            build_route_card(
                directory,
                "Shipments",
                "Release",
                "Live Release Lane",
                "Use this lane when the founder needs the live shipment stack from active movement through release gate and funding approval in one pass.",
                [
                    ("Active Shipments", "03_operations/03_shipments/active/OPEN-HERE.html"),
                    ("China to USA Shipment", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/OPEN-HERE.html"),
                    ("Pre-Shipment Release", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/OPEN-HERE.html"),
                    ("Funding Release", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/OPEN-HERE.html"),
                ],
            ),
            build_route_card(
                directory,
                "Shipments",
                "Proof",
                "Packet Proof Lane",
                "Open this lane when packet completeness, supplier release language, and shipment review proof matter more than the release gate alone.",
                [
                    ("Document Packet", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/OPEN-HERE.html"),
                    ("Supplier Release Packet", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/OPEN-HERE.html"),
                    ("Shipment Review", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/OPEN-HERE.html"),
                    ("Archive Closeout SOP", "05_sops/07_archive/Archive-Closeout-SOP.html"),
                ],
            ),
            build_route_card(
                directory,
                "Shipments",
                "Founder",
                "Founder Intervention Lane",
                "Start here when movement is live but still needs executive control, executable-check closure, or scenario response before widening shipment motion.",
                [
                    ("Shipment Control Tower", "06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html"),
                    ("Operations Command", "06_dashboard/03_operations/Daily-Operations-Command-Center.html"),
                    ("Executable Checks", "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html"),
                    ("Scenario Response", "06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.html"),
                ],
            ),
        ]
        title = "Shipment Route Lanes"
        copy = "Start with the shipment lane that matches the founder question instead of opening the movement tree and scanning every module manually."
    elif relative == "03_operations/03_shipments/active":
        cards = [
            build_route_card(
                directory,
                "Shipments",
                "Release",
                "Shipment Release Stack",
                "Use this route when the founder needs the active shipment path from live control tower to pre-shipment release and payment release in one move.",
                [
                    ("China to USA Shipment", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/OPEN-HERE.html"),
                    ("Shipment Control Tower", "06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html"),
                    ("Pre-Shipment Release", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/OPEN-HERE.html"),
                    ("Funding Release", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/OPEN-HERE.html"),
                ],
            ),
            build_route_card(
                directory,
                "Shipments",
                "Proof",
                "Packet and Proof Stack",
                "Open this route when the founder wants the shipment packet, external supplier release packet, and after-action proof chain without hunting through subfolders.",
                [
                    ("Document Packet", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/OPEN-HERE.html"),
                    ("Supplier Release Packet", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/OPEN-HERE.html"),
                    ("Shipment Review", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/OPEN-HERE.html"),
                    ("Archive Closeout SOP", "05_sops/07_archive/Archive-Closeout-SOP.html"),
                ],
            ),
            build_route_card(
                directory,
                "Shipments",
                "Contained",
                "Contained Movement Shipment Stack",
                "Start here when a live shipment is technically ready but still constrained by executable checks, scenario response, or risk posture.",
                [
                    ("Operations Command", "06_dashboard/03_operations/Daily-Operations-Command-Center.html"),
                    ("Executable Checks", "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html"),
                    ("Scenario Response", "06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.html"),
                    ("Risk Register", "06_dashboard/18_executive-risk-register/Executive-Risk-Register.html"),
                ],
            ),
        ]
        title = "Active Shipment Fast Routes"
        copy = "Use these grouped paths when a shipment is already live and the founder needs the right release, proof, or containment stack immediately."
    elif relative == "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA":
        cards = [
            build_route_card(
                directory,
                "China to USA",
                "Release",
                "Shipment Release War Room",
                "Use this route when the founder wants the exact answer on whether the shipment may move, what still blocks it, and what payment logic remains open.",
                [
                    ("Pre-Shipment Release", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/OPEN-HERE.html"),
                    ("Funding Release", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/FUND-2026-001_Garlic-Payment-Release/OPEN-HERE.html"),
                    ("Shipment Control Tower", "06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html"),
                    ("Operations Command", "06_dashboard/03_operations/Daily-Operations-Command-Center.html"),
                ],
            ),
            build_route_card(
                directory,
                "China to USA",
                "Packet",
                "Shipment Packet War Room",
                "Open this route when the founder needs the document packet, supplier-facing packet, and post-shipment evidence trail in one visual stack.",
                [
                    ("Export Packet", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/DOCCTRL-2026-001_Garlic-Export-Packet/OPEN-HERE.html"),
                    ("Supplier Packet", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/COMM-2026-002_GoldenHarvest-Supplier-Release-Packet/OPEN-HERE.html"),
                    ("Shipment Review", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/SREV-2026-001_Shipment-Review/OPEN-HERE.html"),
                    ("Archive SOP", "05_sops/07_archive/Archive-Closeout-SOP.html"),
                ],
            ),
            build_route_card(
                directory,
                "China to USA",
                "Contained",
                "Shipment Containment War Room",
                "Start here when the shipment is in contained movement mode and the founder needs the live control answer to stay synchronized across scenario, risk, and executable checks.",
                [
                    ("Executable Checks", "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html"),
                    ("Scenario Response", "06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.html"),
                    ("Risk Register", "06_dashboard/18_executive-risk-register/Executive-Risk-Register.html"),
                    ("Funding Review", "06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.html"),
                ],
            ),
        ]
        title = "China to USA Shipment Fast Routes"
        copy = "Use these curated war rooms when the founder is already inside the active shipment and needs the right release, packet, or containment view immediately."
    elif relative == "04_compliance":
        cards = [
            build_route_card(
                directory,
                "Compliance",
                "Claims",
                "Complaint Containment and Recovery Stack",
                "Use this route when a claim, complaint, or inspection issue needs one coordinated path from daily compliance posture to recovery, CAPA, and evidence-backed containment.",
                [
                    ("Compliance Control", "06_dashboard/04_compliance/Daily-Compliance-Control-Center.html"),
                    ("Claims Recovery", "06_dashboard/30_claims-recovery/Claims-Credits-and-Recovery-Review.html"),
                    ("CAPA Governance", "06_dashboard/31_capa-governance/CAPA-and-Preventive-Action-Review.html"),
                    ("Complaint Case", "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/OPEN-HERE.html"),
                ],
            ),
            build_route_card(
                directory,
                "Compliance",
                "Suppliers",
                "Supplier Approval and Resilience Stack",
                "Open this route when the founder wants to understand whether supplier approval, performance, traceability, and fallback sourcing still support confident execution.",
                [
                    ("Supplier Approval", "04_compliance/06_supplier-approval/OPEN-HERE.html"),
                    ("Supplier Performance", "06_dashboard/07_supplier-performance/Supplier-Performance-Review-Board.html"),
                    ("Supply Resilience", "06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.html"),
                    ("Traceability Case", "04_compliance/04_traceability/TRACE-2026-001_GoldenHarvest-Garlic-LotPath/OPEN-HERE.html"),
                ],
            ),
            build_route_card(
                directory,
                "Compliance",
                "Proof",
                "Inspection and Proof Stack",
                "Start here when the founder needs to prove readiness, recover evidence fast, and preserve the inspection trail instead of searching across separate working folders.",
                [
                    ("FDA Readiness", "04_compliance/05_inspections/INSP-2026-001_FDA-Readiness-Review/OPEN-HERE.html"),
                    ("Traceability", "04_compliance/04_traceability/TRACE-2026-001_GoldenHarvest-Garlic-LotPath/OPEN-HERE.html"),
                    ("Document Control", "01_templates/03_logistics/Document-Control-Register-MASTER.html"),
                    ("Archive SOP", "05_sops/07_archive/Archive-Closeout-SOP.html"),
                ],
            ),
        ]
        title = "Compliance Fast Routes"
        copy = "Use these grouped paths when the founder needs the right compliance stack immediately instead of scanning inspections, supplier approval, and traceability folders one by one."
    elif relative == "04_compliance/05_inspections":
        cards = [
            build_route_card(
                directory,
                "Inspections",
                "Complaint",
                "Complaint Containment Stack",
                "Use this route when a complaint case needs to move from raw issue intake into containment, CAPA, and recovery with a single control trail.",
                [
                    ("Complaint Case", "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/OPEN-HERE.html"),
                    ("Claims Recovery", "06_dashboard/30_claims-recovery/Claims-Credits-and-Recovery-Review.html"),
                    ("CAPA Review", "06_dashboard/31_capa-governance/CAPA-and-Preventive-Action-Review.html"),
                    ("Communication Control", "06_dashboard/36_external-communications/Counterparty-Communication-Control-Board.html"),
                ],
            ),
            build_route_card(
                directory,
                "Inspections",
                "Readiness",
                "Regulatory Readiness Stack",
                "Open this route when the founder wants to understand whether inspection readiness is still supported by current compliance posture and traceability proof.",
                [
                    ("FDA Readiness", "04_compliance/05_inspections/INSP-2026-001_FDA-Readiness-Review/OPEN-HERE.html"),
                    ("Compliance Control", "06_dashboard/04_compliance/Daily-Compliance-Control-Center.html"),
                    ("Traceability Case", "04_compliance/04_traceability/TRACE-2026-001_GoldenHarvest-Garlic-LotPath/OPEN-HERE.html"),
                    ("Supplier Performance", "06_dashboard/07_supplier-performance/Supplier-Performance-Review-Board.html"),
                ],
            ),
            build_route_card(
                directory,
                "Inspections",
                "Proof",
                "Inspection Proof and Archive Stack",
                "Start here when the founder needs the proof chain that shows how the issue was documented, reviewed, retained, and closed.",
                [
                    ("Document Control", "01_templates/03_logistics/Document-Control-Register-MASTER.html"),
                    ("Shipment Review", "01_templates/03_logistics/Shipment-Review-Log-MASTER.html"),
                    ("Archive Record", "01_templates/08_closeout/Closeout-and-Archive-Record-MASTER.html"),
                    ("Archive SOP", "05_sops/07_archive/Archive-Closeout-SOP.html"),
                ],
            ),
        ]
        title = "Inspection Fast Routes"
        copy = "Start with the inspection path that matches the real issue instead of opening complaint and readiness folders separately."
    elif relative == "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim":
        cards = [
            build_route_card(
                directory,
                "Atlantic Claim",
                "Containment",
                "Complaint Containment War Room",
                "Use this route when the founder wants the complaint answer from intake through containment and communication, without losing the governing control chain.",
                [
                    ("Complaint Case", "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/README.html"),
                    ("CAPA Case", "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/CAPA-2026-001_AtlanticFoods-Garlic-Containment-and-Prevention/OPEN-HERE.html"),
                    ("Recovery Case", "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/RECOV-2026-001_AtlanticFoods-Claim-Recovery/OPEN-HERE.html"),
                    ("Communication Control", "06_dashboard/36_external-communications/Counterparty-Communication-Control-Board.html"),
                ],
            ),
            build_route_card(
                directory,
                "Atlantic Claim",
                "Executive",
                "Executive Risk and Recovery War Room",
                "Open this route when the founder needs the complaint read translated into financial, customer, and executive consequence.",
                [
                    ("Claims Recovery Board", "06_dashboard/30_claims-recovery/Claims-Credits-and-Recovery-Review.html"),
                    ("CAPA Board", "06_dashboard/31_capa-governance/CAPA-and-Preventive-Action-Review.html"),
                    ("Customer Account Board", "06_dashboard/08_customer-accounts/Customer-Account-Review-Board.html"),
                    ("Risk Register", "06_dashboard/18_executive-risk-register/Executive-Risk-Register.html"),
                ],
            ),
            build_route_card(
                directory,
                "Atlantic Claim",
                "Proof",
                "Proof and Archive War Room",
                "Start here when the founder needs the proof trail that shows how the complaint was documented, supported, and retained for later challenge or audit.",
                [
                    ("Document Control", "01_templates/03_logistics/Document-Control-Register-MASTER.html"),
                    ("Shipment Review Log", "01_templates/03_logistics/Shipment-Review-Log-MASTER.html"),
                    ("Archive Record", "01_templates/08_closeout/Closeout-and-Archive-Record-MASTER.html"),
                    ("Archive SOP", "05_sops/07_archive/Archive-Closeout-SOP.html"),
                ],
            ),
        ]
        title = "Atlantic Complaint Fast Routes"
        copy = "Use these curated war rooms when the founder is already inside the Atlantic Foods claim and needs containment, executive consequence, or proof immediately."
    elif relative == "05_sops":
        cards = [
            build_route_card(
                directory,
                "SOPs",
                "Founder",
                "Founder Governance SOP Stack",
                "Open this route when the founder wants the governing operating rhythm fast: cadence, system adoption, and archive discipline as one executive playbook.",
                [
                    ("Founder Cadence", "05_sops/06_dashboard/Founder-Operating-Cadence-SOP.html"),
                    ("System Adoption", "05_sops/06_dashboard/Operating-System-Rollout-and-Adoption-SOP.html"),
                    ("Archive Closeout", "05_sops/07_archive/Archive-Closeout-SOP.html"),
                    ("Dashboard SOP Portal", "05_sops/06_dashboard/OPEN-HERE.html"),
                ],
            ),
            build_route_card(
                directory,
                "SOPs",
                "Execution",
                "Commercial Movement SOP Stack",
                "Use this route when the founder needs the operating rules that connect commercial intent, movement posture, live gates, and same-day execution discipline.",
                [
                    ("Lifecycle SOP", "05_sops/04_crm/Commercial-Execution-Lifecycle-SOP.html"),
                    ("Operations Command", "06_dashboard/03_operations/Daily-Operations-Command-Center.html"),
                    ("Funding Review", "06_dashboard/29_funding-release/Funding-and-Payables-Release-Review.html"),
                    ("Shipment Control", "06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html"),
                ],
            ),
            build_route_card(
                directory,
                "SOPs",
                "Outbound",
                "Institutional Outbound SOP Stack",
                "Start here when the founder wants the exact communication rules that keep packets, correspondence, and counterparty promises aligned with live internal control posture.",
                [
                    ("Communication Standard", "05_sops/08_external-communications/Counterparty-Communication-Standard-SOP.html"),
                    ("Transmittal Master", "01_templates/11_external-communications/Official-Document-Transmittal-MASTER.html"),
                    ("Correspondence Master", "01_templates/11_external-communications/Institutional-Trade-Correspondence-MASTER.html"),
                    ("Communication Control", "06_dashboard/36_external-communications/Counterparty-Communication-Control-Board.html"),
                ],
            ),
        ]
        title = "SOP Fast Routes"
        copy = "Use these operating playbooks when the founder wants the governing process fast instead of browsing every SOP folder first."
    elif relative == "05_sops/08_external-communications":
        cards = [
            build_route_card(
                directory,
                "Outbound",
                "Rulebook",
                "Counterparty Rulebook Stack",
                "Use this route when the founder wants the exact outward communication rulebook before anything is sent to a client or supplier.",
                [
                    ("Communication SOP", "05_sops/08_external-communications/Counterparty-Communication-Standard-SOP.html"),
                    ("Style Guide", "00_brand/02_guidelines/UNYRA-Institutional-Communication-Style-Guide.html"),
                    ("Message Framework", "01_templates/11_external-communications/Counterparty-Message-Framework-MASTER.html"),
                    ("Release Checklist", "01_templates/11_external-communications/External-Communication-Release-Checklist-MASTER.html"),
                ],
            ),
            build_route_card(
                directory,
                "Outbound",
                "Packets",
                "Send-Ready Packet Stack",
                "Open this route when the founder wants the exact send-ready masters that package transmittal, correspondence, packet indexing, and release approval.",
                [
                    ("Transmittal", "01_templates/11_external-communications/Official-Document-Transmittal-MASTER.html"),
                    ("Correspondence", "01_templates/11_external-communications/Institutional-Trade-Correspondence-MASTER.html"),
                    ("Packet Index", "01_templates/11_external-communications/Counterparty-Document-Packet-Index-MASTER.html"),
                    ("Atlantic Foods Packet", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/OPEN-HERE.html"),
                ],
            ),
            build_route_card(
                directory,
                "Outbound",
                "Live Control",
                "Live Counterparty Control Stack",
                "Start here when the founder needs the live boards that govern what UNYRA may say, what still requires reply, and what movement is actually safe to communicate.",
                [
                    ("Communication Control", "06_dashboard/36_external-communications/Counterparty-Communication-Control-Board.html"),
                    ("Response Escalation", "06_dashboard/37_response-escalation/Counterparty-Response-SLA-and-Escalation-Board.html"),
                    ("Trust Review", "06_dashboard/38_counterparty-trust/Strategic-Counterparty-Trust-and-Response-Review.html"),
                    ("Trust Matrix", "06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.html"),
                ],
            ),
        ]
        title = "External Communication SOP Routes"
        copy = "Use these grouped routes when outward communication is already live and the founder needs the rulebook, packet layer, or live control layer immediately."
    elif relative == "06_dashboard":
        cards = [
            build_route_card(
                directory,
                "Founder",
                "Daily",
                "Same-Day Founder Control",
                "Start here when the founder needs to orient the day, route the issue, confirm the controls are decision-ready, and then move into the right secondary review.",
                [
                    ("Founder Dashboard", "06_dashboard/01_executive/Daily-Founder-Dashboard.html"),
                    ("Control Routing", "06_dashboard/33_control-routing/Founder-Control-Routing-Matrix.html"),
                    ("Control Integrity", "06_dashboard/34_control-integrity/Executive-Control-Integrity-and-Decision-Readiness-Review.html"),
                    ("Executable Checks", "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html"),
                ],
            ),
            build_route_card(
                directory,
                "Dashboard",
                "Contained",
                "Contained Movement Review Stack",
                "Use this route when release, payment, shipment, or outward communication are constrained and the founder needs the contained-movement answer to stay synchronized across the active control layers.",
                [
                    ("Executable Checks", "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html"),
                    ("Scenario Response", "06_dashboard/25_scenario-response/Executive-Scenario-and-Contingency-Review.html"),
                    ("Risk Register", "06_dashboard/18_executive-risk-register/Executive-Risk-Register.html"),
                    ("Communication Control", "06_dashboard/36_external-communications/Counterparty-Communication-Control-Board.html"),
                ],
            ),
            build_route_card(
                directory,
                "Dashboard",
                "Executive",
                "Weekly to Quarterly Command Stack",
                "Open this route when the founder wants to move from weekly posture to monthly and quarterly direction without losing KPI, risk, and initiative context.",
                [
                    ("Weekly Review", "06_dashboard/14_weekly-executive-review/Weekly-Executive-Operating-Review.html"),
                    ("Monthly Review", "06_dashboard/15_monthly-strategic-review/Monthly-Strategic-Business-Review.html"),
                    ("KPI Scorecard", "06_dashboard/17_executive-kpi-scorecard/Executive-KPI-Scorecard.html"),
                    ("Quarterly Plan", "06_dashboard/22_quarterly-operating-plan/Quarterly-Operating-Plan.html"),
                ],
            ),
        ]
        title = "Dashboard Fast Routes"
        copy = "Use these grouped routes when the founder wants the right dashboard stack immediately instead of scanning the full control surface."
    else:
        return ""

    return f"""
        <section class="home-section" id="featured-routes">
          <div class="section-heading">
            <p class="eyebrow">Featured Routes</p>
            <h2 class="section-title">{html.escape(title)}</h2>
            <p class="section-copy">
              {html.escape(copy)}
            </p>
          </div>
          <div class="route-grid">
            {"".join(cards)}
          </div>
        </section>
"""


def build_portal_hero_context(directory: Path) -> dict[str, object] | None:
    if directory == REPO_ROOT:
        return None

    relative = directory.relative_to(REPO_ROOT).as_posix()
    archive_metrics = get_archive_layer_metrics(directory) if is_archive_directory(directory) else None
    sop_metrics = get_sop_layer_metrics(directory) if is_sops_directory(directory) else None
    dashboard_metrics = get_dashboard_layer_metrics(directory) if is_dashboard_directory(directory) else None
    compliance_metrics = get_compliance_layer_metrics(directory) if is_compliance_directory(directory) else None
    operations_metrics = get_operations_layer_metrics(directory) if is_operations_directory(directory) else None
    crm_metrics = get_crm_layer_metrics(directory) if is_crm_directory(directory) else None
    template_metrics = get_template_layer_metrics(directory) if is_templates_directory(directory) else None
    asset_metrics = get_brand_assets_metrics(directory) if is_brand_assets_directory(directory) else None
    brand_metrics = get_brand_layer_metrics(directory) if is_brand_directory(directory) else None
    approved_visual_file_count = sum(
        1
        for child in directory.iterdir()
        if child.is_file() and child.suffix.lower() in {".png", ".jpg", ".jpeg", ".svg", ".webp"}
    )
    directory_child_dirs = [
        path
        for path in directory.iterdir()
        if path.is_dir() and path.name not in SKIP_DIR_NAMES
    ]
    profiles: dict[str, dict[str, object]] = {
        "00_brand": {
            "static_profile": True,
            "title": "Brand",
            "area": "Brand Layer",
            "cta": "Open Brand",
            "copy": "Use this brand layer to move between approved assets, written brand governance, and export surfaces that carry preview docs and visual standard into founder-facing review.",
            "note": "Start here when the founder needs the brand system itself, from approved assets through guidance rules and export governance.",
            "breadcrumb_label": "Brand",
            "pills": ["Approved Assets", "Guidance Rules", "Export Governance"],
            "stats": [
                (
                    brand_metrics["asset_set_count"] if brand_metrics else 0,
                    "Asset Sets",
                    "00_brand/01_assets/OPEN-HERE.html",
                    "stat-mini--surface",
                ),
                (
                    brand_metrics["guidance_count"] if brand_metrics else 0,
                    "Guidance Standards",
                    "00_brand/02_guidelines/OPEN-HERE.html",
                    "stat-mini--docs",
                ),
                (
                    brand_metrics["preview_benchmark_count"] if brand_metrics else 0,
                    "Preview Benchmarks",
                    "00_brand/03_exports/OPEN-HERE.html",
                    "stat-mini--route",
                ),
            ],
            "actions": [
                ("Open Assets", "00_brand/01_assets/OPEN-HERE.html", "primary"),
                ("Open Brand Guidelines", "00_brand/02_guidelines/OPEN-HERE.html", "secondary"),
                ("Open Exports", "00_brand/03_exports/OPEN-HERE.html", "secondary"),
            ],
        },
        "01_templates": {
            "static_profile": True,
            "title": "Templates",
            "area": "Template Layer",
            "cta": "Open Templates",
            "copy": "Use this template layer to move between protected master formats, template domains, and fast drafting routes before any live case file is opened.",
            "note": "Start here when the founder needs the governed format system itself, from route-ready template packs to the protected master domains.",
            "breadcrumb_label": "Templates",
            "pills": ["Protected Masters", "Template Domains", "Fast Routes"],
            "stats": [
                (
                    template_metrics["master_template_count"] if template_metrics else 0,
                    "Master Templates",
                    "01_templates/README.html",
                    "stat-mini--docs",
                ),
                (
                    template_metrics["template_domain_count"] if template_metrics else len(directory_child_dirs),
                    "Template Domains",
                    "#room-modules",
                    "stat-mini--surface",
                ),
                (
                    template_metrics["fast_route_count"] if template_metrics else 0,
                    "Fast Routes",
                    "#featured-routes",
                    "stat-mini--route",
                ),
            ],
            "actions": [
                ("Open Templates Memo", "01_templates/README.html", "primary"),
                ("Open Fast Routes", "#featured-routes", "secondary"),
                ("Open Founder Control Templates", "01_templates/10_governance/OPEN-HERE.html", "secondary"),
            ],
        },
        "02_crm": {
            "static_profile": True,
            "title": "CRM",
            "area": "CRM Layer",
            "cta": "Open CRM",
            "copy": "Use this CRM layer to move between counterparty layers, deal posture, and founder follow-through without losing commercial context.",
            "note": "Start here when the founder needs the governed commercial system itself, from counterparties and deal posture through founder execution queue.",
            "breadcrumb_label": "CRM",
            "pills": ["Counterparty Layers", "Deal Postures", "Founder Queue"],
            "stats": [
                (
                    crm_metrics["counterparty_layer_count"] if crm_metrics else 0,
                    "Counterparty Layers",
                    "02_crm/02_customers/OPEN-HERE.html",
                    "stat-mini--docs",
                ),
                (
                    crm_metrics["deal_posture_count"] if crm_metrics else 0,
                    "Deal Postures",
                    "02_crm/04_deals/OPEN-HERE.html",
                    "stat-mini--surface",
                ),
                (
                    crm_metrics["execution_queue_count"] if crm_metrics else 0,
                    "Execution Queue",
                    "02_crm/05_tasks/TASK-2026-001_Founder-Execution-Queue/README.html",
                    "stat-mini--route",
                ),
            ],
            "actions": [
                ("Open CRM Memo", "02_crm/README.html", "primary"),
                ("Open Active Deals", "02_crm/04_deals/active/OPEN-HERE.html", "secondary"),
                ("Open Founder Queue", "02_crm/05_tasks/TASK-2026-001_Founder-Execution-Queue/README.html", "secondary"),
            ],
        },
        "03_operations": {
            "static_profile": True,
            "title": "Operations",
            "area": "Operations Layer",
            "cta": "Open Operations",
            "copy": "Use this operations layer to move between active shipments, founder control routes, and execution domains without losing live gate context.",
            "note": "Start here when the founder needs the governed execution system itself, from live shipments and operations command through working-file support.",
            "breadcrumb_label": "Operations",
            "pills": ["Active Shipments", "Founder Control", "Execution Domains"],
            "stats": [
                (
                    operations_metrics["active_shipment_count"] if operations_metrics else 0,
                    "Active Shipments",
                    "03_operations/03_shipments/active/OPEN-HERE.html",
                    "stat-mini--docs",
                ),
                (
                    operations_metrics["execution_domain_count"] if operations_metrics else len(directory_child_dirs),
                    "Execution Domains",
                    "#room-modules",
                    "stat-mini--surface",
                ),
                (
                    operations_metrics["fast_route_count"] if operations_metrics else 0,
                    "Fast Routes",
                    "#featured-routes",
                    "stat-mini--route",
                ),
            ],
            "actions": [
                ("Open Operations Memo", "03_operations/README.html", "primary"),
                ("Open Active Shipments", "03_operations/03_shipments/active/OPEN-HERE.html", "secondary"),
                ("Open Operations Command", "06_dashboard/03_operations/Daily-Operations-Command-Center.html", "secondary"),
            ],
        },
        "04_compliance": {
            "static_profile": True,
            "title": "Compliance",
            "area": "Compliance Layer",
            "cta": "Open Compliance",
            "copy": "Use this compliance layer to move between governed cases, supplier control, and proof routes without losing regulatory context.",
            "note": "Start here when the founder needs the governed compliance system itself, from complaint recovery and supplier approval through traceability proof.",
            "breadcrumb_label": "Compliance",
            "pills": ["Governed Cases", "Supplier Control", "Proof Routes"],
            "stats": [
                (
                    compliance_metrics["governed_case_count"] if compliance_metrics else 0,
                    "Governed Cases",
                    "04_compliance/05_inspections/OPEN-HERE.html",
                    "stat-mini--docs",
                ),
                (
                    compliance_metrics["compliance_domain_count"] if compliance_metrics else len(directory_child_dirs),
                    "Compliance Domains",
                    "#room-modules",
                    "stat-mini--surface",
                ),
                (
                    compliance_metrics["fast_route_count"] if compliance_metrics else 0,
                    "Fast Routes",
                    "#featured-routes",
                    "stat-mini--route",
                ),
            ],
            "actions": [
                ("Open Compliance Memo", "04_compliance/README.html", "primary"),
                ("Open Inspection Cases", "04_compliance/05_inspections/OPEN-HERE.html", "secondary"),
                ("Open Supplier Approval", "04_compliance/06_supplier-approval/OPEN-HERE.html", "secondary"),
            ],
        },
        "05_sops": {
            "static_profile": True,
            "title": "SOPs",
            "area": "SOP Layer",
            "cta": "Open SOPs",
            "copy": "Use this SOP layer to move between written operating standards, founder rhythm rules, and release discipline without losing procedural control.",
            "note": "Start here when the founder needs the governing procedure system itself, from founder cadence and commercial lifecycle through communication control and archive discipline.",
            "breadcrumb_label": "SOPs",
            "pills": ["Founder Rhythm", "Lifecycle Control", "Communication Discipline"],
            "stats": [
                (
                    sop_metrics["sop_surface_count"] if sop_metrics else len(directory_child_dirs),
                    "SOP Surfaces",
                    "#room-modules",
                    "stat-mini--surface",
                ),
                (
                    sop_metrics["founder_standard_count"] if sop_metrics else 0,
                    "Founder Standards",
                    "05_sops/06_dashboard/Founder-Operating-Cadence-SOP.html",
                    "stat-mini--docs",
                ),
                (
                    sop_metrics["fast_route_count"] if sop_metrics else 0,
                    "Fast Routes",
                    "#featured-routes",
                    "stat-mini--route",
                ),
            ],
            "actions": [
                ("Open SOP Memo", "05_sops/README.html", "primary"),
                ("Open Founder Cadence SOP", "05_sops/06_dashboard/Founder-Operating-Cadence-SOP.html", "secondary"),
                ("Open Commercial Lifecycle SOP", "05_sops/04_crm/Commercial-Execution-Lifecycle-SOP.html", "secondary"),
            ],
        },
        "06_dashboard": {
            "static_profile": True,
            "title": "Dashboards",
            "area": "Dashboard Layer",
            "cta": "Open Dashboards",
            "copy": "Use this dashboard layer to move between founder control boards, cadence reviews, and execution watch surfaces without losing linked operating context.",
            "note": "Start here when the founder needs the cross-functional control system itself, from the daily dashboard and executable checks through weekly, monthly, and quarterly cadence.",
            "breadcrumb_label": "Dashboards",
            "pills": ["Founder Control", "Cadence Reviews", "Execution Watch"],
            "stats": [
                (
                    dashboard_metrics["dashboard_surface_count"] if dashboard_metrics else len(directory_child_dirs),
                    "Dashboard Surfaces",
                    "#room-modules",
                    "stat-mini--surface",
                ),
                (
                    dashboard_metrics["founder_cadence_count"] if dashboard_metrics else 0,
                    "Founder Cadences",
                    "06_dashboard/14_weekly-executive-review/Weekly-Executive-Operating-Review.html",
                    "stat-mini--docs",
                ),
                (
                    dashboard_metrics["fast_route_count"] if dashboard_metrics else 0,
                    "Fast Routes",
                    "#featured-routes",
                    "stat-mini--route",
                ),
            ],
            "actions": [
                ("Open Dashboard Memo", "06_dashboard/README.html", "primary"),
                ("Open Founder Dashboard", "06_dashboard/01_executive/Daily-Founder-Dashboard.html", "secondary"),
                ("Open Executable Checks", "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html", "secondary"),
            ],
        },
        "07_archive": {
            "static_profile": True,
            "title": "Archive",
            "area": "Archive Layer",
            "cta": "Open Archive",
            "copy": "Use this archive layer to move between retained history, archive closeout control, and concrete retrieval routes without disturbing the active operating layer.",
            "note": "Start here when the founder needs prior-case reference, archived matter retrieval, and a governed answer on whether history is truly ready to stay closed.",
            "breadcrumb_label": "Archive",
            "pills": ["Retained History", "Closeout Control", "Retrieval Routes"],
            "stats": [
                (
                    archive_metrics["archived_matter_count"] if archive_metrics else 0,
                    "Archived Matters",
                    "07_archive/03_crm/DEAL-2026-001_AtlanticFoods_Garlic-CLOSED/README.html",
                    "stat-mini--docs",
                ),
                (
                    archive_metrics["archive_function_count"] if archive_metrics else len(directory_child_dirs),
                    "Archive Functions",
                    "#room-modules",
                    "stat-mini--surface",
                ),
                (
                    archive_metrics["fast_route_count"] if archive_metrics else 0,
                    "Fast Routes",
                    "#featured-routes",
                    "stat-mini--route",
                ),
            ],
            "actions": [
                ("Open Archive Memo", "07_archive/README.html", "primary"),
                ("Open Archived CRM", "07_archive/03_crm/OPEN-HERE.html", "secondary"),
                ("Open Archive Closeout SOP", "05_sops/07_archive/Archive-Closeout-SOP.html", "secondary"),
            ],
        },
        "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution": {
            "title": "Atlantic Foods Account Room",
            "area": "Customer War Room",
            "copy": "Use this executive account room to decide whether Atlantic Foods should receive wider release, tighter collections pressure, or more strategic weight.",
            "note": "Focus this room on trust posture, credit exposure, and whether growth still fits the account's current institutional quality.",
            "breadcrumb_label": "Atlantic Foods Account Room",
            "lens_target": "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CTRUST-2026-Q2_AtlanticFoods-Relationship-Trust-Review/OPEN-HERE.html",
            "decision_target": "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CREDIT-2026-001_AtlanticFoods-Release-Control/OPEN-HERE.html",
            "pills": ["Atlantic Foods", "Trust and Release", "Cash Exposure", "Growth Weight"],
            "stats": [
                ("Trust", "Primary Lens"),
                ("Release", "Decision Now"),
                ("Monthly", "Escalation Rhythm"),
            ],
            "actions": [
                ("Open Account Brief", "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/README.html", "primary"),
                ("Open Customer Board", "06_dashboard/08_customer-accounts/Customer-Account-Review-Board.html", "secondary"),
                ("Open Trust Review", "02_crm/02_customers/CUST-2026-001_AtlanticFoods-Distribution/CTRUST-2026-Q2_AtlanticFoods-Relationship-Trust-Review/OPEN-HERE.html", "secondary"),
            ],
        },
        "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic": {
            "title": "Atlantic Foods Garlic Deal Room",
            "area": "Live Deal War Room",
            "copy": "Use this live deal room to move from decision control to commercial commitment and institutional outbound without losing case discipline.",
            "note": "Start with the war room that matches the next decision: control, commitment, or communication.",
            "breadcrumb_label": "Atlantic Foods Garlic Deal Room",
            "lens_target": "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control/OPEN-HERE.html",
            "decision_target": "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/ALLOC-2026-Q2_AtlanticFoods-Release-Priority/OPEN-HERE.html",
            "pills": ["Live Deal", "Matter Control", "Commercial Commitments", "Institutional Outbound"],
            "stats": [
                ("Control", "Primary Lens"),
                ("Commit", "Decision Now"),
                ("Same-Day", "Escalation Rhythm"),
            ],
            "actions": [
                ("Open Deal Brief", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/README.html", "primary"),
                ("Open Matter Control", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/MCTRL-2026-001_AtlanticFoods-Garlic-Matter-Control/OPEN-HERE.html", "secondary"),
                ("Open Formal Offer Packet", "02_crm/04_deals/active/DEAL-2026-001_AtlanticFoods_Garlic/COMM-2026-001_AtlanticFoods-Formal-Offer-Packet/OPEN-HERE.html", "secondary"),
            ],
        },
        "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA": {
            "title": "China to USA Shipment Room",
            "area": "Live Shipment War Room",
            "copy": "Use this live shipment room to judge release readiness, packet completeness, and contained-movement posture before anything physically moves.",
            "note": "This room is strongest when the founder needs one synchronized answer across release, funding, packet proof, and containment.",
            "breadcrumb_label": "China to USA Shipment Room",
            "lens_target": "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/OPEN-HERE.html",
            "decision_target": "#room-outcome-path-move",
            "pills": ["Active Shipment", "Release Gate", "Packet Proof", "Contained Movement"],
            "stats": [
                ("Release", "Primary Lens"),
                ("Move", "Decision Now"),
                ("Same-Day", "Escalation Rhythm"),
            ],
            "actions": [
                ("Open Shipment Brief", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/README.html", "primary"),
                ("Open Release Gate", "03_operations/03_shipments/active/SHIP-2026-001_China-to-USA/REL-2026-001_Pre-Shipment-Release/OPEN-HERE.html", "secondary"),
                ("Open Control Tower", "06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html", "secondary"),
            ],
        },
        "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim": {
            "title": "Atlantic Foods Claim Room",
            "area": "Complaint War Room",
            "copy": "Use this complaint room to move from issue containment to recovery consequence and proof retention without splitting the case across folders.",
            "note": "Start with containment, then move to executive consequence and the archive trail needed for later challenge or audit.",
            "breadcrumb_label": "Atlantic Foods Claim Room",
            "lens_target": "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/CAPA-2026-001_AtlanticFoods-Garlic-Containment-and-Prevention/OPEN-HERE.html",
            "decision_target": "#room-outcome-path-recover",
            "pills": ["Active Claim", "Containment", "Recovery Consequence", "Proof Trail"],
            "stats": [
                ("Contain", "Primary Lens"),
                ("Recover", "Decision Now"),
                ("Weekly", "Escalation Rhythm"),
            ],
            "actions": [
                ("Open Claim Brief", "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/README.html", "primary"),
                ("Open CAPA Case", "04_compliance/05_inspections/COMP-2026-001_AtlanticFoods-Garlic-Claim/CAPA-2026-001_AtlanticFoods-Garlic-Containment-and-Prevention/OPEN-HERE.html", "secondary"),
                ("Open Claims Recovery", "06_dashboard/30_claims-recovery/Claims-Credits-and-Recovery-Review.html", "secondary"),
            ],
        },
        "04_compliance/05_inspections/INSP-2026-001_FDA-Readiness-Review": {
            "title": "FDA Readiness Room",
            "area": "Readiness Review Room",
            "cta": "Open FDA Readiness Room",
            "copy": "Use this readiness room to move from regulator-readiness framing into response closeout, proof control, and founder escalation without falling into raw compliance folders.",
            "note": "Start with the readiness brief when the founder needs the readiness narrative, then widen into the inspection lane or compliance control only as needed.",
            "breadcrumb_label": "FDA Readiness Room",
            "pills": ["Readiness Brief", "Response Closeout", "Compliance Control"],
            "stats": [
                (1, "Readiness Brief", "./README.html", "stat-mini--brief"),
                (3, "Route Lanes", "#featured-routes", "stat-mini--route"),
                (1, "Compliance Control", "../../../06_dashboard/04_compliance/Daily-Compliance-Control-Center.html", "stat-mini--surface"),
            ],
            "actions": [
                ("Open Readiness Brief", "./README.html", "primary"),
                ("Open Inspection Cases", "../OPEN-HERE.html", "secondary"),
                ("Open Compliance Control", "../../../06_dashboard/04_compliance/Daily-Compliance-Control-Center.html", "secondary"),
            ],
        },
    }
    direct_profile = profiles.get(relative)
    if direct_profile:
        if direct_profile.get("static_profile"):
            profile = dict(direct_profile)
            profile.pop("static_profile", None)
            return profile
        profile = dict(direct_profile)
        pills = list(profile.get("pills", []))
        base_stats = list(profile.get("stats", []))
        actions = list(profile.get("actions", []))
        sequence_local, sequence_external = get_decision_sequence_scope_counts(directory)
        local_outcomes, external_outcomes = get_outcome_path_scope_counts(directory)
        route_posture = get_route_posture(
            sequence_local,
            sequence_external,
            local_outcomes,
            external_outcomes,
        )
        sequence_focus_href = "#decision-sequence-in-room" if sequence_local and sequence_external else "#decision-sequence"
        outcome_focus_href = "#outcome-room-paths" if local_outcomes and external_outcomes else "#outcome-paths"
        outcome_external_href = "#outcome-external-controls" if local_outcomes and external_outcomes else "#outcome-paths"

        sequence_scope_summary = get_route_scope_pill_override(directory, "Sequence") or format_route_scope_pill("Sequence", sequence_local, sequence_external)
        outcome_scope_summary = get_route_scope_pill_override(directory, "Outcomes") or format_route_scope_pill("Outcomes", local_outcomes, external_outcomes)
        pills.extend(
            [
                (
                    str(route_posture["label"]),
                    f"{str(route_posture['pill_class'])} meta-pill--link",
                    "#founder-start-here",
                ),
                (
                    sequence_scope_summary,
                    f"{get_room_nav_summary_pill_class(sequence_scope_summary, 'controls')} meta-pill--link",
                    sequence_focus_href,
                ),
                (
                    outcome_scope_summary,
                    f"{get_room_nav_summary_pill_class(outcome_scope_summary, 'controls')} meta-pill--link",
                    outcome_focus_href,
                ),
            ]
        )

        room_has_watch = brief_has_escalation_triggers(directory / "README.md")
        lens_target = str(profile.get("lens_target", "")).strip()
        decision_target = str(profile.get("decision_target", "")).strip()
        route_logic_value = "In Room"
        if sequence_external or external_outcomes:
            route_logic_value = "Mixed" if sequence_local or local_outcomes else "Board Led"
        stats: list[tuple[str, str] | tuple[str, str, str] | tuple[str, str, str, str]] = [
            (
                str(base_stats[0][0]),
                str(base_stats[0][1]),
                lens_target or "#founder-start-here",
                "stat-mini--module" if lens_target else "stat-mini--brief",
            )
        ] if base_stats else []
        if len(base_stats) > 1:
            stats.append(
                (
                    str(base_stats[1][0]),
                    str(base_stats[1][1]),
                    decision_target or outcome_focus_href,
                    "stat-mini--decision" if decision_target else "stat-mini--outcome",
                )
            )
        if len(base_stats) > 2:
            if room_has_watch:
                stats.append(
                    (
                        str(base_stats[2][0]),
                        str(base_stats[2][1]),
                        "#escalation-trigger-01",
                        "stat-mini--watch",
                    )
                )
            else:
                stats.append((str(base_stats[2][0]), str(base_stats[2][1])))
        stats.extend(
            [
                (route_logic_value, "Route Logic", "#founder-start-here", "stat-mini--brief"),
                (f"{sequence_local}/{sequence_external}", "Seq In/Out", sequence_focus_href, "stat-mini--sequence"),
                (f"{local_outcomes}/{external_outcomes}", "Outcome In/Out", outcome_external_href, "stat-mini--outcome"),
            ]
        )

        if local_outcomes or external_outcomes:
            if local_outcomes and external_outcomes:
                actions.append(("Open In-Room", "#outcome-room-paths", "secondary"))
                actions.append(("Open External", "#outcome-external-controls", "secondary"))
            else:
                actions.append(("Open Outcomes", "#outcome-paths", "secondary"))
        note = str(profile.get("note", "")).strip()
        route_note = str(route_posture.get("note", "")).strip()
        if route_note:
            note = f"{note} {route_note}".strip() if note else route_note
        profile["note"] = note
        profile["pills"] = pills
        profile["stats"] = stats
        profile["actions"] = actions
        return profile

    state_profiles: dict[str, dict[str, object]] = {
        LEADS_RELATIVE: {
            "title": "Leads",
            "area": "Lead Flow Lane",
            "copy": "Use this lead-flow lane to review the live prospect room, qualification routes, and founder follow-through without reopening the full CRM stack.",
            "note": "Start with the live lead room when the founder needs the current prospect answer, then widen into pipeline or follow-through only as needed.",
            "breadcrumb_label": "Leads",
            "pills": ["Live Lead Room", "Qualification Routes", "Founder Follow-Through"],
            "stats": [
                (1, "Lead Room", "./LEAD-2026-001_CrescentMarket-Wholesale/OPEN-HERE.html", "stat-mini--surface"),
                (3, "Lead Routes", "#featured-routes", "stat-mini--route"),
                (1, "Sales Pipeline", "../../06_dashboard/02_sales-pipeline/Daily-Sales-Pipeline-Command-Center.html", "stat-mini--docs"),
            ],
            "actions": [
                ("Open Lead Room", "./LEAD-2026-001_CrescentMarket-Wholesale/OPEN-HERE.html", "primary"),
                ("Open Lead Routes", "#featured-routes", "secondary"),
                ("Open Sales Pipeline", "../../06_dashboard/02_sales-pipeline/Daily-Sales-Pipeline-Command-Center.html", "secondary"),
                ("Open Founder Queue", "../05_tasks/TASK-2026-001_Founder-Execution-Queue/OPEN-HERE.html", "secondary"),
            ],
        },
        LEAD_ROOM_RELATIVE: {
            "title": "Crescent Market Wholesale Lead Room",
            "area": "Lead Pursuit Room",
            "copy": "Use this lead-pursuit room to keep Crescent Market qualification, pipeline pressure, and the next founder move under one governed prospect answer.",
            "note": "Start with the lead brief when the founder needs the qualification narrative, then widen into pipeline or follow-through only when the next move is explicit.",
            "breadcrumb_label": "Crescent Market Wholesale Lead Room",
            "pills": ["Lead Brief", "Qualification Track", "Next Move"],
            "stats": [
                (1, "Lead Brief", "./README.html", "stat-mini--brief"),
                (3, "Route Paths", "#decision-sequence", "stat-mini--route"),
                (1, "Sales Pipeline", "../../../06_dashboard/02_sales-pipeline/Daily-Sales-Pipeline-Command-Center.html", "stat-mini--surface"),
            ],
            "actions": [
                ("Open Lead Brief", "./README.html", "primary"),
                ("Open Qualification Route", "#decision-sequence", "secondary"),
                ("Open Sales Pipeline", "../../../06_dashboard/02_sales-pipeline/Daily-Sales-Pipeline-Command-Center.html", "secondary"),
                ("Open Founder Queue", "../../05_tasks/TASK-2026-001_Founder-Execution-Queue/OPEN-HERE.html", "secondary"),
            ],
        },
        CUSTOMERS_RELATIVE: {
            "title": "Customer Accounts",
            "area": "Customer Account Lane",
            "copy": "Use this customer-account lane to review the live account room, trust posture, collections pressure, and release exposure without reopening the full CRM stack.",
            "note": "Start with the Atlantic Foods account room when the founder needs the current customer answer, then widen into trust, collections, or concentration routes only as needed.",
            "breadcrumb_label": "Customer Accounts",
            "pills": ["Live Account Room", "Trust Routes", "Collections Pressure", "Release Exposure"],
            "stats": [
                (1, "Account Room", "./CUST-2026-001_AtlanticFoods-Distribution/OPEN-HERE.html", "stat-mini--surface"),
                (3, "Customer Routes", "#featured-routes", "stat-mini--route"),
                (1, "Customer Board", "../../06_dashboard/08_customer-accounts/Customer-Account-Review-Board.html", "stat-mini--docs"),
            ],
            "actions": [
                ("Open Account Room", "./CUST-2026-001_AtlanticFoods-Distribution/OPEN-HERE.html", "primary"),
                ("Open Customer Routes", "#featured-routes", "secondary"),
                ("Open Customer Board", "../../06_dashboard/08_customer-accounts/Customer-Account-Review-Board.html", "secondary"),
                ("Open Trust Matrix", "../../06_dashboard/39_trust-posture/Counterparty-Trust-Tier-and-Release-Posture-Matrix.html", "secondary"),
            ],
        },
        SUPPLIERS_RELATIVE: {
            "title": "Suppliers",
            "area": "Supplier Continuity Lane",
            "copy": "Use this supplier-continuity lane to review the live sourcing room, approval routes, and performance posture without reopening the full CRM stack.",
            "note": "Start with the live supplier room when the founder needs the current sourcing answer, then widen into approval or performance only when the risk truly depends on them.",
            "breadcrumb_label": "Suppliers",
            "pills": ["Live Supplier Room", "Approval Routes", "Performance Posture"],
            "stats": [
                (1, "Supplier Room", "./SUP-2026-001_GoldenHarvest-Produce/OPEN-HERE.html", "stat-mini--surface"),
                (3, "Supplier Routes", "#featured-routes", "stat-mini--route"),
                (1, "Supplier Approval", "../../04_compliance/06_supplier-approval/OPEN-HERE.html", "stat-mini--docs"),
            ],
            "actions": [
                ("Open Supplier Room", "./SUP-2026-001_GoldenHarvest-Produce/OPEN-HERE.html", "primary"),
                ("Open Supplier Routes", "#featured-routes", "secondary"),
                ("Open Supplier Approval", "../../04_compliance/06_supplier-approval/OPEN-HERE.html", "secondary"),
                ("Open Supplier Performance", "../../06_dashboard/07_supplier-performance/Supplier-Performance-Review-Board.html", "secondary"),
            ],
        },
        SUPPLIER_ROOM_RELATIVE: {
            "title": "Golden Harvest Produce Supplier Room",
            "area": "Supplier Continuity Room",
            "copy": "Use this supplier-continuity room to keep Golden Harvest approval posture, sourcing dependence, and next founder move under one governed supplier answer.",
            "note": "Start with the supplier brief when the founder needs the sourcing narrative, then widen into approval or performance only when the answer truly depends on them.",
            "breadcrumb_label": "Golden Harvest Produce Supplier Room",
            "pills": ["Supplier Brief", "Approval Track", "Continuity Risk"],
            "stats": [
                (1, "Supplier Brief", "./README.html", "stat-mini--brief"),
                (3, "Route Paths", "#decision-sequence", "stat-mini--route"),
                (1, "Supplier Approval", "../../../04_compliance/06_supplier-approval/OPEN-HERE.html", "stat-mini--surface"),
            ],
            "actions": [
                ("Open Supplier Brief", "./README.html", "primary"),
                ("Open Approval Route", "#decision-sequence", "secondary"),
                ("Open Supplier Approval", "../../../04_compliance/06_supplier-approval/OPEN-HERE.html", "secondary"),
                ("Open Supplier Performance", "../../../06_dashboard/07_supplier-performance/Supplier-Performance-Review-Board.html", "secondary"),
            ],
        },
        TASKS_RELATIVE: {
            "title": "Tasks",
            "area": "Execution Queue Lane",
            "copy": "Use this execution-queue lane to review the founder queue, live gate routes, and accountable follow-through without reopening the full CRM stack.",
            "note": "Start with the founder queue when the founder needs the current execution answer, then widen into gate closure or owner accountability only as needed.",
            "breadcrumb_label": "Tasks",
            "pills": ["Founder Queue", "Live Gate Routes", "Owner Accountability"],
            "stats": [
                (1, "Founder Queue", "./TASK-2026-001_Founder-Execution-Queue/OPEN-HERE.html", "stat-mini--surface"),
                (3, "Execution Routes", "#featured-routes", "stat-mini--route"),
                (1, "Executable Checks", "../../06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html", "stat-mini--docs"),
            ],
            "actions": [
                ("Open Founder Queue", "./TASK-2026-001_Founder-Execution-Queue/OPEN-HERE.html", "primary"),
                ("Open Execution Routes", "#featured-routes", "secondary"),
                ("Open Executable Checks", "../../06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html", "secondary"),
                ("Open Owner Accountability", "../../06_dashboard/28_owner-accountability/Executive-Owner-Accountability-and-Follow-Through-Review.html", "secondary"),
            ],
        },
        TASK_ROOM_RELATIVE: {
            "title": "Founder Execution Queue",
            "area": "Execution Queue Room",
            "copy": "Use this execution-queue room to keep live gate pressure, required proof, and founder follow-through under one governed action answer.",
            "note": "Start with the execution brief when the founder needs the blocker narrative, then widen into executable checks or owner accountability only when closure really depends on them.",
            "breadcrumb_label": "Founder Execution Queue",
            "pills": ["Execution Brief", "Gate Closure", "Owner Follow-Through"],
            "stats": [
                (1, "Execution Brief", "./README.html", "stat-mini--brief"),
                (3, "Route Paths", "#decision-sequence", "stat-mini--route"),
                (1, "Executable Checks", "../../../06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html", "stat-mini--surface"),
            ],
            "actions": [
                ("Open Execution Brief", "./README.html", "primary"),
                ("Open Live Gate Route", "#decision-sequence", "secondary"),
                ("Open Executable Checks", "../../../06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html", "secondary"),
                ("Open Owner Accountability", "../../../06_dashboard/28_owner-accountability/Executive-Owner-Accountability-and-Follow-Through-Review.html", "secondary"),
            ],
        },
        TRACEABILITY_RELATIVE: {
            "title": "Traceability",
            "area": "Proof Chain Lane",
            "copy": "Use this proof-chain lane to review the live lot-path room, audit-readiness posture, and the control routes that defend traceability under pressure.",
            "note": "Start with the traceability room when the founder needs the current lot-lineage answer, then widen into compliance control or recovery only as needed.",
            "breadcrumb_label": "Traceability",
            "pills": ["Live Traceability Room", "Lot Retrieval", "Audit Readiness"],
            "stats": [
                (1, "Traceability Room", "./TRACE-2026-001_GoldenHarvest-Garlic-LotPath/OPEN-HERE.html", "stat-mini--surface"),
                (3, "Proof Routes", "#featured-routes", "stat-mini--route"),
                (1, "Compliance Control", "../../06_dashboard/04_compliance/Daily-Compliance-Control-Center.html", "stat-mini--surface"),
            ],
            "actions": [
                ("Open Traceability Room", "./TRACE-2026-001_GoldenHarvest-Garlic-LotPath/OPEN-HERE.html", "primary"),
                ("Open Proof Routes", "#featured-routes", "secondary"),
                ("Open Compliance Control", "../../06_dashboard/04_compliance/Daily-Compliance-Control-Center.html", "secondary"),
                ("Open Claims Recovery", "../../06_dashboard/30_claims-recovery/Claims-Credits-and-Recovery-Review.html", "secondary"),
            ],
        },
        TRACEABILITY_ROOM_RELATIVE: {
            "title": "Golden Harvest Garlic Lot Path Traceability Room",
            "area": "Traceability Proof Room",
            "copy": "Use this traceability-proof room to keep lot lineage, retrieval proof, and audit-readiness pressure under one governed founder answer.",
            "note": "Start with the traceability brief when the founder needs the lot-path narrative, then widen into compliance control or recovery only when the proof answer is explicit.",
            "breadcrumb_label": "Golden Harvest Garlic Lot Path Traceability Room",
            "pills": ["Traceability Brief", "Lot Path Defense", "Audit Readiness"],
            "stats": [
                (1, "Traceability Brief", "./README.html", "stat-mini--brief"),
                (3, "Route Paths", "#decision-sequence", "stat-mini--route"),
                (1, "Compliance Control", "../../../06_dashboard/04_compliance/Daily-Compliance-Control-Center.html", "stat-mini--surface"),
            ],
            "actions": [
                ("Open Traceability Brief", "./README.html", "primary"),
                ("Open Proof Route", "#decision-sequence", "secondary"),
                ("Open Compliance Control", "../../../06_dashboard/04_compliance/Daily-Compliance-Control-Center.html", "secondary"),
                ("Open Claims Recovery", "../../../06_dashboard/30_claims-recovery/Claims-Credits-and-Recovery-Review.html", "secondary"),
            ],
        },
        "02_crm/04_deals/active": {
            "title": "Active Deals",
            "area": "Deal Flow Lane",
            "copy": "Use this deal-flow lane to review the live commercial room, founder routes, and outbound commitment surfaces that still carry active revenue pressure.",
            "note": "Start with the memo when the founder needs the active-deal brief, then widen into control, commitment, or communication routes without leaving the live deal lane.",
            "breadcrumb_label": "Active Deals",
            "pills": ["Live Deal Room", "Founder Routes", "Outbound Commitment"],
            "stats": [
                (1, "Active Deals Memo", "./README.html", "stat-mini--brief"),
                (3, "Founder Routes", "#featured-routes", "stat-mini--route"),
                (1, "Live Deal Room", "#room-modules", "stat-mini--surface"),
            ],
            "actions": [
                ("Open Active Deals Memo", "./README.html", "primary"),
                ("Open Founder Routes", "#featured-routes", "secondary"),
                ("Open Live Deal Room", "#room-modules", "secondary"),
            ],
        },
        "02_crm/04_deals": {
            "title": "Deals",
            "area": "Deal Hub",
            "copy": "Use this deal hub to move between live commercial pressure, retained wins, and loss learning without losing the current posture of the overall deal book.",
            "note": "Start with the memo when the founder needs the lane map across active, won, and lost deals before narrowing into one commercial track.",
            "breadcrumb_label": "Deals",
            "pills": ["Active Deals", "Won Record", "Lost Learning", "Commercial Posture"],
            "stats": [
                (1, "Deals Memo", "./README.html", "stat-mini--brief"),
                (3, "Deal Lanes", "#room-modules", "stat-mini--surface"),
                (1, "Active Deal Lane", "./active/OPEN-HERE.html", "stat-mini--route"),
            ],
            "actions": [
                ("Open Deals Memo", "./README.html", "primary"),
                ("Open Deal Lanes", "#room-modules", "secondary"),
                ("Open Active Deals", "./active/OPEN-HERE.html", "secondary"),
            ],
        },
        "02_crm/04_deals/won": {
            "title": "Won Deals",
            "area": "Retained Win Lane",
            "copy": "Use this retained-win lane to review closed commercial successes that still matter for precedent, replication, and institutional continuity.",
            "note": "Start with the memo when the founder needs the preserved win map before narrowing into the Harbor Fresh reference room or back into live deal pressure.",
            "breadcrumb_label": "Won Deals",
            "pills": ["Reference Win", "Retained Precedent", "Narrative Continuity"],
            "stats": [
                (1, "Won Deals Memo", "./README.html", "stat-mini--brief"),
                (1, "Reference Win Room", "#room-modules", "stat-mini--surface"),
                (1, "Active Deal Lane", "../active/OPEN-HERE.html", "stat-mini--route"),
            ],
            "actions": [
                ("Open Won Deals Memo", "./README.html", "primary"),
                ("Open Reference Win Room", "#room-modules", "secondary"),
                ("Open Active Deals", "../active/OPEN-HERE.html", "secondary"),
            ],
        },
        "02_crm/04_deals/lost": {
            "title": "Lost Deals",
            "area": "Recovery Learning Lane",
            "copy": "Use this recovery-learning lane to review missed commercial matters that still matter for accountability, reset logic, and future commercial discipline.",
            "note": "Start with the memo when the founder needs the preserved loss map before narrowing into the Crescent Market learning room or back into live deal pressure.",
            "breadcrumb_label": "Lost Deals",
            "pills": ["Recovery Learning", "Decision Record", "Future Reset"],
            "stats": [
                (1, "Lost Deals Memo", "./README.html", "stat-mini--brief"),
                (1, "Learning Room", "#room-modules", "stat-mini--surface"),
                (1, "Active Deal Lane", "../active/OPEN-HERE.html", "stat-mini--route"),
            ],
            "actions": [
                ("Open Lost Deals Memo", "./README.html", "primary"),
                ("Open Learning Room", "#room-modules", "secondary"),
                ("Open Active Deals", "../active/OPEN-HERE.html", "secondary"),
            ],
        },
        "02_crm/04_deals/won/DEAL-2026-003_HarborFresh_Garlic": {
            "title": "Harbor Fresh Garlic Won Deal Room",
            "area": "Reference Win Room",
            "copy": "Use this reference-win room to preserve the closed commercial narrative, transfer logic, and reusable execution pattern behind Harbor Fresh Garlic.",
            "note": "Start with the room memo when the founder needs the retained win narrative, then move into the trade review or back out to the won-deal lane only as needed.",
            "breadcrumb_label": "Harbor Fresh Garlic Won Deal Room",
            "pills": ["Reference Win", "Execution Handoff", "Retained Narrative"],
            "stats": [
                (1, "Room Memo", "./README.html", "stat-mini--brief"),
                (1, "Trade Review Module", "./PROFIT-2026-001_HarborFresh-Garlic-Trade-Review/OPEN-HERE.html", "stat-mini--surface"),
                (1, "Won Deal Lane", "../OPEN-HERE.html", "stat-mini--route"),
            ],
            "actions": [
                ("Open Room Memo", "./README.html", "primary"),
                ("Open Trade Review", "./PROFIT-2026-001_HarborFresh-Garlic-Trade-Review/OPEN-HERE.html", "secondary"),
                ("Open Won Deals", "../OPEN-HERE.html", "secondary"),
                ("Open Active Deals", "../../active/OPEN-HERE.html", "secondary"),
            ],
        },
        "02_crm/04_deals/lost/DEAL-2026-002_CrescentMarket_Ginger": {
            "title": "Crescent Market Ginger Lost Deal Room",
            "area": "Recovery Learning Room",
            "copy": "Use this recovery-learning room to preserve the missed commercial narrative, pricing lesson, and reset logic behind Crescent Market Ginger.",
            "note": "Start with the room memo when the founder needs the retained miss record, then move back to lost deals or active deals depending on whether the next answer is retrospective or live.",
            "breadcrumb_label": "Crescent Market Ginger Lost Deal Room",
            "pills": ["Recovery Learning", "Reset Logic", "Decision Record"],
            "stats": [
                (1, "Room Memo", "./README.html", "stat-mini--brief"),
                (1, "Lost Deal Lane", "../OPEN-HERE.html", "stat-mini--surface"),
                (1, "Active Deal Lane", "../../active/OPEN-HERE.html", "stat-mini--route"),
            ],
            "actions": [
                ("Open Room Memo", "./README.html", "primary"),
                ("Open Lost Deals", "../OPEN-HERE.html", "secondary"),
                ("Open Active Deals", "../../active/OPEN-HERE.html", "secondary"),
                ("Open Deals", "../../OPEN-HERE.html", "secondary"),
            ],
        },
        "02_crm/04_deals/won/DEAL-2026-003_HarborFresh_Garlic/PROFIT-2026-001_HarborFresh-Garlic-Trade-Review": {
            "title": "Harbor Fresh Garlic Trade Review",
            "area": "Trade Review Module",
            "copy": "Use this trade-review module to compare planned and realized economics behind Harbor Fresh Garlic without leaving the retained win stack.",
            "note": "Start with the memo when the founder needs the variance story, then move back to the won deal room or deal lanes only when wider precedent or live pressure matters.",
            "breadcrumb_label": "Harbor Fresh Garlic Trade Review",
            "pills": ["Margin Variance", "Planned vs Realized", "Release Precedent"],
            "stats": [
                (1, "Trade Review Memo", "./README.html", "stat-mini--brief"),
                (1, "Won Deal Room", "../OPEN-HERE.html", "stat-mini--surface"),
                (1, "Won Deal Lane", "../../OPEN-HERE.html", "stat-mini--route"),
            ],
            "actions": [
                ("Open Trade Review Memo", "./README.html", "primary"),
                ("Open Won Deal Room", "../OPEN-HERE.html", "secondary"),
                ("Open Won Deals", "../../OPEN-HERE.html", "secondary"),
                ("Open Active Deals", "../../../active/OPEN-HERE.html", "secondary"),
            ],
        },
        "03_operations/03_shipments": {
            "title": "Shipments",
            "area": "Shipment Hub",
            "copy": "Use this shipment hub to move between active shipments, live release gates, packet proof, and founder intervention routes without dropping into raw folders.",
            "note": "Start here when the founder needs the governed shipment system itself, from active movement lanes and packet proof through control-tower escalation.",
            "breadcrumb_label": "Shipments",
            "pills": ["Active Shipments", "Release Gates", "Packet Proof"],
            "stats": [
                (1, "Active Shipment", "./active/OPEN-HERE.html", "stat-mini--docs"),
                (3, "Route Lanes", "#featured-routes", "stat-mini--route"),
                (1, "Control Tower", "../../06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html", "stat-mini--surface"),
            ],
            "actions": [
                ("Open Active Shipments", "./active/OPEN-HERE.html", "primary"),
                ("Open Shipment Routes", "#featured-routes", "secondary"),
                ("Open Shipment Control Tower", "../../06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html", "secondary"),
            ],
        },
        "03_operations/03_shipments/active": {
            "title": "Active Shipments",
            "area": "Active Shipment Lane",
            "copy": "Use this active-shipment lane to move between the live movement brief, release stack, packet proof, and the current shipment room without losing contained-motion context.",
            "note": "Start with the shipment brief when the founder needs the current movement logic, then widen into route lanes or the live shipment room only as needed.",
            "breadcrumb_label": "Active Shipments",
            "pills": ["Shipment Brief", "Route Lanes", "Packet Proof"],
            "stats": [
                (1, "Shipment Brief", "#founder-start-here", "stat-mini--brief"),
                (3, "Route Lanes", "#featured-routes", "stat-mini--route"),
                (1, "Live Shipment Room", "#room-modules", "stat-mini--surface"),
            ],
            "actions": [
                ("Open Shipment Brief", "#founder-start-here", "primary"),
                ("Open Route Lanes", "#featured-routes", "secondary"),
                ("Open Shipment Control Tower", "../../../06_dashboard/05_shipments/Daily-Shipment-Control-Tower.html", "secondary"),
            ],
        },
        "04_compliance/06_supplier-approval": {
            "title": "Supplier Approval",
            "area": "Supplier Approval Hub",
            "copy": "Use this supplier-approval hub to move between governed supplier rooms, performance control, and resilience review without reopening raw compliance folders.",
            "note": "Start here when the founder needs one supplier-governance lane that connects current approval status, quarterly performance, and backup-sourcing resilience.",
            "breadcrumb_label": "Supplier Approval",
            "pills": ["Governed Supplier", "Performance Control", "Resilience Review"],
            "stats": [
                (1, "Governed Supplier", "./SUPPLIER-2026-001_GoldenHarvest-Produce/OPEN-HERE.html", "stat-mini--surface"),
                (2, "Review Modules", "./SUPPLIER-2026-001_GoldenHarvest-Produce/OPEN-HERE.html#room-modules", "stat-mini--route"),
                (2, "Control Boards", "../../06_dashboard/07_supplier-performance/Supplier-Performance-Review-Board.html", "stat-mini--docs"),
            ],
            "actions": [
                ("Open Golden Harvest Supplier Room", "./SUPPLIER-2026-001_GoldenHarvest-Produce/OPEN-HERE.html", "primary"),
                ("Open Supplier Performance Board", "../../06_dashboard/07_supplier-performance/Supplier-Performance-Review-Board.html", "secondary"),
                ("Open Supply Resilience Board", "../../06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.html", "secondary"),
            ],
        },
        "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce": {
            "title": "Golden Harvest Produce Supplier Approval Room",
            "area": "Supplier Governance Room",
            "copy": "Use this supplier-governance room to keep Golden Harvest approval, quarterly performance, and backup-sourcing resilience under one founder-ready answer.",
            "note": "Start with the supplier brief when the founder needs the approval narrative, then widen into performance or resilience only when the answer truly depends on those tracks.",
            "breadcrumb_label": "Golden Harvest Produce Supplier Approval Room",
            "pills": ["Supplier Brief", "Performance Track", "Resilience Track"],
            "stats": [
                (1, "Supplier Brief", "./README.html", "stat-mini--brief"),
                (2, "Review Modules", "#room-modules", "stat-mini--surface"),
                (2, "Control Boards", "../../../06_dashboard/07_supplier-performance/Supplier-Performance-Review-Board.html", "stat-mini--route"),
            ],
            "actions": [
                ("Open Supplier Brief", "./README.html", "primary"),
                ("Open Supplier Performance Board", "../../../06_dashboard/07_supplier-performance/Supplier-Performance-Review-Board.html", "secondary"),
                ("Open Supply Resilience Board", "../../../06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.html", "secondary"),
            ],
        },
        "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce/PERF-2026-Q2_GoldenHarvest-Supplier-Performance": {
            "title": "Golden Harvest Supplier Performance",
            "area": "Supplier Performance Module",
            "copy": "Use this supplier-performance module to assess Golden Harvest scorecard posture, response quality, and whether approved-with-controls status still holds.",
            "note": "Start here when the founder needs the focused performance readout before widening back to the supplier brief or the executive performance board.",
            "breadcrumb_label": "Golden Harvest Supplier Performance",
            "pills": ["Performance Module", "Approval Track", "Scorecard Review"],
            "stats": [
                (1, "Module Memo", "./README.html", "stat-mini--brief"),
                (1, "Supplier Brief", "../README.html", "stat-mini--surface"),
                (1, "Performance Board", "../../../../06_dashboard/07_supplier-performance/Supplier-Performance-Review-Board.html", "stat-mini--route"),
            ],
            "actions": [
                ("Open Module Memo", "./README.html", "primary"),
                ("Open Supplier Brief", "../README.html", "secondary"),
                ("Open Supplier Performance Board", "../../../../06_dashboard/07_supplier-performance/Supplier-Performance-Review-Board.html", "secondary"),
            ],
        },
        "04_compliance/06_supplier-approval/SUPPLIER-2026-001_GoldenHarvest-Produce/CAPACITY-2026-Q2_GoldenHarvest-Backup-Sourcing-Review": {
            "title": "Golden Harvest Backup Sourcing Review",
            "area": "Backup Sourcing Review Module",
            "copy": "Use this resilience module to assess backup sourcing depth, capacity confidence, and whether Golden Harvest dependence still has enough contingency behind it.",
            "note": "Start here when the founder needs the resilience readout before widening back to the supplier brief or the supply resilience board.",
            "breadcrumb_label": "Golden Harvest Backup Sourcing Review",
            "pills": ["Resilience Module", "Backup Coverage", "Supply Confidence"],
            "stats": [
                (1, "Module Memo", "./README.html", "stat-mini--brief"),
                (1, "Supplier Brief", "../README.html", "stat-mini--surface"),
                (1, "Resilience Board", "../../../../06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.html", "stat-mini--route"),
            ],
            "actions": [
                ("Open Module Memo", "./README.html", "primary"),
                ("Open Supplier Brief", "../README.html", "secondary"),
                ("Open Supply Resilience Board", "../../../../06_dashboard/21_supply-resilience/Supplier-Capacity-and-Backup-Sourcing-Review.html", "secondary"),
            ],
        },
        "00_brand/01_assets/04_signatures": {
            "title": "Brand Signatures",
            "area": "Signature Reference",
            "copy": "Use this signature reference surface to review approved outbound signature treatments without reopening the protected asset repository.",
            "note": "Start here when the founder needs the approved signature stack before choosing broader lockups, seals, or visual governance.",
            "breadcrumb_label": "Brand Signatures",
            "pills": ["Approved Signatures", "Identity Closure", "Outbound Use"],
            "stats": [
                (approved_visual_file_count, "Approved Signatures", "./OPEN-HERE.html", "stat-mini--surface"),
                (1, "Reference Memo", "./README.html", "stat-mini--brief"),
                (1, "Governance Surface", "../../03_exports/01_visual-standard/OPEN-HERE.html", "stat-mini--route"),
            ],
            "actions": [
                ("Open Signatures Memo", "./README.html", "primary"),
                ("Open Assets", "../OPEN-HERE.html", "secondary"),
                ("Open Approved Compositions", "../05_approved-compositions/OPEN-HERE.html", "secondary"),
            ],
        },
        "00_brand/01_assets/05_approved-compositions": {
            "title": "Approved Compositions",
            "area": "Composition Reference",
            "copy": "Use this composition reference surface to review approved lockups, seals, and signature-adjacent brand treatments without reopening the protected asset repository.",
            "note": "Start here when the founder needs the approved lockup system before widening into signatures or the governing visual standard.",
            "breadcrumb_label": "Approved Compositions",
            "pills": ["Approved Lockups", "Seal System", "Header Use"],
            "stats": [
                (approved_visual_file_count, "Approved Compositions", "./OPEN-HERE.html", "stat-mini--surface"),
                (1, "Reference Memo", "./README.html", "stat-mini--brief"),
                (1, "Governance Surface", "../../03_exports/01_visual-standard/OPEN-HERE.html", "stat-mini--route"),
            ],
            "actions": [
                ("Open Compositions Memo", "./README.html", "primary"),
                ("Open Assets", "../OPEN-HERE.html", "secondary"),
                ("Open Brand Signatures", "../04_signatures/OPEN-HERE.html", "secondary"),
            ],
        },
    }
    state_profile = state_profiles.get(relative)
    if state_profile:
        return dict(state_profile)

    generic_profiles: dict[str, dict[str, object]] = {
        "00_brand/01_assets/04_signatures": {
            "title": "Brand Signatures",
            "area": "Signature Layer",
            "cta": "Open Brand Signatures",
            "copy": "Use this signature layer to review approved email signatures and identity closures without reopening the raw asset repository.",
            "note": "Start here when the founder needs approved signature treatments rather than broader brand compositions.",
            "breadcrumb_label": "Brand Signatures",
            "pills": ["Approved Signatures", "Identity Closure", "Outbound Use"],
        },
        "00_brand/01_assets/05_approved-compositions": {
            "title": "Approved Compositions",
            "area": "Composition Layer",
            "cta": "Open Approved Compositions",
            "copy": "Use this composition layer to review approved branded layouts and lockups without dropping into raw asset folders.",
            "note": "Start here when the founder needs approved visual compositions rather than single asset files.",
            "breadcrumb_label": "Approved Compositions",
            "pills": ["Approved Layouts", "Brand Lockups", "Reusable Compositions"],
        },
        "00_brand/02_guidelines": {
            "title": "Brand Guidelines",
            "area": "Brand Guidance",
            "cta": "Open Brand Guidelines",
            "copy": "Use brand guidelines to review identity rules, document standards, and institutional voice discipline before moving into exports or live benchmark surfaces.",
            "note": "Start here when the founder needs the governing rule set behind approved marks, writing discipline, and presentation standards.",
            "breadcrumb_label": "Brand Guidelines",
            "pills": ["Identity Rules", "Document Standard", "Voice Discipline"],
        },
        "00_brand/01_assets": {
            "static_profile": True,
            "title": "Assets",
            "area": "Asset Layer",
            "cta": "Open Asset Custody Memo",
            "copy": "Use this asset layer to review signatures and approved compositions while keeping logos, icons, and imagery protected inside the approved brand asset system.",
            "note": "Start here when the founder needs the governed asset map behind review-ready surfaces and protected source sets.",
            "breadcrumb_label": "Assets",
            "pills": ["Approved Assets", "Review Surfaces", "Protected Sets"],
            "stats": [
                (
                    asset_metrics["asset_set_count"] if asset_metrics else 0,
                    "Asset Sets",
                    "00_brand/01_assets/README.html",
                    "stat-mini--docs",
                ),
                (
                    asset_metrics["review_surface_count"] if asset_metrics else 0,
                    "Review Surfaces",
                    "00_brand/01_assets/OPEN-HERE.html#room-modules",
                    "stat-mini--surface",
                ),
                (
                    asset_metrics["protected_set_count"] if asset_metrics else 0,
                    "Protected Sets",
                    "00_brand/01_assets/README.html#doc-reading-surface",
                    "stat-mini--route",
                ),
            ],
            "actions": [
                ("Open Asset Custody Memo", "00_brand/01_assets/README.html", "primary"),
                ("Open Brand Signatures", "00_brand/01_assets/04_signatures/OPEN-HERE.html", "secondary"),
                ("Open Approved Compositions", "00_brand/01_assets/05_approved-compositions/OPEN-HERE.html", "secondary"),
            ],
        },
        "00_brand/03_exports": {
            "title": "Exports",
            "area": "Export Layer",
            "cta": "Open Exports",
            "copy": "Use exports to move between preview docs, domain lanes, and the governing visual standard that controls founder-facing benchmark output.",
            "note": "Start here when the founder needs either the preview benchmark hub or the governing visual standard before opening a single piece.",
            "breadcrumb_label": "Exports",
            "pills": ["Preview Docs", "Domain Lanes", "Visual Standard"],
        },
        "00_brand/03_exports/01_visual-standard": {
            "title": "Visual Standard",
            "area": "Visual Standard Layer",
            "cta": "Open Visual Standard",
            "copy": "Use this visual-standard layer to review the governed design system, premium document rules, and export styling surfaces in one place.",
            "note": "Start here when the founder needs the styling standard that governs branded previews and documents.",
            "breadcrumb_label": "Visual Standard",
            "pills": ["Design Standard", "Preview Governance", "Export Styling"],
        },
        "00_brand/03_exports/02_preview-docs": {
            "title": "Preview Docs",
            "area": "Preview Docs Layer",
            "cta": "Open Preview Docs",
            "copy": "Use preview docs to route founder review across pathways, domain lanes, benchmark library, and approved brand anchors without reopening raw folders.",
            "note": "Start here when the founder needs the right preview route, benchmark lane, or brand anchor before opening a single benchmark.",
            "breadcrumb_label": "Preview Docs",
            "pills": ["Founder Pathways", "Domain Lanes", "Brand Anchors"],
        },
        "02_crm/01_leads": {
            "title": "Leads",
            "area": "Lead Layer",
            "cta": "Open Leads",
            "copy": "Use this lead layer to review active prospect rooms and early commercial posture without reopening the full CRM stack.",
            "note": "Start here when the founder needs pipeline posture, qualification, and next-move discipline for live prospects.",
            "breadcrumb_label": "Leads",
            "pills": ["Lead Rooms", "Pipeline Posture", "Qualification"],
        },
        "02_crm/02_customers": {
            "title": "Customer Accounts",
            "area": "Customer Layer",
            "cta": "Open Customer Accounts",
            "copy": "Use this customer layer to review account rooms, trust posture, collections, and release exposure without reopening the full CRM tree.",
            "note": "Start here when the founder needs customer quality, collections posture, or account exposure before opening a single room.",
            "breadcrumb_label": "Customer Accounts",
            "pills": ["Account Rooms", "Trust Posture", "Collections", "Release Exposure"],
        },
        "02_crm/03_suppliers": {
            "title": "Suppliers",
            "area": "Supplier Layer",
            "cta": "Open Suppliers",
            "copy": "Use this supplier layer to review live supplier rooms, continuity risk, and approval posture in one commercial surface.",
            "note": "Start here when the founder needs supplier confidence, continuity, or dependency posture without opening the whole CRM tree.",
            "breadcrumb_label": "Suppliers",
            "pills": ["Supplier Rooms", "Continuity Risk", "Approval Posture"],
        },
        "02_crm/04_deals": {
            "title": "Deals",
            "area": "Deal Layer",
            "cta": "Open Deals",
            "copy": "Use this deal layer to review active, won, and lost commercial rooms without losing the connection between live commitment, retained wins, and recovery learning.",
            "note": "Start here when the founder needs the full commercial pipeline posture rather than a single live matter.",
            "breadcrumb_label": "Deals",
            "pills": ["Active Deals", "Won Deals", "Lost Deals", "Commercial Posture"],
        },
        "02_crm/05_tasks": {
            "title": "Tasks",
            "area": "Task Layer",
            "cta": "Open Tasks",
            "copy": "Use this task layer to review live execution queues, founder follow-through, and operational ownership in one place.",
            "note": "Start here when the founder needs the current action queue rather than a room-specific control surface.",
            "breadcrumb_label": "Tasks",
            "pills": ["Execution Queue", "Owner Follow-Through", "Pending Actions"],
        },
        "04_compliance/04_traceability": {
            "title": "Traceability",
            "area": "Traceability Layer",
            "cta": "Open Traceability",
            "copy": "Use this traceability layer to review proof-chain surfaces that support shipment control, complaint defense, and audit readiness.",
            "note": "Start here when the founder needs retained proof rather than a live commercial or movement room.",
            "breadcrumb_label": "Traceability",
            "pills": ["Proof Chain", "Audit Readiness", "Retained Evidence"],
        },
        "04_compliance/05_inspections": {
            "title": "Inspection Cases",
            "area": "Inspection Cases Hub",
            "cta": "Open Inspection Cases",
            "copy": "Use this inspection-cases hub to move between complaint containment, readiness response, and founder control without reopening raw compliance folders.",
            "note": "Start here when the founder needs the governed case lane behind complaint and readiness answers before widening into control boards.",
            "breadcrumb_label": "Inspection Cases",
            "pills": ["Claim Room", "FDA Readiness", "Compliance Control"],
        },
        "04_compliance/06_supplier-approval": {
            "title": "Supplier Approval",
            "area": "Supplier Approval Layer",
            "cta": "Open Supplier Approval",
            "copy": "Use this supplier-approval layer to review onboarding, continuity, and governance surfaces for approved supply partners.",
            "note": "Start here when supplier dependency needs a governed approval view rather than a commercial room.",
            "breadcrumb_label": "Supplier Approval",
            "pills": ["Approval Rooms", "Supplier Governance", "Continuity"],
        },
        "03_operations/03_shipments": {
            "title": "Shipments",
            "area": "Shipment Layer",
            "cta": "Open Shipments",
            "copy": "Use this shipment layer to review live movement rooms, release gates, and packet-control surfaces without dropping into the raw operations tree.",
            "note": "Start here when the founder needs the shipment-wide movement layer before opening a single live room.",
            "breadcrumb_label": "Shipments",
            "pills": ["Live Shipments", "Release Gates", "Packet Control", "Movement Layer"],
        },
        WORKING_FILES_RELATIVE: {
            "title": "Working Files",
            "area": "Operations Staging Surface",
            "cta": "Open Working Files",
            "copy": "Use this staging surface to review temporary trackers and support records that still need routing into a deal, shipment, compliance case, or archive lane.",
            "note": "Start here only when the founder needs to confirm what is still temporary, what must move, and which operating lane owns the settled record.",
            "breadcrumb_label": "Working Files",
            "pills": ["Temporary Staging", "Relocation Discipline", "Operations Control"],
            "stats": [
                (1, "Staging Memo", "./README.html", "stat-mini--brief"),
                (1, "Operations Hub", "../OPEN-HERE.html", "stat-mini--surface"),
                (1, "Operations Command", "../../06_dashboard/03_operations/Daily-Operations-Command-Center.html", "stat-mini--route"),
            ],
            "actions": [
                ("Open Staging Memo", "./README.html", "primary"),
                ("Open Operations", "../OPEN-HERE.html", "secondary"),
                ("Open Active Shipments", "../03_shipments/active/OPEN-HERE.html", "secondary"),
                ("Open Operations Command", "../../06_dashboard/03_operations/Daily-Operations-Command-Center.html", "secondary"),
            ],
        },
        ARCHIVED_CRM_RELATIVE: {
            "title": "Archived CRM",
            "area": "Retained Commercial Lane",
            "cta": "Open Archived CRM",
            "copy": "Use this retained commercial lane to review closed deal memory, archive closeout posture, and prior relationship history without reopening the live CRM stack.",
            "note": "Start with the closed Atlantic Foods deal room when the founder needs commercial memory, precedent, or archive retrieval context.",
            "breadcrumb_label": "Archived CRM",
            "pills": ["Retained Deal Room", "Commercial Memory", "Archive Closeout"],
            "stats": [
                (1, "Closed Deal Room", "./DEAL-2026-001_AtlanticFoods_Garlic-CLOSED/OPEN-HERE.html", "stat-mini--surface"),
                (1, "Archive Hub", "../OPEN-HERE.html", "stat-mini--route"),
                (1, "Closeout SOP", "../../05_sops/07_archive/Archive-Closeout-SOP.html", "stat-mini--docs"),
            ],
            "actions": [
                ("Open Closed Deal Room", "./DEAL-2026-001_AtlanticFoods_Garlic-CLOSED/OPEN-HERE.html", "primary"),
                ("Open Archive", "../OPEN-HERE.html", "secondary"),
                ("Open Archive Closeout SOP", "../../05_sops/07_archive/Archive-Closeout-SOP.html", "secondary"),
                ("Open Live CRM", "../../02_crm/OPEN-HERE.html", "secondary"),
            ],
        },
    }
    generic_profile = generic_profiles.get(relative)
    if generic_profile:
        return dict(generic_profile)

    parent = directory.parent
    parent_relative = parent.relative_to(REPO_ROOT).as_posix() if parent != REPO_ROOT else ""
    base_name = humanize_surface_name(directory.name)

    if parent_relative == "02_crm/01_leads":
        return {
            "title": f"{base_name} Lead Room",
            "area": "Lead Room",
            "copy": f"Use this lead room to review {base_name}'s pursuit posture, qualification quality, and next commercial move without leaving the pipeline layer.",
            "note": "Treat this room as the live prospect surface for qualification, trust, and commercial next-step discipline.",
            "breadcrumb_label": f"{base_name} Lead Room",
            "pills": [base_name, "Lead Pursuit", "Commercial Qualification"],
        }
    if parent_relative == "02_crm/03_suppliers":
        return {
            "title": f"{base_name} Supplier Room",
            "area": "Supplier Room",
            "copy": f"Use this supplier room to review {base_name}'s approval posture, continuity risk, and institutional dependence in one place.",
            "note": "Treat this room as the live supplier surface for continuity, quality, and approval confidence.",
            "breadcrumb_label": f"{base_name} Supplier Room",
            "pills": [base_name, "Supplier Continuity", "Approval Confidence"],
        }
    if parent_relative == "02_crm/04_deals/won":
        return {
            "title": f"{base_name} Won Deal Room",
            "area": "Won Deal Room",
            "copy": f"Use this won deal room to preserve the retained commercial narrative, proof trail, and reusable pattern behind {base_name}.",
            "note": "Treat this room as a reference win and institutional memory surface, not as a live commitment layer.",
            "breadcrumb_label": f"{base_name} Won Deal Room",
            "pills": [base_name, "Reference Win", "Retained Narrative"],
        }
    if parent_relative == "02_crm/04_deals/lost":
        return {
            "title": f"{base_name} Lost Deal Room",
            "area": "Lost Deal Room",
            "copy": f"Use this lost deal room to review the missed commercial matter, recovery learning, and decision record behind {base_name}.",
            "note": "Treat this room as a learning and accountability surface rather than a live commercial path.",
            "breadcrumb_label": f"{base_name} Lost Deal Room",
            "pills": [base_name, "Recovery Learning", "Decision Record"],
        }
    if parent_relative == "02_crm/05_tasks":
        return {
            "title": base_name,
            "area": "Task Surface",
            "copy": f"Use this task surface to review {base_name.lower()} and the current execution queue tied to founder follow-through.",
            "note": "Treat this surface as the live task layer for execution ownership and next actions.",
            "breadcrumb_label": base_name,
            "pills": [base_name, "Execution Queue", "Owner Follow-Through"],
            "cta": f"Open {base_name}",
        }
    if parent_relative == "04_compliance/06_supplier-approval":
        return {
            "title": f"{base_name} Supplier Approval Room",
            "area": "Supplier Approval Room",
            "copy": f"Use this supplier approval room to review {base_name}'s onboarding posture, compliance readiness, and continuity risk in one governed surface.",
            "note": "Treat this room as the live supplier-governance surface for approval, continuity, and proof.",
            "breadcrumb_label": f"{base_name} Supplier Approval Room",
            "pills": [base_name, "Supplier Governance", "Approval Readiness"],
        }
    if parent_relative == "04_compliance/04_traceability":
        return {
            "title": f"{base_name} Traceability Room",
            "area": "Traceability Room",
            "copy": f"Use this traceability room to review {base_name}, proof-chain continuity, and lot-level audit readiness in one governed surface.",
            "note": "Treat this room as the live proof-chain surface for traceability, challenge defense, and retained evidence.",
            "breadcrumb_label": f"{base_name} Traceability Room",
            "pills": [base_name, "Proof Chain", "Audit Readiness"],
        }
    if parent_relative == "04_compliance/05_inspections":
        return {
            "title": f"{base_name} Inspection Review",
            "area": "Inspection Review Room",
            "copy": f"Use this inspection-review room to assess {base_name}, readiness posture, and follow-up discipline without splitting the governed record.",
            "note": "Treat this room as the live readiness and inspection surface for proof, response, and escalation.",
            "breadcrumb_label": f"{base_name} Inspection Review",
            "pills": [base_name, "Inspection Readiness", "Governed Response"],
        }
    if parent_relative.startswith("04_compliance/06_supplier-approval/SUPPLIER-"):
        return {
            "title": base_name,
            "area": "Supplier Review Module",
            "copy": f"Use this supplier-review module to assess {base_name} inside the approved supplier record without reopening the full governance room.",
            "note": "Treat this module as a supporting supplier-governance surface for continuity, quality, and backup readiness.",
            "breadcrumb_label": base_name,
            "pills": [base_name, "Supplier Review", "Governed Module"],
        }
    if parent_relative == ARCHIVED_CRM_RELATIVE:
        closed_base_name = re.sub(r"\s+CLOSED$", "", base_name, flags=re.IGNORECASE).strip() or base_name
        return {
            "title": f"{closed_base_name} Closed Deal Room",
            "area": "Retained Deal Room",
            "copy": f"Use this retained deal room to review {closed_base_name}, final proof, closeout posture, and commercial history without reopening the active CRM layer.",
            "note": "Treat this room as archived deal memory for later reference, replication, and founder review.",
            "breadcrumb_label": f"{closed_base_name} Closed Deal Room",
            "pills": [closed_base_name, "Closed Deal", "Retained Proof", "Commercial Memory"],
            "stats": [
                (1, "Closed Deal Memo", "./README.html", "stat-mini--brief"),
                (1, "Archived CRM", "../OPEN-HERE.html", "stat-mini--surface"),
                (1, "Archive Hub", "../../OPEN-HERE.html", "stat-mini--route"),
            ],
            "actions": [
                ("Open Closed Deal Memo", "./README.html", "primary"),
                ("Open Archived CRM", "../OPEN-HERE.html", "secondary"),
                ("Open Archive", "../../OPEN-HERE.html", "secondary"),
                ("Open Live CRM", "../../../02_crm/OPEN-HERE.html", "secondary"),
            ],
        }
    if parent_relative == "01_templates":
        master_template_count = sum(
            1
            for child in directory.iterdir()
            if child.is_file() and child.suffix.lower() == ".md" and child.name.endswith("-MASTER.md")
        )
        return {
            "title": f"{base_name} Templates",
            "area": f"{base_name} Templates",
            "copy": f"Use this template surface to review approved {base_name} formats, governed starting points, and reusable drafting structure in one place.",
            "note": "Treat this surface as the canonical starting layer before case-specific drafting or export.",
            "breadcrumb_label": f"{base_name} Templates",
            "pills": [base_name, "Approved Templates", "Reusable Structure"],
            "stats": [
                (master_template_count, "Master Templates", "#supporting-files", "stat-mini--docs"),
                (1, "Templates Hub", "../OPEN-HERE.html", "stat-mini--surface"),
                (1, "Fast Route Stack", "../OPEN-HERE.html#featured-routes", "stat-mini--route"),
            ],
            "actions": [
                ("Open Template Pack", "#supporting-files", "primary"),
                ("Open Templates", "../OPEN-HERE.html", "secondary"),
                ("Open Fast Routes", "../OPEN-HERE.html#featured-routes", "secondary"),
            ],
        }
    if parent_relative == "05_sops":
        sop_count = sum(
            1
            for child in directory.iterdir()
            if child.is_file() and child.suffix.lower() == ".md" and child.name != "README.md"
        )
        return {
            "title": f"{base_name} Procedures",
            "area": f"{base_name} Procedures",
            "copy": f"Use this procedure surface to review {base_name} standards, handoffs, and control discipline without reopening the raw SOP tree.",
            "note": "Treat this surface as the governing procedure layer behind the live system.",
            "breadcrumb_label": f"{base_name} Procedures",
            "pills": [base_name, "Procedure Standards", "Control Discipline"],
            "stats": [
                (sop_count, "Procedure Standards", "#supporting-files", "stat-mini--docs"),
                (1, "SOP Hub", "../OPEN-HERE.html", "stat-mini--surface"),
                (1, "Fast Route Stack", "../OPEN-HERE.html#featured-routes", "stat-mini--route"),
            ],
            "actions": [
                ("Open Procedure Stack", "#supporting-files", "primary"),
                ("Open SOPs", "../OPEN-HERE.html", "secondary"),
                ("Open Fast Routes", "../OPEN-HERE.html#featured-routes", "secondary"),
            ],
        }
    if parent_relative == "06_dashboard":
        primary_doc = get_dashboard_pack_primary_doc(directory)
        board_title = humanize_surface_name(primary_doc.stem) if primary_doc else f"{base_name} Board"
        board_href = f"./{primary_doc.with_suffix('.html').name}" if primary_doc else "#supporting-files"
        return {
            "title": f"{base_name} Board",
            "area": f"{base_name} Board",
            "copy": f"Use this board surface to review {base_name} signals through a founder-ready control layer instead of raw repository structure.",
            "note": "Treat this board as a control readout for executive posture, exceptions, and current signal flow.",
            "breadcrumb_label": f"{base_name} Board",
            "pills": [base_name, "Control Board", "Executive Readout"],
            "stats": [
                (1 if primary_doc else 0, "Control Board", board_href, "stat-mini--docs"),
                (1, "Dashboard Hub", "../OPEN-HERE.html", "stat-mini--surface"),
                (3, "Fast Routes", "../OPEN-HERE.html#featured-routes", "stat-mini--route"),
            ],
            "actions": [
                (f"Open {board_title}", board_href, "primary"),
                ("Open Dashboards", "../OPEN-HERE.html", "secondary"),
                ("Open Dashboard Fast Routes", "../OPEN-HERE.html#featured-routes", "secondary"),
            ],
        }
    if parent_relative.startswith("02_crm/04_deals/won/DEAL-"):
        return {
            "title": base_name,
            "area": "Won Deal Module",
            "copy": f"Use this retained-win module to review {base_name.lower()} inside the preserved commercial record without reopening the full deal stack.",
            "note": "Treat this module as a supporting reference surface inside the retained win record.",
            "breadcrumb_label": base_name,
            "pills": [base_name, "Reference Module", "Execution Handoff"],
        }
    if parent_relative.startswith("02_crm/04_deals/lost/DEAL-"):
        return {
            "title": base_name,
            "area": "Lost Deal Module",
            "copy": f"Use this recovery-learning module to review {base_name.lower()} inside the preserved commercial miss without reopening the full deal stack.",
            "note": "Treat this module as a supporting learning surface inside the retained loss record.",
            "breadcrumb_label": base_name,
            "pills": [base_name, "Learning Module", "Reset Surface"],
        }

    if parent != REPO_ROOT:
        parent_relative = parent.relative_to(REPO_ROOT).as_posix()
        room_profile = profiles.get(parent_relative)
        module_profile = build_folder_card_profile(parent, directory)
        if room_profile and module_profile:
            room_title = str(room_profile["title"])
            room_short = " ".join(room_title.split()[-2:])
            module_title = str(module_profile.get("title") or humanize_slug(directory.name))
            module_copy = str(module_profile.get("copy") or f"Use this module inside {room_title}.")
            module_pill = str(module_profile.get("pill") or "Module")
            sequence_context = get_module_sequence_jump_links(directory)
            stack_context = get_module_stack_jump_links(directory)
            path_context = get_module_room_path_context(parent, directory)
            room_stats = list(room_profile.get("stats", []))
            room_decision = str(room_stats[1][0]) if len(room_stats) > 1 else "Current"
            room_escalation = str(room_stats[2][0]) if len(room_stats) > 2 else "As needed"
            next_action = (
                tuple(sequence_context["next_action"])
                if sequence_context and sequence_context.get("next_action")
                else (f"Return to {room_short}", f"{parent_relative}/OPEN-HERE.html")
            )
            previous_action = (
                tuple(sequence_context["previous_action"])
                if sequence_context and sequence_context.get("previous_action")
                else None
            )
            stack_current_action = (
                tuple(stack_context["full_links"][1])
                if stack_context and len(stack_context.get("full_links", [])) >= 2
                else None
            )
            stack_current_href = str(stack_current_action[1]) if stack_current_action and len(stack_current_action) > 1 else ""
            sequence_current_href = "#module-sequence-current"
            sequence_next_href = (
                str(sequence_context["full_links"][2][1])
                if sequence_context and len(sequence_context.get("full_links", [])) >= 3
                else "#module-sequence-context"
            )
            actions: list[tuple[str, str, str]] = [
                (str(next_action[0]), str(next_action[1]), "primary"),
            ]
            if stack_current_action:
                actions.append((str(stack_current_action[0]), str(stack_current_action[1]), "secondary"))
            if previous_action:
                actions.append((str(previous_action[0]), str(previous_action[1]), "secondary"))
            room_entry_action = (
                get_room_entry_label(parent, "Open Room Brief", "Open Room Entry"),
                get_room_entry_href(directory, parent),
                "secondary",
            )
            room_bridge_action = (
                room_entry_action
                if str(next_action[0]).strip() == "Open Room Outcomes"
                else ("Open Room Outcomes", f"{parent_relative}/OPEN-HERE.html#outcome-paths", "secondary")
            )
            actions.append(room_bridge_action)
            if not stack_current_action:
                actions.append((f"Return to {room_short}", f"{parent_relative}/OPEN-HERE.html", "secondary"))

            path_value = str(path_context["pill"]) if path_context else "Support"
            path_pill = f"{path_value} Path" if path_context else "Supporting Control"
            path_pill_item: str | tuple[str, str, str]
            path_focus_href = stack_current_href or ("#stack-live-path-modules" if path_context else "#stack-supporting-controls")
            if path_context:
                path_pill_item = (
                    path_pill,
                    "meta-pill meta-pill--path-current meta-pill--link",
                    path_focus_href,
                )
            else:
                path_pill_item = (
                    path_pill,
                    "meta-pill meta-pill--path-supporting meta-pill--link",
                    path_focus_href,
                )
            sequence_pills: list[str | tuple[str, str, str]] = []
            if sequence_context:
                position_pill = str(sequence_context.get("position_pill") or "").strip()
                next_pill = str(sequence_context.get("next_pill") or "").strip()
                if position_pill:
                    sequence_pills.append(
                        (
                            position_pill,
                            "meta-pill meta-pill--nav-sequence meta-pill--link",
                            sequence_current_href,
                        )
                    )
                if next_pill:
                    next_pill_class = "meta-pill meta-pill--nav-sequence meta-pill--link"
                    if "External" in next_pill:
                        next_pill_class = "meta-pill meta-pill--route-external meta-pill--link"
                    elif "Outcomes" in next_pill:
                        next_pill_class = "meta-pill meta-pill--nav-outcome meta-pill--link"
                    elif "In Room" in next_pill:
                        next_pill_class = "meta-pill meta-pill--route-local meta-pill--link"
                    sequence_pills.append((next_pill, next_pill_class, sequence_next_href))
            if stack_current_action:
                sequence_pills.append(
                    (
                        "Stack Ready",
                        "meta-pill meta-pill--nav-stack meta-pill--link",
                        stack_current_href,
                    )
                )
            note = (
                f"This module currently carries the room's {path_value.lower()} path inside {room_title}. Return to the room when the founder needs the full case answer across linked controls."
                if path_context
                else f"This module supports {room_title}'s broader answer. Return to the room when the founder needs the full case answer across linked controls."
            )
            if sequence_context and sequence_context.get("note"):
                note = f"{note} {str(sequence_context['note'])}"

            has_module_outcomes = bool(get_outcome_paths_profile(parent.relative_to(REPO_ROOT).as_posix()))
            module_has_watch = brief_has_escalation_triggers(parent / "README.md")
            path_anchor = path_focus_href
            module_outcome_local, module_outcome_external = get_outcome_path_scope_counts(parent)
            module_outcome_focus_href = (
                "#module-outcome-room-paths"
                if module_outcome_local and module_outcome_external
                else "#module-outcome-paths"
            )
            room_decision_stat: tuple[str, str] | tuple[str, str, str, str]
            if has_module_outcomes:
                room_decision_stat = (room_decision, "Room Decision", module_outcome_focus_href, "stat-mini--outcome")
            else:
                room_decision_stat = (room_decision, "Room Decision")
            escalation_stat: tuple[str, str] | tuple[str, str, str, str]
            if module_has_watch:
                escalation_stat = (room_escalation, "Escalation Rhythm", "#module-escalation-trigger-01", "stat-mini--watch")
            else:
                escalation_stat = (room_escalation, "Escalation Rhythm")

            stats: list[tuple[str, str] | tuple[str, str, str, str]] = [
                (module_pill.replace(" Module", ""), "Module Role", "#module-brief-snapshot", "stat-mini--brief"),
                (path_value, "Room Path", path_anchor, "stat-mini--path"),
                room_decision_stat,
                escalation_stat,
            ]
            if sequence_context and sequence_context.get("position_value"):
                stats.insert(
                    2,
                    (
                        str(sequence_context["position_value"]),
                        "Sequence Position",
                        sequence_current_href,
                        "stat-mini--sequence",
                    ),
                )

            return {
                "title": module_title,
                "area": module_pill,
                "copy": module_copy,
                "note": note,
                "breadcrumb_label": module_title,
                "pills": [
                    str(room_profile["pills"][0]),
                    module_pill,
                    path_pill_item,
                    *sequence_pills,
                    (
                        room_short,
                        "meta-pill meta-pill--nav-room-route meta-pill--link",
                        get_room_entry_href(directory, parent),
                    ),
                ],
                "stats": stats,
                "actions": actions,
            }

    return None


def build_default_portal_hero_stats(
    directory: Path,
    docs_for_dir: list[dict[str, str]],
    child_dirs: list[Path],
) -> list[tuple[object, ...]]:
    if directory == REPO_ROOT:
        system_metrics = get_system_layer_metrics(directory)
        return [
            (
                system_metrics["operating_hub_count"],
                count_label(system_metrics["operating_hub_count"], "Operating Hub"),
                "#room-modules",
                "stat-mini--surface",
            ),
            (
                system_metrics["founder_cadence_count"],
                count_label(system_metrics["founder_cadence_count"], "Founder Cadence"),
                "06_dashboard/14_weekly-executive-review/Weekly-Executive-Operating-Review.html",
                "stat-mini--docs",
            ),
            (
                system_metrics["live_control_route_count"],
                count_label(system_metrics["live_control_route_count"], "Live Control Route"),
                "06_dashboard/33_control-routing/Founder-Control-Routing-Matrix.html",
                "stat-mini--route",
            ),
        ]

    relative = directory.relative_to(REPO_ROOT).as_posix()
    if relative == BRAND_GUIDELINES_RELATIVE:
        guidance_metrics = get_brand_guidelines_metrics(directory)
        return [
            (
                guidance_metrics["guidance_count"],
                count_label(guidance_metrics["guidance_count"], "Guidance Standard"),
                "#supporting-files",
                "stat-mini--docs",
            ),
            (
                guidance_metrics["governance_surface_count"],
                count_label(guidance_metrics["governance_surface_count"], "Governance Surface"),
                "../03_exports/01_visual-standard/OPEN-HERE.html",
                "stat-mini--surface",
            ),
            (
                guidance_metrics["reference_layer_count"],
                count_label(guidance_metrics["reference_layer_count"], "Reference Layer"),
                "../03_exports/OPEN-HERE.html",
                "stat-mini--route",
            ),
        ]
    if relative == EXPORTS_RELATIVE:
        export_metrics = get_exports_metrics(directory)
        return [
            (
                export_metrics["benchmark_count"],
                count_label(export_metrics["benchmark_count"], "Preview Benchmark"),
                "./02_preview-docs/index.html#full-catalog",
                "stat-mini--route",
            ),
            (
                export_metrics["domain_lane_count"],
                count_label(export_metrics["domain_lane_count"], "Domain Lane"),
                "./02_preview-docs/index.html#full-catalog",
                "stat-mini--surface",
            ),
            (
                export_metrics["reference_surface_count"],
                count_label(export_metrics["reference_surface_count"], "Reference Surface"),
                "#room-modules",
                "stat-mini--docs",
            ),
        ]
    if relative == VISUAL_STANDARD_RELATIVE:
        preview_metrics = get_preview_hub_metrics(REPO_ROOT / PREVIEW_DOCS_RELATIVE)
        return [
            (
                1,
                "Standard Memo",
                "#supporting-files",
                "stat-mini--docs",
            ),
            (
                preview_metrics["benchmark_count"],
                count_label(preview_metrics["benchmark_count"], "Preview Benchmark"),
                "../02_preview-docs/index.html#full-catalog",
                "stat-mini--route",
            ),
            (
                1,
                "Export Hub",
                "../OPEN-HERE.html",
                "stat-mini--surface",
            ),
        ]
    if relative == PREVIEW_DOCS_RELATIVE:
        preview_metrics = get_preview_hub_metrics(directory)
        return [
            (
                preview_metrics["benchmark_count"],
                count_label(preview_metrics["benchmark_count"], "Preview Benchmark"),
                "./index.html#full-catalog",
                "stat-mini--route",
            ),
            (
                preview_metrics["domain_lane_count"],
                count_label(preview_metrics["domain_lane_count"], "Domain Lane"),
                "./index.html#full-catalog",
                "stat-mini--surface",
            ),
            (
                preview_metrics["brand_anchor_count"],
                count_label(preview_metrics["brand_anchor_count"], "Brand Anchor"),
                "./index.html#brand-anchors",
                "stat-mini--docs",
            ),
        ]
    if relative == INSPECTIONS_RELATIVE:
        return [
            (
                len(child_dirs),
                count_label(len(child_dirs), "Governed Case"),
                "#room-modules",
                "stat-mini--surface",
            ),
            (
                3,
                "Fast Routes",
                "#featured-routes",
                "stat-mini--route",
            ),
            (
                1,
                "Compliance Control",
                "../../06_dashboard/04_compliance/Daily-Compliance-Control-Center.html",
                "stat-mini--docs",
            ),
        ]
    brief_count = sum(
        1
        for doc in docs_for_dir
        if (build_doc_card_profile(directory, Path(str(doc["path"]))) or {}).get("kind") == "Executive Brief"
    )
    readable_count = sum(
        1
        for doc in docs_for_dir
        if (build_doc_card_profile(directory, Path(str(doc["path"]))) or {}).get("kind") != "Executive Brief"
    )
    route_layers: list[tuple[str, str]] = []
    if get_decision_sequence_profile(relative):
        route_layers.append(("Decision Sequence", "#decision-sequence"))
    if get_outcome_paths_profile(relative):
        route_layers.append(("Outcome Paths", "#outcome-paths"))
    if brief_has_escalation_triggers(directory / "README.md"):
        route_layers.append(("Escalation Watch", "#escalation-watch"))

    stats: list[tuple[object, ...]] = []
    if brief_count:
        stats.append((brief_count, count_label(brief_count, "Executive Brief"), "#founder-start-here", "stat-mini--brief"))
    if child_dirs:
        stats.append((len(child_dirs), count_label(len(child_dirs), "Live Folder"), "#room-modules", "stat-mini--surface"))
    if route_layers:
        stats.append((len(route_layers), count_label(len(route_layers), "Route Layer"), route_layers[0][1], "stat-mini--route"))
    if readable_count and len(stats) < 3:
        stats.append((readable_count, count_label(readable_count, "Readable File"), "#supporting-files", "stat-mini--docs"))
    if len(stats) < 3:
        stats.append((1, "Source Integrity", "#visual-system", "stat-mini--system"))
    return stats[:3]


def build_default_portal_hero_actions(
    directory: Path,
    docs_for_dir: list[dict[str, str]],
    child_dirs: list[Path],
) -> list[tuple[str, str, str]]:
    if directory == REPO_ROOT:
        return [
            ("Open System Memo", "README.html", "primary"),
            ("Open Founder Dashboard", "06_dashboard/01_executive/Daily-Founder-Dashboard.html", "secondary"),
            ("Open Control Routing", "06_dashboard/33_control-routing/Founder-Control-Routing-Matrix.html", "secondary"),
            ("Open Executable Checks", "06_dashboard/40_executable-checks/Trust-Override-Executable-Check-Control-Board.html", "secondary"),
        ]

    relative = directory.relative_to(REPO_ROOT).as_posix()
    if relative == BRAND_GUIDELINES_RELATIVE:
        return [
            ("Open Brand Guidelines Memo", "./README.html", "primary"),
            ("Open Visual Standard", "../03_exports/01_visual-standard/OPEN-HERE.html", "secondary"),
            ("Open Exports", "../03_exports/OPEN-HERE.html", "secondary"),
        ]
    if relative == EXPORTS_RELATIVE:
        return [
            ("Open Preview Docs", "./02_preview-docs/OPEN-HERE.html", "primary"),
            ("Open Domain Lanes", "./02_preview-docs/index.html#full-catalog", "secondary"),
            ("Open Visual Standard", "./01_visual-standard/OPEN-HERE.html", "secondary"),
        ]
    if relative == VISUAL_STANDARD_RELATIVE:
        return [
            ("Open Visual Standard Memo", "./README.html", "primary"),
            ("Open Preview Docs", "../02_preview-docs/OPEN-HERE.html", "secondary"),
            ("Open Exports", "../OPEN-HERE.html", "secondary"),
        ]
    if relative == PREVIEW_DOCS_RELATIVE:
        return [
            ("Open Founder Pathways", "./index.html#founder-pathways", "primary"),
            ("Open Domain Lanes", "./index.html#full-catalog", "secondary"),
            ("Open Brand Anchors", "./index.html#brand-anchors", "secondary"),
        ]
    if relative == INSPECTIONS_RELATIVE:
        return [
            ("Open Complaint Case", "./COMP-2026-001_AtlanticFoods-Garlic-Claim/OPEN-HERE.html", "primary"),
            ("Open FDA Readiness", "./INSP-2026-001_FDA-Readiness-Review/OPEN-HERE.html", "secondary"),
            ("Open Compliance Control", "../../06_dashboard/04_compliance/Daily-Compliance-Control-Center.html", "secondary"),
        ]
    brief_count = sum(
        1
        for doc in docs_for_dir
        if (build_doc_card_profile(directory, Path(str(doc["path"]))) or {}).get("kind") == "Executive Brief"
    )
    readable_count = sum(
        1
        for doc in docs_for_dir
        if (build_doc_card_profile(directory, Path(str(doc["path"]))) or {}).get("kind") != "Executive Brief"
    )
    has_sequence = bool(get_decision_sequence_profile(relative))
    has_outcomes = bool(get_outcome_paths_profile(relative))
    has_watch = brief_has_escalation_triggers(directory / "README.md")

    candidates: list[tuple[str, str, str]] = []
    if brief_count:
        candidates.append(("Open Executive Brief", "#founder-start-here", "primary"))
    if has_sequence:
        candidates.append(("Open Decision Sequence", "#decision-sequence", "secondary"))
    if has_outcomes:
        candidates.append(("Open Outcome Paths", "#outcome-paths", "secondary"))
    if child_dirs:
        candidates.append(("Open Live Folders", "#room-modules", "secondary"))
    if readable_count:
        candidates.append(("Open Readable Layers", "#supporting-files", "secondary"))
    if has_watch:
        candidates.append(("Open Watch", "#escalation-watch", "secondary"))
    candidates.append(("Open Source Integrity", "#visual-system", "secondary"))

    deduped: list[tuple[str, str, str]] = []
    seen_targets: set[str] = set()
    for label, target, style in candidates:
        if target in seen_targets:
            continue
        seen_targets.add(target)
        deduped.append((label, target, style))

    if deduped and deduped[0][2] != "primary":
        first_label, first_target, _ = deduped[0]
        deduped[0] = (first_label, first_target, "primary")
    return deduped[:3]


def build_preview_benchmark_routes_section(directory: Path) -> str:
    if not is_preview_docs_directory(directory):
        return ""

    preview_metrics = get_preview_hub_metrics(directory)
    return f"""
        <section class="home-section" id="preview-benchmark-routes">
          <div class="section-heading">
            <p class="eyebrow">Preview Hub Routes</p>
            <h2 class="section-title">Open the preview hub through the entry routes that now govern founder review.</h2>
            <p class="section-copy">
              This layer already carries {preview_metrics["benchmark_count"]} preview benchmarks, {preview_metrics["pathway_count"]} curated founder pathways, {preview_metrics["domain_lane_count"]} benchmark domain lanes, and {preview_metrics["brand_anchor_count"]} approved brand anchors. Use the cards below to enter the right route instead of reopening the full static folder blind.
            </p>
          </div>
          <div class="route-grid">
            <article class="route-card">
              <div class="card-meta">
                <span class="meta-pill">Founder Paths</span>
                <span class="meta-pill">{preview_metrics["pathway_count"]} Curated Routes</span>
              </div>
              <h3 class="card-title">Founder Pathways</h3>
              <p class="card-copy">
                Start here when the founder wants the right review route fast instead of scanning the full benchmark library one file at a time.
              </p>
              <div class="route-links">
                <a class="button-secondary" href="index.html#founder-pathways">Open Founder Pathways</a>
                <a class="button-secondary" href="index.html#contained-movement-route">Contained Movement</a>
                <a class="button-secondary" href="founder-dashboard-preview.html">Executive Dashboard</a>
                <a class="button-secondary" href="founder-control-routing-matrix-preview.html">Control Routing</a>
              </div>
            </article>
            <article class="route-card">
              <div class="card-meta">
                <span class="meta-pill">Domain Lanes</span>
                <span class="meta-pill">{preview_metrics["domain_lane_count"]} Lane Entries</span>
              </div>
              <h3 class="card-title">Benchmark Domain Lanes</h3>
              <p class="card-copy">
                Use the domain lanes when the founder wants a curated library entry by operating theme instead of jumping directly into a single benchmark file.
              </p>
              <div class="route-links">
                <a class="button-secondary" href="index.html#full-catalog">Open Domain Lanes</a>
                <a class="button-secondary" href="index.html#benchmark-system-foundations">System Foundations Lane</a>
                <a class="button-secondary" href="index.html#benchmark-executive-control">Executive Control Lane</a>
                <a class="button-secondary" href="index.html#benchmark-institutional-outbound">Institutional Outbound Lane</a>
              </div>
            </article>
            <article class="route-card">
              <div class="card-meta">
                <span class="meta-pill">Benchmark Library</span>
                <span class="meta-pill">{preview_metrics["benchmark_count"]} Preview Benchmarks</span>
              </div>
              <h3 class="card-title">Benchmark Library</h3>
              <p class="card-copy">
                Use the benchmark library when the founder wants the full preview surface, not just the fast-path routes, and needs to jump directly into a specific document benchmark.
              </p>
              <div class="route-links">
                <a class="button-secondary" href="index.html#full-catalog">Open Benchmark Library</a>
                <a class="button-secondary" href="commercial-invoice-preview.html">Commercial Invoice</a>
                <a class="button-secondary" href="official-document-transmittal-preview.html">Transmittal</a>
                <a class="button-secondary" href="monthly-strategic-business-review-preview.html">Monthly Review</a>
              </div>
            </article>
            <article class="route-card">
              <div class="card-meta">
                <span class="meta-pill">Reference Surface</span>
                <span class="meta-pill">{preview_metrics["brand_anchor_count"]} Brand Anchors</span>
              </div>
              <h3 class="card-title">Brand Anchors and Standards</h3>
              <p class="card-copy">
                Open the approved design anchors when the founder wants to confirm that preview benchmarks still inherit the right brand lineage and styling discipline.
              </p>
              <div class="route-links">
                <a class="button-secondary" href="index.html#brand-anchors">Open Brand Anchors</a>
                <a class="button-secondary" href="../01_visual-standard/OPEN-HERE.html">Open Visual Standard</a>
                <a class="button-secondary" href="README.html">Open Preview Docs Memo</a>
                <a class="button-secondary" href="../OPEN-HERE.html">Open Exports</a>
              </div>
            </article>
          </div>
        </section>
"""


def build_portal_html(directory: Path, docs_for_dir: list[dict[str, str]], child_dirs: list[Path], total_md: int, total_portals: int) -> str:
    def resolve_hero_action_href(target: str) -> str:
        if target.startswith("#"):
            return target
        if target.startswith("./") or target.startswith("../"):
            return target
        if "#" in target:
            path_part, anchor = target.split("#", 1)
            if path_part.startswith("./") or path_part.startswith("../"):
                return target
            return f"{relative_url(directory, REPO_ROOT / path_part)}#{anchor}"
        return relative_url(directory, REPO_ROOT / target)

    css_href = relative_url(directory, CSS_PATH)
    lockup_href = relative_url(directory, LOCKUP_PATH)
    preview_hub_href = relative_url(directory, PREVIEW_HUB_PATH)
    root_href = relative_url(directory, ROOT_INDEX_PATH)
    seal_href = relative_url(directory, SEAL_PATH)
    directory_label = humanize_surface_name(directory.name) if directory != REPO_ROOT else "UNYRA System"
    title = directory_label
    area = "System Hub" if directory == REPO_ROOT else AREA_LABELS.get(directory.parts[len(REPO_ROOT.parts)], "System")
    copy = (
        "Use this system hub to move between founder control, operating hubs, and live decision routes without dropping into raw repository structure."
        if directory == REPO_ROOT
        else f"Use this operating surface to review {directory_label} in the branded layer without dropping into repository structure."
    )
    hero_profile = build_portal_hero_context(directory)
    breadcrumbs = build_portal_breadcrumbs(directory, hero_profile)
    section_profile = build_portal_section_profile(directory)
    if hero_profile:
        title = str(hero_profile["title"])
        area = str(hero_profile["area"])
        copy = str(hero_profile["copy"])
    hero_context_section = ""
    if hero_profile:
        rendered_pills: list[str] = []
        for pill in hero_profile.get("pills", []):
            pill_label = str(pill)
            pill_class = "meta-pill"
            pill_href = ""
            if isinstance(pill, (tuple, list)):
                pill_label = str(pill[0])
                if len(pill) > 1 and pill[1]:
                    pill_class = str(pill[1])
                if len(pill) > 2 and pill[2]:
                    pill_href = str(pill[2])
            if pill_href:
                rendered_pills.append(
                    f'<a class="{html.escape(pill_class, quote=True)}" href="{html.escape(pill_href, quote=True)}">{html.escape(pill_label)}</a>'
                )
            else:
                rendered_pills.append(
                    f'<span class="{html.escape(pill_class, quote=True)}">{html.escape(pill_label)}</span>'
                )
        pills = "".join(rendered_pills)
        note = html.escape(str(hero_profile.get("note", "")))
        hero_context_section = f"""
            <div class="hero-context-strip">
              <div class="card-meta">
                {pills}
              </div>
              <p class="hero-context-note">{note}</p>
            </div>
"""
    hero_stats = (
        hero_profile.get("stats")
        if hero_profile and hero_profile.get("stats")
        else build_default_portal_hero_stats(directory, docs_for_dir, child_dirs)
    )
    rendered_stats: list[str] = []
    for stat in hero_stats:
        value = stat[0]
        label = stat[1]
        href = ""
        class_name = "stat-mini"
        if isinstance(stat, (tuple, list)):
            if len(stat) > 2 and stat[2]:
                href = resolve_hero_action_href(str(stat[2]))
                class_name += " stat-mini--link"
            if len(stat) > 3 and stat[3]:
                class_name += f" {str(stat[3])}"
        stat_inner = (
            f'<p class="stat-mini-value">{html.escape(str(value))}</p>'
            f'<p class="stat-mini-label">{html.escape(str(label))}</p>'
        )
        if href:
            rendered_stats.append(
                f"""
              <a class="{html.escape(class_name, quote=True)}" href="{html.escape(href, quote=True)}">
                {stat_inner}
              </a>"""
            )
        else:
            rendered_stats.append(
                f"""
              <div class="{html.escape(class_name, quote=True)}">
                {stat_inner}
              </div>"""
            )
    hero_stats_html = "".join(rendered_stats)
    hero_actions = hero_profile.get("actions") if hero_profile else None
    if hero_actions:
        button_row_html = "".join(
            f'<a class="button-{"primary" if str(style) == "primary" else "secondary"}" href="{html.escape(resolve_hero_action_href(str(target)), quote=True)}">{html.escape(str(label))}</a>'
            for label, target, style in hero_actions
        )
    else:
        button_row_html = "".join(
            f'<a class="button-{"primary" if str(style) == "primary" else "secondary"}" href="{html.escape(resolve_hero_action_href(str(target)), quote=True)}">{html.escape(str(label))}</a>'
            for label, target, style in build_default_portal_hero_actions(directory, docs_for_dir, child_dirs)
        )
    ordered_child_dirs = order_child_directories(directory, child_dirs)
    has_room_paths = bool(get_outcome_paths_profile(directory.relative_to(REPO_ROOT).as_posix()))
    path_order = get_outcome_path_order_map(directory.relative_to(REPO_ROOT).as_posix())
    folder_cards = []
    path_folder_entries: list[tuple[int, str, str, tuple[str, str | None]]] = []
    support_folder_cards: list[str] = []
    for child_dir in ordered_child_dirs:
        child_markdowns = [doc["path"] for doc in docs_for_dir if False]
        nested_docs = list(child_dir.glob("*.md"))
        nested_subdirs = [path for path in child_dir.iterdir() if path.is_dir() and path.name not in SKIP_DIR_NAMES]
        path_context = get_module_room_path_context(directory, child_dir) if has_room_paths else None
        anchor_id = f"room-path-{slugify_heading(str(path_context['pill']))}" if path_context else None
        card_html = build_folder_card(child_dir, directory, nested_docs, nested_subdirs, anchor_id=anchor_id)
        folder_cards.append(card_html)
        if path_context:
            pill_name = str(path_context["pill"])
            path_sequence = get_outcome_path_sequence(directory.relative_to(REPO_ROOT).as_posix(), pill_name)
            path_folder_entries.append(
                (
                    path_order.get(pill_name, len(path_order)),
                    pill_name,
                    card_html,
                    (f"{path_sequence[0]:02d} {pill_name} Path", f"#{anchor_id}" if anchor_id else None),
                )
            )
        else:
            support_folder_cards.append(card_html)

    path_folder_cards = [entry[2] for entry in sorted(path_folder_entries, key=lambda item: (item[0], item[1]))]
    path_folder_pills = [entry[3] for entry in sorted(path_folder_entries, key=lambda item: (item[0], item[1]))]

    priority_brief_docs = [
        doc
        for doc in docs_for_dir
        if (build_doc_card_profile(directory, Path(str(doc["path"]))) or {}).get("kind") == "Executive Brief"
    ]
    docs_for_cards = [
        doc
        for doc in docs_for_dir
        if (build_doc_card_profile(directory, Path(str(doc["path"]))) or {}).get("kind") != "Executive Brief"
    ] if priority_brief_docs else docs_for_dir
    if directory == REPO_ROOT:
        docs_for_cards = [
            doc
            for doc in docs_for_cards
            if Path(str(doc["path"])).name != "AGENTS.md"
        ]
    has_folder_section = bool(folder_cards)
    doc_cards = [
        build_doc_card(Path(doc["path"]), directory, doc["title"], doc["subtitle"], doc["kind"])
        for doc in docs_for_cards
    ]
    has_docs_section = bool(doc_cards)
    priority_brief_section = build_priority_brief_section(directory, docs_for_dir)
    decision_sequence_section = build_decision_sequence_section(directory)
    outcome_paths_section = build_outcome_paths_section(directory)
    escalation_watch_section = build_escalation_watch_section(directory, docs_for_dir)
    room_module_stack_section = build_room_module_stack_section(directory)
    module_brief_snapshot_section = build_module_brief_snapshot_section(directory)
    module_sequence_context_section = build_module_sequence_context_section(directory)
    module_outcome_paths_section = build_module_outcome_paths_section(directory)
    module_escalation_watch_section = build_module_escalation_watch_section(directory)
    module_decision_support_section = build_module_decision_support_section(directory)
    module_related_rooms_section = build_module_related_rooms_section(directory)
    room_navigation_section = build_portal_room_navigation(
        directory,
        has_folder_section,
        has_docs_section,
        bool(escalation_watch_section),
    )
    module_navigation_section = build_module_portal_navigation(
        directory,
        has_folder_section,
        has_docs_section,
        bool(module_brief_snapshot_section),
        bool(module_sequence_context_section),
        bool(room_module_stack_section),
        bool(module_outcome_paths_section),
        bool(module_escalation_watch_section),
        bool(module_decision_support_section),
        bool(module_related_rooms_section),
    )
    folders_eyebrow = section_profile.get("folders_eyebrow", "Folder Surface") if section_profile else "Folder Surface"
    folders_title = section_profile.get("folders_title", "Open the next operating surfaces through branded folder views.") if section_profile else "Open the next operating surfaces through branded folder views."
    folders_copy = section_profile.get(
        "folders_copy",
        "These folder cards carry the next rooms, modules, or system layers so the founder can move deeper without dropping into repository structure.",
    ) if section_profile else "These folder cards carry the next rooms, modules, or system layers so the founder can move deeper without dropping into repository structure."
    folder_section = (
        f"""
        <section class="home-section" id="room-modules">
          <div class="section-heading">
            <p class="eyebrow">{html.escape(folders_eyebrow)}</p>
            <h2 class="section-title">{html.escape(folders_title)}</h2>
            <p class="section-copy">
              {html.escape(folders_copy)}
            </p>
          </div>
          {(
            build_module_group_panel(
                "Live Path Modules",
                "Start with the modules that currently carry the room answer.",
                "These modules currently hold the active room path, so they should be scanned before supporting controls when the founder needs the live case answer fast.",
                path_folder_cards,
                anchor_id="room-live-path-modules",
                summary_pills=[(format_count_label(len(path_folder_cards), "Active Path"), None), *list(dict.fromkeys(path_folder_pills))],
                current_path=True,
            )
            + build_module_group_panel(
                "Supporting Controls",
                "Use supporting controls to confirm or tighten the live path.",
                "These modules support the active room answer with checks, proof, exposure logic, or follow-through before the founder widens movement.",
                support_folder_cards,
                anchor_id="room-supporting-controls",
                summary_pills=[(format_count_label(len(support_folder_cards), "Supporting Control"), None), ("Confirmation Layer", None)] if support_folder_cards else None,
                current_path=False,
            )
            if has_room_paths and path_folder_cards
            else f'''<div class="viewer-grid">{"".join(folder_cards)}</div>'''
          )}
        </section>
"""
        if folder_cards
        else ""
    )
    if priority_brief_docs and doc_cards:
        docs_eyebrow = "Supporting Layers"
        docs_title = "Open supporting readable layers after the executive brief."
        docs_copy = "The founder memo already holds first-reading priority, so the cards below focus on supporting records and secondary reading layers."
    else:
        docs_eyebrow = section_profile.get("docs_eyebrow", "Readable Layers") if section_profile else "Readable Layers"
        docs_title = section_profile.get("docs_title", "Open the readable layers that carry narrative, support, and source context.") if section_profile else "Open the readable layers that carry narrative, support, and source context."
        docs_copy = section_profile.get(
            "docs_copy",
            "These cards keep the founder in the branded reading layer while the underlying source stays protected in the repository.",
        ) if section_profile else "These cards keep the founder in the branded reading layer while the underlying source stays protected in the repository."
    docs_section = (
        f"""
        <section class="home-section" id="supporting-files">
          <div class="section-heading">
            <p class="eyebrow">{html.escape(docs_eyebrow)}</p>
            <h2 class="section-title">{html.escape(docs_title)}</h2>
            <p class="section-copy">
              {html.escape(docs_copy)}
            </p>
          </div>
          <div class="viewer-grid">
            {"".join(doc_cards)}
          </div>
        </section>
"""
        if doc_cards
        else ""
    )
    area_routes_section = build_area_routes_section(directory)
    preview_benchmark_routes_section = build_preview_benchmark_routes_section(directory)
    root_routes_section = (
        """
        <section class="home-section" id="founder-fast-routes">
          <div class="section-heading">
            <p class="eyebrow">Founder Fast Routes</p>
            <h2 class="section-title">Start with the right path, not the full tree.</h2>
            <p class="section-copy">
              These routes shorten the distance from the repository root to the most important control stacks inside the premium visual layer.
            </p>
          </div>
          <div class="route-grid">
            <article class="route-card">
              <div class="card-meta">
                <span class="meta-pill">Contained</span>
                <span class="meta-pill">Movement</span>
              </div>
              <h3 class="card-title">Contained Movement Trail</h3>
              <p class="card-copy">
                Open this route when movement is constrained and the founder needs one clean path from executable checks and risk logic to outward wording and live operational gates.
              </p>
              <div class="route-links">
                <a class="button-secondary" href="00_brand/03_exports/02_preview-docs/index.html#contained-movement-route">Open Hub Route</a>
                <a class="button-secondary" href="00_brand/03_exports/02_preview-docs/trust-override-executable-check-board-preview.html">Executable Checks</a>
                <a class="button-secondary" href="00_brand/03_exports/02_preview-docs/executive-scenario-contingency-review-preview.html">Scenario Response</a>
                <a class="button-secondary" href="00_brand/03_exports/02_preview-docs/official-document-transmittal-preview.html">Transmittal</a>
              </div>
            </article>
            <article class="route-card">
              <div class="card-meta">
                <span class="meta-pill">Outbound</span>
                <span class="meta-pill">Institutional</span>
              </div>
              <h3 class="card-title">Institutional Outbound Route</h3>
              <p class="card-copy">
                Use this route when UNYRA is preparing customer or supplier-facing material and the founder wants the send-ready layer to feel bank-grade and fully controlled.
              </p>
              <div class="route-links">
                <a class="button-secondary" href="00_brand/03_exports/02_preview-docs/index.html#founder-pathways">Open Hub Pathways</a>
                <a class="button-secondary" href="00_brand/03_exports/02_preview-docs/official-document-transmittal-preview.html">Transmittal</a>
                <a class="button-secondary" href="00_brand/03_exports/02_preview-docs/institutional-trade-correspondence-preview.html">Correspondence</a>
                <a class="button-secondary" href="00_brand/03_exports/02_preview-docs/communication-release-checklist-preview.html">Release Checklist</a>
              </div>
            </article>
            <article class="route-card">
              <div class="card-meta">
                <span class="meta-pill">Templates</span>
                <span class="meta-pill">Live Gates</span>
              </div>
              <h3 class="card-title">Core Execution Docs</h3>
              <p class="card-copy">
                Open this route when the founder wants to inspect the underlying commercial and operational source documents that now carry movement posture, stop rules, and next safe movement.
              </p>
              <div class="route-links">
                <a class="button-secondary" href="00_brand/03_exports/02_preview-docs/proforma-invoice-preview.html">Proforma</a>
                <a class="button-secondary" href="00_brand/03_exports/02_preview-docs/purchase-order-preview.html">Purchase Order</a>
                <a class="button-secondary" href="00_brand/03_exports/02_preview-docs/shipping-instructions-preview.html">Shipping Instructions</a>
                <a class="button-secondary" href="00_brand/03_exports/02_preview-docs/sales-contract-preview.html">Sales Contract</a>
              </div>
            </article>
          </div>
        </section>
"""
        if directory == REPO_ROOT
        else ""
    )

    active_deal_module = get_active_deal_module_context(directory)
    active_shipment_module = get_active_shipment_module_context(directory)
    active_account_module = get_active_account_module_context(directory)
    active_claim_module = get_active_claim_module_context(directory)
    supplier_approval_module = get_supplier_approval_module_context(directory)
    active_deal_room_return = get_active_deal_room_return_context(directory)
    active_shipment_room_return = get_active_shipment_room_return_context(directory)
    active_account_room_return = get_active_account_room_return_context(directory)
    active_claim_room_return = get_active_claim_room_return_context(directory)
    fda_readiness_room_return = get_fda_readiness_room_return_context(directory)
    supplier_approval_room_return = get_supplier_approval_room_return_context(directory)
    relative = directory.relative_to(REPO_ROOT).as_posix() if directory != REPO_ROOT else ""
    deal_portal_return = get_deal_portal_return_profile(relative)
    if active_deal_module:
        integrity_eyebrow = "Return Surface"
        integrity_title = f"Close {str(active_deal_module['module_title'])} back into the live deal routes."
        integrity_copy = f"This portal keeps {str(active_deal_module['module_title']).lower()} connected to the module memo, {str(active_deal_module['room_title'])}, Active Deals, and the wider deals hub instead of ending on generic repository framing."
        integrity_card_one_title = "Live room stays connected"
        integrity_card_one_copy = f"{str(active_deal_module['room_title'])} remains the governed case room behind this module, so founder review can return to the full live answer whenever a single control view stops being enough."
        integrity_card_two_title = "Commercial lane stays visible"
        integrity_card_two_copy = "When this module resolves, the founder can step back into Active Deals or the wider deals hub without losing the live commercial map."
    elif active_shipment_module:
        integrity_eyebrow = "Return Surface"
        integrity_title = f"Close {str(active_shipment_module['module_title'])} back into the live shipment routes."
        integrity_copy = f"This portal keeps {str(active_shipment_module['module_title']).lower()} connected to the module memo, {str(active_shipment_module['room_title'])}, Active Shipments, and the wider shipments hub instead of ending on generic repository framing."
        integrity_card_one_title = "Live shipment room stays connected"
        integrity_card_one_copy = f"{str(active_shipment_module['room_title'])} remains the governed movement room behind this module, so founder review can return to the full live answer whenever a single shipment control view stops being enough."
        integrity_card_two_title = "Movement lane stays visible"
        integrity_card_two_copy = "When this module resolves, the founder can step back into Active Shipments or the wider shipments hub without losing the live movement map."
    elif active_account_module:
        integrity_eyebrow = "Return Surface"
        integrity_title = f"Close {str(active_account_module['module_title'])} back into the live account routes."
        integrity_copy = f"This portal keeps {str(active_account_module['module_title']).lower()} connected to the module memo, {str(active_account_module['room_title'])}, Customers, and the wider CRM hub instead of ending on generic repository framing."
        integrity_card_one_title = "Live account room stays connected"
        integrity_card_one_copy = f"{str(active_account_module['room_title'])} remains the governed counterparty room behind this module, so founder review can return to the full live answer whenever a single account control view stops being enough."
        integrity_card_two_title = "Counterparty lane stays visible"
        integrity_card_two_copy = "When this module resolves, the founder can step back into Customers or the wider CRM hub without losing the live counterparty map."
    elif active_claim_module:
        integrity_eyebrow = "Return Surface"
        integrity_title = f"Close {str(active_claim_module['module_title'])} back into the live claim routes."
        integrity_copy = f"This portal keeps {str(active_claim_module['module_title']).lower()} connected to the module memo, {str(active_claim_module['room_title'])}, Inspection Cases, and the wider Compliance hub instead of ending on generic repository framing."
        integrity_card_one_title = "Live claim room stays connected"
        integrity_card_one_copy = f"{str(active_claim_module['room_title'])} remains the governed case room behind this module, so founder review can return to the full live answer whenever a single claim control view stops being enough."
        integrity_card_two_title = "Case lane stays visible"
        integrity_card_two_copy = "When this module resolves, the founder can step back into Inspection Cases or the wider Compliance hub without losing the governed case map."
    elif supplier_approval_module:
        integrity_eyebrow = "Return Surface"
        integrity_title = f"Close {str(supplier_approval_module['module_title'])} back into the governed supplier routes."
        integrity_copy = f"This portal keeps {str(supplier_approval_module['module_title']).lower()} connected to the module memo, {str(supplier_approval_module['room_title'])}, Supplier Approval, Compliance, and the board that confirms the next supplier answer instead of ending on generic repository framing."
        integrity_card_one_title = "Supplier room stays connected"
        integrity_card_one_copy = f"{str(supplier_approval_module['room_title'])} remains the governed supplier room behind this module, so founder review can return to the full approval narrative whenever one control track stops being enough."
        integrity_card_two_title = "Lane and board stay visible"
        integrity_card_two_copy = "When this module resolves, the founder can step back into Supplier Approval, Compliance, and the linked executive board without losing the supplier-governance map."
    elif active_deal_room_return:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close this deal room on the routes that keep the commercial stack coherent."
        integrity_copy = "This war room now closes on the deal brief, the live deal lane, the wider deals hub, and preview docs instead of ending on generic source framing."
        integrity_card_one_title = "Deal brief stays connected"
        integrity_card_one_copy = "The executive brief remains the controlled founder reading layer behind this room, so the room can widen without losing the live narrative."
        integrity_card_two_title = "Lane and hub stay visible"
        integrity_card_two_copy = "When the room answer is ready to widen, the founder can move into Active Deals, the wider deals hub, or preview docs without losing the live commercial map."
    elif deal_portal_return:
        integrity_eyebrow = str(deal_portal_return["eyebrow"])
        integrity_title = str(deal_portal_return["title"])
        integrity_copy = str(deal_portal_return["copy"])
        integrity_card_one_title = str(deal_portal_return["card_one_title"])
        integrity_card_one_copy = str(deal_portal_return["card_one_copy"])
        integrity_card_two_title = str(deal_portal_return["card_two_title"])
        integrity_card_two_copy = str(deal_portal_return["card_two_copy"])
    elif active_shipment_room_return:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close this shipment room on the routes that keep movement control coherent."
        integrity_copy = "This war room now closes on the shipment brief, the live shipment lane, the wider shipments hub, and the shipment control tower instead of ending on generic source framing."
        integrity_card_one_title = "Shipment brief stays connected"
        integrity_card_one_copy = "The executive brief remains the controlled founder reading layer behind this room, so movement decisions can widen without losing the live shipment narrative."
        integrity_card_two_title = "Lane and board stay visible"
        integrity_card_two_copy = "When the room answer is ready to widen, the founder can move into Active Shipments, the wider shipments hub, or the shipment control tower without losing the live movement map."
    elif active_account_room_return:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close this account room on the routes that keep counterparty control coherent."
        integrity_copy = "This war room now closes on the account brief, the customers lane, the wider CRM hub, and the customer account review board instead of ending on generic source framing."
        integrity_card_one_title = "Account brief stays connected"
        integrity_card_one_copy = "The executive brief remains the controlled founder reading layer behind this room, so account decisions can widen without losing the live counterparty narrative."
        integrity_card_two_title = "Lane and board stay visible"
        integrity_card_two_copy = "When the room answer is ready to widen, the founder can move into Customers, the wider CRM hub, or the customer account review board without losing the live counterparty map."
    elif active_claim_room_return:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close this claim room on the routes that keep complaint governance coherent."
        integrity_copy = "This war room now closes on the claim brief, the inspection-case lane, the wider compliance hub, and claims recovery instead of ending on generic source framing."
        integrity_card_one_title = "Claim brief stays connected"
        integrity_card_one_copy = "The executive brief remains the controlled founder reading layer behind this room, so complaint decisions can widen without losing the live claim narrative."
        integrity_card_two_title = "Lane and board stay visible"
        integrity_card_two_copy = "When the room answer is ready to widen, the founder can move into Inspection Cases, the wider Compliance hub, or Claims Recovery without losing the governed case map."
    elif fda_readiness_room_return:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close this readiness room on the routes that keep inspection governance coherent."
        integrity_copy = "This readiness room now closes on the readiness brief, the inspection-case lane, the wider compliance hub, and compliance control instead of ending on generic source framing."
        integrity_card_one_title = "Readiness brief stays connected"
        integrity_card_one_copy = "The executive brief remains the controlled founder reading layer behind this room, so readiness decisions can widen without losing the live response narrative."
        integrity_card_two_title = "Lane and control board stay visible"
        integrity_card_two_copy = "When the readiness answer is ready to widen, the founder can move into Inspection Cases, the wider Compliance hub, or Compliance Control without losing the governed inspection map."
    elif supplier_approval_room_return:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close this supplier room on the routes that keep approval, performance, and resilience coherent."
        integrity_copy = "This supplier room now closes on the supplier brief, the supplier-approval lane, the wider compliance hub, and the supplier performance and resilience boards instead of ending on generic source framing."
        integrity_card_one_title = "Supplier brief stays connected"
        integrity_card_one_copy = "The executive brief remains the controlled founder reading layer behind this room, so supplier decisions can widen without losing the approval narrative."
        integrity_card_two_title = "Lane and boards stay visible"
        integrity_card_two_copy = "When the supplier answer is ready to widen, the founder can move into Supplier Approval, the wider Compliance hub, Supplier Performance, or Supply Resilience without losing the governed supplier map."
    elif directory.relative_to(REPO_ROOT).as_posix() == TRACEABILITY_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close the traceability lane on the routes that keep proof, audit readiness, and recovery consequence coherent."
        integrity_copy = "This traceability lane now closes on the live traceability room, the traceability brief, compliance control, and claims recovery instead of ending on generic source framing."
        integrity_card_one_title = "Traceability room stays connected"
        integrity_card_one_copy = "The governed Golden Harvest lot-path room remains the founder-ready answer behind this lane, so proof review can drop into the live lineage narrative without losing continuity."
        integrity_card_two_title = "Control and recovery stay visible"
        integrity_card_two_copy = "When the proof answer is ready to widen, the founder can move into Compliance Control, Claims Recovery, or the wider Compliance hub without losing the governed proof-chain map."
    elif directory.relative_to(REPO_ROOT).as_posix() == TRACEABILITY_ROOM_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close this traceability room on the routes that keep lot proof and challenge defense coherent."
        integrity_copy = "This traceability room now closes on the traceability brief, the traceability lane, compliance control, and claims recovery instead of ending on generic source framing."
        integrity_card_one_title = "Traceability brief stays connected"
        integrity_card_one_copy = "The executive brief remains the controlled founder reading layer behind this room, so proof decisions can widen without losing the live lot-path narrative."
        integrity_card_two_title = "Lane and boards stay visible"
        integrity_card_two_copy = "When the room answer is ready to widen, the founder can move into Traceability, Compliance Control, Claims Recovery, or the wider Compliance hub without losing the governed proof-chain map."
    elif is_dashboard_pack_directory(directory):
        primary_doc = get_dashboard_pack_primary_doc(directory)
        board_title = humanize_surface_name(primary_doc.stem) if primary_doc else humanize_surface_name(directory.name)
        integrity_eyebrow = "Return Surface"
        integrity_title = f"Close {board_title} on the dashboard routes that keep founder control coherent."
        integrity_copy = "This board portal now closes on the live board, the dashboard hub, and the fast-route stack instead of ending on generic source framing."
        integrity_card_one_title = "Board surface stays connected"
        integrity_card_one_copy = f"{board_title} remains the controlled dashboard readout behind this portal, so founder review can open the board directly without losing its dashboard family context."
        integrity_card_two_title = "Hub and routes stay visible"
        integrity_card_two_copy = "When the board answer needs wider posture, the founder can move back into Dashboards or Dashboard Fast Routes without falling into repository framing."
    elif directory.relative_to(REPO_ROOT).as_posix() == BRAND_RELATIVE:
        integrity_eyebrow = "Brand Return"
        integrity_title = "Close brand review on the routes that keep approved assets, guidance rules, and export governance coherent."
        integrity_copy = "This brand hub now closes on approved assets, brand guidelines, exports, and retained brand control instead of ending on generic source framing."
        integrity_card_one_title = "Approved assets stay connected"
        integrity_card_one_copy = "Assets remains the governed identity layer behind this hub, so founder review can open signatures, lockups, and protected visual sets without drifting into raw source custody."
        integrity_card_two_title = "Guidance and exports stay visible"
        integrity_card_two_copy = "Brand Guidelines and Exports remain adjacent to the hub, keeping written rules, visual standard, and benchmark surfaces tied to one governed brand system."
    elif directory.relative_to(REPO_ROOT).as_posix() == BRAND_GUIDELINES_RELATIVE:
        integrity_eyebrow = "Guidance Return"
        integrity_title = "Close brand guidelines on the routes that keep identity rules, document standards, and export governance aligned."
        integrity_copy = "This guidance hub now closes on approved assets, visual standard, exports, and preview benchmarks instead of ending on generic source framing."
        integrity_card_one_title = "Rule set stays actionable"
        integrity_card_one_copy = "The three guidance standards remain the controlled reading layer behind this hub, so founder review can move from identity, document, or voice rules into the right governed surface."
        integrity_card_two_title = "Assets and exports stay connected"
        integrity_card_two_copy = "Assets, Visual Standard, Exports, and Preview Docs remain adjacent, keeping approved marks, styling discipline, and benchmark output tied to one brand-governance spine."
    elif directory.relative_to(REPO_ROOT).as_posix() == "06_dashboard":
        integrity_eyebrow = "Dashboard Return"
        integrity_title = "Close dashboards on the routes that keep founder control, cadence review, and executable checks connected."
        integrity_copy = "This dashboard hub now closes on daily control, weekly cadence, control routing, and executable checks instead of ending on generic source framing."
        integrity_card_one_title = "Founder control stays connected"
        integrity_card_one_copy = "The Daily Founder Dashboard, Control Routing, and Executable Checks remain the core command spine behind this hub, so founder review can move from posture into action without scanning the full tree."
        integrity_card_two_title = "Cadence and evidence stay visible"
        integrity_card_two_copy = "Weekly Review, Monthly Review, Quarterly Plan, risk boards, and proof-linked execution watches remain adjacent, keeping summaries tied to accountable operating records."
    elif directory.relative_to(REPO_ROOT).as_posix() == EXPORTS_RELATIVE:
        integrity_eyebrow = "Export Return"
        integrity_title = "Close exports on the routes that keep benchmark routing, domain lanes, and visual governance coherent."
        integrity_copy = "This export hub now closes on preview docs, domain lanes, visual standard, and benchmark governance instead of ending on generic source framing."
        integrity_card_one_title = "Benchmark hub stays connected"
        integrity_card_one_copy = "Preview Docs remains the governed founder-facing library behind this hub, so review can move from export overview into benchmark pathways without opening raw generated folders."
        integrity_card_two_title = "Visual standard stays visible"
        integrity_card_two_copy = "Visual Standard remains adjacent to exports, keeping styling discipline, domain lanes, and benchmark output tied to one controlled brand-governance route."
    elif directory.relative_to(REPO_ROOT).as_posix() == PREVIEW_DOCS_RELATIVE:
        integrity_eyebrow = "Preview Return"
        integrity_title = "Close preview docs on the routes that keep founder pathways, benchmark lanes, and brand anchors coherent."
        integrity_copy = "This preview-docs surface now closes on founder pathways, domain lanes, benchmark library, and brand anchors instead of ending on generic source framing."
        integrity_card_one_title = "Pathways stay connected"
        integrity_card_one_copy = "Founder Pathways remains the governed fast-entry route behind this surface, so review can move into the right decision lane before scanning the full benchmark library."
        integrity_card_two_title = "Benchmarks and anchors stay visible"
        integrity_card_two_copy = "Domain Lanes, Benchmark Library, and Brand Anchors remain adjacent, keeping each preview tied to approved visual lineage and founder-facing review logic."
    elif directory.relative_to(REPO_ROOT).as_posix() == VISUAL_STANDARD_RELATIVE:
        integrity_eyebrow = "Standard Return"
        integrity_title = "Close visual standard on the routes that keep styling discipline connected to benchmarks and exports."
        integrity_copy = "This visual-standard surface now closes on exports, preview docs, the stylesheet, and memo governance instead of ending on generic source framing."
        integrity_card_one_title = "Preview governance stays connected"
        integrity_card_one_copy = "Preview Docs remains adjacent to the standard, so founder review can verify how document chrome, route language, and benchmark styling appear in live examples."
        integrity_card_two_title = "Stylesheet custody stays clear"
        integrity_card_two_copy = "The visual standard keeps styling governance distinct from raw source custody, so premium presentation changes can be reviewed before they propagate across the branded layer."
    elif directory.relative_to(REPO_ROOT).as_posix() == ARCHIVE_RELATIVE:
        integrity_eyebrow = "Archive Return"
        integrity_title = "Close archive on the routes that keep retained history, closeout control, and retrieval ownership coherent."
        integrity_copy = "This archive hub now closes on archived CRM, archive closeout standards, closed matter retrieval, and retained-record functions instead of ending on generic source framing."
        integrity_card_one_title = "Retained history stays connected"
        integrity_card_one_copy = "Archived CRM remains the governed retained commercial lane behind this hub, so founder review can open concrete closed matters without disturbing active CRM."
        integrity_card_two_title = "Closeout control stays visible"
        integrity_card_two_copy = "Archive Closeout and closed-deal retrieval stay adjacent to the hub, keeping historical records tied to the standards that decide when a matter is truly ready to stay closed."
    elif directory.relative_to(REPO_ROOT).as_posix() == ARCHIVED_CRM_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close archived CRM on the routes that keep retained commercial memory coherent."
        integrity_copy = "This archive lane now closes on the closed deal room, the archive hub, archive closeout standards, and live CRM reference instead of ending on generic source framing."
        integrity_card_one_title = "Closed deal room stays connected"
        integrity_card_one_copy = "The retained Atlantic Foods room remains the founder-ready archive answer behind this lane, so review can open final commercial history without losing archive context."
        integrity_card_two_title = "Archive and CRM stay visible"
        integrity_card_two_copy = "When the retained answer needs wider posture, the founder can move into Archive, Archive Closeout, or live CRM reference without disturbing the closed record."
    elif directory.relative_to(REPO_ROOT).as_posix() == ARCHIVED_CLOSED_DEAL_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close this retained deal room on the routes that keep archive memory and commercial context coherent."
        integrity_copy = "This closed deal room now closes on the closed deal memo, archived CRM, the archive hub, and live CRM reference instead of ending on generic source framing."
        integrity_card_one_title = "Closed deal memo stays connected"
        integrity_card_one_copy = "The memo remains the controlled retained reading layer behind this room, so founder review can return to final proof and closeout posture without reopening the live deal."
        integrity_card_two_title = "Archive lane stays visible"
        integrity_card_two_copy = "When the retained matter needs wider context, the founder can move into Archived CRM, Archive, or live CRM reference without losing the closed commercial map."
    elif directory.relative_to(REPO_ROOT).as_posix() == WORKING_FILES_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close working files on the routes that keep temporary work moving toward governed ownership."
        integrity_copy = "This staging surface now closes on Operations, Active Shipments, and Operations Command instead of ending on generic source framing."
        integrity_card_one_title = "Staging memo stays connected"
        integrity_card_one_copy = "The memo remains the controlled rule layer behind this surface, so temporary files stay framed as staging inputs rather than final operating records."
        integrity_card_two_title = "Operating routes stay visible"
        integrity_card_two_copy = "When a support file settles, the founder can move it toward Operations, Active Shipments, or Operations Command without leaving unresolved records in the staging lane."
    elif directory.relative_to(REPO_ROOT).as_posix() == OPERATIONS_RELATIVE:
        integrity_eyebrow = "Operations Return"
        integrity_title = "Close operations on the routes that keep live execution, command control, and support files coherent."
        integrity_copy = "This operations hub now closes on active shipments, operations command, working files, and fast execution routes instead of ending on generic source framing."
        integrity_card_one_title = "Live movement stays connected"
        integrity_card_one_copy = "Active Shipments remains the governed execution lane behind this hub, so founder review can drop into release gates, packet proof, and shipment rooms without losing operating context."
        integrity_card_two_title = "Command and staging stay visible"
        integrity_card_two_copy = "Operations Command and Working Files stay adjacent to the hub, keeping same-day intervention and temporary support records tied to the governed execution map."
    elif directory.relative_to(REPO_ROOT).as_posix() == CRM_RELATIVE:
        integrity_eyebrow = "CRM Return"
        integrity_title = "Close CRM on the routes that keep counterparties, deal posture, and founder follow-through coherent."
        integrity_copy = "This CRM hub now closes on customer accounts, active deals, founder queue, and commercial fast routes instead of ending on generic source framing."
        integrity_card_one_title = "Commercial lanes stay connected"
        integrity_card_one_copy = "Customers, suppliers, deals, and tasks remain visible as one governed commercial map, so founder review can move from counterparty quality into live deal pressure without losing context."
        integrity_card_two_title = "Founder queue stays visible"
        integrity_card_two_copy = "The execution queue remains adjacent to relationship and deal posture, keeping follow-through, executable checks, and matter ownership tied to the CRM control surface."
    elif directory.relative_to(REPO_ROOT).as_posix() == COMPLIANCE_RELATIVE:
        integrity_eyebrow = "Compliance Return"
        integrity_title = "Close compliance on the routes that keep governed cases, supplier control, and proof readiness coherent."
        integrity_copy = "This compliance hub now closes on inspection cases, supplier approval, traceability, and compliance fast routes instead of ending on generic source framing."
        integrity_card_one_title = "Governed cases stay connected"
        integrity_card_one_copy = "Inspection cases and traceability remain visible as one proof-and-recovery map, so founder review can move from complaint containment into evidence control without losing regulatory context."
        integrity_card_two_title = "Supplier control stays visible"
        integrity_card_two_copy = "Supplier Approval remains adjacent to proof and inspection lanes, keeping continuity, fallback readiness, and approval confidence tied to the governed compliance surface."
    elif directory.relative_to(REPO_ROOT).as_posix() == LEADS_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close the lead lane on the routes that keep qualification, advancement, and escalation coherent."
        integrity_copy = "This lead lane now closes on the live lead room, the lead brief, the sales-pipeline board, and the founder queue instead of ending on generic source framing."
        integrity_card_one_title = "Lead room stays connected"
        integrity_card_one_copy = "The governed lead room remains the founder-ready answer behind this lane, so qualification review can drop into the live prospect narrative without losing continuity."
        integrity_card_two_title = "Lane and boards stay visible"
        integrity_card_two_copy = "When the lead answer is ready to widen, the founder can move into Sales Pipeline, Founder Queue, or the wider CRM hub without losing the qualification map."
    elif directory.relative_to(REPO_ROOT).as_posix() == CUSTOMERS_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close the customer lane on the routes that keep account trust, release exposure, and growth posture coherent."
        integrity_copy = "This customer lane now closes on the live account room, customer board, trust matrix, and CRM hub instead of ending on generic source framing."
        integrity_card_one_title = "Account room stays connected"
        integrity_card_one_copy = "The governed Atlantic Foods account room remains the founder-ready answer behind this lane, so customer review can drop into the live account narrative without losing continuity."
        integrity_card_two_title = "Lane and boards stay visible"
        integrity_card_two_copy = "When the customer answer is ready to widen, the founder can move into Customer Accounts, Trust Posture, Collections, or the wider CRM hub without losing the account-quality map."
    elif directory.relative_to(REPO_ROOT).as_posix() == LEAD_ROOM_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close this lead room on the routes that keep prospect qualification coherent."
        integrity_copy = "This lead room now closes on the lead brief, the leads lane, the wider CRM hub, and the boards that govern advancement and escalation instead of ending on generic source framing."
        integrity_card_one_title = "Lead brief stays connected"
        integrity_card_one_copy = "The executive brief remains the controlled founder reading layer behind this room, so qualification decisions can widen without losing the live prospect narrative."
        integrity_card_two_title = "Lane and boards stay visible"
        integrity_card_two_copy = "When the room answer is ready to widen, the founder can move into Leads, Sales Pipeline, Founder Queue, or the wider CRM hub without losing the governed lead map."
    elif directory.relative_to(REPO_ROOT).as_posix() == SUPPLIERS_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close the supplier lane on the routes that keep approval, performance, and continuity coherent."
        integrity_copy = "This supplier lane now closes on the live supplier room, the supplier brief, supplier approval, and the performance and resilience boards instead of ending on generic source framing."
        integrity_card_one_title = "Supplier room stays connected"
        integrity_card_one_copy = "The governed supplier room remains the founder-ready answer behind this lane, so sourcing review can drop into the live supplier narrative without losing continuity."
        integrity_card_two_title = "Lane and boards stay visible"
        integrity_card_two_copy = "When the supplier answer is ready to widen, the founder can move into Supplier Approval, Supplier Performance, Supply Resilience, or the wider CRM hub without losing the sourcing map."
    elif directory.relative_to(REPO_ROOT).as_posix() == SUPPLIER_ROOM_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close this supplier room on the routes that keep sourcing continuity coherent."
        integrity_copy = "This supplier room now closes on the supplier brief, the suppliers lane, the wider CRM hub, and the approval and performance surfaces that govern live sourcing posture instead of ending on generic source framing."
        integrity_card_one_title = "Supplier brief stays connected"
        integrity_card_one_copy = "The executive brief remains the controlled founder reading layer behind this room, so sourcing decisions can widen without losing the live supplier narrative."
        integrity_card_two_title = "Lane and boards stay visible"
        integrity_card_two_copy = "When the room answer is ready to widen, the founder can move into Suppliers, Supplier Approval, Supplier Performance, or the wider CRM hub without losing the governed sourcing map."
    elif directory.relative_to(REPO_ROOT).as_posix() == TASKS_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close the execution lane on the routes that keep gate closure and follow-through coherent."
        integrity_copy = "This execution lane now closes on the founder queue, the execution brief, executable checks, and owner accountability instead of ending on generic source framing."
        integrity_card_one_title = "Execution room stays connected"
        integrity_card_one_copy = "The governed founder queue remains the founder-ready answer behind this lane, so live execution review can drop into the active gate narrative without losing continuity."
        integrity_card_two_title = "Lane and boards stay visible"
        integrity_card_two_copy = "When the execution answer is ready to widen, the founder can move into Executable Checks, Owner Accountability, or the wider CRM hub without losing the governed queue map."
    elif directory.relative_to(REPO_ROOT).as_posix() == TASK_ROOM_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close this execution room on the routes that keep gate closure and owner accountability coherent."
        integrity_copy = "This execution room now closes on the execution brief, the tasks lane, the wider CRM hub, and the boards that govern executable checks and follow-through instead of ending on generic source framing."
        integrity_card_one_title = "Execution brief stays connected"
        integrity_card_one_copy = "The executive brief remains the controlled founder reading layer behind this room, so closure decisions can widen without losing the live execution narrative."
        integrity_card_two_title = "Lane and boards stay visible"
        integrity_card_two_copy = "When the room answer is ready to widen, the founder can move into Tasks, Executable Checks, Owner Accountability, or the wider CRM hub without losing the governed execution map."
    elif directory.relative_to(REPO_ROOT).as_posix() == BRAND_ASSETS_RELATIVE:
        integrity_eyebrow = "Asset Return"
        integrity_title = "Close asset custody on the routes that keep approved identity materials protected and reviewable."
        integrity_copy = "This asset hub now closes on brand governance, signature review, approved compositions, and protected source custody instead of ending on generic source framing."
        integrity_card_one_title = "Review surfaces stay connected"
        integrity_card_one_copy = "Brand Signatures and Approved Compositions remain the founder-ready surfaces behind this hub, so approved identity treatments can be reviewed without opening raw asset folders."
        integrity_card_two_title = "Protected assets stay authoritative"
        integrity_card_two_copy = "Logos, icons, imagery, lockups, and seals remain governed in their approved folders while this portal stays a navigation and review layer, not a replacement source of record."
    elif directory.relative_to(REPO_ROOT).as_posix() == "00_brand/01_assets/04_signatures":
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close brand signatures on the routes that keep approved signature use coherent."
        integrity_copy = "This signature surface now closes on the signatures memo, the assets hub, approved compositions, and the visual standard instead of ending on generic source framing."
        integrity_card_one_title = "Reference memo stays connected"
        integrity_card_one_copy = "The memo remains the controlled reading layer behind this surface, so founder review can widen without losing the approved signature narrative."
        integrity_card_two_title = "Assets and standard stay visible"
        integrity_card_two_copy = "When the founder needs wider posture, this surface now points directly into Assets, Approved Compositions, and Visual Standard instead of collapsing into repository framing."
    elif directory.relative_to(REPO_ROOT).as_posix() == "00_brand/01_assets/05_approved-compositions":
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close approved compositions on the routes that keep lockups and seals coherent."
        integrity_copy = "This composition surface now closes on the compositions memo, the assets hub, brand signatures, and the visual standard instead of ending on generic source framing."
        integrity_card_one_title = "Reference memo stays connected"
        integrity_card_one_copy = "The memo remains the controlled reading layer behind this surface, so founder review can widen without losing the approved lockup narrative."
        integrity_card_two_title = "Assets and signatures stay visible"
        integrity_card_two_copy = "When the founder needs wider posture, this surface now points directly into Assets, Brand Signatures, and Visual Standard instead of collapsing into repository framing."
    elif directory.relative_to(REPO_ROOT).as_posix() == SHIPMENTS_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close shipment navigation on the routes that keep live movement control coherent."
        integrity_copy = "This shipment hub now closes on active shipments, the live shipment room, operations, and the shipment control tower instead of ending on generic source framing."
        integrity_card_one_title = "Lane stays connected"
        integrity_card_one_copy = "Active Shipments remains the controlled movement lane behind this hub, so founder review can drop from route selection into live release and packet proof without losing continuity."
        integrity_card_two_title = "Operations stack stays visible"
        integrity_card_two_copy = "When the founder needs wider posture, the shipment hub now points directly back to Operations and the Shipment Control Tower instead of collapsing into repository framing."
    elif directory.relative_to(REPO_ROOT).as_posix() == ACTIVE_SHIPMENTS_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close the active shipment lane on the routes that keep contained movement coherent."
        integrity_copy = "This active-shipment lane now closes on the shipment brief, the live shipment room, the wider shipments hub, and the shipment control tower instead of ending on generic source framing."
        integrity_card_one_title = "Brief stays connected"
        integrity_card_one_copy = "The shipment brief remains the controlled reading layer behind this lane, so the founder can widen into release, packet, and containment logic without losing the live movement narrative."
        integrity_card_two_title = "Room and tower stay visible"
        integrity_card_two_copy = "When the lane answer is ready to widen, the founder can move into the live shipment room, the wider shipments hub, or the shipment control tower without losing the contained-movement map."
    elif directory.relative_to(REPO_ROOT).as_posix() == INSPECTIONS_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close inspection cases on the routes that keep complaint and readiness governance coherent."
        integrity_copy = "This case hub now closes on the complaint room, FDA readiness, and compliance control instead of ending on generic source framing."
        integrity_card_one_title = "Case lane stays connected"
        integrity_card_one_copy = "Complaint containment and FDA readiness remain together inside one governed inspection lane, so founder review can widen without losing case continuity."
        integrity_card_two_title = "Control board stays visible"
        integrity_card_two_copy = "When the founder needs wider posture, the inspection lane now points directly into Compliance and Compliance Control instead of falling back to repository framing."
    elif directory.relative_to(REPO_ROOT).as_posix() == SUPPLIER_APPROVAL_RELATIVE:
        integrity_eyebrow = "Return Surface"
        integrity_title = "Close supplier approval on the routes that keep supplier governance coherent."
        integrity_copy = "This supplier-approval hub now closes on the Golden Harvest room, supplier performance, supply resilience, and the wider compliance hub instead of ending on generic source framing."
        integrity_card_one_title = "Supplier room stays connected"
        integrity_card_one_copy = "The governed Golden Harvest room remains the founder-ready answer behind this hub, so approval review can drop into the live supplier narrative without losing continuity."
        integrity_card_two_title = "Boards stay visible"
        integrity_card_two_copy = "When the founder needs wider posture, this hub now points directly into Supplier Performance, Supply Resilience, and Compliance instead of collapsing into repository framing."
    elif is_templates_directory(directory):
        integrity_eyebrow = "Template Governance"
        integrity_title = "Keep the protected template system connected to the right drafting paths."
        integrity_copy = "This templates hub now closes on domain packs, fast routes, and founder-control drafting paths instead of ending on generic source framing."
        integrity_card_one_title = "Protected masters stay connected"
        integrity_card_one_copy = "Each template domain remains grouped as a governed master system, so founder review can widen across drafting families without losing custody of the protected source."
        integrity_card_two_title = "Routes stay visible"
        integrity_card_two_copy = "When the founder needs wider posture, this hub now points directly into fast routes and founder-control template packs instead of collapsing into repository framing."
    elif is_sops_directory(directory):
        integrity_eyebrow = "Procedure Governance"
        integrity_title = "Keep the SOP system connected to the right operating paths."
        integrity_copy = "This SOP hub now closes on procedure domains, fast routes, and founder operating standards instead of ending on generic source framing."
        integrity_card_one_title = "Governed procedures stay connected"
        integrity_card_one_copy = "Each SOP domain remains grouped as a governed operating rulebook, so founder review can widen across procedure families without losing discipline."
        integrity_card_two_title = "Routes stay visible"
        integrity_card_two_copy = "When the founder needs wider posture, this hub now points directly into fast procedure routes and founder cadence standards instead of collapsing into repository framing."
    elif directory != REPO_ROOT and directory.parent.relative_to(REPO_ROOT).as_posix() == "01_templates":
        integrity_eyebrow = "Template Governance"
        integrity_title = "Keep each protected template pack connected to the wider drafting system."
        integrity_copy = "This template domain now closes on the approved pack, the wider templates hub, and the fast drafting routes instead of ending on generic source framing."
        integrity_card_one_title = "Protected pack stays connected"
        integrity_card_one_copy = "Each master in this domain remains grouped inside one governed template pack, so founder review can move between approved formats without losing drafting continuity."
        integrity_card_two_title = "Hub and routes stay visible"
        integrity_card_two_copy = "When the founder needs wider posture, this domain now points directly into the Templates hub and its fast drafting routes instead of collapsing into repository framing."
    elif directory != REPO_ROOT and directory.parent.relative_to(REPO_ROOT).as_posix() == "05_sops":
        integrity_eyebrow = "Procedure Governance"
        integrity_title = "Keep each procedure domain connected to the wider operating rulebook."
        integrity_copy = "This procedure domain now closes on the governed stack, the wider SOP hub, and the fast procedure routes instead of ending on generic source framing."
        integrity_card_one_title = "Governed stack stays connected"
        integrity_card_one_copy = "Each procedure in this domain remains grouped inside one governed operating stack, so founder review can move between standards without losing control discipline."
        integrity_card_two_title = "Hub and routes stay visible"
        integrity_card_two_copy = "When the founder needs wider posture, this domain now points directly into the SOP hub and its fast procedure routes instead of collapsing into repository framing."
    else:
        integrity_eyebrow = "System Integrity" if directory == REPO_ROOT else "Source Integrity"
        integrity_title = (
            "Keep founder navigation premium while the operating record stays governed."
            if directory == REPO_ROOT
            else "Keep source protected, review in a premium layer."
        )
        integrity_copy = (
            "This entry layer gives the founder a cleaner system view while the repository remains the authoritative operating record behind every hub, memo, room, and control."
            if directory == REPO_ROOT
            else "These portals give the founder a cleaner reading surface while the editable repository remains the authoritative operating record behind every room, brief, and control."
        )
        integrity_card_one_title = "System source stays authoritative" if directory == REPO_ROOT else "Source layer stays authoritative"
        integrity_card_one_copy = (
            "Operating hubs, dashboards, templates, SOPs, and archives still remain governed in the repository. This root portal is a founder reading layer, not a second operating fork."
            if directory == REPO_ROOT
            else "Templates, dashboards, SOPs, and briefs remain the controlled system of record in the repository. These portals are a reading layer, not an editing fork."
        )
        integrity_card_two_title = "Visual layer stays synchronized" if directory == REPO_ROOT else "Branded layer stays synchronized"
        integrity_card_two_copy = (
            "When hubs, memos, rooms, or briefs change, the visual layer can be regenerated so founder navigation stays current without weakening the governed source."
            if directory == REPO_ROOT
            else "When rooms, modules, or briefs change, the branded layer can be regenerated so founder navigation stays current without rewriting the protected source."
        )

    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{html.escape(title)} | UNYRA Visual</title>
    {GENERATED_MARKER}
    <link rel="stylesheet" href="{css_href}" />
  </head>
  <body class="preview-shell">
    <main class="preview-home">
      <section class="hero-panel" id="room-top">
        <div class="hero-grid">
          <div class="hero-copy">
            <div class="breadcrumbs">{breadcrumbs}</div>
            <p class="eyebrow">{html.escape(area)}</p>
            <h1 class="hero-title">{html.escape(title)}</h1>
            <p class="hero-subtitle">{html.escape(copy)}</p>
            {hero_context_section}
            <div class="button-row">
              {button_row_html}
            </div>
            <div class="hero-stats">
              {hero_stats_html}
            </div>
          </div>
          <img
            class="lockup-lg"
            src="{lockup_href}"
            alt="UNYRA GROUP LLC approved horizontal lockup"
          />
        </div>
      </section>

      {root_routes_section}
      {room_navigation_section}
      {module_navigation_section}
      {module_brief_snapshot_section}
      {priority_brief_section}
      {decision_sequence_section}
      {outcome_paths_section}
      {escalation_watch_section}
      {module_sequence_context_section}
      {room_module_stack_section}
      {module_outcome_paths_section}
      {module_escalation_watch_section}
      {module_decision_support_section}
      {module_related_rooms_section}
      {area_routes_section}
      {preview_benchmark_routes_section}
      {folder_section}
      {docs_section}

      <section class="home-section" id="visual-system">
        <div class="section-heading">
          <p class="eyebrow">{html.escape(integrity_eyebrow)}</p>
          <h2 class="section-title">{html.escape(integrity_title)}</h2>
          <p class="section-copy">
            {html.escape(integrity_copy)}
          </p>
        </div>
        <div class="viewer-grid">
          <article class="viewer-card">
            <div class="card-meta">
              <span class="meta-pill">Protected</span>
              <span class="meta-pill">Authoritative</span>
            </div>
            <h3 class="viewer-card-title">{html.escape(integrity_card_one_title)}</h3>
            <p class="viewer-card-copy">
              {html.escape(integrity_card_one_copy)}
            </p>
          </article>
          <article class="viewer-card">
            <div class="card-meta">
              <span class="meta-pill">Refreshable</span>
              <span class="meta-pill">Current</span>
            </div>
            <h3 class="viewer-card-title">{html.escape(integrity_card_two_title)}</h3>
            <p class="viewer-card-copy">
              {html.escape(integrity_card_two_copy)}
            </p>
          </article>
          <article class="viewer-card">
            <div class="card-meta">
              <span class="meta-pill">Coverage</span>
              <span class="meta-pill">Current</span>
            </div>
            <h3 class="viewer-card-title">Coverage stays visible</h3>
            <p class="viewer-card-copy">
              This layer currently spans {total_md} branded document views and {total_portals} folder portals, so the founder can widen review without losing traceability.
            </p>
            <p class="doc-path">{total_md} branded views / {total_portals} folder portals</p>
          </article>
        </div>
      </section>
    </main>
  </body>
</html>
"""


def main() -> None:
    markdown_files = collect_markdown_files()
    directories = collect_directories(markdown_files)

    doc_registry: dict[Path, list[dict[str, str]]] = {directory: [] for directory in directories}

    for markdown_path in markdown_files:
        title, subtitle, meta, body_lines = extract_document_parts(markdown_path.read_text(encoding="utf-8"), humanize_slug(markdown_path.stem))
        doc_kind = detect_kind(markdown_path)
        if doc_kind == "Overview":
            title = get_overview_display_title(markdown_path.parent, title)
        body_lines_for_render = body_lines
        meta_for_cards = meta
        meta_cards = ""
        focus_panel_html = ""
        action_panel_html = ""
        reading_panel_html = ""
        decision_panel_html = ""
        trigger_panel_html = ""
        module_panel_html = ""
        usage_panel_html = ""
        support_panel_html = ""
        related_panel_html = ""
        source_panel_html = ""
        nav_panel_html = ""
        distribution_panel_html = ""
        body_html = ""
        brief_header_identity_html = ""
        if doc_kind == "Executive Brief":
            distribution_panel_html = render_brief_distribution_panel(meta, markdown_path.parent)
            immediate_actions = extract_section_list_items(body_lines, "Immediate Founder Actions")
            action_panel_html = render_brief_action_panel(immediate_actions, markdown_path.parent)
            if immediate_actions:
                body_lines_for_render = remove_section(body_lines, "Immediate Founder Actions")
            current_reading_rows = extract_section_table_rows(body_lines, "Current Reading")
            reading_panel_html = render_brief_reading_panel(current_reading_rows, markdown_path.parent)
            if current_reading_rows:
                body_lines_for_render = remove_section(body_lines_for_render, "Current Reading")
            decision_agenda_items = extract_section_list_items(body_lines, "Decision Agenda")
            decision_panel_html = render_brief_decision_panel(decision_agenda_items, markdown_path.parent)
            if decision_agenda_items:
                body_lines_for_render = remove_section(body_lines_for_render, "Decision Agenda")
            escalation_trigger_items = extract_section_list_items(body_lines, "Escalation Triggers")
            trigger_panel_html = render_brief_trigger_panel(escalation_trigger_items, markdown_path.parent)
            if escalation_trigger_items:
                body_lines_for_render = remove_section(body_lines_for_render, "Escalation Triggers")
            module_profiles = collect_brief_module_profiles(markdown_path.parent, body_lines)
            module_panel_html = render_brief_module_panel(module_profiles)
            if module_profiles:
                body_lines_for_render = remove_section(body_lines_for_render, "Core Modules In This Room")
            founder_usage_items = extract_section_list_items(body_lines, "Founder Usage Standard")
            usage_panel_html = render_brief_usage_panel(founder_usage_items, markdown_path.parent)
            if founder_usage_items:
                body_lines_for_render = remove_section(body_lines_for_render, "Founder Usage Standard")
            support_panel_html = render_brief_support_panel(collect_decision_support_links(markdown_path.parent))
            related_panel_html = render_brief_related_panel(collect_related_rooms(markdown_path.parent))
            body_html = render_markdown(body_lines_for_render, markdown_path.parent)
            if body_html == EMPTY_MARKDOWN_STATE_HTML:
                source_panel_html = render_brief_source_panel(markdown_path.parent, has_residual_body=False)
            source_layer_ready = True
            focus_panel_html = render_brief_focus_panel(
                meta,
                markdown_path.parent,
                source_layer_ready=source_layer_ready,
            )
            nav_items: list[tuple[str, str]] = []
            nav_items.append(("Brief Top", "brief-top"))
            if distribution_panel_html:
                nav_items.append(("Brief Distribution", "brief-distribution"))
            if focus_panel_html:
                nav_items.append(("Executive Focus", "executive-focus"))
            if action_panel_html:
                nav_items.append(("Immediate Founder Actions", "immediate-founder-actions"))
            if reading_panel_html:
                nav_items.append(("Current Reading", "current-reading"))
            if decision_panel_html:
                nav_items.append(("Decision Agenda", "decision-agenda"))
            if trigger_panel_html:
                nav_items.append(("Escalation Triggers", "escalation-triggers"))
            if module_panel_html:
                nav_items.append(("Quick Open Modules", "quick-open-modules"))
            if usage_panel_html:
                nav_items.append(("Founder Usage Standard", "founder-usage-standard"))
            if support_panel_html:
                nav_items.append(("Decision Support Links", "decision-support-links"))
            if related_panel_html:
                nav_items.append(("Related Rooms", "related-rooms"))
            if source_layer_ready:
                nav_items.append(("Source Layer", "brief-source-layer"))
            for heading in extract_markdown_headings(body_lines_for_render):
                nav_items.append((heading, slugify_heading(heading)))
            nav_panel_html = render_brief_nav_panel(markdown_path.parent, nav_items)
        if doc_kind == "Executive Brief":
            brief_header_meta_items = build_brief_header_meta_items(
                markdown_path.parent,
                markdown_path,
                meta,
                reading_ready=bool(reading_panel_html),
                focus_ready=bool(focus_panel_html),
                decision_ready=bool(decision_panel_html),
                support_ready=bool(support_panel_html),
                related_ready=bool(related_panel_html),
                source_ready=True,
            )
            brief_header_identity_html = render_brief_header_identity(brief_header_meta_items)
            meta_cards = render_brief_header_meta_cards(brief_header_meta_items)
        else:
            meta_cards = render_meta_cards(markdown_path, doc_kind, meta_for_cards, subtitle)
        if not body_html:
            body_html = render_markdown(body_lines_for_render, markdown_path.parent)
        html_output = wrap_document_html(
            markdown_path,
            title,
            subtitle,
            doc_kind,
            brief_header_identity_html,
            meta_cards,
            nav_panel_html,
            distribution_panel_html,
            focus_panel_html,
            action_panel_html,
            reading_panel_html,
            decision_panel_html,
            trigger_panel_html,
            module_panel_html,
            usage_panel_html,
            support_panel_html,
            related_panel_html,
            source_panel_html,
            body_html,
        )
        markdown_path.with_suffix(".html").write_text(html_output, encoding="utf-8")
        doc_registry.setdefault(markdown_path.parent, []).append(
            {
                "path": str(markdown_path),
                "title": title,
                "subtitle": subtitle,
                "kind": doc_kind,
            }
        )

    total_portals = 0
    for directory in directories:
        child_dirs = sorted(
            [
                path
                for path in directory.iterdir()
                if path.is_dir() and path.name not in SKIP_DIR_NAMES and path in directories
            ]
        )
        docs_for_dir = sort_docs_for_directory(directory, doc_registry.get(directory, []))
        portal_html = build_portal_html(directory, docs_for_dir, child_dirs, len(markdown_files), len(directories))
        (directory / "OPEN-HERE.html").write_text(portal_html, encoding="utf-8")
        total_portals += 1

    root_portal = (REPO_ROOT / "OPEN-HERE.html").read_text(encoding="utf-8")
    ROOT_INDEX_PATH.write_text(root_portal, encoding="utf-8")
    ROOT_START_PATH.write_text(root_portal, encoding="utf-8")

    print(f"Generated {len(markdown_files)} branded document views.")
    print(f"Generated {total_portals} folder portals.")
    print(f"Root launcher: {ROOT_INDEX_PATH}")


if __name__ == "__main__":
    main()
