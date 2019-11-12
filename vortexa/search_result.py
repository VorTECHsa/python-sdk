from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

import pandas as pd


@dataclass
class Result(ABC):
    """Abstract Container that holds a list of *_records*."""

    _records: List

    def to_list(self) -> List:
        """Represent *_records* as a list."""
        return self._records

    @abstractmethod
    def to_df(self, columns=None) -> pd.DataFrame:
        """Represent *_records* as a `pd.DataFrame` with given columns."""
        pass

    def __len__(self):
        """Delegate to *_records*."""
        return len(self._records)

    def __str__(self):
        """Delegate to *_records*."""
        return str(self._records)

    def __iter__(self):
        """Delegate to *_records*."""
        return iter(self._records)

    def __getitem__(self, item):
        """Delegate to *_records*."""
        return self._records.__getitem__(item)
