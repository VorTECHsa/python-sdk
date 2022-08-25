from pydantic import BaseModel


from vortexasdk.api.shared_types import Node


class Attribute(Node, BaseModel):
    """
    Represent an Attribute reference record returned by the API.
    """

    id: str
    name: str
    type: str
