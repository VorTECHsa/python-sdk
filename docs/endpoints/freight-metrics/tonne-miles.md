# Tonne Miles Time Series

_Please note: you will require a subscription to our Freight module to access this endpoint._

The Voyages Time Series Endpoint, using `breakdown_property: ‘tonne-miles’`, is used to retrieve the tonne-miles data as a time series. You can find detailed information regarding the Voyages Time Series Endpoint [here](/endpoints/voyages_timeseries).

You can find more information regarding the methodology for tonne-miles here (link to API docs).

Example - daily tonne miles for vessels leaving Rotterdam between 26th and 30th April 2022:

```python
from vortexasdk import VoyagesTimeseries, Geographies
from datetime import datetime
rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
search_result = VoyagesTimeseries().search(
    origins=rotterdam,
    time_min=datetime(2022, 4, 26),
    time_max=datetime(2022, 4, 30, 23, 59),
    breakdown_property="tonne_miles"
    ).to_df()

```

|     | key                       |       value | count | breakdown.0.label | breakdown.0.count | breakdown.0.value |
| --: | :------------------------ | ----------: | ----: | :---------------- | :---------------- | :---------------- |
|   0 | 2022-04-26 00:00:00+00:00 | 4.39122e+08 |   173 |                   |                   |                   |
|   1 | 2022-04-27 00:00:00+00:00 | 4.29226e+08 |   175 |                   |                   |                   |
|   2 | 2022-04-28 00:00:00+00:00 | 4.10637e+08 |   174 |                   |                   |                   |
|   3 | 2022-04-29 00:00:00+00:00 | 4.55488e+08 |   166 |                   |                   |                   |
|   4 | 2022-04-30 00:00:00+00:00 | 4.68367e+08 |   161 |                   |                   |                   |

```

```
