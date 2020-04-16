from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import VesselMovements


class TestVesselMovementsRealVesselStatus(TestCaseUsingRealAPI):
    def test_search(self):
        v = VesselMovements().search(
            filter_time_min=datetime(2019, 10, 1),
            filter_time_max=datetime(2019, 10, 15),
            filter_vessel_classes=["vlcc"],
            filter_vessel_status="vessel_status_ballast",
        )

        assert len(v) > 50
