from tests.testcases import TestCaseUsingRealAPI
from tests.timer import Timer
from vortexasdk.endpoints.attributes import Attributes


class TestAttributesReal(TestCaseUsingRealAPI):
    def test_search_ids(self):
        ids = [
            "14c7b073809eb565",
            "3ace0e050724707b",
        ]

        attributes = Attributes().search(ids=ids).to_list()
        assert len(attributes) == 2

        print([x.name for x in attributes])

    def test_search_filters_term(self):
        term = ["Open Loop Hybrid Ready"]

        attributes = Attributes().search(term=term).to_list()

        actual = {x.name for x in attributes}

        assert actual == set(term)

    def test_search_ids_dataframe(self):
        ids = [
            "4729c38b99262b73",
            "478fca39000c49d6",
        ]

        df = Attributes().search(ids=ids).to_df()
        assert list(df.columns) == ["id", "name", "type"]
        assert len(df) == 2

    def test_load_all(self):
        all_attributes = Attributes().load_all()

        assert len(all_attributes) > 40

    def test_search_load_all_attributes(self):
        with Timer("Search"):
            result = Attributes().search()

        with Timer("Serialize"):
            result.to_list()

        with Timer("Dataframe"):
            df = result.to_df()
            print(df.head())

        assert len(result) >= 40

    def test_search_is_case_agnostic(self):
        uppercase = {v.id for v in Attributes().search(term="open").to_list()}
        lowercase = {v.id for v in Attributes().search(term="OpEn").to_list()}

        assert uppercase == lowercase
