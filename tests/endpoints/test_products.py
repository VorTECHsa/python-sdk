from unittest import TestCase
#from tests.mock_client import MockVortexaClient
#from vortexa.client import set_client
from vortexa.endpoints.products import Products


#class TestProducts(TestCase):
#
#    @classmethod
#    def setUpClass(cls) -> None:
#        set_client(MockVortexaClient())
#
#    def test_search_ids_retreives_names(self):
#        products = Products().search().to_list()
#
#        names = [x.name for x in products]
#
#        assert names == ['0', '058']




if __name__ == '__main__':
    import vortexa.endpoints.products_vcopy as p
    datap = p.Products().search(term='sul')
    data_df = datap.to_df()
    data_list = datap.to_list()

