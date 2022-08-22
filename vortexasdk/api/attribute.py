from pydantic.dataclasses import dataclass


from vortexasdk.api.shared_types import Node


@dataclass(
    frozen=True,
)
class Attribute(Node):
    """
    Represent an Attribute reference record returned by the API.
    """

    id: str
    name: str
    type: str
