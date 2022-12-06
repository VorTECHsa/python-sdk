# Origin Breakdown

_Please note: you will require a subscription to our Freight module to access this endpoint._

The Voyages Top Hits Endpoint, using `breakdown_property: vessel_count` and one of `breakdown_split_property: 'origin_region','origin_shipping_region','origin_trading_region','origin_trading_sub_region','origin_trading_block','origin_country','origin_port','origin_terminal'`. The endpoint is used to retrieve vessel count broken down by an origin geography layer. You can find detailed information regarding the Voyages Top Hits Endpoint here.

You can find more information regarding the methodology for the origin breakdown here (link to API docs).

Example - breakdown by origin country of vessels heading to Rotterdam between 26th and 30th April 2022:

```python
from vortexasdk import VoyagesTimeseries, Geographies
from datetime import datetime
rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
search_result = VoyagesTopHits().search(
    time_min=datetime(2022, 4, 26),
    time_max=datetime(2022, 4, 30, 23, 59),
    destinations = rotterdam,
    breakdown_split_property= "origin_country"
    ).to_df()
```

|     | id               | value | count | label          |
| --: | :--------------- | ----: | ----: | :------------- |
|   0 | 2dfc3d43a21697c0 |    37 |   145 | Netherlands    |
|   1 | 2aaad41b89dfad19 |    31 |    99 | United Kingdom |
|   2 | 2d92cc08f22524db |    28 |   117 | United States  |
|   3 | b563622dd5a266e6 |    27 |    98 | Belgium        |
|   4 | b996521be9c996db |    25 |    89 | Russia         |
|   5 | 3267ef2a83a74905 |    17 |    77 | Malaysia       |
|   6 | 612eeab9024bfb73 |    16 |    77 | Indonesia      |
|   7 | c1698979b983b265 |    16 |    67 | Spain          |
|   8 | 934c47f36c16a58d |    15 |    71 | China          |
|   9 | 430f0e467f3a408f |     8 |    38 | Nigeria        |

```

```
