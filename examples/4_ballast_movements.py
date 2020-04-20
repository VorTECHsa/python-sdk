"""
Let's find some ballast movements
"""
from datetime import datetime

from vortexasdk import VesselMovements

if __name__ == "__main__":
    # Query the API
    search_result = VesselMovements().search(
        filter_time_min=datetime(2017, 10, 1, 0),
        filter_time_max=datetime(2017, 10, 1, 1),
        filter_vessel_status="vessel_status_ballast",
    )

    # Convert the search result to a dataframe
    ballast_movements = search_result.to_df()
