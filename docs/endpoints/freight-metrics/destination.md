# Destination Breakdown

_Please note: you will require a subscription to our Freight module to access this endpoint._

The Voyages Top Hits Endpoint, using `breakdown_property: vessel_count` and one of `breakdown_split_property: 'destination_region','destination_shipping_region','destination_trading_region','destination_trading_sub_region','destination_trading_block','destination_country','destination_port','destination_terminal'`. The endpoint is used to retrieve vessel count broken down by an destination geography layer. You can find detailed information regarding the Voyages Top Hits Endpoint here.

You can find more information regarding the methodology for the destination breakdown here (link to API docs).

Example - breakdown by destination country of vessels departing from Rotterdam between 26th and 30th April 2022:

```python
from vortexasdk import VoyagesTimeseries, Geographies
from datetime import datetime
rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
search_result = VoyagesTopHits().search(
    time_min=datetime(2022, 4, 26),
    time_max=datetime(2022, 4, 30, 23, 59),
    origins = rotterdam,
    breakdown_split_property= "destination_country"
    ).to_df()
```

|     | id               | value | count | label          |
| --: | :--------------- | ----: | ----: | :------------- |
|   0 | 2dfc3d43a21697c0 |    32 |   138 | Netherlands    |
|   1 | 2aaad41b89dfad19 |    32 |   109 | United Kingdom |
|   2 | 2d92cc08f22524db |    28 |   115 | United States  |
|   3 | b996521be9c996db |    28 |   108 | Russia         |
|   4 | b563622dd5a266e6 |    15 |    63 | Belgium        |
|   5 | e9e556620469f46a |    12 |    52 | France         |
|   6 | f04ac0af071c3907 |    11 |    35 | Sweden         |
|   7 | 459d056652a0b7aa |    10 |    29 | Norway         |
|   8 | 70425373a1836d6d |     6 |    27 | India          |
|   9 | 934c47f36c16a58d |     5 |    25 | China          |

```

```
