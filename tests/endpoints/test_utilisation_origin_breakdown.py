from datetime import datetime
from vortexasdk.endpoints.utilisation_origin_breakdown import UtilisationOriginBreakdown


from docs.utils import to_markdown
from tests.testcases import TestCaseUsingRealAPI


class TestOriginBreakdownReal(TestCaseUsingRealAPI):
    def test_search_returns_one_day(self):
        date = datetime(2019, 11, 10)

        result = UtilisationOriginBreakdown().search(
            filter_time_min=date,
            filter_time_max=date
        )

        assert len(result) > 0

    def test_to_df(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        df = (
            UtilisationOriginBreakdown()
            .search(
                filter_time_min=start,
                filter_time_max=end
            )
            .to_df()
        )

        assert list(df.columns) == ["key", "value", "count"]

    def test_with_params(self):
        start = datetime(2020, 10, 18)
        end = datetime(2021, 1, 18)

        df = (
            UtilisationOriginBreakdown()
            .search(
                filter_time_min=start,
                filter_time_max=end,
                breakdown_size='5',
                breakdown_geography='country'
            )
            .to_df()
        )

        assert len(df) == 5

    def test_to_list(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        time_series_list = (
            UtilisationOriginBreakdown()
            .search(
                filter_time_min=start,
                filter_time_max=end
            )
            .to_list()
        )

        assert len(time_series_list) > 0