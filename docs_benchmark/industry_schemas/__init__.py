"""Central registry for industry schemas."""

from docs_benchmark.industry_schemas.field_services import INDUSTRY_SCHEMA as FIELD_SERVICES
from docs_benchmark.industry_schemas.healthcare_clinic import INDUSTRY_SCHEMA as HEALTHCARE_CLINIC
from docs_benchmark.industry_schemas.manufacturing import INDUSTRY_SCHEMA as MANUFACTURING
from docs_benchmark.industry_schemas.professional_services import INDUSTRY_SCHEMA as PROFESSIONAL_SERVICES
from docs_benchmark.industry_schemas.property_management import INDUSTRY_SCHEMA as PROPERTY_MANAGEMENT
from docs_benchmark.industry_schemas.retail import INDUSTRY_SCHEMA as RETAIL
from docs_benchmark.industry_schemas.subscription_saas import INDUSTRY_SCHEMA as SUBSCRIPTION_SAAS
from docs_benchmark.industry_schemas.wholesale_distribution import INDUSTRY_SCHEMA as WHOLESALE_DISTRIBUTION


INDUSTRY_SCHEMAS = {
    schema.name: schema
    for schema in (
        PROFESSIONAL_SERVICES,
        FIELD_SERVICES,
        RETAIL,
        WHOLESALE_DISTRIBUTION,
        HEALTHCARE_CLINIC,
        PROPERTY_MANAGEMENT,
        MANUFACTURING,
        SUBSCRIPTION_SAAS,
    )
}

INDUSTRIES = tuple(INDUSTRY_SCHEMAS.keys())


def get_industry_schema(industry: str):
    if industry not in INDUSTRY_SCHEMAS:
        raise KeyError(f"Unknown industry '{industry}'")
    return INDUSTRY_SCHEMAS[industry]
