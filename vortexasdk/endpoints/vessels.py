"""
Try me out in your browser:

[![Binder](https://img.shields.io/badge/try%20me%20out-launch%20notebook-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/VorTECHsa/python-sdk/master?filepath=docs%2Fexamples%2Ftry_me_out%2Fvessels.ipynb)
"""
from typing import Any, Dict, List, Union

from vortexasdk.api.id import ID
from vortexasdk.endpoints.endpoints import VESSELS_REFERENCE
from vortexasdk.endpoints.vessels_result import VesselsResult
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_to_list


class Vessels(Reference, Search):
    """Vessels endpoint."""

    def __init__(self):
        """Instantiate endpoint using reference endpoint."""
        Reference.__init__(self, VESSELS_REFERENCE)
        Search.__init__(self, VESSELS_REFERENCE)

    def load_all(self) -> VesselsResult:
        """Load all vessels."""
        return self.search()

    def search(
        self,
        term: Union[str, List[str]] = None,
        ids: Union[str, List[str]] = None,
        vessel_classes: Union[str, List[str]] = None,
        vessel_product_types: Union[ID, List[ID]] = None,
        vessel_scrubbers: str = "disabled",
        exact_term_match: bool = False,
    ) -> VesselsResult:
        """
        Find all vessels matching given search arguments. Search arguments are combined in an AND manner.

        # Arguments
            term: The name(s) (or partial name(s)) of a vessel we'd like to search

            ids: ID or IDs of vessels we'd like to search

            vessel_classes: vessel_class (or list of vessel classes) we'd like to search. Each vessel class must be one of `"oil_coastal", "oil_intermediate", "oil_flexi", "oil_handysize", "oil_mr1","oil_handymax", "oil_mr2", "oil_panamax", "oil_lr1", "oil_aframax", "oil_lr2", "oil_suezmax","oil_lr3", "oil_vlcc","lpg_coasters", "lpg_handysize", "lpg_mgc", "lpg_lgc", "lpg_vlgc", "lpg_vlec", "lng_small_scale_lng", "lng_mid_scale_lng", "lng_two_stroke", "lng_tfde_dfde", "lng_steam", "lng_ssd", "lng_q_flex", "lng_q_max", "oil_coastal", "oil_specialised", "oil_handysize_mr1", "oil_handymax_mr2", "oil_panamax_lr1", "oil_aframax_lr2", "oil_suezmax_lr3", "oil_vlcc","lpg_sgc", "lpg_mgc", "lpg_lgc", "lpg_vlgc_vlec","lng_small_scale_lng", "lng_mid_scale_lng","lng_conventional_lng", "lng_q_fleet", "oil", "lpg", "lng",`. Refer to [VortexaAPI Vessel Entities](https://docs.vortexa.com/reference/intro-vessel-entities) for the most up-to-date list of vessel classes.

            vessel_product_types: A product ID, or list of product IDs to filter on, searching vessels _currently_ carrying these products.

            vessel_scrubbers: An optional filter to filter on vessels with or without scrubbers.
             To disable the filter (the default behaviour), enter 'disabled'.
             To only include vessels with scrubbers, enter 'inc'.
             To exclude vessels with scrubbers, enter 'exc'.

             exact_term_match: Search on only exact term matches, or allow similar matches.
                 e.g. When searching for "Ocean" with `exact_term_match=False`, then the SDK will yield vessels named
                ['Ocean', 'Ocean Wisdom', ...] etc. When `exact_term_match=True`,
                the SDK will only yield the vessel named `Ocean`.


        # Returns
        List of vessels matching the search arguments.


        # Examples

        - Let's find all the VLCCs with 'ocean' in their name, or related names.

        ```python
        >>> from vortexasdk import Vessels
        >>> vessels_df = Vessels().search(vessel_classes='oil_vlcc', term='ocean').to_df(columns=['name', 'imo', 'mmsi', 'related_names'])

        ```
        |    | name         |     imo |      mmsi | related_names             |
        |---:|:-------------|--------:|----------:|:--------------------------|
        |  0 | OCEANIS      | 9532757 | 241089000 | ['OCEANIS']               |
        |  1 | AEGEAN       | 9732553 | 205761000 | ['GENER8 OCEANUS']        |
        |  2 | OCEANIA      | 9246633 | 205753000 | ['OCEANIA'| 'TI OCEANIA'] |
        |  3 | ENEOS OCEAN  | 9662875 | 432986000 | ['ENEOS OCEAN']           |
        |  4 | OCEAN LILY   | 9284960 | 477178100 | ['OCEAN LILY']            |
        |  5 | SHINYO OCEAN | 9197868 | 636019316 | ['SHINYO OCEAN']          |
        |  6 | NASHA        | 9079107 | 370497000 | ['OCEANIC']               |
        |  7 | HUMANITY     | 9180281 | 422204700 | ['OCEAN NYMPH']           |

        Note the `term` search also looks for vessels with matching `related_names`


        - Let's find all the vessels currently carrying Crude.

        ```python
        >>> from vortexasdk import Vessels, Products
        >>> crude = [p.id for p in Products().search(term="crude").to_list() if 'group' in p.layer]
        >>> vessels_df = Vessels().search(vessel_product_types=crude).to_df()

        ```

        # Further Documentation

        [VortexaAPI Vessel Reference](https://docs.vortexa.com/reference/POST/reference/vessels)

        """
        api_params: Dict[str, Any] = {
            "term": [str(e) for e in convert_to_list(term)],
            "ids": convert_to_list(ids),
            "vessel_product_types": convert_to_list(vessel_product_types),
            "vessel_classes": [
                v.lower() for v in convert_to_list(vessel_classes)
            ],
            "vessel_scrubbers": vessel_scrubbers,
        }

        response = super().search_with_client(
            exact_term_match=exact_term_match, **api_params
        )

        return VesselsResult(
            records=response["data"], reference=response["reference"]
        )

    def reference(self, id: ID) -> Dict:
        """
        Perform a vessel lookup.

        # Arguments
            id: Vessel ID to lookup

        # Returns
        Vessel record matching the ID

        # Further Documentation:
        [VortexaAPI Vessel Reference](https://docs.vortexa.com/reference/GET/reference/vessels/%7Bid%7D)

        """
        return super().reference(id)


AVAILABLE_VESSEL_CLASSES = [
    "oil_coastal",
    "oil_intermediate",
    "oil_flexi",
    "oil_handysize",
    "oil_mr1",
    "oil_handymax",
    "oil_mr2",
    "oil_panamax",
    "oil_lr1",
    "oil_aframax",
    "oil_lr2",
    "oil_suezmax",
    "oil_lr3",
    "oil_vlcc",
    "lpg_coasters",
    "lpg_handysize",
    "lpg_mgc",
    "lpg_lgc",
    "lpg_vlgc",
    "lpg_vlec",
    "lng_small_scale_lng",
    "lng_mid_scale_lng",
    "lng_two_stroke",
    "lng_tfde_dfde",
    "lng_steam",
    "lng_ssd",
    "lng_q_flex",
    "lng_q_max",
    "oil_coastal",
    "oil_specialised",
    "oil_handysize_mr1",
    "oil_handymax_mr2",
    "oil_panamax_lr1",
    "oil_aframax_lr2",
    "oil_suezmax_lr3",
    "oil_vlcc",
    "lpg_sgc",
    "lpg_mgc",
    "lpg_lgc",
    "lpg_vlgc_vlec",
    "lng_small_scale_lng",
    "lng_mid_scale_lng",
    "lng_conventional_lng",
    "lng_q_fleet",
    "oil",
    "lpg",
    "lng",
]
