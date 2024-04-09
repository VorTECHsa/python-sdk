from datetime import datetime
from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.endpoints.canal_transit_timeseries import (
    CanalTransitTimeseries,
)


class TestCanalTransitTimeseries(TestCaseUsingRealAPI):
    def test_default_search(self):
        CanalTransitTimeseries().search()

    def test_canal_timeseries_with_filtering(self):
        nonLng = CanalTransitTimeseries().search(
            time_min=datetime(2023, 9, 5),
            time_max=datetime(2023, 9, 7),
            exclude_filter_vessel_classes=["lng"],
            metric="count_of_vessels",
            timeseries_activity="started_waiting",
        )
        all = CanalTransitTimeseries().search(
            time_min=datetime(2023, 9, 5),
            time_max=datetime(2023, 9, 7),
            metric="count_of_vessels",
            timeseries_activity="started_waiting",
        )

        assert all[0]["count"] > nonLng[0]["count"]

    def test_timeseries_buckets_count(self):
        dailyBuckets = CanalTransitTimeseries().search(
            time_min=datetime(2023, 9, 5),
            time_max=datetime(2023, 9, 10),
            metric="count_of_vessels",
            timeseries_activity="started_waiting",
        )
        monthlyBuckets = CanalTransitTimeseries().search(
            time_min=datetime(2023, 9, 5),
            time_max=datetime(2023, 12, 7),
            metric="count_of_vessels",
            timeseries_activity="started_waiting",
            timeseries_frequency="week",
        )

        assert len(dailyBuckets) == 6
        assert len(monthlyBuckets) == 14
