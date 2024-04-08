from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.endpoints.canal_transit import CanalTransit
from vortexasdk.endpoints.canal_transit_result import DEFAULT_COLUMNS


class TestCanalTransitReal(TestCaseUsingRealAPI):
    def test_default_search(self):
        CanalTransit().search()

    def test_search_for_lng_vessels(self):
        df = CanalTransit().search(filter_vessel_classes=["lng"]).to_df()

        assert list(df.columns) == DEFAULT_COLUMNS
