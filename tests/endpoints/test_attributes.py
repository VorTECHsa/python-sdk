from tests.testcases import TestCaseUsingMockAPI
from vortexasdk.endpoints.attributes import Attributes


class TestAttributes(TestCaseUsingMockAPI):
    def test_search_ids_retreives_names(self):
        attributes = Attributes().search().to_list()

        names = [x.name for x in attributes]

        assert names == ["Open Loop", "Unknown", "DFDE"]

    def test_search_names(self):
        attributes = Attributes().search(ids=["14c7b073809eb565"]).to_list()

        names = [a.name for a in attributes]
        assert "Open Loop" in names
