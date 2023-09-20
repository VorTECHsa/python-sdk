"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fasset_tanks.ipynb)
"""
from typing import List, Union
from vortexasdk.endpoints.endpoints import ASSET_TANKS_REFERENCE
from vortexasdk.endpoints.asset_tanks_result import AssetTankResult
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_to_list


class AssetTanks(Reference, Search):
    """
    Asset Tanks endpoint.

    An Asset Tank is a reference value that corresponds to an ID associated with other entities.

    For example, an Asset Tank object may have the following keys:

    ```json
    {
        "name": "AAM001",
        "storage_type": "tdb"
        "crude_confidence": "confirmed"
        ...
    }
    ```

    IDs represent asset tanks which can be found via the Asset Tank reference endpoint.

    When the asset tanks endpoint is searched with those ids as parameters:

    ```python
        >>> from vortexasdk import AssetTanks
        >>> df = AssetTanks().search(ids=["6114b93026e61993797db33a46a5d2acbeacdbd63238a4271efaeafcee94b1d2"]).to_df()

    ```

    Returns

    |    | id                      | capacity_bbl | crude_confidence | location_id                     | name   | storage_type | lat | lon |
    |---:|:------------------------|:-------------|:-----------------|:--------------------------------|:-------|:-------------|-----|-----|
    |  0 | 6114b93026e61993797d... | 645201       | confirmed         | b839dc5fee39ff7efd5e1cf2494... | AAM001 | tbd          |  90 | 180 |


    """

    def __init__(self):
        Reference.__init__(self, ASSET_TANKS_REFERENCE)
        Search.__init__(self, ASSET_TANKS_REFERENCE)

    def load_all(self) -> AssetTankResult:
        """
        Load all asset tanks.
        """
        return self.search()

    # noinspection PyShadowingBuiltins
    def search(
        self,
        ids: Union[str, List[str]] = None,
        corporate_entity_ids: Union[str, List[str]] = None,
        crude_confidence: List[str] = None,
        location_ids: Union[str, List[str]] = None,
        storage_type: List[str] = None,
        term: Union[str, List[str]] = None,
    ) -> AssetTankResult:
        """
        Find all asset tanks matching given type.

        # Arguments

            ids: An array of unique Asset Tanks ID(s) to filter on.
            corporate_entity_ids: An array of owner ID(s) to filter on.
            crude_confidence: An array of confidence metrics to filter on. Possible values are: `'confirmed’`, `‘probable’`, `‘unlikely’`
            location_ids: An array of geography ID(s) to filter on.
            storage_types: An array of storage types to filter on. Possible values are: `'refinery'`, `'commercial'`, `'spr'`


        # Returns
        List of asset tanks matching `type`


        # Examples

        Find all asset tanks with a storage_type of `refinery`.
        ```python
        >>> from vortexasdk import AssetTanks
        >>> df = AssetTanks().search(storage_type=["refinery"]).to_df()

        ```
        Returns

        |    | id                      | capacity_bbl | crude_confidence | location_id                     | name   | storage_type | lat | lon |
        |---:|:------------------------|:-------------|:-----------------|:--------------------------------|:-------|:-------------|-----|-----|
        |  0 | 0a736a1816c0fea49a88... | 104815       | probable         | f726416f49adcac6d5d296c49a00... | HOM009 | refinery     | -60 |  24 |
        |  1 | b96adfb025a719b66927... | 139279       | unlikely         | f726416f49adcac6d5d296c49a00... | HOM022 | refinery     | 100 | -90 |

        """

        search_params = {
            "ids": convert_to_list(ids),
            "corporate_entity_ids": convert_to_list(corporate_entity_ids),
            "crude_confidence": convert_to_list(crude_confidence),
            "location_ids": convert_to_list(location_ids),
            "storage_type": convert_to_list(storage_type),
            "term": [str(e) for e in convert_to_list(term)],
        }

        response = super().search_with_client(
            exact_term_match=False,
            response_type=None,
            headers=None,
            **search_params
        )

        return AssetTankResult(
            records=response["data"], reference=response["reference"]
        )
