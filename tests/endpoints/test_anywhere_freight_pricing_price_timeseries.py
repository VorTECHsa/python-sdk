from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import AnywhereFreightPricingPriceTimeseries


class TestAnywhereFreightPricingPriceTimeseries(TestCaseUsingRealAPI):
    def test_search_returns_data(self):
        routes = [
            {
                "origin": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
                "destination": "ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
                "product": "clean",
                "vessel_class": "oil_handymax_mr2",
            }
        ]

        result = AnywhereFreightPricingPriceTimeseries().search(
            routes=routes,
            time_min=datetime(2026, 2, 20),
            time_max=datetime(2026, 5, 20),
            frequency="month",
            unit="usd_per_tonne",
        )

        result_list = result.to_list()
        assert len(result_list) > 0
        assert "origin" in result_list[0]
        assert "destination" in result_list[0]
        assert "prices" in result_list[0]

    def test_search_to_df(self):
        routes = [
            {
                "origin": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
                "destination": "ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
                "product": "clean",
                "vessel_class": "oil_handymax_mr2",
            }
        ]

        result = AnywhereFreightPricingPriceTimeseries().search(
            routes=routes,
            time_min=datetime(2026, 2, 20),
            time_max=datetime(2026, 5, 20),
            frequency="month",
            unit="usd_per_tonne",
        )

        df = result.to_df()
        assert len(df) > 0
        # Top-level keys preserved, nested arrays like prices stay as lists
        assert "origin" in df.columns
        assert "destination" in df.columns
        assert "vessel_class" in df.columns
