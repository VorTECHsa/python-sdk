from tests.testcases import TestCaseUsingMockAPI
from vortexasdk.endpoints.attributes import Attributes


class TestAttributes(TestCaseUsingMockAPI):

    def test_pandas_version(self):
        import pandas as pd

        if pd.__version__ != '0.25.2':
            raise ImportError(f"Running pandas {pd.__version__}")

    def test_search_ids_retreives_names(self):
        attributes = Attributes().search().to_list()

        names = [x.name for x in attributes]

        assert names == ["Open Loop", "Unknown", "DFDE"]
