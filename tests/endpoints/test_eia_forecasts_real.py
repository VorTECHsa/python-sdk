from tests.testcases import TestCaseUsingRealAPI
from datetime import datetime
from tests.timer import Timer
from vortexasdk.endpoints.eia_forecasts import EIAForecasts
from docs.utils import to_markdown


class TestEIAForecastsReal(TestCaseUsingRealAPI):
    def test_search_preset_crude_imports(self):

        preset = "padd1-crude-imports"
        filter_time_min = datetime(2020, 1, 20)
        filter_time_max = datetime(2020, 1, 24)

        forecasts = EIAForecasts().search(
            preset=preset,
            filter_time_min=filter_time_min,
            filter_time_max=filter_time_max,
        )
        assert len(forecasts) == 1
        values = [g.date for g in forecasts.to_list()]

        assert "2020-01-24T00:00:00.000Z" in values

        print(to_markdown(forecasts.to_df()))

    def test_search_preset_gasoline_exports(self):

        preset = "us-gasoline-exports"
        filter_time_min = datetime(2020, 3, 20)
        filter_time_max = datetime(2020, 4, 20)

        forecasts = EIAForecasts().search(
            preset=preset,
            filter_time_min=filter_time_min,
            filter_time_max=filter_time_max,
        )
        assert len(forecasts) == 5

        values = [g.date for g in forecasts.to_list()]
        assert "2020-04-17T00:00:00.000Z" in values
        assert "2020-04-10T00:00:00.000Z" in values
        assert "2020-04-03T00:00:00.000Z" in values
        assert "2020-03-27T00:00:00.000Z" in values
        assert "2020-03-20T00:00:00.000Z" in values

        print(to_markdown(forecasts.to_df()))
