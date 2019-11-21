"""Corporations Endpoint."""
from typing import List, Union

from vortexasdk.endpoints.endpoints import CORPORATIONS_REFERENCE
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_values_to_list


class Corporations(Reference, Search):
    """Corporations Endpoint."""

    def __init__(self):
        Reference.__init__(self, CORPORATIONS_REFERENCE)
        Search.__init__(self, CORPORATIONS_REFERENCE)

    def search(self, term: Union[str, List[str]]):
        """
        Find all Corporations matching given search terms.

        # Arguments
            term: The corporation name(s) we're filtering on

        # Returns
        List of corporation matching `term`


        # Examples


        ```python
        >>> from vortexasdk import Corporations
        >>> [x["name"] for x in Corporations().search(term="do")]
            ['Donsotank', 'Dorval SC']
        ```
        """
        params = convert_values_to_list({"term": term})
        return super().search(**params)
