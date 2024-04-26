from typing_extensions import Literal
from pydantic import BaseModel, Field
from typing import Any, Dict, List

import pandas as pd


class Result(BaseModel):
    """Abstract Container that holds a list of *records*."""

    records: List = Field(default_factory=list)
    reference: Dict[str, Any] = Field(default_factory=dict)

    def to_list(self) -> List:
        """Represent *records* as a list."""
        return self.records

    def to_df(
        self, columns: Literal["all"] | List[str] | None
    ) -> pd.DataFrame:
        """Represent *records* as a `pd.DataFrame` with given columns."""
        pass

    def __len__(self: "Result") -> int:
        """Delegate to *records*."""
        return len(self.records)

    def __str__(self: "Result") -> str:
        """Delegate to *records*."""
        return str(self.records)

    def __iter__(self: "Result"):
        """Delegate to *records*."""
        return iter(self.records)

    def __getitem__(self: "Result", item):
        """Delegate to *records*."""
        return self.records.__getitem__(item)
