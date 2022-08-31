from unittest import TestCase
import json

from vortexasdk.api.geography import GeographyEntity


class TestGeographyEntity(TestCase):
    def test_serialize(self):
        with open("tests/api/examples/geography_entity1.json", "r") as f:
            serialized = json.load(f)
            deserialized = GeographyEntity.parse_obj(serialized)

            expected = GeographyEntity(
                id="2aaad41b89dfad19e5668918018ae02695d7710bcbe5f2dc689234e8da492de3",
                layer="country",
                label="United Kingdom",
                source="model",
                probability=1,
            )

            assert expected == deserialized
