from datetime import datetime
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode

from vortexasdk.client import default_client, _handle_response
from vortexasdk.endpoints.endpoints import ANYWHERE_FREIGHT_PRICING_PRICE_DETAILS
from vortexasdk.endpoints.anywhere_freight_pricing_result import (
    AnywhereFreightPricingResult,
)
from vortexasdk.logger import get_logger
from vortexasdk.retry_session import retry_get

logger = get_logger(__name__)


def _to_date_string(dt: datetime) -> str:
    """Convert datetime to YYYY-MM-DD date string as required by AFP API."""
    return dt.strftime("%Y-%m-%d")


class AnywhereFreightPricingGetPriceDetails:
    """
    Anywhere Freight Pricing Get Price Details endpoint.

    Given a set of details about a single route (origin, destination, etc),
    this will find rates, lumpsums and prediction confidence of the route.

    Please note: you will require a subscription to our Anywhere Freight Pricing
    module to access this endpoint.
    """

    def __init__(self) -> None:
        self._resource = ANYWHERE_FREIGHT_PRICING_PRICE_DETAILS

    def search(
        self,
        time_min: datetime,
        time_max: datetime,
        origin_port: str,
        destination_port: str,
        vessel_class: str,
        product: str,
        unit: str = "usd_per_tonne",
        avoid_zone: Optional[List[str]] = None,
        suggested_tonnage: Optional[float] = None,
    ) -> AnywhereFreightPricingResult:
        """
        List prices of a route.

        Given a set of details about a single route (origin, destination, etc),
        this will find rates, lumpsums and prediction confidence of the route.

        # Arguments

            time_min: The UTC start date of the time filter.

            time_max: The UTC end date of the time filter.

            origin_port: Geographic ID of the origin port.

            destination_port: Geographic ID of the destination port.

            vessel_class: The vessel class for the route. Must be one of:
                `'oil_coastal'`, `'oil_specialised'`, `'oil_handysize_mr1'`,
                `'oil_handymax_mr2'`, `'oil_panamax_lr1'`, `'oil_aframax_lr2'`,
                `'oil_suezmax_lr3'`, `'oil_vlcc'`.

            product: The product type. Must be one of: `'clean'`, `'dirty'`, `'crude'`.

            unit: The unit for pricing. Must be one of: `'usd_per_tonne'`, `'usd_per_barrel'`.
                Defaults to `'usd_per_tonne'`.

            avoid_zone: Routing zones to avoid for this route. Options:
                `'Panama Canal'`, `'Suez Canal'`.

            suggested_tonnage: Override the default suggested tonnage Vortexa will
                suggest based on the vessel class.

        # Returns
        `AnywhereFreightPricingResult`

        # Example
        _Get price details for an Aframax LR2 crude route from Houston to Rotterdam._

        ```python
        >>> from vortexasdk import AnywhereFreightPricingGetPriceDetails
        >>> from datetime import datetime
        >>> result = AnywhereFreightPricingGetPriceDetails().search(
        ...     time_min=datetime(2024, 1, 1),
        ...     time_max=datetime(2024, 12, 31),
        ...     origin_port="7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
        ...     destination_port="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
        ...     vessel_class="oil_aframax_lr2",
        ...     product="crude",
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
        logger.info(
            f"Fetching Anywhere Freight Pricing price details for route "
            f"{origin_port} -> {destination_port}"
        )

        params: Dict[str, Any] = {
            "time_min": _to_date_string(time_min),
            "time_max": _to_date_string(time_max),
            "origin_port": origin_port,
            "destination_port": destination_port,
            "vessel_class": vessel_class,
            "product": product,
            "unit": unit,
        }

        if avoid_zone:
            params["avoid_zone"] = avoid_zone

        if suggested_tonnage is not None:
            params["suggested_tonnage"] = suggested_tonnage

        client = default_client()
        url = client._create_url(self._resource)

        # Use doseq=True to handle list parameters (avoid_zone)
        query_string = urlencode(params, doseq=True)
        url = f"{url}&{query_string}"

        response = retry_get(url)

        data = _handle_response(response)
        return AnywhereFreightPricingResult(
            records=data.get("data", []),
            reference=data.get("metadata", {}),
        )
