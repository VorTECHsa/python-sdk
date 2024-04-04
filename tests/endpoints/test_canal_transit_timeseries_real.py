from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.endpoints.canal_transit_timeseries import CanalTransitTimeseries


class TestCanalTransitTimeseries(TestCaseUsingRealAPI):
    def test_default_search(self):
        CanalTransitTimeseries().search()
