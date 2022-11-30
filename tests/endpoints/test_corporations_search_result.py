from unittest import TestCase

import pandas as pd

from tests.mock_client import example_corporations
from vortexasdk.endpoints.corporations_result import CorporationsResult


class TestCorporationsSearchResult(TestCase):
    cr = CorporationsResult(records=example_corporations, reference={})

    def test_to_df(self):
        df = self.cr.to_df(["name", "corporate_entity_type"])

        expected = pd.DataFrame(
            {
                "name": {0: "3J", 1: "5XJAPANESE"},
                "corporate_entity_type": {
                    0: ["effective_controller"],
                    1: ["effective_controller"],
                },
            }
        )
        assert expected.equals(df)

    def test_to_list(self):
        names = [x.name for x in self.cr.to_list()]

        assert names == ["3J", "5XJAPANESE"]
