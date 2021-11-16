from typing import List, Dict

import jsons

from vortexasdk.api import ID
from vortexasdk.abstract_client import AbstractVortexaClient
from vortexasdk.endpoints.endpoints import (
    ASSET_TANKS_REFERENCE,
    ATTRIBUTES_REFERENCE,
    CARGO_TIMESERIES_RESOURCE,
    CORPORATIONS_REFERENCE,
    PRODUCTS_REFERENCE,
    STORAGE_TERMINALS_REFERENCE,
    VESSEL_MOVEMENTS_RESOURCE,
    VESSELS_REFERENCE,
)


def _read(example_file) -> List[Dict]:
    with open(f"tests/api/examples/{example_file}", "r") as f:
        return jsons.loads(f.read(), List)


example_asset_tanks: List[Dict] = _read("asset_tanks.json")
example_attributes: List[Dict] = _read("attributes.json")
example_cargo_movements: List[Dict] = _read("vessel_movements.json")
example_corporations: List[Dict] = _read("corporations.json")
example_products: List[Dict] = _read("products.json")
example_storage_terminals: List[Dict] = _read("storage_terminals.json")
example_time_series = _read("cargo_time_series.json")
example_vessel_movements: List[Dict] = _read("vessel_movements.json")
example_vessels: List[Dict] = _read("vessels.json")


class MockVortexaClient(AbstractVortexaClient):
    _results = {
        ASSET_TANKS_REFERENCE: example_asset_tanks,
        ATTRIBUTES_REFERENCE: example_attributes,
        CARGO_TIMESERIES_RESOURCE: example_time_series,
        CORPORATIONS_REFERENCE: example_corporations,
        PRODUCTS_REFERENCE: example_products,
        STORAGE_TERMINALS_REFERENCE: example_storage_terminals,
        VESSEL_MOVEMENTS_RESOURCE: example_vessel_movements,
        VESSELS_REFERENCE: example_vessels,
    }

    def get_reference(self, resource: str, id: ID) -> List[Dict]:
        entities = MockVortexaClient._results[resource]
        return [e for e in entities if e["id"] == id]

    def search(self, resource: str, response_type=None, **data) -> List:
        return MockVortexaClient._results[resource]
