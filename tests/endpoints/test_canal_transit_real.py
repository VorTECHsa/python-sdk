from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.endpoints.canal_transit import CanalTransit


class TestCanalTransitReal(TestCaseUsingRealAPI):
    def test_default_search(self):
        CanalTransit().search()
