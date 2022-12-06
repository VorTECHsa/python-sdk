# Average Speed Time Series

_Please note: you will require a subscription to our Freight module to access this endpoint._

The Voyages Time Series Endpoint, using `breakdown_property: avg_speed`, is used to retrieve the average speed data as a time series. You can find detailed information regarding the Voyages Time Series Endpoint [here](/endpoints/voyages_timeseries).

You can find more information regarding the methodology for average speed here (link to API docs).

Example - daily average speed of vessels leaving Rotterdam between 26th and 30th April 2022:

```python
from vortexasdk import VoyagesTimeseries, Geographies
from datetime import datetime
rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
search_result = VoyagesTimeseries().search(
    origins=rotterdam,
    time_min=datetime(2022, 4, 26),
    time_max=datetime(2022, 4, 30, 23, 59),
    breakdown_property="avg_speed"
    ).to_df()

```

|     | key                       |   value | count | breakdown.0.label | breakdown.0.count | breakdown.0.value |
| --: | :------------------------ | ------: | ----: | :---------------- | :---------------- | :---------------- |
|   0 | 2022-04-26 00:00:00+00:00 | 27874.1 |   215 |                   |                   |                   |
|   1 | 2022-04-27 00:00:00+00:00 | 25878.7 |   227 |                   |                   |                   |
|   2 | 2022-04-28 00:00:00+00:00 |   25569 |   228 |                   |                   |                   |
|   3 | 2022-04-29 00:00:00+00:00 | 26389.5 |   226 |                   |                   |                   |
|   4 | 2022-04-30 00:00:00+00:00 | 26366.6 |   221 |                   |                   |                   |

```

```
