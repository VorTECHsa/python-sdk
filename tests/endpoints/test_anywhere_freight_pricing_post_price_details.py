from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import AnywhereFreightPricingPostPriceDetails


class TestAnywhereFreightPricingPostPriceDetails(TestCaseUsingRealAPI):
    def test_search_returns_data(self):
        routes = [
            {
                "origin": "7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
                "destination": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
                "product": "crude",
                "vessel_class": "oil_aframax_lr2",
            }
        ]

        result = AnywhereFreightPricingPostPriceDetails().search(
            routes=routes,
            time_min=datetime(2024, 1, 1),
            time_max=datetime(2024, 1, 31),
            unit="usd_per_tonne",
        )

        result_list = result.to_list()
        assert len(result_list) > 0
        assert "origin" in result_list[0]
        assert "destination" in result_list[0]
        assert "vessel_class" in result_list[0]
        assert "rates" in result_list[0]

    def test_search_to_df(self):
        routes = [
            {
                "origin": "7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
                "destination": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
                "product": "crude",
                "vessel_class": "oil_aframax_lr2",
            }
        ]

        result = AnywhereFreightPricingPostPriceDetails().search(
            routes=routes,
            time_min=datetime(2024, 1, 1),
            time_max=datetime(2024, 1, 31),
            unit="usd_per_tonne",
        )

        df = result.to_df()
        assert len(df) > 0
        # pd.json_normalize uses dot notation for nested keys
        assert "origin.id" in df.columns
        assert "destination.id" in df.columns
        assert "vessel_class" in df.columns

    def test_search_multiple_routes(self):
        routes = [
            {
                "origin": "7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
                "destination": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
                "product": "crude",
                "vessel_class": "oil_aframax_lr2",
            },
            {
                "origin": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
                "destination": "ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
                "product": "clean",
                "vessel_class": "oil_handymax_mr2",
            },
        ]

        result = AnywhereFreightPricingPostPriceDetails().search(
            routes=routes,
            time_min=datetime(2024, 1, 1),
            time_max=datetime(2024, 1, 31),
            unit="usd_per_tonne",
        )

        result_list = result.to_list()
        assert len(result_list) >= 2

    def test_search_with_avoid_zone(self):
        routes = [
            {
                "origin": "7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
                "destination": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
                "product": "crude",
                "vessel_class": "oil_aframax_lr2",
                "avoid_zone": ["Suez Canal"],
            }
        ]

        result = AnywhereFreightPricingPostPriceDetails().search(
            routes=routes,
            time_min=datetime(2024, 1, 1),
            time_max=datetime(2024, 1, 31),
            unit="usd_per_tonne",
        )

        result_list = result.to_list()
        assert len(result_list) > 0
