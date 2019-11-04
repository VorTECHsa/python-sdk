import os

import requests

PAGE_SIZE = 500
REFERENCE_PAGE_SIZE = 2000

API_URL = 'https://api.vortexa.com/v5'


def logInfo(a):
    print(a)  # TODO()


class VortexaAPI(object):

    def __init__(self, **kwargs):
        self.api_key = kwargs["api_key"]

    def get_reference(self, resource, id):
        url = f'{API_URL}{resource}/{id}?apikey={self.api_key}'

        response = requests.get(url).json()

        logInfo(f'URL: {url}')
        logInfo(f'Response: {response}')

        return response['data']

    def search(self, resource, **data):
        print("searhing")
        url = f'{API_URL}{resource}?apikey={self.api_key}'
        request = requests.post(url, data=data)
        response = request.json()

        hand_data = {"term": "portsmouth"}

        print(hand_data)
        print(data)
        # response = requests.post("https://api.vortexa.com/v5/reference/geographies?apikey=017e57d2-1302-4ac5-80bc-0a0e3eb1548e", data=hand_data).json()

        logInfo(f'URL: {request.url}')
        logInfo(f'hedaers: {request.headers}')
        logInfo(f'Response: {response}')

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
        super().__init__()

    def reference(self, id):
        api = default_api()
        return api.get_reference("/reference" + self._resource, id)


class CargoMovements:
    pass


#
#     def __init__(self):
#         super().__init__("/search/cargo_movements")


class Vessels(Reference):

    def __init__(self):
        super().__init__("/vessels")


class Geographies(Reference):

    def __init__(self):
        super().__init__("/geographies")


class Products(Reference):

    def __init__(self):
        super().__init__("/products")


class VortexaSDK:

    def __init__(self):
        default_api()
        self.cargo_movements: CargoMovements = CargoMovements()
        self.vessels: Vessels = Vessels()
        self.geographies: Geographies = Geographies()
        self.products: Products = Products()


v = VortexaSDK()

# assert False
# print(default_api().reference("/reference/products", "8d752368ce24f1ef748a89da1cd14c0e4e8bba4042295815a63eaf736eda1a70"))
default_api().search("/reference/geographies", term="portsmouth")
#
# v.cargo_movements.search(origin='Sture [NO]')

for a in [
    v.vessels.reference(id='6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509'),
    v.geographies.reference(id='48fca2ce4042e5e670a26f1ed2c9dbb8788bfd9bf763deb339791c3e818e2926'),
    v.products.reference(id='8d752368ce24f1ef748a89da1cd14c0e4e8bba4042295815a63eaf736eda1a70'),
    v.geographies.reference(id='fdlgkalkh')
]:
    print(a)

# print(v.cargo_movements.search(id='123234'))
# print(v.cargo_movements.search(id='123234'))
# v.vessels.search(id='123234')
