from datetime import datetime
from vortexasdk import OnshoreInventoriesTimeseries

from tests.testcases import TestCaseUsingRealAPI


START = datetime(2021, 8, 5, 0)
END = datetime(2021, 8, 23, 1)


class TestOnshoreInventoriesTimeseries(TestCaseUsingRealAPI):
    def test_timeseries_returns_3_weeks_of_data(self):
        df = (
            OnshoreInventoriesTimeseries()
            .search(
                time_max=END,
                time_min=START,
                timeseries_frequency="week",
                timeseries_split_property="quantity",
                timeseries_unit_operator="fill",
            )
            .to_df()
        )

        assert len(df) == 3

    def test_timeseries_breakdowns_by_country_should_contain_over_100_unique_splits(
        self,
    ):
        result_list = (
            OnshoreInventoriesTimeseries()
            .search(
                time_max=END,
                time_min=START,
                timeseries_frequency="week",
                timeseries_split_property="location_country",
                timeseries_unit_operator="fill",
            )
            .to_list()
        )

        assert len(result_list[0].breakdown) > 100

    def test_timeseries_breadown_with_exclusion(self):
        result_list = (
            OnshoreInventoriesTimeseries()
            .search(
                location_ids=[
                    "ee1de4914cc26e8f1326b49793b089131870d478714c07e0c99c56cb307704c5"
                ],
                time_min=datetime(2021, 1, 5),
                time_max=datetime(2021, 1, 12),
                timeseries_frequency="week",
                timeseries_split_property="location_country",
                timeseries_unit="b",
                timeseries_unit_operator="capacity",
            )
            .to_list()
        )

        assert result_list[0].breakdown[0]["label"] == "Italy"

    def test_should_throw_an_error_when_invalid_params_are_passed(self):
        self.assertRaises(
            ValueError,
            lambda: OnshoreInventoriesTimeseries().search(
                time_max=END,
                time_min=START,
                timeseries_frequency="week",
                timeseries_split_property="invalid argument",
                timeseries_unit_operator="fill",
            ),
        )
