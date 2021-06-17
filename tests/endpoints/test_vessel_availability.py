from vortexasdk.endpoints.vessel_availability_search import VesselAvailability

from tests.testcases import TestCaseUsingRealAPI

singapore = "1b79e18416d358d7e07b978abcab3f17e2ca75085a6d70ce1811cf4eaeaea886"
days_to_arrival = {"min": 0, "max": 5}

class TestVesselAvailabilityReal(TestCaseUsingRealAPI):
    def test_default_search(self):
        results = VesselAvailability().search(
            filter_port=singapore,
            filter_days_to_arrival=days_to_arrival
        )
        assert len(results) > 10
    
    def test_days_to_arrival(self):
        results = VesselAvailability().search(
            filter_port=singapore,
            filter_days_to_arrival=days_to_arrival
        )
        assert len(results) > 10

    def test_exclusion_filters(self):
        results = VesselAvailability().search(
            filter_port=singapore,
            filter_days_to_arrival=days_to_arrival,
            exclude_vessel_classes=["vlcc_plus"],
            exclude_products=["54af755a090118dcf9b0724c9a4e9f14745c26165385ffa7f1445bc768f06f11"]
        )
        assert len(results) > 10

    def test_multiple_classes(self):
        results = VesselAvailability().search(
            filter_port=singapore,
            filter_days_to_arrival=days_to_arrival,
            filter_vessel_classes=["vlcc_plus", "suezmax"],
        )

        assert len(results) > 10