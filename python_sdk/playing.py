from python_sdk.operations import Reference, Search
from python_sdk.client import default_client
from python_sdk.constants import GEOGRAPHIES_REFERENCE


def logInfo(a):
    print(a)  # TODO()


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
        default_client()
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
    Search("/reference/vessels").search(term="DHT"),
    v.geographies.search(term="portsmouth"),  # [0]['name']
    [x["name"] for x in v.geographies.search(term="portsmouth")],  # [0]['name']

    # v.geographies.search(termo="portsmouth")  # [0]['name']
]:
    print(f'{len(a)} {a}')
