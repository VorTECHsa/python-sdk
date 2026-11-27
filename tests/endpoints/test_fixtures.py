from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.endpoints.fixtures import Fixtures
from datetime import datetime


class TestFixtures(TestCaseUsingRealAPI):
    def test_search_fixtures_by_ids(self):
        fixtures = (
            Fixtures()
            .search(
                filter_time_field="fixing_timestamp",
                filter_time_min=datetime(2020, 1, 1),
                filter_time_max=datetime(2020, 1, 2),
            )
            .to_df()
        )
        assert len(fixtures) > 0

    def test_to_list(self):
        fixtures = (
            Fixtures()
            .search(
                filter_time_field="fixing_timestamp",
                filter_time_min=datetime(2020, 1, 1),
                filter_time_max=datetime(2020, 1, 2),
            )
            .to_list()
        )
        assert len(fixtures) > 0

    def test_filter_time_field_laycan_from_is_applied(self):
        time_min = datetime(2020, 1, 1)
        time_max = datetime(2020, 1, 8)

        fixtures = (
            Fixtures()
            .search(
                filter_time_field="laycan_from",
                filter_time_min=time_min,
                filter_time_max=time_max,
            )
            .to_list()
        )

        assert len(fixtures) > 0
        # Every result has a laycan start inside the requested range.
        for fixture in fixtures:
            laycan_from = datetime.strptime(
                fixture.laycan_from[:10], "%Y-%m-%d"
            )
            assert time_min <= laycan_from <= time_max

    def test_exclude_charterers_is_applied(self):
        search_params = dict(
            filter_time_field="fixing_timestamp",
            filter_time_min=datetime(2020, 1, 1),
            filter_time_max=datetime(2020, 1, 8),
        )
        fixtures = Fixtures().search(**search_params).to_list()
        charterer_id = next(f.charterer.id for f in fixtures if f.charterer)

        filtered_fixtures = (
            Fixtures()
            .search(**search_params, exclude_charterers=charterer_id)
            .to_list()
        )

        assert len(filtered_fixtures) < len(fixtures)
        # No result belongs to the excluded charterer.
        assert all(
            f.charterer is None or f.charterer.id != charterer_id
            for f in filtered_fixtures
        )
