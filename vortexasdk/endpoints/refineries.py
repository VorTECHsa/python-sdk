"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%refineries.ipynb)
"""

from typing import Any, Dict, List, Optional, Union, Literal

from vortexasdk.api import ID
from vortexasdk.endpoints.endpoints import REFINERY_REFERENCE
from vortexasdk.endpoints.refineries_result import RefineriesResult
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_to_list


class Refineries(Reference, Search):
    """Refineries endpoint."""

    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self) -> None:
        """Instantiate endpoint using reference endpoint."""
        Reference.__init__(self, REFINERY_REFERENCE)
        Search.__init__(self, REFINERY_REFERENCE)

    def load_all(self) -> RefineriesResult:
        """Load all refineries."""
        return self.search()

    def search(
        self,
        term: Optional[Union[str, List[str]]] = None,
        size: Optional[int] = None,
        ids: Optional[Union[str, List[str]]] = None,
        refinery_name: Optional[str] = None,
        status: Optional[
            Literal["Active", "Shut", "Unknown", "Upcoming"]
        ] = None,
        owner_id: Optional[Union[str, List[str]]] = None,
        operator_id: Optional[Union[str, List[str]]] = None,
        exact_term_match: bool = False,
    ) -> RefineriesResult:
        """
        Find all refineries matching the given search arguments. Search arguments are combined in an AND manner.

        # Arguments
            term: The name(s) (or partial name(s)) of a refinery to search.
            ids: ID or IDs of refineries to search.
            refinery_name: The exact refinery name to search.
            status: The current status of the refinery. Must be one of "Active", "Shut", "Unknown", or "Upcoming".
            owner_id: Owner ID or list of owner IDs to filter the refineries.
            operator_id: Operator ID or list of operator IDs to filter the refineries.
            exact_term_match: If True, only exact name matches will be returned. If False, similar matches are allowed.

        # Returns
        List of refineries matching the search arguments.


        # Examples

        - Let's find all the Refineries with 'San' in their name.

        ```python
        >>> from vortexasdk import Refineries
        >>> refineries = Refineries().search("San").to_df(columns=['name', 'country_name'])

        ```
        |    |                                  name | country_name |
        |---:|--------------------------------------:|:-------------|
        |  0 | San Lorenzo Refinery Oil Combustibles | Argentina    |
        |  1 | Gibraltar-San Roque Refinery          | Spain        |

        # Further Documentation

        [VortexaAPI Refineries Reference](https://docs.vortexa.com/reference/POST/reference/refineries)

        """
        api_params: Dict[str, Any] = {
            "term": [str(e) for e in convert_to_list(term)],
            "size": size if size is not None else self._MAX_PAGE_RESULT_SIZE,
            "ids": convert_to_list(ids),
            "refinery_name": refinery_name,
            "status": status,
            "owner_id": convert_to_list(owner_id),
            "operator_id": convert_to_list(operator_id),
        }

        response = super().search_with_client(
            exact_term_match=exact_term_match, **api_params
        )

        return RefineriesResult(
            records=response["data"], reference=response["reference"]
        )

    def reference(self, id: ID) -> Dict:
        """
        Perform a refinery lookup.

        # Arguments
            id: Refinery ID to lookup

        # Returns
        Refinery record matching the ID

        # Further Documentation:
        [VortexaAPI Refinery Reference](https://docs.vortexa.com/reference/GET/reference/refineries)

        """
        return super().reference(id)
