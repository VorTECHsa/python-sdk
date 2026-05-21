from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import AnywhereFreightPricingTopPortsDestination


class TestAnywhereFreightPricingTopPortsDestination(TestCaseUsingRealAPI):
    def test_search_returns_data(self):
        result = AnywhereFreightPricingTopPortsDestination().search(
            origin_id="7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
            vessel_class="oil_handymax_mr2",
            product="clean",
            unit="usd_per_tonne",
        )

        result_list = result.to_list()
        assert len(result_list) > 0
        assert "geography" in result_list[0]
        assert "price_details" in result_list[0]
        assert "id" in result_list[0]["geography"]
        assert "name" in result_list[0]["geography"]

    def test_search_to_df(self):
        result = AnywhereFreightPricingTopPortsDestination().search(
            origin_id="7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
            vessel_class="oil_handymax_mr2",
            product="clean",
            unit="usd_per_tonne",
        )

        df = result.to_df()
        assert len(df) > 0
        # pd.json_normalize uses dot notation for nested keys
        assert "geography.id" in df.columns
        assert "geography.name" in df.columns

    def test_search_with_avoid_zone(self):
        result = AnywhereFreightPricingTopPortsDestination().search(
            origin_id="7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
            vessel_class="oil_handymax_mr2",
            product="clean",
            unit="usd_per_tonne",
            avoid_zone=["Suez Canal"],
        )

        result_list = result.to_list()
        assert len(result_list) > 0
