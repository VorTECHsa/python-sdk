from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import Geographies


class TestGeographiesReal(TestCaseUsingRealAPI):
    def test_search(self):
        geographies = Geographies().search(term=["Liverpool", "Southampton"])
        names = [g["name"] for g in geographies]

        assert "Liverpool [GB]" in names

    def test_search_to_df(self):
        Geographies().search(term=["Liverpool", "Southampton"]).to_df()
