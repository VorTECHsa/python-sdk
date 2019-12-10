"""
Let's find all crude cargo movements from Saudi Arabia to India that loaded in the last month.

The below script returns a `pd.DataFrame`, similar to the table given in the movements tab of `https://analytics.vortexa.com`,
 filtering on `Products: Crude` with `Origin: Saudi Arabia`, `Destination: India` and `Date Range: Departures in the last Month`.

"""
from datetime import datetime
from dateutil.relativedelta import relativedelta

from docs.utils import to_markdown
from vortexasdk import CargoMovements

now = datetime.utcnow()
one_month_ago = now - relativedelta(months=1)

# Query the API.
search_result = CargoMovements().search(
    filter_activity="loading_end",
    filter_origins="Saudi Arabia",
    filter_destinations="India",
    filter_products="Crude",
    filter_time_min=one_month_ago,
    filter_time_max=now,
)

# A complete list of available columns can be found at https://v0rt3x4.github.io/python-sdk/endpoints/cargo_movements/#notes
# We only require a subset of available columns here
required_columns = [
    # A cargo movement can be carried by multiple vessels across various STS transfers. You can find all the vessels that
    # the cargo was onboard by inspecting the 'vessels.0', 'vessels.1' columns etc.
    # The 'vessels.0' columns shows the primary vessel associated with the cargo movement
    "vessels.0.name",
    "vessels.0.vessel_class",
    # Here we show any corporate information associated with the primary vessel
    "vessels.0.corporate_entities.charterer.label",
    "vessels.0.corporate_entities.time_charterer.label",
    "vessels.0.corporate_entities.commercial_owner.label",
    # Show the product information and quantity
    "product.group.label",
    "product.grade.label",
    "quantity",
    # Is the vessel in transit, has it already discharged, or is it in floating storage?
    "status",
    # Show the loading Port name, and the loading timestamp
    "events.cargo_port_load_event.0.location.port.label",
    "events.cargo_port_load_event.0.end_timestamp",
    # Show the discharge Port name, and the discharge timestamp
    "events.cargo_port_unload_event.0.location.port.label",
    "events.cargo_port_unload_event.0.end_timestamp",
]

# Convert the search result to a dataframe
df = search_result.to_df(columns=required_columns)

# Sort the dataframe by loading timestamp
df = df.sort_values(by=["events.cargo_port_load_event.0.end_timestamp"])

print(to_markdown(df))
