"""Geographies Endpoint."""
from typing import List, Union

from vortexa.constants import GEOGRAPHIES_REFERENCE
from vortexa.operations import Reference, Search
from vortexa.utils import convert_values_to_list


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

        params = convert_values_to_list({"term": term})
        return super().search(**params)
