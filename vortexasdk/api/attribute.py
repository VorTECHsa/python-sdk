from typing import Optional


from vortexasdk.api.shared_types import Node


class Attribute(Node):
    """
    Represent an Attribute reference record returned by the API.
    """

    type: Optional[str] = None
