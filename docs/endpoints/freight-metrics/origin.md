# Origin Breakdown

_Please note: you will require a subscription to our Freight module to access this endpoint._

The Voyages Top Hits Endpoint, using `breakdown_property: vessel_count` and one of `breakdown_split_property: 'origin_region','origin_shipping_region','origin_trading_region','origin_trading_sub_region','origin_trading_block','origin_country','origin_port','origin_terminal'`. The endpoint is used to retrieve vessel count broken down by an origin geography layer. You can find detailed information regarding the Voyages Top Hits Endpoint here.

You can find more information regarding the methodology for the origin breakdown here (link to API docs).

Example:

```
res = VoyagesTopHits()
    .search(
        time_min=datetime(2022, 4, 26),
        time_max=datetime(2022, 4, 28, 23, 59),
        breakdown_split_property="origin_country",
        breakdown_size=5,
    ).to_df()
```
