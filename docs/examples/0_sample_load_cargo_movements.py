"""
Let's retrieve some sample cargo movements in a dataframe.

The below script returns something similar to:

|    | events.cargo_port_unload_event.0.start_timestamp   | product.group.label   | product.grade.label   |   quantity | vessels.0.name   |
|---:|:---------------------------------------------------|:----------------------|:----------------------|-----------:|:-----------------|
|  0 | 2019-10-08T00:41:00+0000                           | Crude                 | Djeno                 |     123457 | AROME            |
|  1 | 2019-11-08T00:41:52+0000                           | Crude                 | Arab Medium           |      99898 | SCOOBYDOO        |
|  2 | 2019-09-30T23:49:41+0000                           | Crude                 | Arab Heavy            |    9879878 | DAVID            |
|  3 | 2019-12-01T01:40:00+0000                           | Crude                 | Usan                  |     999999 | DUCK             |


"""
from datetime import datetime

from vortexasdk import CargoMovements

if __name__ == "__main__":
    # Query API to find all vessels that were loading on the 1st of Aug 2019
    search_result = CargoMovements().search(
        filter_activity="loading_start",
        filter_time_min=datetime(2019, 8, 1),
        filter_time_max=datetime(2019, 8, 1),
    )
    print("Cargo movements successfully loaded")

    # Convert search result to dataframe
    df = search_result.to_df()

    print(df.head())
