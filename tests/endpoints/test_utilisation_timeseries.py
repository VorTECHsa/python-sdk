from datetime import datetime
from vortexasdk import FleetUtilisationTimeseries, Products


from tests.testcases import TestCaseUsingRealAPI


class TestFleetUtilisationTimeSeries(TestCaseUsingRealAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 1, 11)
        end = datetime(2021, 1, 18)

        rotterdam = (
            "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
        )
        crude = [
            p.id
            for p in Products().search("crude").to_list()
            if "Crude" == p.name
        ]

        df = (
            FleetUtilisationTimeseries()
            .search(
                filter_time_min=start,
                filter_time_max=end,
                timeseries_frequency="day",
                filter_origins=rotterdam,
                filter_products=crude,
                timeseries_property="quantity",
            )
            .to_df()
        )

        assert len(df) == 8

    def test_with_params(self):
        start = datetime(2021, 1, 11)
        end = datetime(2021, 1, 18)

        df = (
            FleetUtilisationTimeseries()
            .search(
                filter_time_min=start,
                filter_time_max=end,
                filter_vessel_status="vessel_status_laden_known",
                filter_products="54af755a090118dcf9b0724c9a4e9f14745c26165385ffa7f1445bc768f06f11",
                filter_origins="80aa9e4f3014c3d96559c8e642157edbb2b684ea0144ed76cd20b3af75110877",
                filter_destinations="934c47f36c16a58d68ef5e007e62a23f5f036ee3f3d1f5f85a48c572b90ad8b2",
                timeseries_property="vessel_class",
                timeseries_frequency="day",
            )
            .to_df()
        )

        assert len(df) == 8
