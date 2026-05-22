import unittest

from finbalance.doc_schemas import DOC_SCHEMAS
from finbalance.industry_schemas import INDUSTRY_SCHEMAS
from finbalance.generation.helpers import PERIOD_TYPES


class SchemaRegistryTests(unittest.TestCase):
    def test_doc_schema_registry_has_unique_keys(self):
        self.assertGreaterEqual(len(DOC_SCHEMAS), 52)
        self.assertEqual(len(DOC_SCHEMAS), len(set(DOC_SCHEMAS.keys())))

    def test_industry_plans_reference_known_scenarios(self):
        for industry_name, industry_schema in INDUSTRY_SCHEMAS.items():
            self.assertTrue(industry_schema.allowed_accounts, industry_name)
            self.assertTrue(industry_schema.distractor_doc_types, industry_name)
            for doc_type in industry_schema.distractor_doc_types:
                self.assertIn(doc_type, DOC_SCHEMAS, f"{industry_name}:{doc_type}")
            for period_type in PERIOD_TYPES:
                self.assertIn(period_type, industry_schema.period_plans, industry_name)
                for level, plan in industry_schema.period_plans[period_type].items():
                    self.assertIn(level, {1, 2, 3, 4, 5})
                    for scenario_name in plan.mandatory + plan.optional:
                        self.assertIn(scenario_name, industry_schema.scenarios, f"{industry_name}:{scenario_name}")
                        self.assertIn(period_type, industry_schema.scenarios[scenario_name].period_types, f"{industry_name}:{period_type}:{scenario_name}")

    def test_property_management_uses_rental_revenue(self):
        accounts = INDUSTRY_SCHEMAS["property_management"].allowed_accounts
        self.assertIn("Rental Revenue", accounts)
        self.assertNotIn("Revenue", accounts)
