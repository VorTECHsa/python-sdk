"""
Let's see how much Medium-Sour Crude is in long term floating storage, in January 2019.

The below script returns:

|     | key                      |    value |   count |
|----:|:-------------------------|---------:|--------:|
|   0 | 2019-01-01T00:00:00.000Z |  7381    |       9 |
|   1 | 2019-01-02T00:00:00.000Z |  8127    |      23 |
|   2 | 2019-01-03T00:00:00.000Z |  2333    |      32 |
|   3 | 2019-01-04T00:00:00.000Z |  447759  |      43 |
|   4 | 2019-01-05T00:00:00.000Z |  7777144 |       4 |
...

"""

from datetime import datetime

from docs.utils import to_markdown
from vortexasdk import CargoTimeSeries, Products

if __name__ == "__main__":
    # Find Medium Sour ID
    medium_sour = [
        p.id
        for p in Products().search(term="Medium-Sour").to_list()
        if p.name == "Medium-Sour"
    ]
    # Check we've only got one ID
    assert len(medium_sour) == 1

    # Query API
    search_result = CargoTimeSeries().search(
        # We're looking at daily storage levels
        timeseries_frequency="day",
        # We want 'b' for barrels here
        timeseries_unit="b",
        # We're only interested in storage of Medium-Sour Crude
        filter_products=medium_sour,
        # We're only included in cargo's that were in floating storage
        filter_activity="storing_state",
        # We're only interested in floating storage that lasted longer than 14 days
        timeseries_activity_time_span_min=1000 * 60 * 60 * 24 * 14,
        # Let's limit the search to January 2019 storage events
        filter_time_min=datetime(2019, 1, 1),
        filter_time_max=datetime(2019, 2, 1),
    )

    # Convert search result to dataframe
    df = search_result.to_df()

    print(to_markdown(df.head()))
