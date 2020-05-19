from tests.testcases import TestCaseUsingMockAPI
from vortexasdk.endpoints.attributes import Attributes


class TestAttributes(TestCaseUsingMockAPI):
    def test_search_ids_retreives_names(self):
        attributes = Attributes().search().to_list()

        names = [x.name for x in attributes]

        assert names == ["Open Loop", "Unknown", "DFDE"]
