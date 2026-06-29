"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAABZCAMAAABi1XidAAAB8lBMVEX///9XmsrmZYH1olJXmsr1olJXmsrmZYH1olJXmsr1olJXmsrmZYH1olL1olJXmsr1olJXmsrmZYH1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olJXmsrmZYH1olL1olL0nFf1olJXmsrmZYH1olJXmsq8dZb1olJXmsrmZYH1olJXmspXmspXmsr1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olLeaIVXmsrmZYH1olL1olL1olJXmsrmZYH1olLna31Xmsr1olJXmsr1olJXmsrmZYH1olLqoVr1olJXmsr1olJXmsrmZYH1olL1olKkfaPobXvviGabgadXmsqThKuofKHmZ4Dobnr1olJXmsr1olJXmspXmsr1olJXmsrfZ4TuhWn1olL1olJXmsqBi7X1olJXmspZmslbmMhbmsdemsVfl8ZgmsNim8Jpk8F0m7R4m7F5nLB6jbh7jbiDirOEibOGnKaMhq+PnaCVg6qWg6qegKaff6WhnpKofKGtnomxeZy3noG6dZi+n3vCcpPDcpPGn3bLb4/Mb47UbIrVa4rYoGjdaIbeaIXhoWHmZYHobXvpcHjqdHXreHLroVrsfG/uhGnuh2bwj2Hxk17yl1vzmljzm1j0nlX1olL3AJXWAAAAbXRSTlMAEBAQHx8gICAuLjAwMDw9PUBAQEpQUFBXV1hgYGBkcHBwcXl8gICAgoiIkJCQlJicnJ2goKCmqK+wsLC4usDAwMjP0teleN20NbsvaOsY2+3LL9/Tz1bC0dLQ1dXZ2Nrf4+Lk5urq7/P3+fn4+Pz9/f7+/gB+Q1KaQJdScAAAAAElFTkSuQmCC)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fanywhere_freight_pricing_post_price_details.ipynb)
"""
from datetime import datetime
from typing import Any, Dict, List

from vortexasdk.endpoints.endpoints import (
    ANYWHERE_FREIGHT_PRICING_PRICE_DETAILS,
)
from vortexasdk.endpoints.anywhere_freight_pricing_result import (
    AnywhereFreightPricingResult,
)
from vortexasdk.endpoints.anywhere_freight_pricing_types import (
    AfpRoute,
    AfpUnit,
)
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search
from vortexasdk.api.shared_types import to_date_string

logger = get_logger(__name__)


class AnywhereFreightPricingPostPriceDetails(Search):
    """
    Anywhere Freight Pricing Post Price Details endpoint.

    Given a set of details about multiple routes (origin, destination, etc),
    this will find rates, lumpsums and prediction confidences of each of the routes.
    Rates represent the per-unit price (voyage + port + canal costs).
    Lumpsums are the total voyage cost in USD.
    The confidence returns the confidence of these value estimations.

    Please note, a subscription to our Anywhere Freight Pricing module is
    required to access Anywhere Freight Pricing.
    """

    def __init__(self) -> None:
        Search.__init__(self, ANYWHERE_FREIGHT_PRICING_PRICE_DETAILS)

    def search(
        self,
        routes: List[AfpRoute],
        time_min: datetime,
        time_max: datetime,
        unit: AfpUnit = "usd_per_tonne",
    ) -> AnywhereFreightPricingResult:
        """
        List historical prices for multiple routes.

        Given a set of details about multiple routes (origin, destination, etc),
        this will find historical rates, lumpsums and prediction confidences of each of the routes.
        Rates represent the per-unit price (voyage + port + canal costs).
        Lumpsums are the total voyage cost in USD.
        The confidence returns the confidence of these value estimations.

        # Arguments

            routes: A list of route dictionaries. Each route must contain:
                - `origin` (str, required): Geographical ID of the origin port.
                - `destination` (str, required): Geographical ID of the destination port.
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
                Defaults to `'usd_per_tonne'`.

        # Returns
        `AnywhereFreightPricingResult`

        # Example
        _Get price details for multiple routes._

        ```python
        >>> from vortexasdk import AnywhereFreightPricingPostPriceDetails
        >>> from datetime import datetime
        >>> routes = [
        ...     {
        ...         "origin": "7f314ba0a498c36359b1c88781e94a73e19dcc9bbb030ec6b82f944a73d4da2f",
        ...         "destination": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
        ...         "product": "crude",
        ...         "vessel_class": "oil_aframax_lr2",
        ...     },
        ...     {
        ...         "origin": "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
        ...         "destination": "ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
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
        |  0 | 2024-01-01 | 12.50 | 1250000.0 |          2 |
        |  1 | 2024-01-02 | 12.75 | 1275000.0 |          2 |

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
