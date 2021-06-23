
from vortexasdk.endpoints.geographies import Geographies
from vortexasdk.endpoints.availability_search import AvailabilitySearch
from tests.testcases import TestCaseUsingRealAPI

singapore = "1b79e18416d358d7e07b978abcab3f17e2ca75085a6d70ce1811cf4eaeaea886"
days_to_arrival = {"min": 0, "max": 5}

class TestAvailabilityReal(TestCaseUsingRealAPI):
    def test_default_search(self):
        results = AvailabilitySearch().search(
            filter_port=singapore,
            filter_days_to_arrival=days_to_arrival
        )
        assert len(results) > 10
    
    def test_days_to_arrival(self):
        results = AvailabilitySearch().search(
            filter_port=singapore,
            filter_days_to_arrival=days_to_arrival
        )
        assert len(results) > 10

    def test_exclusion_filters(self):
        results = AvailabilitySearch().search(
            filter_port=singapore,
            filter_days_to_arrival=days_to_arrival,
            exclude_vessel_classes=["vlcc_plus"],
            exclude_products=["54af755a090118dcf9b0724c9a4e9f14745c26165385ffa7f1445bc768f06f11"]
        )
        assert len(results) > 10

    def test_multiple_classes(self):
        results = AvailabilitySearch().search(
            filter_port=singapore,
            filter_days_to_arrival=days_to_arrival,
            filter_vessel_classes=["vlcc_plus", "suezmax"],
        )

        assert len(results) > 10
  
    def test_df(self):
        rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
        df = AvailabilitySearch().search(
            filter_port=rotterdam[0],
            filter_days_to_arrival=days_to_arrival,
        ).to_df().head(2)

        assert len(df) == 2