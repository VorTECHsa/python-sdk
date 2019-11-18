from abc import ABC
from typing import List

from vortexasdk.api import ID


class AbstractVortexaClient(ABC):
    """Base client."""

    def get_reference(self, resource: str, id: ID) -> str:
        """Lookup reference data."""
        raise NotImplementedError

    def search(self, resource: str, **data) -> List:
        """Search."""
        raise NotImplementedError
