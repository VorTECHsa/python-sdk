"""

Here we find all vessels that have diverted too or from the United States.


The below script returns something similar to:

(The above data has been anonymised in this example)
"""
from datetime import datetime, timedelta

from vortexasdk import VesselDiversions, Geographies


if __name__ == "__main__":

    usa = Geographies().search("United States", exact_term_match=True).to_list()[0].id

    # Query API
    search_result = VesselDiversions().search(

        # Find all vessels that have diverted in the last 2 weeks
        filter_time_min=datetime.now() - timedelta(weeks=2),

        # We're only interested in vessels that have diverted to, from, or within the USA
        filter_locations=usa,
    )

    df = search_result.to_df()
