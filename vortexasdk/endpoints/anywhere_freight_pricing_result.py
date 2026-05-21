from typing import Any, Dict, List

import pandas as pd
from pydantic import Field

from vortexasdk.api.search_result import Result


class AnywhereFreightPricingResult(Result):
    """Container class that holds results from Anywhere Freight Pricing endpoints."""

    records: List = Field(default_factory=list)
    reference: Dict[str, Any] = Field(default_factory=dict)

    def to_list(self) -> List[Dict[str, Any]]:
        """
        Represent the results as a list of records.

        Returns the raw API response data.
        """
        return self.records

    def to_df(self) -> pd.DataFrame:
        """
        Represent the results as a DataFrame.

        Uses pd.json_normalize to flatten nested structures.
        """
        if not self.records:
            return pd.DataFrame()

        return pd.json_normalize(self.records)
