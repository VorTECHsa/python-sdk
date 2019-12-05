import os
from multiprocessing.pool import Pool
from typing import List

import pandas as pd

from vortexasdk.api.search_result import Result
from vortexasdk.api.timeseries_item import TimeSeriesItem


class TimeSeriesResult(Result):
    def to_list(self) -> List[TimeSeriesItem]:
        list_of_dicts = super().to_list()
        with Pool(os.cpu_count()) as pool:
            return list(pool.map(TimeSeriesItem.from_dict, list_of_dicts))

    def to_df(self, columns=None) -> pd.DataFrame:
        return pd.DataFrame(data=super().to_list())
