"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAABZCAMAAABi1XidAAAB8lBMVEX///9XmsrmZYH1olJXmsr1olJXmsrmZYH1olJXmsr1olJXmsrmZYH1olL1olJXmsr1olJXmsrmZYH1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olJXmsrmZYH1olL1olL0nFf1olJXmsrmZYH1olJXmsq8dZb1olJXmsrmZYH1olJXmspXmspXmsr1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olLeaIVXmsrmZYH1olL1olL1olJXmsrmZYH1olLna31Xmsr1olJXmsr1olJXmsrmZYH1olLqoVr1olJXmsr1olJXmsrmZYH1olL1olKkfaPobXvviGabgadXmsqThKuofKHmZ4Dobnr1olJXmsr1olJXmspXmsr1olJXmsrfZ4TuhWn1olL1olJXmsqBi7X1olJXmspZmslbmMhbmsdemsVfl8ZgmsNim8Jpk8F0m7R4m7F5nLB6jbh7jbiDirOEibOGnKaMhq+PnaCVg6qWg6qegKaff6WhnpKofKGtnomxeZy3noG6dZi+n3vCcpPDcpPGn3bLb4/Mb47UbIrVa4rYoGjdaIbeaIXhoWHmZYHobXvpcHjqdHXreHLroVrsfG/uhGnuh2bwj2Hxk17yl1vzmljzm1j0nlX1olL3AJXWAAAAbXRSTlMAEBAQHx8gICAuLjAwMDw9PUBAQEpQUFBXV1hgYGBkcHBwcXl8gICAgoiIkJCQlJicnJ2goKCmqK+wsLC4usDAwMjP0teleN20NbsvaOsY2+3LL9/Tz1bC0dLQ1dXZ2Nrf4+Lk5urq7/P3+fn4+Pz9/f7+/gB+Q1KaQJdScAAAAAElFTkSuQmCC)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fanywhere_freight_pricing_top_ports_destination.ipynb)
"""
from typing import Any, Dict, List, Optional

from vortexasdk.client import default_client, _handle_response
from vortexasdk.endpoints.endpoints import (
    ANYWHERE_FREIGHT_PRICING_TOP_PORTS_DESTINATION,
)
from vortexasdk.endpoints.anywhere_freight_pricing_result import (
    AnywhereFreightPricingResult,
)
from vortexasdk.endpoints.anywhere_freight_pricing_types import (
    AfpAvoidZone,
    AfpProduct,
    AfpUnit,
    AfpVesselClass,
)
from vortexasdk.logger import get_logger
from vortexasdk.retry_session import retry_post

logger = get_logger(__name__)


class AnywhereFreightPricingTopPortsDestination:
    """
    Anywhere Freight Pricing Top Ports Destination endpoint.

    List top destination ports. A top destination port refers to the port
    with the greatest volume of incoming voyages from vessels in a specified class.

    Please note: you will require a subscription to our Anywhere Freight Pricing
    module to access this endpoint.
    """

    def __init__(self) -> None:
        self._resource = ANYWHERE_FREIGHT_PRICING_TOP_PORTS_DESTINATION

    def search(
        self,
        origin_id: str,
        vessel_class: AfpVesselClass,
        product: AfpProduct,
        unit: AfpUnit = "usd_per_tonne",
        avoid_zone: Optional[List[AfpAvoidZone]] = None,
    ) -> AnywhereFreightPricingResult:
        """
        List top destination ports from a given origin.

        A top destination port refers to the port with the greatest volume of
        incoming voyages from vessels in a specified class.

        # Arguments

            origin_id: Geographical ID of the origin port.

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
        _Get top destination ports for clean products from Houston using MR2 vessels._

        ```python
        >>> from vortexasdk import AnywhereFreightPricingTopPortsDestination
        >>> result = AnywhereFreightPricingTopPortsDestination().search(
        ...     origin_id="7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
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
        |  0 | Callao [PE]    | 2024-01-01 | 63.55 | 2351511.83  |          2 |

        """
        logger.info(
            f"Fetching Anywhere Freight Pricing top destination ports for origin {origin_id}"
        )

        payload: Dict[str, Any] = {
            "origin_id": origin_id,
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
