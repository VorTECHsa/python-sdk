from unittest import TestCase

import jsons

from python_sdk.api.resources.product import ProductEntity, ProductLayer


class TestProductEntity(TestCase):

    def test_serialize(self):
        with open("test/api/examples/product_entry1.json", 'r') as f:
            serialized = f.read()
            deserialized = jsons.loads(serialized, ProductEntity)

            expected = ProductEntity(
                id='6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653',
                layer=ProductLayer.group,
                probability=0.9369364,
                label='Crude & Condensates'
            )

            assert expected == deserialized
