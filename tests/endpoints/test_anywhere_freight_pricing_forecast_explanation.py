from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import AnywhereFreightPricingForecastExplanation


class TestAnywhereFreightPricingForecastExplanation(TestCaseUsingRealAPI):
    def test_search_returns_data(self):
        result = AnywhereFreightPricingForecastExplanation().search(
            origin_port="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
            destination_port="ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
            vessel_class="oil_handymax_mr2",
            product="clean",
            frequency="month",
        )

        result_list = result.to_list()
        assert len(result_list) > 0
        assert "base_date" in result_list[0]
        assert "explanation" in result_list[0]

    def test_search_to_df(self):
        result = AnywhereFreightPricingForecastExplanation().search(
            origin_port="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
            destination_port="ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
            vessel_class="oil_handymax_mr2",
            product="clean",
            frequency="month",
        )

        df = result.to_df()
        assert len(df) > 0
        assert "base_date" in df.columns
        assert "explanation" in df.columns

    def test_search_with_week_frequency(self):
        result = AnywhereFreightPricingForecastExplanation().search(
            origin_port="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
            destination_port="ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
            vessel_class="oil_handymax_mr2",
            product="clean",
            frequency="week",
        )

        result_list = result.to_list()
        assert len(result_list) > 0
        assert "base_date" in result_list[0]
        assert "explanation" in result_list[0]

    def test_search_with_avoid_zone(self):
        result = AnywhereFreightPricingForecastExplanation().search(
            origin_port="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
            destination_port="ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
            vessel_class="oil_handymax_mr2",
            product="clean",
            frequency="month",
            avoid_zone=["Suez Canal"],
        )

        result_list = result.to_list()
        assert len(result_list) > 0

    def test_search_with_include_port_costs(self):
        result = AnywhereFreightPricingForecastExplanation().search(
            origin_port="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
            destination_port="ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
            vessel_class="oil_handymax_mr2",
            product="clean",
            frequency="month",
            include_port_costs=True,
        )

        result_list = result.to_list()
        assert len(result_list) > 0
