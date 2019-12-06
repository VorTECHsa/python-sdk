from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import CargoMovements


class TestVortexaClient(TestCaseUsingRealAPI):
    def test_get_reference(self):
        CargoMovements().search(
            filter_activity="loading_state",
            filter_origins=[
                "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
            ],
            filter_time_min=datetime(2016, 8, 29),
            filter_time_max=datetime(2020, 10, 29),
        )
