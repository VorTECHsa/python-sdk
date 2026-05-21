from vortexasdk.client import default_client, _handle_response
from vortexasdk.endpoints.endpoints import ANYWHERE_FREIGHT_PRICING_VESSEL_CLASSES_DETAILS
from vortexasdk.endpoints.anywhere_freight_pricing_result import (
    AnywhereFreightPricingResult,
)
from vortexasdk.logger import get_logger
from vortexasdk.retry_session import retry_get

logger = get_logger(__name__)


class AnywhereFreightPricingVesselClassesDetails:
    """
    Anywhere Freight Pricing Vessel Classes Details endpoint.

    Lists all the vessel classes supported for Anywhere Freight Pricing
    and the tonnages they can carry.

    Please note: you will require a subscription to our Anywhere Freight Pricing
    module to access this endpoint.
    """

    def __init__(self) -> None:
        self._resource = ANYWHERE_FREIGHT_PRICING_VESSEL_CLASSES_DETAILS

    def search(self) -> AnywhereFreightPricingResult:
        """
        List vessel classes with tonnages.

        Lists all the vessel classes supported for Anywhere Freight Pricing
        and the tonnages they can carry.

        # Returns
        `AnywhereFreightPricingResult`

        # Example
        _Get all supported vessel classes and their tonnage ranges._

        ```python
        >>> from vortexasdk import AnywhereFreightPricingVesselClassesDetails
        >>> result = AnywhereFreightPricingVesselClassesDetails().search()
        >>> df = result.to_df()

        ```

        Returns a DataFrame with vessel class details:

        |    | name              | suggested_tonnage | min_tonnage | max_tonnage |
        |---:|:------------------|------------------:|------------:|------------:|
        |  0 | oil_handymax_mr2  |           37000.0 |     18000.0 |     54000.0 |
        |  1 | oil_panamax_lr1   |           60000.0 |     30000.0 |     79000.0 |
        |  2 | oil_aframax_lr2   |           85000.0 |     42000.0 |    119000.0 |

        """
        logger.info("Fetching Anywhere Freight Pricing vessel classes details")

        client = default_client()
        url = client._create_url(self._resource)

        response = retry_get(url)

        data = _handle_response(response)
        return AnywhereFreightPricingResult(
            records=data.get("data", []),
            reference=data.get("metadata", {}),
        )
