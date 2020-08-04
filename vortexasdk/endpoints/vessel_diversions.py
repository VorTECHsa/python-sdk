"""Vessel Diversions Endpoint."""
from datetime import datetime, timedelta
from typing import List, Union

from vortexasdk.api import ID
from vortexasdk.api.shared_types import to_ISODate
from vortexasdk.endpoints.endpoints import VESSEL_DIVERSIONS_RESOURCE
from vortexasdk.endpoints.vessel_diversions_result import VesselDiversionsResult
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list

logger = get_logger(__name__)


class VesselDiversions(Search):
    """
    Vessel Diversions Endpoint, use this to search through Vortexa's vessel diversions.
    """

    _MAX_PAGE_RESULT_SIZE = 500
    _MAX_DIVERSION_HISTORIC_DAYS = 30

    def __init__(self):
        Search.__init__(self, VESSEL_DIVERSIONS_RESOURCE)

    # noinspection PyMethodOverriding
    def search(
            self,
            behaviour: str = "country_diversion",
            filter_locations: Union[ID, List[ID]] = None,
            filter_products: Union[ID, List[ID]] = None,
            filter_vessels: Union[ID, List[ID]] = None,
            filter_vessel_classes: Union[str, List[str]] = None,
            filter_vessel_flags: Union[str, List[str]] = None,
            filter_scrubbers_fitted: str = "disabled",
            unit: str = "b",
            include_waypoints="true",
            exclude_vessel_classes: Union[str, List[str]] = None,
            exclude_vessel_flags: Union[str, List[str]] = None,
            exclude_locations: Union[ID, List[ID]] = None,
            exclude_products: Union[ID, List[ID]] = None,
            exclude_vessels: Union[ID, List[ID]] = None,
            filter_time_min: datetime = datetime.now() - timedelta(days=7),

    ) -> VesselDiversionsResult:
        """

        Find vessel diversions matching the given search parameters.

        # Arguments

        # Returns
        `VesselDiversionsResult`, containing all the diversions matching the given search terms.
        """

        api_params = {
            "behaviour": behaviour,
            "includeWaypoints": include_waypoints,
            "location": convert_to_list(filter_locations),
            "locationExcluded": convert_to_list(exclude_locations),
            "products": convert_to_list(filter_products),
            "productsExcluded": convert_to_list(exclude_products),
            "scrubbersFitted": filter_scrubbers_fitted,
            "startTimestamp": to_ISODate(filter_time_min),
            "unit": unit,
            "vesselClasses": convert_to_list(filter_vessel_classes),
            "vesselClassesExcluded": convert_to_list(exclude_vessel_classes),
            "vesselFlags": convert_to_list(filter_vessel_flags),
            "vesselFlagsExcluded": convert_to_list(exclude_vessel_flags),
            "vessels": convert_to_list(filter_vessels),
            "vesselsExcluded": convert_to_list(exclude_vessels),
            "size": self._MAX_PAGE_RESULT_SIZE,
        }

        earliest_allowed_date = datetime.now() - timedelta(days=self._MAX_DIVERSION_HISTORIC_DAYS)
        if filter_time_min < earliest_allowed_date:
            raise ValueError(
                f"Max limit of {self._MAX_DIVERSION_HISTORIC_DAYS} days of diversions breached. Minimum filter date: {earliest_allowed_date}"
            )

        return VesselDiversionsResult(super().search(**api_params))
