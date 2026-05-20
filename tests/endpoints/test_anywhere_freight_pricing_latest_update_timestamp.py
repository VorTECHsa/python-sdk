from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import AnywhereFreightPricingLatestUpdateTimestamp

class TestAnywhereFreightPricingLatestUpdateTimestamp(TestCaseUsingRealAPI):
    def test_search_returns_timestamp(self):
        result = AnywhereFreightPricingLatestUpdateTimestamp().search()
        assert "timestamp" in result