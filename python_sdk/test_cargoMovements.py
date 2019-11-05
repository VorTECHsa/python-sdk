from unittest import TestCase

from python_sdk.movements import CargoMovements


class TestCargoMovements(TestCase):
    def test_defaullt_search(self):
        print(CargoMovements().search())

    def test_search(self):
        result = CargoMovements().search(
            filter_origins=['68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e'],
            cm_size=10
        )

        assert len(result) == 10
