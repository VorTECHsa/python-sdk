from vortexasdk import VesselAvailabilitySearch
from tests.testcases import TestCaseUsingRealAPI

rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
singapore = "1b79e18416d358d7e07b978abcab3f17e2ca75085a6d70ce1811cf4eaeaea886"
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
            exclude_vessel_classes=["oil_vlcc"],
            exclude_products=[
                "54af755a090118dcf9b0724c9a4e9f14745c26165385ffa7f1445bc768f06f11"
            ],
        )
        assert len(results) > 10

    def test_multiple_classes(self):
        results = VesselAvailabilitySearch().search(
            filter_port=rotterdam,
            filter_days_to_arrival=days_to_arrival,
            filter_vessel_classes=["oil_vlcc", "oil_suezmax"],
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

    def test_vessel_properties(self):
        df = (
            VesselAvailabilitySearch()
            .search(
                filter_port=singapore,
                filter_vessel_risk_level="high",
                filter_vessel_tags=[
                    [
                        {"tag": "vessel_fso_tag"},
                        {"tag": "vessel_decommissioned_tag"},
                        {"tag": "vessel_fsru_tag"},
                    ],
                    [{"tag": "vessel_coated_tag"}],
                ],
                size=10,
            )
            .to_df(
                columns=[
                    "available_at",
                    "vessel_name",
                    "vessel_class",
                    "vessel_risk_level",
                    "vessel_flag",
                    "vessel_tags",
                    "vessel_ice_class",
                ]
            )
            .head(10)
        )
        assert len(df) == 10
