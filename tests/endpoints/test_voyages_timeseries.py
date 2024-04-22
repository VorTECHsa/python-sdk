from datetime import datetime
from vortexasdk import VoyagesTimeseries

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.endpoints.geographies import Geographies
from vortexasdk.api.shared_types import VoyageDateRangeActivity

rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"


class TestVoyagesTimeseries(TestCaseUsingRealAPI):
    def test_search_returns_all_days(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)
        numbers_of_days_between_start_and_end = 4

        df = (
            VoyagesTimeseries()
            .search(time_min=start, time_max=end, origins=rotterdam)
            .to_df()
        )
        assert len(df) == numbers_of_days_between_start_and_end

    def test_search_arrivals(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)
        numbers_of_days_between_start_and_end = 4

        df = (
            VoyagesTimeseries()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                voyage_date_range_activity=VoyageDateRangeActivity.ARRIVALS.value,
            )
            .to_df()
        )
        assert len(df) >= numbers_of_days_between_start_and_end

    def test_search_departures(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)
        numbers_of_days_between_start_and_end = 4

        df = (
            VoyagesTimeseries()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                voyage_date_range_activity=VoyageDateRangeActivity.DEPARTURES.value,
            )
            .to_df()
        )
        assert len(df) >= numbers_of_days_between_start_and_end

    def test_search_departures_with_last_discharge_behaviour(self):
        start = datetime(2021, 6, 17)
        end = datetime(2021, 6, 21)
        numbers_of_days_between_start_and_end = 4

        df = (
            VoyagesTimeseries()
            .search(
                time_min=start,
                time_max=end,
                origins=rotterdam,
                voyage_date_range_activity=VoyageDateRangeActivity.DEPARTURES.value,
                destination_behaviour="last_discharge",
            )
            .to_df()
        )
        assert len(df) >= numbers_of_days_between_start_and_end

    def test_from_description(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 28, 23, 59)

        rotterdam = [
            g.id
            for g in Geographies().search("rotterdam").to_list()
            if "port" in g.layer
        ]

        df = (
            VoyagesTimeseries()
            .search(
                origins=rotterdam,
                time_min=start,
                time_max=end,
                breakdown_frequency="day",
                breakdown_property="vessel_count",
                breakdown_split_property="location_country",
            )
            .to_df()
        )

        assert len(df) > 0

    def test_avg_unit_operator(self):
        start = datetime(2022, 4, 26)
        end = datetime(2022, 4, 28, 23, 59)

        rotterdam = [
            g.id
            for g in Geographies().search("rotterdam").to_list()
            if "port" in g.layer
        ]

        df = (
            VoyagesTimeseries()
            .search(
                origins=rotterdam,
                time_min=start,
                time_max=end,
                breakdown_frequency="day",
                breakdown_property="avg_distance",
                breakdown_split_property="location_country",
                breakdown_unit_operator="avg",
            )
            .to_df()
        )

        assert len(df) > 0
