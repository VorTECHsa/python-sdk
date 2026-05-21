from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import AnywhereFreightPricingTopPortsOrigin


class TestAnywhereFreightPricingTopPortsOrigin(TestCaseUsingRealAPI):
    def test_search_returns_data(self):
        result = AnywhereFreightPricingTopPortsOrigin().search(
            destination_id="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
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
        result = AnywhereFreightPricingTopPortsOrigin().search(
            destination_id="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
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
        result = AnywhereFreightPricingTopPortsOrigin().search(
            destination_id="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
            vessel_class="oil_handymax_mr2",
            product="clean",
            unit="usd_per_tonne",
            avoid_zone=["Suez Canal"],
        )

        result_list = result.to_list()
        assert len(result_list) > 0
