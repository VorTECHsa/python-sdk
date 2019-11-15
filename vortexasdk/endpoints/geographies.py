"""Geographies Endpoint."""
from typing import List, Union

from vortexasdk.api.id import ID
from vortexasdk.endpoints.endpoints import GEOGRAPHIES_REFERENCE
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_values_to_list


class Geographies(Reference, Search):
    """Geographies endpoint."""

    def __init__(self):
        Reference.__init__(self, GEOGRAPHIES_REFERENCE)
        Search.__init__(self, GEOGRAPHIES_REFERENCE)

    def search(self, term: Union[str, List[str]]):
        """
        Find all geographies matching given search terms.

        # Arguments
            term: The geography name (or names) we're filtering on

        # Returns
        List of geographies matching `term`


        # Examples

        Find all geographies with `portsmouth` in the name.
            >>> [x["name"] for x in Geographies().search(term="portsmouth")]
            ['Portsmouth [GB]', 'Portsmouth, NH [US]']


        Search multiple geography terms
            >>> [x["name"] for x in Geographies().search(term=["Liverpool", "Southampton"])]
            ['Liverpool [GB]', 'Southampton [GB]', 'Liverpool Docks', 'Liverpool Bulk Liquids']

        """
        params = convert_values_to_list({"term": term})
        return super().search(**params)


def _search_geography_ids(names: List[str]) -> List[ID]:
    """Find list of IDs matching names."""
    return [g['id'] for g in Geographies().search(term=names)]
