from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import AnywhereFreightPricingForecastTimeseries


class TestAnywhereFreightPricingForecastTimeseries(TestCaseUsingRealAPI):
    def test_search_returns_data(self):
        routes = [
            {
                "origin_port": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
                "destination_port": "ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
                "product": "clean",
                "vessel_class": "oil_handymax_mr2",
            }
        ]

        result = AnywhereFreightPricingForecastTimeseries().search(
            routes=routes,
            time_min=datetime(2026, 5, 26),
            time_max=datetime(2026, 8, 26),
            frequency="week",
            unit="usd_per_tonne",
        )

        result_list = result.to_list()
        assert len(result_list) > 0
        assert "origin_port" in result_list[0]
        assert "destination_port" in result_list[0]
        assert "prices" in result_list[0]
        assert "lumpsums" in result_list[0]
        assert "suggested_tonnage" in result_list[0]

    def test_search_to_df(self):
        routes = [
            {
                "origin_port": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
                "destination_port": "ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
                "product": "clean",
                "vessel_class": "oil_handymax_mr2",
            }
        ]

        result = AnywhereFreightPricingForecastTimeseries().search(
            routes=routes,
            time_min=datetime(2026, 5, 26),
            time_max=datetime(2026, 8, 26),
            frequency="week",
            unit="usd_per_tonne",
        )

        df = result.to_df()
        assert len(df) > 0
        assert "origin_port" in df.columns
        assert "destination_port" in df.columns
        assert "vessel_class" in df.columns
        assert "suggested_tonnage" in df.columns

    def test_search_multiple_routes(self):
        routes = [
            {
                "origin_port": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
                "destination_port": "ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
                "vessel_class": "oil_handymax_mr2",
                "product": "clean",
            },
            {
                "origin_port": "7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
                "destination_port": "57a5c821cdc0d9e7187ffc242cd8afd8e86e287b725c1949c65396b575cb5d1e",
                "vessel_class": "oil_handymax_mr2",
                "product": "clean",
            },
        ]

        result = AnywhereFreightPricingForecastTimeseries().search(
            routes=routes,
            time_min=datetime(2026, 5, 26),
            time_max=datetime(2026, 8, 26),
            frequency="week",
            unit="usd_per_tonne",
        )

        result_list = result.to_list()
        assert len(result_list) == 2
