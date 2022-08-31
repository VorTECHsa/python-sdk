from typing import Optional
from pydantic import BaseModel


from vortexasdk.api.shared_types import Node


class Attribute(Node, BaseModel):
    """
    Represent an Attribute reference record returned by the API.
    """

    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
