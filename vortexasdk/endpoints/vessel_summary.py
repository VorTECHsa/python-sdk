"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fvessel_summary.ipynb)
"""
from typing import Any, Dict, List, Union

from vortexasdk.api.shared_types import ISODate
from vortexasdk.endpoints.endpoints import VESSEL_SUMMARY
from vortexasdk.endpoints.vessel_summary_result import VesselSummaryResult
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list


class VesselSummary(Search):
    """Vessels endpoint."""

    def __init__(self):
        """Instantiate endpoint"""
        Search.__init__(self, VESSEL_SUMMARY)

    def search(
        self,
        vessel_id: Union[str, List[str]] = None,
        vessel_class: Union[str, List[str]] = None,
        timestamp: ISODate = None,
    ) -> VesselSummaryResult:
        """
        Find all latest summary of vessels matching given search arguments. Search arguments are combined in an AND manner.

        # Arguments
            timestamp: The earliest timestamp before which you'd like your summaries sourced from

            vessel_id: ID or IDs of vessels we'd like to search

            vessel_class: vessel_class (or list of vessel classes) we'd like to search. This will give you summaries for all vessels within this class. Each vessel class must be one of `"oil_coastal", "oil_intermediate", "oil_flexi", "oil_handysize", "oil_mr1","oil_handymax", "oil_mr2", "oil_panamax", "oil_lr1", "oil_aframax", "oil_lr2", "oil_suezmax","oil_lr3", "oil_vlcc","lpg_coasters", "lpg_handysize", "lpg_mgc", "lpg_lgc", "lpg_vlgc", "lpg_vlec", "lng_small_scale_lng", "lng_mid_scale_lng", "lng_two_stroke", "lng_tfde_dfde", "lng_steam", "lng_ssd", "lng_q_flex", "lng_q_max", "oil_coastal", "oil_specialised", "oil_handysize_mr1", "oil_handymax_mr2", "oil_panamax_lr1", "oil_aframax_lr2", "oil_suezmax_lr3", "oil_vlcc","lpg_sgc", "lpg_mgc", "lpg_lgc", "lpg_vlgc_vlec","lng_small_scale_lng", "lng_mid_scale_lng","lng_conventional_lng", "lng_q_fleet", "oil", "lpg", "lng",`. Refer to [VortexaAPI Vessel Entities](https://docs.vortexa.com/reference/intro-vessel-entities) for the most up-to-date list of vessel classes.

        # Returns
        List of vessel summaries matching the search arguments.

        # Examples

        - Let's find all summaries for all Aframax and VLCC_PLUS vessels, from the week prior to October 31st, 2023.

        ```python
        >>> from vortexasdk import VesselSummary
        >>> vessel_summary_df = VesselSummary().search(vessel_class=['oil_aframax', 'oil_vlcc'], timestamp='2023-10-31T23:59:59.000Z').to_df(columns=['vessel_id', 'timestamp', 'lat', 'lon', 'speed', 'heading', 'declared_destination', 'draught'])

        ```
        |    | vessel_id        |     lat  |      lon   | timestamp                | speed  | heading | declared_destination | draught |
        |---:|:----------------:|---------:|-----------:|:-------------------------|-------:|--------:|---------------------:|--------:|
        |  0 | bc49bed3d600b394 | 17.36560 | -161.39080 | 2023-10-31T23:57:11.000Z | 19.299 | 308     | >JP KZU XX           | 11      |
        |  ...to >800 results

        Note that we will show you all fields by default if you don't set the columns argument.
        ```

        - Now let's find summaries for vessels carrying crude, using the Vessels and Product Reference endpoints

        ```python
        >>> from vortexasdk import Vessels, Products
        >>> crude = [p.id for p in Products().search(term="crude").to_list() if 'group' in p.layer]
        >>> vessels_list = Vessels().search(vessel_product_types=crude).to_list()
        >>> vessel_ids = [v.id for v in vessels_list]
        >>> crude_summaries = VesselSummary().search(vessel_id=vessel_ids).to_df()

        ```

        # Further Documentation

        [VortexaAPI Vessel Summary Reference](https://docs.vortexa.com/reference/POST/signals/vessel-summary)

        """
        api_params: Dict[str, Any] = {
            "vessel_id": convert_to_list(vessel_id),
            "vessel_class": [v.lower() for v in convert_to_list(vessel_class)],
            "timestamp": timestamp,
            "size": 10000,
            # High size param is workaround for pagination, since summary does not support it.
            # If we don't set this, py sdk defaults size to 1000, and so will re-run the call total / 1000 times...
        }

        response = super().search_with_client(**api_params)

        return VesselSummaryResult(records=response["data"])
