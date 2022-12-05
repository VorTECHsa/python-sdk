# Utilisation Time Series

_Please note: you will require a subscription to our Freight module to access this endpoint._

The Voyages Time Series Endpoint, using `breakdown_property: 'utilisation'`, is used to retrieve the utilisation data as a time series. You can find detailed information regarding the Voyages Time Series Endpoint [here](/endpoints/voyages_timeseries).

You can find more information regarding the methodology for utilisation here (link to API docs).

Example:

```
res = VoyagesTimeseries()
    .search(
        time_min=datetime(2022, 4, 26),
        time_max=datetime(2022, 4, 28, 23, 59),
        breakdown_property="utilisation",
    ).to_df()
```
