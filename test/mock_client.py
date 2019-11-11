from typing import List

import jsons

from vortexa.api.shared_types import ID
from vortexa.client import AbstractVortexaClient
from vortexa.constants import *


def _read(example_file):
    with open(f'test/api/examples/{example_file}', 'r') as f:
        return jsons.loads(f.read(), List)


charterers = _read("charterers.json")
vessels = _read("vessels.json")


class MockVortexaClient(AbstractVortexaClient):
    _results = {
        CHARTERERS_REFERENCE: charterers,
        VESSELS_REFERENCE: vessels
    }

    def get_reference(self, resource: str, id: ID) -> str:
        return ""

    def search(self, resource: str, **data) -> List:
        return MockVortexaClient._results[resource]
