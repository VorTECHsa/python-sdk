"""Geographies Endpoint."""
from typing import List, Union

from python_sdk.constants import GEOGRAPHIES_REFERENCE
from python_sdk.operations import Reference, Search


class Geographies(Reference, Search):

    def __init__(self):
        Reference.__init__(self, GEOGRAPHIES_REFERENCE)
        Search.__init__(self, GEOGRAPHIES_REFERENCE)

    def search(self, term: Union[str, List[str]]):
        """

        # Arguments
            term: The geography name (or names) we're filtering on

        # Returns
        List of geographies matching `term`


        # Examples

            >>> [x["name"] for x in Geographies().search(term="portsmouth")]
            ['Portsmouth [GB]', 'Portsmouth, NH [US]']

        """

        search_params = {"term": term}
        return super().search(**search_params)
