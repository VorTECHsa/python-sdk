from typing import Any, Dict, List, Optional, Union

import pandas as pd
from pydantic import Field
from typing_extensions import Literal

from vortexasdk.api.search_result import Result


class VoyageCalculatorResult(Result):
    """
    Container class holding results returned from the voyage calculator endpoint.

    This class has `to_list()` and `to_df()` methods for representing results.
    """

    def to_list(self) -> List[dict]:
        """Represent voyage calculations as a list of dictionaries."""
        return super().to_list()

    def to_df(
        self, columns: Optional[Union[List[str], Literal["all"]]] = "all"
    ) -> pd.DataFrame:
        """
        Represent voyage calculations as a `pd.DataFrame`.

        # Arguments
            columns: Output columns present in the `pd.DataFrame`.
            Enter `columns='all'` to return all available columns.
            Enter a list of column names to return only those columns.

        # Returns
        `pd.DataFrame` with one row per calculated voyage.

        """
        if not self.records:
            return pd.DataFrame()

        df = pd.json_normalize(self.records)

        if columns is None or columns == "all":
            return df

        available_columns = [col for col in columns if col in df.columns]
        return df[available_columns]


class VoyageCalculatorBatchResult(Result):
    """
    Container class holding results returned from the voyage calculator batch endpoint.

    This class has `to_list()`, `to_df()`, and `metadata` for per-item status messages.
    """

    metadata: List[Dict[str, Any]] = Field(default_factory=list)

    def to_list(self) -> List[dict]:
        """Represent batch voyage calculations as a list of dictionaries."""
        return super().to_list()

    def to_df(
        self, columns: Optional[Union[List[str], Literal["all"]]] = "all"
    ) -> pd.DataFrame:
        """
        Represent batch voyage calculations as a `pd.DataFrame`.

        Each row includes correlation fields (origin, destination, vessel_class, avoid_zone)
        alongside the calculation results (ETA, ETD, speed, duration).

        # Arguments
            columns: Output columns present in the `pd.DataFrame`.
            Enter `columns='all'` to return all available columns.
            Enter a list of column names to return only those columns.

        # Returns
        `pd.DataFrame` with one row per calculated voyage.

        """
        if not self.records:
            return pd.DataFrame()

        df = pd.json_normalize(self.records)

        if columns is None or columns == "all":
            return df

        available_columns = [col for col in columns if col in df.columns]
        return df[available_columns]
