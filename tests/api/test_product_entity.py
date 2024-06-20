import json
from unittest import TestCase

from vortexasdk.api.product import ProductEntityWithSingleLayer


class TestProductEntity(TestCase):
    def test_serialize(self):
        with open("tests/api/examples/product_entity1.json", "r") as f:
            serialized = json.load(f)
            deserialized = ProductEntityWithSingleLayer.parse_obj(serialized)

            expected = ProductEntityWithSingleLayer(
                id="6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653",
                layer="group",
                probability=0.9369364,
                label="Crude & Condensates",
                source="model",
            )

            assert expected == deserialized

    def test_instantiate_from_dict(self):
        dictionary = {
            "id": "b68cbb746f8b9098c50e2ba36bcad83001a53bd362e9031fb49085d02c36659c",
            "layer": "group",
            "probability": 0.4756425,
            "source": "model",
            "label": "Clean products",
        }

        p = ProductEntityWithSingleLayer.parse_obj(dictionary)

        assert p.source == "model"
