from unittest import TestCase

import jsons

from python_sdk.api.resources.corporate import CorporateEntity, CorporateLayer


class TestCorporateEntity(TestCase):

    def test_serialize(self):
        with open("test/api/examples/corporate_entry1.json", 'r') as f:
            serialized = f.read()
            deserialized = jsons.loads(serialized, CorporateEntity)

            expected = CorporateEntity(
                id='cbd7dfe8a9fb0fa0ce3252ce7643437db6a32d0947a0c23d68dc5dea2f2d65d7',
                layer=CorporateLayer.commercial_owner,
                probability=1,
                label='NGM Energy',
                source='external'
            )

            assert expected == deserialized
