from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import Corporations


class TestCorporationsReal(TestCaseUsingRealAPI):
    def test_search(self):
        Corporations().search().to_df()

    def test_load_all(self):
        all_corporations = Corporations().load_all()

        assert len(all_corporations) > 1000
