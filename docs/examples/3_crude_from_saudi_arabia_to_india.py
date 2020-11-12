"""
Let's find all crude cargo movements from Saudi Arabia to India that loaded in the last month.

The below script returns a `pd.DataFrame`, similar to the table given in the movements tab of `https://analytics.vortexa.com`,
 filtering on `Products: Crude` with `Origin: Saudi Arabia`, `Destination: India` and `Date Range: Departures in the last Month`.

"""
from datetime import datetime

from dateutil.relativedelta import relativedelta

from vortexasdk import CargoMovements, Geographies, Products

if __name__ == "__main__":
    now = datetime.utcnow()



    one_month_ago = now - relativedelta(months=1)

    # For this analysis we need the geography ID for India, and the geography ID for Saudi Arabia. We're going to
    # show 2 ways to retrieve geography IDs. You'll want to chose method 1 or 2 depending on your use case.

    # Option 1. We look up a geography with an exact matching name
    saudi_arabia = (
        Geographies()
        .search("Saudi Arabia", exact_term_match=True)
        .to_list()[0]
        .id
    )

    # Option 2. We search for geographies with similar names, then pick the one we're looking for

    # First we find the ID for the country India. Note that when searching geographies with the term 'india', we'll
    # retrieve all geographies with india in the name, ie Indiana, British Indian Ocean Territory...
    all_geogs_with_india_in_the_name = Geographies().search("india").to_list()

    # If running interactively, you may want to print all the names here to inspect them for yourself
    for g in all_geogs_with_india_in_the_name:
        print(g.name)

    # We're only interested in the country India here
    india = [
        g.id for g in all_geogs_with_india_in_the_name if g.name == "India"
    ]
    # Check we've only got one ID for India
    assert len(india) == 1

    # Let's find the Crude ID,
    # here we know the exact name of the product we're looking for so we set exact_term_match=True
    crude = Products().search("Crude", exact_term_match=True).to_list()[0].id

    # Query the API.
    search_result = CargoMovements().search(
        filter_activity="loading_end",
        filter_origins=saudi_arabia,
        filter_destinations=india,
        filter_products=crude,
        filter_time_min=one_month_ago,
        filter_time_max=now,
    )

    # A complete list of available columns can be found at https://vortechsa.github.io/python-sdk/endpoints/cargo_movements/#notes
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
