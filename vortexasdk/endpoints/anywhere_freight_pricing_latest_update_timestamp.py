from typing import Dict

from vortexasdk.client import default_client, _handle_response
from vortexasdk.endpoints.endpoints import (
    ANYWHERE_FREIGHT_PRICING_LATEST_UPDATE,
)
from vortexasdk.logger import get_logger
from vortexasdk.retry_session import retry_get

logger = get_logger(__name__)


class AnywhereFreightPricingLatestUpdateTimestamp:
    """
    Anywhere Freight Pricing Latest Update Timestamp endpoint.

    Please note: you will require a subscription to our Anywhere Freight Pricing
    module to access this endpoint.
    """

    def __init__(self) -> None:
        self._resource = ANYWHERE_FREIGHT_PRICING_LATEST_UPDATE

    def search(self) -> Dict[str, str]:
        """
        Get the time the predicted route prices were last updated.

        # Returns
        A dictionary containing a `timestamp` key with the ISO 8601 formatted
        date-time string of when the pricing predictions were last updated.

        # Example
        _Get the latest update timestamp for Anywhere Freight Pricing._

        ```python
        >>> from vortexasdk import AnywhereFreightPricingLatestUpdateTimestamp
        >>> result = AnywhereFreightPricingLatestUpdateTimestamp().search()

        ```

        Returns:

        ```
        {
            'timestamp': '2025-01-30T14:40:06.803Z'
        }
        ```

        """
        logger.info(
            "Fetching Anywhere Freight Pricing latest update timestamp"
        )

        client = default_client()
        url = client._create_url(self._resource)
        response = retry_get(url)

        return _handle_response(response)
