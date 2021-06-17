from datetime import datetime
from vortexasdk.endpoints.vessel_origin_breakdown import VesselOriginBreakdown


from docs.utils import to_markdown
from tests.testcases import TestCaseUsingRealAPI


class TestVesselOriginBreakdownReal(TestCaseUsingRealAPI):
    def test_search_returns_one_day(self):
        date = datetime(2019, 11, 10)

        result = VesselOriginBreakdown().search(
            breakdown_geography="country",
            filter_time_min=date,
            filter_time_max=date,
            breakdown_size=1000,
            breakdown_unit="b"
        )

        assert len(result) == 1

    def test_search_returns_all_days(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        result = VesselOriginBreakdown().search(
            breakdown_geography="country",
            filter_time_min=start,
            filter_time_max=end,
            breakdown_size=1000,
            breakdown_unit="b"
        )

        n_days = (end - start).days + 1

        assert n_days == len(result)

    def test_to_df(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        df = (
            VesselOriginBreakdown()
            .search(
                breakdown_geography="country",
                filter_time_min=start,
                filter_time_max=end,
                breakdown_size=1000,
                breakdown_unit="b"
            )
            .to_df()
        )

        print(to_markdown(df.head()))

        n_days = (end - start).days + 1

        assert len(df) == n_days
        assert list(df.columns) == ["key", "value", "count"]

    def test_to_list(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        time_series_list = (
            VesselOriginBreakdown()
            .search(
                breakdown_geography="country",
                filter_time_min=start,
                filter_time_max=end,
                breakdown_size=1000,
                breakdown_unit="b"
            )
            .to_list()
        )

        n_days = (end - start).days + 1

        assert len(time_series_list) == n_days
