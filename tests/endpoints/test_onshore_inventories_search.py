from datetime import datetime
from vortexasdk import OnshoreInventoriesSearch

from tests.testcases import TestCaseUsingRealAPI


class TestOnshoreInventoriesSearch(TestCaseUsingRealAPI):
    def test_timeseries_returns_data_frame(self):
        df = (
            OnshoreInventoriesSearch()
            .search(crude_confidence=["unlikely"], storage_types=["refinery"])
            .to_df()
        )

        assert len(df) > 100

    def test_filter_by_measurement_ids(self):
        df = (
            OnshoreInventoriesSearch()
            .search(
                measurement_ids=[
                    "71c138f8c1f93b81e6a6c7d6429b71e5b4d8d2321a3a7cafa92ffedf430f5cf0"
                ],
                time_min=datetime(2022, 1, 1),
                time_max=datetime(2022, 1, 14),
            )
            .to_df()
        )
        # There should be exactly one result returned
        assert len(df) == 1

    def test_timeseries_returns_list(self):
        lst = (
            OnshoreInventoriesSearch()
            .search(crude_confidence=["probable"], storage_types=["refinery"])
            .to_list()
        )

        assert len(lst) > 0

    def test_should_throw_an_error_when_invalid_params_are_passed(self):
        self.assertRaises(
            ValueError,
            lambda: OnshoreInventoriesSearch().search(
                crude_confidence=["hello"]
            ),
        )
