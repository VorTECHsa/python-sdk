"""
Anywhere Freight Pricing Forecast Explanation endpoint.

Explains forecast price movements for a route.

Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAABZCAMAAABi1XidAAAB8lBMVEX///9XmsrmZYH1olJXmsr1olJXmsrmZYH1olJXmsr1olJXmsrmZYH1olL1olJXmsr1olJXmsrmZYH1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olJXmsrmZYH1olL1olL0nFf1olJXmsrmZYH1olJXmsq8dZb1olJXmsrmZYH1olJXmspXmspXmsr1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olLeaIVXmsrmZYH1olL1olL1olJXmsrmZYH1olLna31Xmsr1olJXmsr1olJXmsrmZYH1olLqoVr1olJXmsr1olJXmsrmZYH1olL1olKkfaPobXvviGabgadXmsqThKuofKHmZ4Dobnr1olJXmsr1olJXmspXmsr1olJXmsrfZ4TuhWn1olL1olJXmsqBi7X1olJXmspZmslbmMhbmsdemsVfl8ZgmsNim8Jpk8F0m7R4m7F5nLB6jbh7jbiDirOEibOGnKaMhq+PnaCVg6qWg6qegKaff6WhnpKofKGtnomxeZy3noG6dZi+n3vCcpPDcpPGn3bLb4/Mb47UbIrVa4rYoGjdaIbeaIXhoWHmZYHobXvpcHjqdHXreHLroVrsfG/uhGnuh2bwj2Hxk17yl1vzmljzm1j0nlX1olL3AJXWAAAAbXRSTlMAEBAQHx8gICAuLjAwMDw9PUBAQEpQUFBXV1hgYGBkcHBwcXl8gICAgoiIkJCQlJicnJ2goKCmqK+wsLC4usDAwMjP0teleN20NbsvaOsY2+3LL9/Tz1bC0dLQ1dXZ2Nrf4+Lk5urq7/P3+fn4+Pz9/f7+/gB+Q1KaQJdScAAAAAElFTkSuQmCC)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fanywhere_freight_pricing_forecast_explanation.ipynb)
"""
from typing import Any, Dict, List, Optional

from vortexasdk.client import default_client, _handle_response
from vortexasdk.endpoints.endpoints import (
    ANYWHERE_FREIGHT_PRICING_FORECAST_EXPLANATION,
)
from vortexasdk.endpoints.anywhere_freight_pricing_result import (
    AnywhereFreightPricingResult,
)
from vortexasdk.endpoints.anywhere_freight_pricing_types import (
    AfpAvoidZone,
    AfpExplanationFrequency,
    AfpForecastVesselClass,
    AfpProduct,
)
from vortexasdk.logger import get_logger
from vortexasdk.retry_session import retry_get

logger = get_logger(__name__)


class AnywhereFreightPricingForecastExplanation:
    """
    Anywhere Freight Pricing Forecast Explanation endpoint.

    Explains forecast price movements for a route by providing a base date
    and a list of explanations for upcoming time periods.

    Please note: you will require a subscription to our Anywhere Freight Pricing
    module to access this endpoint.
    """

    def __init__(self) -> None:
        self._resource = ANYWHERE_FREIGHT_PRICING_FORECAST_EXPLANATION

    def search(
        self,
        origin_port: str,
        destination_port: str,
        vessel_class: AfpForecastVesselClass,
        product: AfpProduct,
        frequency: AfpExplanationFrequency = "month_fixed",
        avoid_zone: Optional[List[AfpAvoidZone]] = None,
        include_port_costs: Optional[bool] = None,
    ) -> AnywhereFreightPricingResult:
        """
        Get forecast price movement explanations for a route.

        Given a route (origin, destination, vessel class, product), this returns
        a base date and a list of forecast explanations for upcoming time periods.

        # Arguments

            origin_port: Geographic ID of the origin port.

            destination_port: Geographic ID of the destination port.

            vessel_class: The vessel class for the route. Must be one of:
                `'oil_coastal'`, `'oil_specialised'`, `'oil_handysize_mr1'`,
                `'oil_handymax_mr2'`, `'oil_panamax_lr1'`, `'oil_aframax_lr2'`,
                `'oil_suezmax_lr3'`, `'oil_vlcc'`, `'lpg_sgc'`, `'lpg_mgc'`,
                `'lpg_lgc'`, `'lpg_vlgc_vlec'`, `'lng_small_scale_lng'`,
                `'lng_mid_scale_lng'`, `'lng_conventional_lng'`, `'lng_q_fleet'`.

            product: The product type. Must be one of: `'clean'`, `'dirty'`, `'crude'`.

            frequency: Frequency for the explanation periods. Must be one of:
                `'day'`, `'week'`, `'month'`, `'month_fixed'`. Defaults to `'month_fixed'`

            avoid_zone: Routing zones to avoid for this route. Options:
                `'Panama Canal'`, `'Suez Canal'`.

            include_port_costs: Whether to include port costs in the calculation.

        # Returns
        `AnywhereFreightPricingResult`

        # Example
        _Get monthly forecast explanation for a Handymax MR2 clean route
        from Rotterdam to Houston._

        ```python
        >>> from vortexasdk import AnywhereFreightPricingForecastExplanation
        >>> result = AnywhereFreightPricingForecastExplanation().search(
        ...     origin_port="68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e",
        ...     destination_port="ea4921c8ad4fddb5fe3e7a4f834c1aa5863e43283c73da5f02d93bbc5dba72eb",
        ...     vessel_class="oil_handymax_mr2",
        ...     product="clean",
        ...     frequency="month",
        ... )
        >>> df = result.to_df()

        ```

        Returns a DataFrame with columns:

        |    | base_date   | explanation                                              |
        |---:|:------------|:---------------------------------------------------------|
        |  0 | 2026-05-26  | [{'start_date': '2026-06-01', 'end_date': '2026-06-30'...}] |

        Each explanation entry contains:
        - `start_date`: Start of the forecast period
        - `end_date`: End of the forecast period
        - `explanation`: Text explanation of expected price movements

        """
        logger.info(
            f"Fetching Anywhere Freight Pricing forecast explanation for route "
            f"{origin_port} -> {destination_port}"
        )

        params: Dict[str, Any] = {
            "origin_port": origin_port,
            "destination_port": destination_port,
            "vessel_class": vessel_class,
            "product": product,
            "frequency": frequency,
        }

        if avoid_zone is not None:
            params["avoid_zone"] = avoid_zone

        if include_port_costs is not None:
            params["include_port_costs"] = str(include_port_costs).lower()

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
