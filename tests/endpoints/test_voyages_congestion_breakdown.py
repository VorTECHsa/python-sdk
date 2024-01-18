from datetime import datetime
from vortexasdk import VoyagesCongestionBreakdown

from tests.testcases import TestCaseUsingRealAPI


class TestVoyagesCongestionBreakdown(TestCaseUsingRealAPI):
    def test_search_returns_one_day(self):
        date = datetime(2019, 11, 10)
        end_date = datetime(2019, 11, 11)

        result = VoyagesCongestionBreakdown().search(
            time_min=date, time_max=end_date, breakdown_size=1
        )

        assert len(result) == 1

    def test_search_returns_all_days(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        result = VoyagesCongestionBreakdown().search(
            time_min=start, time_max=end, breakdown_size=10
        )

        assert len(result) == 10

    def test_search_returns_for_terminal(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        result = VoyagesCongestionBreakdown().search(
            breakdown_property="terminal",
            time_min=start,
            time_max=end,
            breakdown_size=10,
        )

        assert len(result) == 10

    def test_search_returns_larger_size(self):
        start = datetime(2019, 1, 1)
        end = datetime(2019, 3, 1)

        result = VoyagesCongestionBreakdown().search(
            time_min=start, time_max=end, breakdown_size=25
        )

        assert len(result) == 25

    def test_to_df(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        df = (
            VoyagesCongestionBreakdown()
            .search(time_min=start, time_max=end, breakdown_size=10)
            .to_df()
        )

        assert len(df) == 10
        assert list(df.columns) == [
            "avg_waiting_time",
            "vessel_dwt",
            "vessel_cubic_capacity",
            "vessel_count",
            "cargo_quantity",
            "avg_waiting_time_laden",
            "vessel_dwt_laden",
            "vessel_cubic_capacity_laden",
            "vessel_count_laden",
            "avg_waiting_time_ballast",
            "vessel_dwt_ballast",
            "vessel_cubic_capacity_ballast",
            "vessel_count_ballast",
            "location_details.0.label",
        ]

    def test_with_params(self):
        df = (
            VoyagesCongestionBreakdown()
            .search(
                origins="80aa9e4f3014c3d96559c8e642157edbb2b684ea0144ed76cd20b3af75110877",
                destinations="934c47f36c16a58d68ef5e007e62a23f5f036ee3f3d1f5f85a48c572b90ad8b2",
                time_min=datetime(2020, 12, 19),
                time_max=datetime(2021, 1, 18),
            )
            .to_df()
            .head()
        )

        assert list(df.columns) == [
            "avg_waiting_time",
            "vessel_dwt",
            "vessel_cubic_capacity",
            "vessel_count",
            "cargo_quantity",
            "avg_waiting_time_laden",
            "vessel_dwt_laden",
            "vessel_cubic_capacity_laden",
            "vessel_count_laden",
            "avg_waiting_time_ballast",
            "vessel_dwt_ballast",
            "vessel_cubic_capacity_ballast",
            "vessel_count_ballast",
            "location_details.0.label",
        ]

    def test_to_list(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        time_series_list = (
            VoyagesCongestionBreakdown()
            .search(time_min=start, time_max=end, breakdown_size=10)
            .to_list()
        )

        assert len(time_series_list) == 10

    def test_from_docs(self):
        search_result = (
            VoyagesCongestionBreakdown()
            .search(
                time_min=datetime(2022, 4, 26),
                time_max=datetime(2022, 4, 26, 23, 59),
                movement_status="congestion",
                breakdown_property="shipping_region",
                breakdown_size=2,
            )
            .to_df()
        )

        assert len(search_result) == 2
