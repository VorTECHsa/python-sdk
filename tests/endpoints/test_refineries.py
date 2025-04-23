from tests.testcases import TestCaseUsingMockAPI
from vortexasdk.endpoints.refineries import Refineries


class TestRefineries(TestCaseUsingMockAPI):
    def test_search_ids_retrieves_names(self):
        refineries = Refineries().search().to_list()

        names = [x.name for x in refineries]

        assert names == ["Mock Industrial Refinery"]

    def test_convert_to_df(self):
        df = Refineries().search().to_df()
        assert len(df) > 0
