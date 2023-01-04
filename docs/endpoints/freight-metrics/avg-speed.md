# Average Speed Time Series

_Please note: you will require a subscription to our Freight module to access this endpoint._

The Voyages Time Series Endpoint, using `breakdown_property: avg_speed`, is used to retrieve the average speed data as a time series. You can find detailed information regarding the Voyages Time Series Endpoint [here](/python-sdk/endpoints/voyages_timeseries).

You can find more information regarding the methodology for average speed here [here](https://docs.vortexa.com/reference/intro-freight-metrics).

Example - daily average speed of vessels leaving Rotterdam between 26th and 30th April 2022:

```python
from vortexasdk import VoyagesTimeseries, Geographies
from datetime import datetime
rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
search_result = VoyagesTimeseries().search(
    origins=rotterdam,
    time_min=datetime(2022, 4, 26),
    time_max=datetime(2022, 4, 30, 23, 59),
    breakdown_property="avg_speed",
    breakdown_unit_operator="avg",
    ).to_df(columns=['key', 'value', 'count'])

```

|     | key                       |     value | count |
| --: | :------------------------ | --------: | ----: |
|   0 | 2022-04-26 00:00:00+00:00 | 11.737703 |   215 |
|   1 | 2022-04-27 00:00:00+00:00 | 11.736763 |   227 |
|   2 | 2022-04-28 00:00:00+00:00 |  11.44699 |   228 |
|   3 | 2022-04-29 00:00:00+00:00 | 11.586345 |   226 |
|   4 | 2022-04-30 00:00:00+00:00 | 11.398125 |   221 |

```

```
