from typing import List, Optional, Union

import pandas as pd
from typing_extensions import Literal

from vortexasdk.api.search_result import Result


class AnywhereFreightPricingResult(Result):
    """Container class that holds results from Anywhere Freight Pricing endpoints."""

    def to_df(
        self, columns: Optional[Union[List[str], Literal["all"]]] = "all"
    ) -> pd.DataFrame:
        """
        Represent the results as a DataFrame.

        # Arguments
            columns: Output columns present in the `pd.DataFrame`.
            Enter `columns='all'` to return all available columns.
            Enter a list of column names to return only those columns.

        # Returns
        `pd.DataFrame` with the results, using json_normalize to flatten nested structures.
        """
        if not self.records:
            return pd.DataFrame()

        df = pd.json_normalize(self.records)

        if columns is None or columns == "all":
            return df

        # Filter to requested columns that exist in the dataframe
        available_columns = [col for col in columns if col in df.columns]
        return df[available_columns]
