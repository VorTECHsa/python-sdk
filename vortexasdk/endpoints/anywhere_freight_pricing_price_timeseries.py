from datetime import datetime
from typing import Any, Dict, List

from vortexasdk.endpoints.endpoints import (
    ANYWHERE_FREIGHT_PRICING_PRICE_TIMESERIES,
)
from vortexasdk.endpoints.anywhere_freight_pricing_result import (
    AnywhereFreightPricingResult,
)
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search
from vortexasdk.utils import to_date_string

logger = get_logger(__name__)


class AnywhereFreightPricingPriceTimeseries(Search):
    """
    Anywhere Freight Pricing Price Timeseries endpoint.

    Please note: you will require a subscription to our Anywhere Freight Pricing
    module to access this endpoint.
    """

    def __init__(self) -> None:
        Search.__init__(self, ANYWHERE_FREIGHT_PRICING_PRICE_TIMESERIES)

    def search(
        self,
        routes: List[Dict[str, Any]],
        time_min: datetime,
        time_max: datetime,
        frequency: str = "month",
        unit: str = "usd_per_tonne",
    ) -> AnywhereFreightPricingResult:
        """
        Get historical pricing over time for multiple routes.

        Given a set of details about multiple routes (origin, destination, etc),
        a time period and frequency, this returns historical pricing over time
        bucketed by the chosen frequency.

        # Arguments

            routes: A list of route dictionaries. Each route must contain:
                - `origin_port` (str, required): Geographical ID of the origin port.
                - `destination_port` (str, required): Geographical ID of the destination port.
                - `product` (str, required): One of `'clean'`, `'dirty'`, `'crude'`.
                - `vessel_class` (str, required): One of `'oil_coastal'`, `'oil_specialised'`,
                  `'oil_handysize_mr1'`, `'oil_handymax_mr2'`, `'oil_panamax_lr1'`,
                  `'oil_aframax_lr2'`, `'oil_suezmax_lr3'`, `'oil_vlcc'`.
                - `avoid_zone` (list, optional): Routing zones to avoid. Options:
                  `'Panama Canal'`, `'Suez Canal'`.
                - `suggested_tonnage` (float, optional): Suggested tonnage for the route.

            time_min: The UTC start date of the time filter.

            time_max: The UTC end date of the time filter.

            frequency: Frequency denoting the granularity of the time series.
                Must be one of: `'day'`, `'week'`, `'doe_week'`, `'month'`, `'quarter'`, `'year'`.

            unit: The unit for pricing. Must be one of: `'usd_per_tonne'`, `'usd_per_barrel'`.

        # Returns
        `AnywhereFreightPricingResult`

        # Example
        _Get daily pricing for a Handymax MR2 clean route from Rotterdam to New York._

        ```python
        >>> from vortexasdk import AnywhereFreightPricingPriceTimeseries
        >>> from datetime import datetime
        >>> routes = [
        ...     {
        ...         "origin_port": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
        ...         "destination_port": "ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
        ...         "product": "clean",
        ...         "vessel_class": "oil_handymax_mr2",
        ...     }
        ... ]
        >>> result = AnywhereFreightPricingPriceTimeseries().search(
        ...     routes=routes,
        ...     time_min=datetime(2026, 2, 20),
        ...     time_max=datetime(2026, 5, 20),
        ...     frequency="day",
        ...     unit="usd_per_tonne",
        ... )
        >>> df = result.to_df()

        ```

        Returns a DataFrame with columns:

        |    | origin_port | destination_port | vessel_class         | product | date       | price | price_lower | price_upper | voyage_price   |
        |---:|:------------|:-----------------|:---------------------|:--------|:-----------|------:|------------:|------------:|-------------- :|
        |  0 | 68faf65a... | ea4921c8...      | oil_handymax_mr2     | clean   | 2026-02-20 | 15.50 |       14.00 |       17.00 |      16.223888 |
        |  1 | 68faf65a... | ea4921c8...      | oil_handymax_mr2     | clean   | 2026-02-21 | 16.20 |       14.80 |       17.60 |      16.223888 |

        """
        api_params: Dict[str, Any] = {
            "routes": routes,
            "time_min": to_date_string(time_min) if time_min else None,
            "time_max": to_date_string(time_max) if time_max else None,
            "frequency": frequency,
            "unit": unit,
        }

        response = super().search_with_client(
            response_type="breakdown", **api_params
        )

        return AnywhereFreightPricingResult(
            records=response["data"], reference=response.get("reference", {})
        )
