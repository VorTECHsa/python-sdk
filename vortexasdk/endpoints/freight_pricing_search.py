"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Ffreight_pricing_search.ipynb)
"""
from datetime import datetime
from typing import Any, Dict, List, Union
from vortexasdk.api.shared_types import to_ISODate_Array
from vortexasdk.endpoints.freight_pricing_result import FreightPricingResult

from vortexasdk.endpoints.endpoints import FREIGHT_PRICING_SEARCH
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list

logger = get_logger(__name__)


class FreightPricingSearch(Search):
    """
    Freight Pricing Endpoint, use this to search through Vortexa's Baltic Exchange pricing data.
    """

    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, FREIGHT_PRICING_SEARCH)

    def search(
        self,
        routes: Union[List[str], str] = None,
        days: List[datetime] = [],
        offset: int = None,
        order: str = None,
        order_direction: str = None,
    ) -> FreightPricingResult:
        """
        List of pricing information applicable for a specified route on a given day.

        # Arguments

            routes: Used to filter by specific routes. Must be one of the following:
            - Clean routes - `TC1`, `TC2_37`, `TC5`, `TC6`, `TC7`, `TC8`, `TC9`, `TC10`, `TC11`, `TC12`, `TC14`, `TC15`, `TC16`, `TC17`, `TC18`, `TC19`.
            - Dirty routes - `TD1`, `TD2`, `TD3C`, `TD6`, `TD7`, `TD8`, `TD9`, `TD12`, `TD14`, `TD15`, `TD17`, `TD18`, `TD19`, `TD20`, `TD21`, `TD22`, `TD23`, `TD24`, `TD25`, `TD26`.
            - BLPG routes - `BLPG1`, `BLPG2`, `BLPG3`.

            days: Used to filter results by day on which the record was generated. Must be an ISO date array or not supplied.

            order: Used to sort the returned results. Must be either 'record_date' or not supplied.

            order_direction: Determines the direction of sorting. ‘asc’ for ascending, ‘desc’ for
            descending.

            offset: Used to page results. The offset from which records should be returned.

            size: Used to page results. The size of the result set. Between 0 and 500.


        # Returns
        `FreightPricingResult`


        # Example
        WS rate for the TD3C route generated on 15th Nov 2021.

        ```python
        >>> from vortexasdk import FreightPricingSearch
        >>> from datetime import datetime
        >>> day = [datetime(2021, 11, 15)]
        >>> df = FreightPricingSearch().search(
        ...        routes=['TD3C'],
        ...        days=day
        ... ).to_df(columns=['short_code','rate','rate_unit'])

        ```

        |    | short_code | rate  | rate_unit |
        |---:|:-----------|:------|----------:|
        |  0 | TD3C       | 43.32 |  WS       |

        """

        api_params: Dict[str, Any] = {
            "routes": convert_to_list(routes),
            "days": convert_to_list(to_ISODate_Array(days)),
            "offset": offset,
            "order": order,
            "order_direction": order_direction,
            "size": self._MAX_PAGE_RESULT_SIZE,
        }

        response = super().search_with_client(**api_params)

        return FreightPricingResult(
            records=response["data"], reference=response["reference"]
        )
