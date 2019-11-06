from abc import ABC, abstractmethod
from typing import List

import pandas as pd


class SearchResult(ABC):
    _result: List[dict]

    def __init__(self, _result: List[dict]):
        self._result: List[dict] = _result

    @abstractmethod
    def to_list(self) -> List[dict]:
        """
        Represents search result as a list
        """
        return self._result

    @abstractmethod
    def to_df(self, columns) -> pd.DataFrame:
        """
        Represents search result as a `pd.DataFrame` with given columns
        """
        pass

    def __len__(self):
        return len(self._result)

    def __str__(self):
        return str(self._result)

    def __iter__(self):
        return iter(self._result)

    def __getitem__(self, item):
        return self._result.__getitem__(item)
