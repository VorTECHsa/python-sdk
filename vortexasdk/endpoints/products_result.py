from typing import List

import jsons as jsons
import pandas as pd

from vortexasdk.api import Product
from vortexasdk.api.search_result import Result


class ProductResult(Result):
    """Container class that holds the result obtained from calling the `Product` endpoint."""

    def to_list(self) -> List[Product]:
        """Represent products as a list."""
        list_of_dicts = super().to_list()
        return jsons.loads(jsons.dumps(list_of_dicts), List[Product])

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent products as a `pd.DataFrame`.

        # Arguments
            columns: The product features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'parent']`.


        # Returns
        `pd.DataFrame` of products.

        """
        if columns is None:
            columns = ['id', 'name', 'parent']

        df = pd.DataFrame(super().to_list())

        if columns == 'all':
            return df
        else:
            return df[columns]
