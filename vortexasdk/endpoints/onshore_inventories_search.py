"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Favailability_search.ipynb)
"""
from datetime import datetime
from typing import Any, Dict, List, Union
from vortexasdk.endpoints.onshore_inventories_result import (
    OnshoreInventoriesResult,
)

from vortexasdk.api.shared_types import to_ISODate
from vortexasdk.api import ID
from vortexasdk.endpoints.endpoints import CRUDE_ONSHORE_INVENTORIES_SEARCH
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list

logger = get_logger(__name__)


class OnshoreInventoriesSearch(Search):
    """
    Crude Onshore Inventories Endpoint, use this to search through Vortexa's Onshore Inventory data.
    Please note: you will require a subscription to our Crude Onshore Inventories module to access this endpoint.
    """

    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, CRUDE_ONSHORE_INVENTORIES_SEARCH)

    def search(
        self,
        asset_tank_ids: Union[ID, List[ID]] = None,
        corporate_entity_ids: Union[ID, List[ID]] = None,
        crude_confidence: List[str] = None,
        location_ids: Union[ID, List[ID]] = None,
        measurement_ids: Union[ID, List[ID]] = None,
        order: str = None,
        order_direction: str = None,
        size: int = None,
        storage_types: List[str] = None,
        time_min: datetime = None,
        time_max: datetime = None,
    ) -> OnshoreInventoriesResult:
        """
        List of crude onshore inventories across the globe.

        # Arguments

            asset_tank_ids: An array of tank IDs to filter on.
            corporate_entity_ids: An array of owner ID(s) to filter on.
            crude_confidence: An array of confidence metrics to filter on. Possible values are: `'confirmed'`, `'probable'`, `'unlikely'`
            location_ids: An array of geography ID(s) to filter on.
            measurement_ids: An array of unique measurements (each COI measurement) to filter on.
            order: Used to sort the returned results. Can be one of:`'measurement_id'`, `'tank_id'`.
            order_direction: Determines the direction of sorting. ‘asc’ for ascending, ‘desc’ for descending.
            size: Used to page results. The size of the result set. Between 0 and 500.
            storage_types: An array of storage types to filter on. Possible values are: `'refinery'`, `'commercial'`, `'spr'`.
            time_min: The UTC start date of the time filter.
            time_max: The UTC end date of the time filter.


        # Returns
        `OnshoreInventoriesResult`


        # Data frame example
        Top 5 Crude Onshore Inventories where 'crude_confidence' status is 'confirmed'.

        ```python
        >>> from vortexasdk import OnshoreInventoriesSearch
        >>> df = OnshoreInventoriesSearch().search(crude_confidence=['confirmed']).to_df().head(5)

        ```

        |    | measurement_id            | tank_id                   | tank_details.capacity_bbl | ... | fill_bbl | fill_tons    | fill_cbm     |
        |---:|:--------------------------|:--------------------------|--------------------------:|-----|----------|--------------|--------------|
        |  0 | 1e41bdfc8fa21a1f3d874d41a | af83f5475ebd45b9167254667 |  225055                   | ... | 194898   | 26648.208642 | 30986.443224 |
        |  1 | 211d96e43ff6893d555f8e7e0 | f7c583b26ff8d4e50d4ba9da5 |  658327                   | ... | 131804   | 18021.429116 | 20955.254352 |
        |  2 | 5ef5595cadf0161f6b59a0769 | 7047360864070b7a08802ae82 |  209196                   | ... | 468790   | 64097.187910 | 74531.984520 |
        |  3 | b70f105d6309fb1acdb4b18c5 | 2ae82a3b79f32105716725460 |  664169                   | ... | 105934   | 14484.249886 | 16842.234792 |
        |  4 | 72841f54183a082de91d9er43 | 802ae82a3b79f321167254667 |  75669                    | ... | 474814   | 64920.843406 | 75489.728232 |


        # List example
        First COI object in the list where 'crude_confidence' status is 'confirmed'.

        ```python
        >>> from vortexasdk import OnshoreInventoriesSearch
        >>> list = OnshoreInventoriesSearch().search(crude_confidence='confirmed').to_list()[0]

        ```

        ```
        {
            measurement_id: '5731385e7b0ce8',
            tank_id: 'c5a6bf5e95e969cf7',
            tank_details: {
                id: 'c5a6bf5e95e969cf7',
                capacity_bbl: 875573,
                capacity_cbm: 139205,
                capacity_ton: 119716,
                corporate_entity_details: {
                    id: 'b25523ae823b9e38bb11a161eb60d42194f1a886e58dfe39592dcc324f06f60e',
                    label: 'Repsol'
                },
                corporate_entity_id: 'b25523ae823b9e38bb11a161eb60d42194f1a886e58dfe39592dcc324f06f60e',
                crude_confidence: 'confirmed',
                last_updated: '2021-08-03T14: 34: 18.533Z',
                leaf: True,
                location_id: 'a98c21d06633d86c8c55',
                location_details: [
                    {
                        id: 'a98c21d06633d86c8c55',
                        label: 'CartagenaLNGTerminal(Enagas)',
                        layer: 'terminal'
                    },
                    {
                        id: 'c7baa1cfb2a11e7c2eca',
                        label: 'Cartagena[
                            ES
                        ]',
                        layer: 'port'
                    }
                ],
                name: 'CGA030',
                pos: (-0.926539,
                37.574),
                radius: 45,
                ref_type: 'asset_tank',
                storage_terminal_id: 'e757382d4aa5a8aa77d0f11ac7f535fb32993bae89bdf581771f155d1c0149b8',
                storage_terminal_name: 'RepsolCartagenaRefinery',
                storage_type: 'refinery'
            },
            measurement_timestamp: '2021-09-06T17: 50: 12',
            publish_timestamp: '2021-09-08T13: 59: 45',
            fill_bbl: 732345,
            fill_tons: 100132.79950499999,
            fill_cbm: 116434.06685999999,
            reference_data_version: '20210906-1631611377217',
            latest_in_day: [1720828800000],
            latest_in_doe_week: [1720782000000],
            latest_in_month: [1719792000000],
            latest_in_quarter: [1719792000000],
            latest_in_week: [1720396800000],
            latest_in_year: [1704067200000]
        }
        ```

        """

        api_params: Dict[str, Any] = {
            "asset_tank_ids": convert_to_list(asset_tank_ids),
            "corporate_entity_ids": convert_to_list(corporate_entity_ids),
            "crude_confidence": convert_to_list(crude_confidence),
            "location_ids": convert_to_list(location_ids),
            "measurement_ids": convert_to_list(measurement_ids),
            "order": order,
            "order_direction": order_direction,
            "size": size if size is not None else self._MAX_PAGE_RESULT_SIZE,
            "storage_types": convert_to_list(storage_types),
            "time_min": to_ISODate(time_min) if time_min is not None else None,
            "time_max": to_ISODate(time_max) if time_max is not None else None,
        }

        response = super().search_with_client(**api_params)

        return OnshoreInventoriesResult(
            records=response["data"], reference=response["reference"]
        )
