from unittest import TestCase, skipIf

from tests.config import SKIP_TAGS
from vortexasdk.client import create_client, set_client
from vortexasdk.endpoints.products import Products


@skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
class TestProductsReal(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        set_client(create_client())

    def test_search_ids(self):
        ids = [
            "e166e6253dd843624f6cbe4fd45e7f2cff4671e600b4d6371172dd92a0255946",
            "6cd99c8f9e67e61892a691237b3342a4caae5ec1c76784b1b93952afda44ae24"
        ]

        products = Products().search(ids=ids).to_list()
        assert len(products) == 2

        print([x.name for x in products])


    def test_search_ids_dataframe(self):
        ids = [
            "e166e6253dd843624f6cbe4fd45e7f2cff4671e600b4d6371172dd92a0255946",
            "6cd99c8f9e67e61892a691237b3342a4caae5ec1c76784b1b93952afda44ae24"
        ]

        df = Products().search(ids=ids).to_df()
        assert list(df.columns) == ['id', 'name', 'parent']
        assert len(df) == 2

