from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import Geographies, Products
from vortexasdk.endpoints.cargo_timeseries import CargoTimeSeries


class TestCargoTimeSeries(TestCaseUsingRealAPI):
    def test_search_returns_one_day(self):
        date = datetime(2019, 11, 10)

        result = CargoTimeSeries().search(
            filter_activity="loading_state",
            filter_time_min=date,
            filter_time_max=date,
        )

        assert len(result) == 1

    def test_search_returns_all_days(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        result = CargoTimeSeries().search(
            filter_activity="loading_state",
            filter_time_min=start,
            filter_time_max=end,
        )

        n_days = (end - start).days + 1

        assert n_days == len(result)

    def test_to_df(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        df = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                filter_time_min=start,
                filter_time_max=end,
            )
            .to_df()
        )

        n_days = (end - start).days + 1

        assert len(df) == n_days
        assert set(df.columns) == {"key", "count", "value"}

    def test_to_list(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        time_series_list = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                filter_time_min=start,
                filter_time_max=end,
            )
            .to_list()
        )

        n_days = (end - start).days + 1

        assert len(time_series_list) == n_days

    def test_filter_geographies_and_products(self):
        start = datetime(2019, 1, 1)
        end = datetime(2019, 10, 31)

        rotterdam = [
            g.id
            for g in Geographies().search(term="rotterdam").to_list()
            if "port" in g.layer
        ]
        crude = [
            p.id
            for p in Products().search("crude").to_list()
            if "Crude" == p.name
        ]

        rotterdam_crude_timeseries = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                timeseries_unit="bpd",
                timeseries_frequency="month",
                filter_time_min=start,
                filter_time_max=end,
                filter_origins=rotterdam,
                filter_products=crude,
            )
            .to_df()
        )

        rotterdam_all_products_timeseries = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                timeseries_unit="bpd",
                timeseries_frequency="month",
                filter_time_min=start,
                filter_time_max=end,
                filter_origins=rotterdam,
            )
            .to_df()
        )

        assert (
            rotterdam_all_products_timeseries["value"].sum()
            > rotterdam_crude_timeseries["value"].sum()
        )

    def test_filter_vessel_classes(self):
        start = datetime(2019, 1, 1)
        end = datetime(2019, 1, 20)

        vlcc_plus = "oil_vlcc"

        vlcc_plus_timeseries = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                timeseries_unit="bpd",
                timeseries_frequency="month",
                filter_time_min=start,
                filter_time_max=end,
                filter_vessel_classes=[vlcc_plus],
            )
            .to_df()
        )

        all_vessel_classes_timeseries = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                timeseries_unit="bpd",
                timeseries_frequency="month",
                filter_time_min=start,
                filter_time_max=end,
            )
            .to_df()
        )

        assert (
            all_vessel_classes_timeseries["value"].sum()
            > vlcc_plus_timeseries["value"].sum()
        )

    def test_search_filters_on_timeseries_max_activity(self):
        df = (
            CargoTimeSeries()
            .search(
                filter_activity="storing_state",
                filter_time_min=datetime(2019, 8, 1),
                filter_time_max=datetime(2019, 8, 31),
                timeseries_activity_time_span_min=1000 * 60 * 60 * 24 * 14,
                timeseries_activity_time_span_max=1000 * 60 * 60 * 24 * 60,
            )
            .to_df()
            .head(2)
        )

        assert len(df) == 2

    def test_endpoint_respects_difference_between_timeseries_activity_and_filter_activity(
        self,
    ):
        min_ts = datetime(2019, 8, 1)
        max_ts = datetime(2019, 8, 31)

        unloading_activity = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                timeseries_activity="unloading_state",
                filter_time_min=min_ts,
                filter_time_max=max_ts,
            )
            .to_list()
        )

        loading_activity = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                timeseries_activity="loading_state",
                filter_time_min=min_ts,
                filter_time_max=max_ts,
            )
            .to_list()
        )

        assert loading_activity != unloading_activity

    def test_timeseries_activity_defaults_to_filter_activity(self):
        min_ts = datetime(2019, 8, 1)
        max_ts = datetime(2019, 8, 31)

        loading_activity_default = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                filter_time_min=min_ts,
                filter_time_max=max_ts,
            )
            .to_list()
        )

        loading_activity = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                timeseries_activity="loading_state",
                filter_time_min=min_ts,
                filter_time_max=max_ts,
            )
            .to_list()
        )

        assert loading_activity == loading_activity_default
