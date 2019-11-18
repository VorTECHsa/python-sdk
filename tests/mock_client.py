from typing import List

import jsons

from vortexasdk.api import ID
from vortexasdk.abstract_client import AbstractVortexaClient
from vortexasdk.endpoints.endpoints import CHARTERERS_REFERENCE, VESSELS_REFERENCE, PRODUCTS_REFERENCE


def _read(example_file) -> List:
    with open(f'tests/api/examples/{example_file}', 'r') as f:
        return jsons.loads(f.read(), List)


example_charterers: List = _read("charterers.json")
example_vessels: List = _read("vessels.json")
example_products: List = _read("products.json")


class MockVortexaClient(AbstractVortexaClient):
    _results = {
        CHARTERERS_REFERENCE: example_charterers,
        VESSELS_REFERENCE: example_vessels,
        PRODUCTS_REFERENCE: example_products,
    }

    def get_reference(self, resource: str, id: ID) -> str:
        return ""

    def search(self, resource: str, **data) -> List:
        return MockVortexaClient._results[resource]
