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
    )

    # Convert the search result to a dataframe
    vessel_movements = search_result.to_df()

    # Ballast movements are movements without a cargo.
    is_ballast_mask = vessel_movements["cargoes.0.product.group.label"].isna()

    ballast_movements = vessel_movements[is_ballast_mask]
