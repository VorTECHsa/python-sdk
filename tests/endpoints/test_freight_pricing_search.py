
from datetime import datetime
from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.endpoints.freight_pricing_search import FreightPricingSearch

day = datetime(2021, 11, 1)


class TestFreightPricingReal(TestCaseUsingRealAPI):
    def test_default_search(self):
        results = FreightPricingSearch().search(
            routes=["TD3C"]
        )
        assert len(results) > 10

    def test_days(self):
        results = FreightPricingSearch().search(
            routes=["TD3C"],
            days=[day]
        )
        assert len(results) == 1

    def test_multiple_days(self):
        day2 = datetime(2021, 11, 2)
        results = FreightPricingSearch().search(
            routes=["TD3C"],
            days=[day, day2]
        )
        assert len(results) == 2

    def test_df(self):
        df = FreightPricingSearch().search(
            routes=["TD3C"]
        ).to_df(columns=['short_code', 'rate', 'rate_unit']).head(2)
        assert len(df) == 2
