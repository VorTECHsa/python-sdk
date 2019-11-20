from unittest import TestCase, skipIf

from tests.config import SKIP_TAGS
from vortexasdk.client import create_client, set_client
from vortexasdk.endpoints.products import Products


@skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
class TestProductsReal(TestCase):

    def setUp(self) -> None:
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

    def test_search_crude(self):
        set_client(create_client())

        result = [p.id for p in Products().search("Crude").to_list()]

        assert "6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653" in result

    def test_lookup_crude(self):
        set_client(create_client())

        result = Products().reference("6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653")

        assert result[0]['name'] == 'Crude'
