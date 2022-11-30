from unittest import TestCase
import json


from vortexasdk.api.corporation import CorporateEntity


class TestCorporateEntity(TestCase):
    def test_serialize(self):
        with open("tests/api/examples/corporate_entity1.json", "r") as f:
            serialized = json.load(f)
            deserialized = CorporateEntity.parse_obj(serialized)

            expected = CorporateEntity(
                id="cbd7dfe8a9fb0fa0ce3252ce7643437db6a32d0947a0c23d68dc5dea2f2d65d7",
                layer="effective_controller",
                probability=1,
                label="NGM Energy",
                source="external",
            )

            assert expected == deserialized
