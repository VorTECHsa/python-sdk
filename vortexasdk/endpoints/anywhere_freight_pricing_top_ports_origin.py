from typing import Any, Dict, List, Optional

from vortexasdk.client import default_client, _handle_response
from vortexasdk.endpoints.endpoints import ANYWHERE_FREIGHT_PRICING_TOP_PORTS_ORIGIN
from vortexasdk.endpoints.anywhere_freight_pricing_result import (
    AnywhereFreightPricingResult,
)
from vortexasdk.logger import get_logger
from vortexasdk.retry_session import retry_post

logger = get_logger(__name__)


class AnywhereFreightPricingTopPortsOrigin:
    """
    Anywhere Freight Pricing Top Ports Origin endpoint.

    List top origin ports. A top origin port refers to the port
    with the greatest volume of outgoing voyages from vessels in a specified class.

    Please note: you will require a subscription to our Anywhere Freight Pricing
    module to access this endpoint.
    """

    def __init__(self) -> None:
        self._resource = ANYWHERE_FREIGHT_PRICING_TOP_PORTS_ORIGIN

    def search(
        self,
        destination_id: str,
        vessel_class: str,
        product: str,
        unit: str = "usd_per_tonne",
        avoid_zone: Optional[List[str]] = None
    ) -> AnywhereFreightPricingResult:
        """
        List top origin ports for a given destination.

        A top origin port refers to the port with the greatest volume of
        outgoing voyages from vessels in a specified class.

        # Arguments

            destination_id: Geographical ID of the destination port.

            vessel_class: The vessel class for the route. Must be one of:
                `'oil_coastal'`, `'oil_specialised'`, `'oil_handysize_mr1'`,
                `'oil_handymax_mr2'`, `'oil_panamax_lr1'`, `'oil_aframax_lr2'`,
                `'oil_suezmax_lr3'`, `'oil_vlcc'`.

            product: The product type. Must be one of: `'clean'`, `'dirty'`, `'crude'`.

            unit: The unit for pricing. Must be one of: `'usd_per_tonne'`, `'usd_per_barrel'`.
                Defaults to `'usd_per_tonne'`.

            avoid_zone: Routing zones to avoid. Options: `'Panama Canal'`, `'Suez Canal'`.

        # Returns
        `AnywhereFreightPricingResult`

        # Example
        _Get top origin ports for clean products to Rotterdam using MR2 vessels._

        ```python
        >>> from vortexasdk import AnywhereFreightPricingTopPortsOrigin
        >>> result = AnywhereFreightPricingTopPortsOrigin().search(
        ...     destination_id="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
        ...     vessel_class="oil_handymax_mr2",
        ...     product="clean",
        ...     unit="usd_per_tonne",
        ... )
        >>> df = result.to_df()

        ```

        Returns a DataFrame with columns including geography info, rates, lumpsums,
        and confidence values:

        |    | geography_name | date       | rate  | lumpsum     | confidence |
        |---:|:---------------|:-----------|------:|------------:|-----------:|
        |  0 | Houston [US]   | 2024-01-01 | 63.55 | 2351511.83  |          2 |

        """
        logger.info(
            f"Fetching Anywhere Freight Pricing top origin ports for destination {destination_id}"
        )

        payload: Dict[str, Any] = {
            "destination_id": destination_id,
            "vessel_class": vessel_class,
            "product": product,
            "unit": unit,
        }

        if avoid_zone is not None:
            payload["avoid_zone"] = avoid_zone

        client = default_client()
        url = client._create_url(self._resource)

        response = retry_post(url, json=payload)

        data = _handle_response(response)
        return AnywhereFreightPricingResult(
            records=data.get("data", []),
            reference=data.get("metadata", {}),
        )
