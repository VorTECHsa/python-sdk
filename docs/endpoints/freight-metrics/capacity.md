# Cubic Capacity Time Series

_Please note: you will require a subscription to our Freight module to access this endpoint._

The Voyages Time Series Endpoint, using `breakdown_property: cubic_capacity`, is used to retrieve the cubic capacity data as a time series. You can find detailed information regarding the Voyages Time Series Endpoint [here](/python-sdk/endpoints/voyages_timeseries).

You can find more information regarding the methodology for cubic capacity [here](https://docs.vortexa.com/reference/intro-freight-metrics).

Example - daily cubic capacity of vessels leaving Rotterdam between 26th and 30th April 2022:

```python
from vortexasdk import VoyagesTimeseries, Geographies
from datetime import datetime
rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
search_result = VoyagesTimeseries().search(
    origins=rotterdam,
    time_min=datetime(2022, 4, 26),
    time_max=datetime(2022, 4, 30, 23, 59),
    breakdown_property="cubic_capacity"
    ).to_df(columns=['key', 'value', 'count'])

```

|     | key                       |    value | count |
| --: | :------------------------ | -------: | ----: |
|   0 | 2022-04-26 00:00:00+00:00 | 13637888 |   215 |
|   1 | 2022-04-27 00:00:00+00:00 | 13125281 |   214 |
|   2 | 2022-04-28 00:00:00+00:00 | 13254700 |   211 |
|   3 | 2022-04-29 00:00:00+00:00 | 13593086 |   207 |
|   4 | 2022-04-30 00:00:00+00:00 | 14149879 |   211 |

```

```
