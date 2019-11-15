from unittest import TestCase, skipIf

import tabulate

from tests.config import SKIP_TAGS
from vortexasdk.client import default_client, set_client
from vortexasdk.endpoints.cargo_movements import CargoMovements


@skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
class TestCargoMovementsReal(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        set_client(default_client())

    def test_defaullt_search(self):
        results = CargoMovements().search()
        print(len(results))

    def test_search_returns_unique_results(self):
        result = CargoMovements().search(
            filter_origins=['68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e'],
            filter_time_min="2017-08-29T00:00:00.000Z",
            filter_time_max="2017-08-30T00:00:00.000Z",
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

        print(tabulate.tabulate(df))

    def test_search_list_filter_id(self):
        df = CargoMovements().search(
            filter_products=['6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653'],
            filter_time_min="2019-08-29T00:00:00.000Z",
            filter_time_max="2019-08-29T00:10:00.000Z",
        ).to_df().head(2)

        print(tabulate.tabulate(df))
