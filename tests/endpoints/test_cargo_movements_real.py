from unittest import TestCase, skipIf

import tabulate

from tests.config import SKIP_TAGS
from tests.timer import Timer
from vortexasdk.client import create_client, set_client
from vortexasdk.endpoints.cargo_movements import CargoMovements


@skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
class TestCargoMovementsReal(TestCase):

    def setUp(self) -> None:
        set_client(create_client())

    def test_default_search(self):
        results = CargoMovements().search()
        print(len(results))

    def test_search_returns_unique_results(self):
        result = CargoMovements().search(
            filter_origins=['68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e'],
            filter_time_min="2019-08-29T00:00:00.000Z",
            filter_time_max="2019-10-30T00:00:00.000Z",
        )

        print("---------------------------------")
        n_results = len(result)
        print(f'Received {n_results} results')

        print(result[0])
        n_unique_results = len(set([str(k) for k in result]))
        print(f'Received {n_unique_results} unique results')

        assert n_results == n_unique_results

    def test_search_single_filter_id(self):
        df = CargoMovements().search(
            filter_products='6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653',
            filter_time_min="2019-08-29T00:00:00.000Z",
            filter_time_max="2019-08-29T00:10:00.000Z",
        ).to_df().head(2)

        assert len(df) == 2

    def test_search_single_filter_origin_name(self):
        df = CargoMovements().search(
            filter_origins='Rotterdam',
            filter_time_min="2019-08-29T00:00:00.000Z",
            filter_time_max="2019-08-29T00:10:00.000Z",
        ).to_df().head(2)

        assert len(df) == 2

    def test_search_single_filter_charterer_name(self):
        df = CargoMovements().search(
            filter_owners="DHT"
        ).to_df().head(2)

        assert len(df) == 2

    def test_search_single_filter_waypoint_name(self):
        df = CargoMovements().search(
            filter_activity='any_activity',
            filter_waypoints='Suez',
            filter_time_min="2019-08-29T00:00:00.000Z",
            filter_time_max="2019-08-29T00:10:00.000Z",
        ).to_df().head(2)

        assert len(df) == 2

    def test_search_list_filter_id(self):
        df = CargoMovements().search(
            filter_products=['6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653'],
            filter_time_min="2019-08-29T00:00:00.000Z",
            filter_time_max="2019-08-29T00:10:00.000Z",
        ).to_df().head(2)

        assert len(df) == 2
        print(tabulate.tabulate(df))

    def test_speed(self):
        with Timer("Search") as t_search:
            cms = CargoMovements().search(
                filter_time_min="2019-08-29T00:00:00.000Z",
                filter_time_max="2019-08-30T00:00:00.000Z",
            )

        with Timer("to_list") as t_to_list:
            cms.to_list()

        with Timer("df") as t_to_df:
            df = cms.to_df()

        # Check we load a reasonable number of cargo movements in a short enough period of time
        assert len(df) > 500
        assert t_search.interval < 5
        assert t_to_list.interval < 5
        assert t_to_df.interval < 5
