from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import AnywhereFreightPricingGetPriceDetails


class TestAnywhereFreightPricingGetPriceDetails(TestCaseUsingRealAPI):
    def test_search_returns_data(self):
        result = AnywhereFreightPricingGetPriceDetails().search(
            time_min=datetime(2024, 1, 1),
            time_max=datetime(2024, 1, 31),
            origin_port="7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
            destination_port="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
            vessel_class="oil_aframax_lr2",
            product="crude",
            unit="usd_per_tonne",
        )

        result_list = result.to_list()
        assert len(result_list) > 0
        assert "origin_port" in result_list[0]
        assert "destination_port" in result_list[0]
        assert "vessel_class" in result_list[0]
        assert "rates" in result_list[0]

    def test_search_to_df(self):
        result = AnywhereFreightPricingGetPriceDetails().search(
            time_min=datetime(2024, 1, 1),
            time_max=datetime(2024, 1, 31),
            origin_port="7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
            destination_port="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
            vessel_class="oil_aframax_lr2",
            product="crude",
            unit="usd_per_tonne",
        )

        df = result.to_df()
        assert len(df) > 0
        # pd.json_normalize uses dot notation for nested keys
        assert "origin_port.id" in df.columns
        assert "destination_port.id" in df.columns
        assert "vessel_class" in df.columns

    def test_search_with_avoid_zone(self):
        result = AnywhereFreightPricingGetPriceDetails().search(
            time_min=datetime(2024, 1, 1),
            time_max=datetime(2024, 1, 31),
            origin_port="7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
            destination_port="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
            vessel_class="oil_aframax_lr2",
            product="crude",
            unit="usd_per_tonne",
            avoid_zone=["Suez Canal"],
        )

        result_list = result.to_list()
        assert len(result_list) > 0
