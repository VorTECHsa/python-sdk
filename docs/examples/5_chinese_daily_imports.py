"""
Let's retrieve the daily sum of Chinese Crude/Condensate imports, across January 2019.

The below script returns:

|     | key                      |    value |   count |
|----:|:-------------------------|---------:|--------:|
|   0 | 2019-01-01T00:00:00.000Z |  1237381 |       9 |
|   1 | 2019-01-02T00:00:00.000Z |  6548127 |      23 |
|   2 | 2019-01-03T00:00:00.000Z | 45457617 |      23 |
|   3 | 2019-01-04T00:00:00.000Z |  6467759 |      43 |
|   4 | 2019-01-05T00:00:00.000Z |  7777144 |       4 |
...

"""
from datetime import datetime

from vortexasdk import CargoTimeSeries, Geographies, Products

if __name__ == "__main__":
    # Find china ID, here we're only looking for geographies with the exact name China, so we set exact_term_match=True
    china = Geographies().search(term="China", exact_term_match=True).to_list()[0].id

    # Find Crude/Condensates ID.
    # Again, we know the exact name of the product we're searching for, so we set exact_term_match=True
    crude_condensates = Products().search(term="Crude/Condensates", exact_term_match=True)[0].id

    # Query API
    search_result = CargoTimeSeries().search(
        # We're only interested in movements into China
        filter_destinations=china,
        # We're looking at daily imports
        timeseries_frequency="day",
        # We want 'b' for barrels here
        timeseries_unit="b",
        # We're only interested in Crude/Condensates
        filter_products=crude_condensates,
        # We want all cargo movements that unloaded in January 2019 to be included
        filter_activity="unloading_start",
        filter_time_min=datetime(2019, 1, 1),
        filter_time_max=datetime(2019, 2, 1),
    )

    # Convert search result to dataframe
    df = search_result.to_df()
