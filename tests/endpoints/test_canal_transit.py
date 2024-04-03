from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.endpoints.canal_transit import CanalTransits


class TestCanalTransitReal(TestCaseUsingRealAPI):
    def test_default_search(self):
        CanalTransits().search()
