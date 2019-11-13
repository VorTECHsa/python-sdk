from unittest import TestCase, skipIf

from tests.config import SKIP_TAGS
from vortexasdk.endpoints.cargo_movements import CargoMovements


@skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
class TestCargoMovementsReal(TestCase):
    def test_defaullt_search(self):
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
