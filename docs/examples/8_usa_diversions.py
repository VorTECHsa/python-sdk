"""

Here we find all vessels that have diverted to, from, or within the United States.


The below script returns something similar to:

|     | vessel_name          | origin.port.label                            | origin.country.label   | timestamp                 | prev_destination.port.label     | next_destination.port.label     | prev_destination.country.label   | next_destination.country.label   | prev_declared_destination   | next_declared_destination   | prev_eta                  | next_eta                  | cargoes.0.product_hierarchy.group.label   | cargoes.0.product_hierarchy.group_product.label   | cargoes.0.product_hierarchy.category.label   | cargoes.0.product_hierarchy.grade.label   | is_considered_waypoint   |
|----:|:---------------------|:---------------------------------------------|:-----------------------|:--------------------------|:--------------------------------|:--------------------------------|:---------------------------------|:---------------------------------|:----------------------------|:----------------------------|:--------------------------|:--------------------------|:------------------------------------------|:--------------------------------------------------|:---------------------------------------------|:------------------------------------------|:-------------------------|
|   0 | MASEL                | Sikka [IN]                                   | India                  | 2020-06-30 01:03:39+00:00 | New York, NY [US]               | Gibraltar [GI]                  | United States                    | Gibraltar                        | NEW YORK                    | GIBRALTAR                   | 2020-07-01 00:39:40+00:00 | 2020-08-01 23:44:44+00:00 | Clean Petroleum Products                  | Gasoline/Blending Components                      | Blending Components                          | Alkylate                                  | True                     |
|   1 | CUCKOO WARRIOR       | Trieste [IT]                                 | Italy                  | 2020-06-22 04:44:44+00:00 | Houston, TX [US]                | Beaumont, TX [US]               | United States                    | United States                    | US HOUSTON                  | US BEAUMONT                 | 2020-07-11 05:00:17+00:00 | 2020-08-10 23:44:44+00:00 | nan                                       | nan                                               | nan                                          | nan                                       | False                    |
|   2 | LAMBRNI              | Puerto Bayovar [PE]                          | Peru                   | 2020-06-21 23:38:21+00:00 | Marcus Hook [US]                | Singapore [SG]                  | United States                    | Singapore                        | PMARCUS HO                  | SINGAPORE                   | 2020-07-01 23:00:00+00:00 | 2020-08-24 23:38:21+00:00 | Crude/Condensates                         | Crude                                             | Heavy-Sour                                   | Loreto                                    | True                     |
...

(The above data has been anonymised in this example)
"""
from datetime import datetime, timedelta

from vortexasdk import VesselDiversions, Geographies


if __name__ == "__main__":

    # Find the id for the United States country. In this case we know the exact name of the polygon we're looking
    # for, so we set exact_term_match=True.
    usa = Geographies().search("United States", exact_term_match=True).to_list()[0].id

    # Query the vessel diversions endpoint
    search_result = VesselDiversions().search(

        # Find all vessels that have diverted in the last 2 weeks
        filter_time_min=datetime.now() - timedelta(weeks=2),

        # We're only interested in vessels that have diverted to, from, or within the USA
        filter_locations=usa,
    )

    # Convert the search result to a dataframe
    df = search_result.to_df()
