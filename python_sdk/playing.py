import os

import requests

PAGE_SIZE = 500
REFERENCE_PAGE_SIZE = 2000

GEOGRAPHIES_REFERENCE = "/reference/geographies"
VESSELS_REFERENCE = "/reference/vessels"
PRODUCTS_REFERENCE = "/reference/products"
CHARTERERS_REFERENCE = "/reference/charterers"

API_URL = 'https://api.vortexa.com/v5'


def logInfo(a):
    print(a)  # TODO()


class VortexaAPI(object):

    def __init__(self, **kwargs):
        self.api_key = kwargs["api_key"]

    def get_reference(self, resource, id):
        url = f'{API_URL}{resource}/{id}?apikey={self.api_key}'

        response = requests.get(url).json()
        # logInfo(f'URL: {url}')
        # logInfo(f'Response: {response}')
        return response['data']

    def search(self, resource, **data):
        url = f'{API_URL}{resource}?apikey={self.api_key}'
        # logInfo(f'URL: {request.url}')
        # logInfo(f'hedaers: {request.headers}')
        response = requests.post(url, data=data).json()
        # logInfo(f'Response: {response}')
        return response['data']


__api__ = None


def default_api():
    global __api__

    if __api__ is None:
        __api__ = VortexaAPI(api_key=os.environ["VORTEXA_API_KEY"])

    return __api__


class Reference:
    def __init__(self, resource):
        self._resource = resource

    def reference(self, id):
        api = default_api()
        return api.get_reference(self._resource, id)


class Search:
    def __init__(self, resource):
        self._resource = resource

    def search(self, **data):
        api = default_api()
        return api.search(self._resource, **data)


class Vessels(Reference):

    def __init__(self):
        super().__init__("/vessels")


class Geographies(Reference, Search):

    def __init__(self):
        Reference.__init__(self, GEOGRAPHIES_REFERENCE)
        Search.__init__(self, GEOGRAPHIES_REFERENCE)

    def search(self, term):
        """

        Args:
            *term*: The geography name we're filtering on

        Returns: List of geographies matching *term*

        Examples:

            >>> [x["name"] for x in Geographies().search(term="portsmouth")]
            ['Portsmouth [GB]', 'Portsmouth, NH [US]']

        """

        search_params = {"term": term}
        return super().search(**search_params)


class Products(Reference):

    def __init__(self):
        super().__init__("")


class VortexaSDK:

    def __init__(self):
        default_api()
        # self.cargo_movements: CargoMovements = CargoMovements()
        # self.vessels: Vessels = Vessels()
        self.geographies: Geographies = Geographies()
        # self.products: Products = Products()


v = VortexaSDK()

print(Geographies.__mro__)

# assert False
# print(default_api().reference("/reference/products", "8d752368ce24f1ef748a89da1cd14c0e4e8bba4042295815a63eaf736eda1a70"))
# default_api().search("/reference/geographies", term="portsmouth")
#
# v.cargo_movements.search(origin='Sture [NO]')

for a in [
    # v.vessels.reference(id='6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509'),
    # v.geographies.reference(id='48fca2ce4042e5e670a26f1ed2c9dbb8788bfd9bf763deb339791c3e818e2926'),
    # v.products.reference(id='8d752368ce24f1ef748a89da1cd14c0e4e8bba4042295815a63eaf736eda1a70'),
    # v.geographies.reference(id='cfb8c4ef76585c3a37792b643791a0f4ff6d5656d5508927d8017319e21f2fca'),
    v.geographies.search(term="portsmouth"),  # [0]['name']
    [x["name"] for x in v.geographies.search(term="portsmouth")],  # [0]['name']

    # v.geographies.search(termo="portsmouth")  # [0]['name']
]:
    print(f'{len(a)} {a}')
