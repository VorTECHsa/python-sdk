from typing import Optional
from pydantic import BaseModel


from vortexasdk.api.shared_types import Node


class Attribute(Node, BaseModel):
    """
    Represent an Attribute reference record returned by the API.
    """

    type: Optional[str] = None
