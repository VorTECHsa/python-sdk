from dataclasses import dataclass

from vortexasdk.api.serdes import FromDictMixin
from vortexasdk.api.shared_types import Node


@dataclass(frozen=True,)
class Attribute(Node, FromDictMixin):
    """
    Represent an Attribute reference record returned by the API.
    """

    id: str
    name: str
    type: str
