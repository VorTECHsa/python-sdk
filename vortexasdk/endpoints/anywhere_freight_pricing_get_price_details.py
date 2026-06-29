"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAABZCAMAAABi1XidAAAB8lBMVEX///9XmsrmZYH1olJXmsr1olJXmsrmZYH1olJXmsr1olJXmsrmZYH1olL1olJXmsr1olJXmsrmZYH1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olJXmsrmZYH1olL1olL0nFf1olJXmsrmZYH1olJXmsq8dZb1olJXmsrmZYH1olJXmspXmspXmsr1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olLeaIVXmsrmZYH1olL1olL1olJXmsrmZYH1olLna31Xmsr1olJXmsr1olJXmsrmZYH1olLqoVr1olJXmsr1olJXmsrmZYH1olL1olKkfaPobXvviGabgadXmsqThKuofKHmZ4Dobnr1olJXmsr1olJXmspXmsr1olJXmsrfZ4TuhWn1olL1olJXmsqBi7X1olJXmspZmslbmMhbmsdemsVfl8ZgmsNim8Jpk8F0m7R4m7F5nLB6jbh7jbiDirOEibOGnKaMhq+PnaCVg6qWg6qegKaff6WhnpKofKGtnomxeZy3noG6dZi+n3vCcpPDcpPGn3bLb4/Mb47UbIrVa4rYoGjdaIbeaIXhoWHmZYHobXvpcHjqdHXreHLroVrsfG/uhGnuh2bwj2Hxk17yl1vzmljzm1j0nlX1olL3AJXWAAAAbXRSTlMAEBAQHx8gICAuLjAwMDw9PUBAQEpQUFBXV1hgYGBkcHBwcXl8gICAgoiIkJCQlJicnJ2goKCmqK+wsLC4usDAwMjP0teleN20NbsvaOsY2+3LL9/Tz1bC0dLQ1dXZ2Nrf4+Lk5urq7/P3+fn4+Pz9/f7+/gB+Q1KaQJdScAAAAAElFTkSuQmCC)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fanywhere_freight_pricing_get_price_details.ipynb)
"""
from datetime import datetime
from typing import Any, Dict, List, Optional

from vortexasdk.client import default_client, _handle_response
from vortexasdk.endpoints.endpoints import (
    ANYWHERE_FREIGHT_PRICING_PRICE_DETAILS,
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
from vortexasdk.retry_session import retry_get
from vortexasdk.api.shared_types import to_date_string

logger = get_logger(__name__)


class AnywhereFreightPricingGetPriceDetails:
    """
    Anywhere Freight Pricing Get Price Details endpoint.

    Given a set of details about a single route (origin, destination, etc),
    this will find rates, lumpsums and prediction confidences of the route.
    Rates represent the per-unit price (voyage + port + canal costs).
    Lumpsums are the total voyage cost in USD.
    The confidence returns the confidence of these estimations.

    Please note, a subscription to our Anywhere Freight Pricing module is
    required to access Anywhere Freight Pricing.
    """

    def __init__(self) -> None:
        self._resource = ANYWHERE_FREIGHT_PRICING_PRICE_DETAILS

    def search(
        self,
        time_min: datetime,
        time_max: datetime,
        origin: str,
        destination: str,
        vessel_class: AfpVesselClass,
        product: AfpProduct,
        unit: AfpUnit = "usd_per_tonne",
        avoid_zone: Optional[List[AfpAvoidZone]] = None,
        suggested_tonnage: Optional[float] = None,
    ) -> AnywhereFreightPricingResult:
        """
        List prices of a route.

        Given a set of details about a single route (origin, destination, etc),
        this will find rates, lumpsums and prediction confidences of the route.
        Rates represent the per-unit price (voyage + port + canal costs).
        Lumpsums are the total voyage cost in USD.
        The confidence returns the confidence of these estimations.

        # Arguments

            time_min: The UTC start date of the time filter.

            time_max: The UTC end date of the time filter.

            origin: Geographic ID of the origin port.

            destination: Geographic ID of the destination port.

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
        ...     origin="7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
        ...     destination="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
        ...     vessel_class="oil_aframax_lr2",
        ...     product="crude",
        ...     unit="usd_per_tonne",
        ... )
        >>> df = result.to_df()

        ```

        Returns a DataFrame with columns including rates, lumpsums, and confidence values:

        |    | date       | rate  | lumpsum   | confidence |
        |---:|:-----------|------:|----------:|-----------:|
        |  0 | 2024-01-01 | 12.50 | 1250000.0 |          2 |
        |  1 | 2024-01-02 | 12.75 | 1275000.0 |          2 |

        """
        logger.info(
            f"Fetching Anywhere Freight Pricing price details for route "
            f"{origin} -> {destination}"
        )

        params: Dict[str, Any] = {
            "time_min": to_date_string(time_min),
            "time_max": to_date_string(time_max),
            "origin": origin,
            "destination": destination,
            "vessel_class": vessel_class,
            "product": product,
            "unit": unit,
        }

        if avoid_zone is not None:
            params["avoid_zone"] = avoid_zone

        if suggested_tonnage is not None:
            params["suggested_tonnage"] = suggested_tonnage

        client = default_client()
        url = client._create_url_with_params(
            self._resource, params, doseq=True
        )

        response = retry_get(url)

        data = _handle_response(response)
        return AnywhereFreightPricingResult(
            records=data.get("data", []),
            reference=data.get("metadata", {}),
        )
