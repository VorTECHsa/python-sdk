"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAABZCAMAAABi1XidAAAB8lBMVEX///9XmsrmZYH1olJXmsr1olJXmsrmZYH1olJXmsr1olJXmsrmZYH1olL1olJXmsr1olJXmsrmZYH1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olJXmsrmZYH1olL1olL0nFf1olJXmsrmZYH1olJXmsq8dZb1olJXmsrmZYH1olJXmspXmspXmsr1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olLeaIVXmsrmZYH1olL1olL1olJXmsrmZYH1olLna31Xmsr1olJXmsr1olJXmsrmZYH1olLqoVr1olJXmsr1olJXmsrmZYH1olL1olKkfaPobXvviGabgadXmsqThKuofKHmZ4Dobnr1olJXmsr1olJXmspXmsr1olJXmsrfZ4TuhWn1olL1olJXmsqBi7X1olJXmspZmslbmMhbmsdemsVfl8ZgmsNim8Jpk8F0m7R4m7F5nLB6jbh7jbiDirOEibOGnKaMhq+PnaCVg6qWg6qegKaff6WhnpKofKGtnomxeZy3noG6dZi+n3vCcpPDcpPGn3bLb4/Mb47UbIrVa4rYoGjdaIbeaIXhoWHmZYHobXvpcHjqdHXreHLroVrsfG/uhGnuh2bwj2Hxk17yl1vzmljzm1j0nlX1olL3AJXWAAAAbXRSTlMAEBAQHx8gICAuLjAwMDw9PUBAQEpQUFBXV1hgYGBkcHBwcXl8gICAgoiIkJCQlJicnJ2goKCmqK+wsLC4usDAwMjP0teleN20NbsvaOsY2+3LL9/Tz1bC0dLQ1dXZ2Nrf4+Lk5urq7/P3+fn4+Pz9/f7+/gB+Q1KaQJdScAAAAAElFTkSuQmCC)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fanywhere_freight_pricing_latest_update_timestamp.ipynb)
"""
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

    Please note, a subscription to our Anywhere Freight Pricing module is
    required to access Anywhere Freight Pricing.
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
