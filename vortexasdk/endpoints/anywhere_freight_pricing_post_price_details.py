from datetime import datetime
from typing import Any, Dict, List

from vortexasdk.endpoints.endpoints import (
    ANYWHERE_FREIGHT_PRICING_PRICE_DETAILS,
)
from vortexasdk.endpoints.anywhere_freight_pricing_result import (
    AnywhereFreightPricingResult,
)
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search
from vortexasdk.utils import to_date_string

logger = get_logger(__name__)


class AnywhereFreightPricingPostPriceDetails(Search):
    """
    Anywhere Freight Pricing Post Price Details endpoint.

    Given a set of details about multiple routes (origin, destination, etc),
    this will find rates, lumpsums and prediction confidence for each route.

    Please note: you will require a subscription to our Anywhere Freight Pricing
    module to access this endpoint.
    """

    def __init__(self) -> None:
        Search.__init__(self, ANYWHERE_FREIGHT_PRICING_PRICE_DETAILS)

    def search(
        self,
        routes: List[Dict[str, Any]],
        time_min: datetime,
        time_max: datetime,
        unit: str = "usd_per_tonne",
    ) -> AnywhereFreightPricingResult:
        """
        List prices for multiple routes.

        Given a set of details about multiple routes (origin, destination, etc),
        this will find rates, lumpsums and prediction confidence for each route.

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

            unit: The unit for pricing. Must be one of: `'usd_per_tonne'`, `'usd_per_barrel'`.

        # Returns
        `AnywhereFreightPricingResult`

        # Example
        _Get price details for multiple routes._

        ```python
        >>> from vortexasdk import AnywhereFreightPricingPostPriceDetails
        >>> from datetime import datetime
        >>> routes = [
        ...     {
        ...         "origin_port": "7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
        ...         "destination_port": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
        ...         "product": "crude",
        ...         "vessel_class": "oil_aframax_lr2",
        ...     },
        ...     {
        ...         "origin_port": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
        ...         "destination_port": "ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
        ...         "product": "clean",
        ...         "vessel_class": "oil_handymax_mr2",
        ...     }
        ... ]
        >>> result = AnywhereFreightPricingPostPriceDetails().search(
        ...     routes=routes,
        ...     time_min=datetime(2024, 1, 1),
        ...     time_max=datetime(2024, 1, 31),
        ...     unit="usd_per_tonne",
        ... )
        >>> df = result.to_df()

        ```

        Returns a DataFrame with columns including rates, lumpsums, and confidence values:

        |    | date       | rate  | lumpsum   | confidence |
        |---:|:-----------|------:|----------:|-----------:|
        |  0 | 2024-01-01 | 12.50 | 1250000.0 |       0.85 |
        |  1 | 2024-01-02 | 12.75 | 1275000.0 |       0.87 |

        """
        api_params: Dict[str, Any] = {
            "routes": routes,
            "time_min": to_date_string(time_min),
            "time_max": to_date_string(time_max),
            "unit": unit,
        }

        response = super().search_with_client(
            response_type="breakdown", **api_params
        )

        return AnywhereFreightPricingResult(
            records=response["data"], reference=response.get("reference", {})
        )
