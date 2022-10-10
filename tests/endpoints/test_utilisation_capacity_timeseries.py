from datetime import datetime
from vortexasdk import Products, FleetUtilisationCapacityTimeseries

from tests.testcases import TestCaseUsingRealAPI


class TestFleetUtilisationCapacityTimeSeries(TestCaseUsingRealAPI):
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
            FleetUtilisationCapacityTimeseries()
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
            FleetUtilisationCapacityTimeseries()
            .search(
                filter_vessel_status="vessel_status_ballast",
                filter_time_min=start,
                filter_time_max=end,
                timeseries_frequency="day",
                filter_origins="80aa9e4f3014c3d96559c8e642157edbb2b684ea0144ed76cd20b3af75110877",
                timeseries_property="origin_country",
            )
            .to_df()
        )

        assert len(df) == 8
