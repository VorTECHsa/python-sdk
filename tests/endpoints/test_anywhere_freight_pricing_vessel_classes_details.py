from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import AnywhereFreightPricingVesselClassesDetails


class TestAnywhereFreightPricingVesselClassesDetails(TestCaseUsingRealAPI):
    def test_search_returns_data(self):
        result = AnywhereFreightPricingVesselClassesDetails().search()

        result_list = result.to_list()
        assert len(result_list) > 0
        assert "name" in result_list[0]
        assert "suggested_tonnage" in result_list[0]
        assert "min_tonnage" in result_list[0]
        assert "max_tonnage" in result_list[0]

    def test_search_to_df(self):
        result = AnywhereFreightPricingVesselClassesDetails().search()

        df = result.to_df()
        assert len(df) > 0
        assert "name" in df.columns
        assert "suggested_tonnage" in df.columns
        assert "min_tonnage" in df.columns
        assert "max_tonnage" in df.columns
