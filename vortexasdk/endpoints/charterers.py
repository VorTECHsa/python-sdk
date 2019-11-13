"""Charterers Endpoint."""
from typing import List, Union

from vortexasdk.endpoints.endpoints import CHARTERERS_REFERENCE
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_values_to_list


class Charterers(Reference, Search):
    """Charterers Endpoint."""

    def __init__(self):
        Reference.__init__(self, CHARTERERS_REFERENCE)
        Search.__init__(self, CHARTERERS_REFERENCE)

    def search(self, term: Union[str, List[str]]):
        """
        Find all Charterers matching given search terms.

        # Arguments
            term: The charterer name(s) we're filtering on

        # Returns
        List of charterers matching `term`


        # Examples

            >>> [x["name"] for x in Charterers().search(term="do")]
            ['Donsotank', 'Dorval SC']

        """
        params = convert_values_to_list({"term": term})
        return super().search(**params)
