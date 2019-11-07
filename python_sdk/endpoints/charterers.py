"""Charterers Endpoint."""
from python_sdk.constants import CHARTERERS_REFERENCE
from python_sdk.operations import Reference, Search


class Charterers(Reference, Search):

    def __init__(self):
        Reference.__init__(self, CHARTERERS_REFERENCE)
        Search.__init__(self, CHARTERERS_REFERENCE)

    def search(self, term):
        """

        # Arguments
            term: The charterer name we're filtering on

        # Returns
        List of charterers matching `term`


        # Examples

            >>> [x["name"] for x in Charterers().search(term="do")]
            ['Donsotank', 'Dorval SC']

        """

        search_params = {"term": term}
        return super().search(**search_params)
