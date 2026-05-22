"""Internal master-data generation for records."""

from __future__ import annotations

import random

from finbalance.types import PeriodSpec


COMPANY_WORDS = [
    "Atlas",
    "Harbor",
    "Northwind",
    "Summit",
    "Cedar",
    "Granite",
    "Beacon",
    "Willow",
    "Pioneer",
    "Silverline",
]

COMPANY_SUFFIXES = [
    "Advisors",
    "Builders",
    "Retail Group",
    "Distribution",
    "Clinic",
    "Property Services",
    "Operations",
    "Manufacturing",
    "Software",
]

ADDRESSES = [
    "14 King Street, Pune",
    "220 Lake View Road, Bengaluru",
    "18 Marina Avenue, Chennai",
    "75 Market Road, Mumbai",
    "90 Hill Park, Hyderabad",
]


def default_company_name(rng: random.Random) -> str:
    return f"{rng.choice(COMPANY_WORDS)} {rng.choice(COMPANY_SUFFIXES)}"


def default_address(rng: random.Random) -> str:
    return rng.choice(ADDRESSES)


def build_master_data(industry: str, rng: random.Random, period_spec: PeriodSpec) -> dict[str, object]:
    industry_label = industry.replace("_", " ").title()
    common = {
        "industry_label": industry_label,
        "period_label": period_spec.label,
        "customers": [
            "Blue Finch Holdings",
            "Metro Edge Partners",
            "Riverfront Group",
            "Maple Ridge Trading",
            "Aster Point Services",
            "Oak Harbor Foods",
            "Crescent Labs",
        ],
        "vendors": [
            "Vertex Supply Co.",
            "Oakline Services",
            "Prime Utility Desk",
            "Pace Office Mart",
            "Golden State Finance",
            "Meridian Support LLP",
            "Beacon Industrial Supply",
        ],
        "employees": ["Maya", "Noah", "Priya", "Liam", "Aarav", "Sara", "Ishaan", "Leah"],
        "insurers": ["CareSure", "Unity Health Plan", "NorthCover", "Harbor Health Network"],
        "tenants": ["Unit A - Ellis", "Unit B - Romero", "Unit C - Shah", "Unit D - Khan"],
        "units": ["A-101", "B-202", "C-303", "D-404"],
        "products": ["Widget A", "Widget B", "Premium Kit", "Filter Pack", "Service Bundle", "Refill Pack"],
        "services": ["Monthly retainer", "Implementation work", "Consulting sprint", "Review pack", "Support package"],
        "job_sites": ["North Yard", "East Tower", "Riverbank Plaza", "Marina Site"],
        "properties": ["Cedar Plaza", "Marina Heights", "Park Lane Residences", "Harbor View Offices"],
        "patients": ["Anaya Patel", "Marcus Lee", "Ella Santos", "Noah Ferreira"],
        "asset_names": ["Office laptops", "Delivery van", "Ultrasound console", "Display fixtures", "CNC router", "Server rack"],
        "processors": ["Axis Payments", "HarborPay", "ClearRoute"],
        "lenders": ["First City Bank", "Stonebridge Finance", "Aurora Capital"],
        "departments": ["Operations", "Sales", "Support", "Plant Floor"],
        "warehouses": ["Main Warehouse", "Overflow Storage", "Plant Floor Store"],
        "raw_materials": ["Steel sheets", "Resin pellets", "Control boards", "Packing film"],
        "finished_goods": ["Panel Kit", "Assembly Unit", "Retail Display", "Subscription Bundle"],
        "insurance_carriers": ["Shield Mutual", "Beacon General", "Marina Assurance"],
        "utility_providers": ["City Power", "Metro Water", "Harbor Utilities"],
        "subscription_plans": ["Annual Growth Plan", "Business Suite", "Enterprise License", "Team Support Plan"],
        "contract_managers": ["Riya Mehta", "Lucas Grant", "Asha Nair", "Daniel Ortiz"],
        "owners": ["Pioneer Capital Owners", "Harbor Equity Partners", "Stonebridge Holdings"],
        "payer_groups": ["Employer Plan A", "Employer Plan B", "Individual Billing"],
    }
    return common
