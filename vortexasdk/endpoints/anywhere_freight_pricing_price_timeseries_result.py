from typing import Any, Dict, List

import pandas as pd
from pydantic import Field

from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class AnywhereFreightPricingPriceTimeseriesResult(Result):
    """Container class that holds the result from the AFP Price Timeseries endpoint."""

    records: List = Field(default_factory=list)
    reference: Dict[str, Any] = Field(default_factory=dict)

    def to_list(self) -> List[Dict[str, Any]]:
        """
        Represent the results as a list of route pricing records.

        Each record contains route details (origin_port, destination_port,
        vessel_class, product) and a list of prices over time.
        """
        return self.records

    def to_df(self) -> pd.DataFrame:
        """
        Represent the results as a flattened DataFrame.

        Each row represents a single price point for a route on a specific date.
        """
        flattened_records = []

        for record in self.records:
            base_info = {
                "origin_port": record.get("origin_port"),
                "destination_port": record.get("destination_port"),
                "vessel_class": record.get("vessel_class"),
                "product": record.get("product"),
                "avoid_zone": record.get("avoid_zone"),
                "suggested_tonnage": record.get("suggested_tonnage"),
            }

            for price_entry in record.get("prices", []):
                row = {
                    **base_info,
                    "date": price_entry.get("date"),
                    "price": price_entry.get("price"),
                    "price_lower": price_entry.get("price_lower"),
                    "price_upper": price_entry.get("price_upper"),
                    "voyage_price": price_entry.get("voyage_price"),
                }
                flattened_records.append(row)

        df = pd.DataFrame(flattened_records)

        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"])

        return df
