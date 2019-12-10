"""
Let's find all crude cargo movements from Saudi Arabia to India that loaded in the last month.

The below script returns a `pd.DataFrame`, similar to the chart shown on `https://analytics.vortexa.com`,
 by selecting the Movements tab, filtering on `Products: Crude` with `Origin: Saudi Arabia`, `Destination: India` and
 `Date Range: Departures in the last Month`.

"""
from datetime import datetime
from dateutil.relativedelta import relativedelta

from docs.utils import to_markdown
from vortexasdk import CargoMovements

now = datetime.utcnow()
one_month_ago = now - relativedelta(months=1)

search_result = CargoMovements().search(
    filter_activity="loading_end",
    filter_origins="Saudi Arabia",
    filter_destinations="India",
    filter_products="Crude",
    filter_time_min=one_month_ago,
    filter_time_max=now,
)

df = search_result.to_df(
    columns=[
        "vessels.0.name",
        "vessels.0.vessel_class",
        "status",
        "vessels.0.corporate_entities.charterer.label",
        "vessels.0.corporate_entities.time_charterer.label",
        "vessels.0.corporate_entities.commercial_owner.label",
        "product.group.label",
        "product.grade.label",
        "quantity",
        "events.cargo_port_load_event.0.location.port.label",
        "events.cargo_port_load_event.0.end_timestamp",
        "events.cargo_port_unload_event.0.location.port.label",
        "events.cargo_port_unload_event.0.end_timestamp",
    ]
)

df = df.sort_values(by=["events.cargo_port_load_event.0.end_timestamp"])

print(to_markdown(df))
