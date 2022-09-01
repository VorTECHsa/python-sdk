from vortexasdk import VesselAvailabilitySearch
from tests.testcases import TestCaseUsingRealAPI

rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
days_to_arrival = {"min": 0, "max": 5}


class TestVesselAvailabilityReal(TestCaseUsingRealAPI):
    def test_default_search(self):
        results = VesselAvailabilitySearch().search(
            filter_port=rotterdam, filter_days_to_arrival=days_to_arrival
        )
        assert len(results) > 10

    def test_days_to_arrival(self):
        results = VesselAvailabilitySearch().search(
            filter_port=rotterdam, filter_days_to_arrival=days_to_arrival
        )
        assert len(results) > 10

    def test_exclusion_filters(self):
        results = VesselAvailabilitySearch().search(
            filter_port=rotterdam,
            filter_days_to_arrival=days_to_arrival,
            exclude_vessel_classes=["vlcc_plus"],
            exclude_products=[
                "54af755a090118dcf9b0724c9a4e9f14745c26165385ffa7f1445bc768f06f11"
            ],
        )
        assert len(results) > 10

    def test_multiple_classes(self):
        results = VesselAvailabilitySearch().search(
            filter_port=rotterdam,
            filter_days_to_arrival=days_to_arrival,
            filter_vessel_classes=["vlcc_plus", "suezmax"],
        )

        assert len(results) > 10

    def test_df(self):
        df = (
            VesselAvailabilitySearch()
            .search(
                filter_port=rotterdam,
                filter_days_to_arrival=days_to_arrival,
            )
            .to_df(columns=["available_at", "vessel_name", "vessel_class"])
            .head(2)
        )
        assert len(df) == 2
