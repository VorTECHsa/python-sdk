from typing import List

import pandas as pd

from python_sdk.constants import VESSELS_REFERENCE
from python_sdk.operations import Reference, Search


class VesselsSearchResult:
    """
    VesselsSearchResult is a wrapper around the result from calling the vessels API endpoint.

    This class lets user represent vessels as a `pd.DataFrame`, or as a list of dictionaries.
    """

    def __init__(self, result: List[dict]):
        self._result: List[dict] = result

    def to_list(self) -> List[dict]:
        """

        Represent vessels as a list of dictionaries.

        """
        return self._result

    def to_df(self, columns=None) -> pd.DataFrame:
        """

        # Arguments
            columns: The vessel features we want in the dataframe.
             Defaults to `columns = ['id', 'name', 'imo', 'vessel_class']`. Enter `columns='all'` to include all features.


        # Returns
        `pd.DataFrame` of vessels.

        """
        if columns is None:
            columns = ['id', 'name', 'imo', 'vessel_class']

        df = pd.DataFrame(self._result)

        if columns == 'all':
            return df
        else:
            return df[columns]

    def __str__(self):
        return str(self._result)


class Vessels(Reference, Search):

    def __init__(self):
        Reference.__init__(self, VESSELS_REFERENCE)
        Search.__init__(self, VESSELS_REFERENCE)

    def search(self,
               term: str = None,
               ids: List[str] = None,
               vessel_classes: List[str] = None,
               vessel_product_types: List[str] = None) -> VesselsSearchResult:
        """

        # Arguments
            term: The name (or partial name) of a vessel we'd like to search
            ids: List of IDS of vessels we'd like to search
            vessel_classes: List of vessel classes, must be one of .. TODO LIST HERE
            vessel_product_types: List of product IDs, searching vessels currently (or recently) carrying these products.

        # Returns
        List of vessels matching the search arguments.


        # Examples

        ```python
        >>> Vessels.search(vessel_classes=['aframax', 'handymax'],
                 vessel_product_types=["6f11b0724c9a4e85ffa7f1445bc768f054af755a090118dcf99f14745c261653"])
        ```
        """

        search_params = {
            "term": term,
            "ids": ids,
            "vessel_classes": vessel_classes,
            "vessel_product_types": vessel_product_types,
        }

        return VesselsSearchResult(super().search(**search_params))
