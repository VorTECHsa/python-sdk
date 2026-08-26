from typing import Any, Dict, List, Optional, Union

from vortexasdk.endpoints.endpoints import VOYAGE_CALCULATOR
from vortexasdk.endpoints.voyage_calculator_result import (
    VoyageCalculatorResult,
)
from vortexasdk.operations import Search

from typing_extensions import Literal

VoyageCalculatorType = Literal["speed", "ETA", "ETD"]
VoyageCalculatorVesselStatus = Literal[
    "vessel_status_ballast",
    "vessel_status_laden_known",
    "vessel_status_laden_unknown",
]
VoyageCalculatorAvoidZone = Literal["Panama Canal", "Suez Canal"]

LatLong = Dict[str, float]


class VoyageCalculator(Search):
    """
    Voyage Calculator endpoint.

    Calculates voyage routes, ETAs, ETDs, or speeds between an origin and destination
    using Vortexa's pathfinder routing engine. The calculator accounts for vessel class,
    laden/ballast status, canal avoidance zones, and optional waypoints.
    """

    def __init__(self) -> None:
        Search.__init__(self, VOYAGE_CALCULATOR)

    def search(
        self,
        type: VoyageCalculatorType,
        vessel_status: VoyageCalculatorVesselStatus,
        origin: Union[str, LatLong],
        destination: Union[str, LatLong],
        vessel_id: Optional[str] = None,
        vessel_class: Optional[str] = None,
        waypoints: Optional[List[str]] = None,
        ETA: Optional[str] = None,
        ETD: Optional[str] = None,
        speed: Optional[float] = None,
        avoid_zone: Optional[List[VoyageCalculatorAvoidZone]] = None,
        voyage_delay_factor: Optional[float] = None,
    ) -> "VoyageCalculatorResult":
        """
        Calculate a voyage route between an origin and destination.

        # Arguments
            type: The type of calculation to perform. One of:
                - `'speed'`: Calculate the speed required given an ETD and ETA.
                - `'ETA'`: Calculate the ETA given an ETD and speed.
                - `'ETD'`: Calculate the ETD given an ETA and speed.

            vessel_status: Whether the vessel is laden or ballast. One of:
                `'vessel_status_ballast'`, `'vessel_status_laden_known'`, `'vessel_status_laden_unknown'`.

            origin: The origin of the voyage. Can be either:
                - A string ID (vessel ID for current position, or geography ID for centroid).
                - A dict with `lat` and `long` keys, e.g. `{"lat": 51.9, "long": 4.5}`.

            destination: The destination of the voyage. Can be either:
                - A geography ID string.
                - A dict with `lat` and `long` keys, e.g. `{"lat": 29.9, "long": 32.5}`.

            vessel_id: A vessel identifier (IMO, MMSI, vessel name, or Vortexa ID).
                Used to determine the vessel's current position (when origin is a vessel ID)
                and deadweight tonnage for routing.

            vessel_class: Vessel class used to determine DWT when `vessel_id` is not provided.
                Examples: `'oil_vlcc'`, `'oil_suezmax_lr3'`, `'oil_aframax_lr2'`, `'lng_conventional_lng'`.

            waypoints: A list of geography IDs representing intermediate waypoints.

            ETA: Estimated time of arrival as an ISO 8601 date string (e.g. `'2024-03-15T00:00:00.000Z'`).
                Required when `type` is `'speed'` or `'ETD'`.

            ETD: Estimated time of departure as an ISO 8601 date string (e.g. `'2024-03-01T00:00:00.000Z'`).
                Required when `type` is `'speed'` or `'ETA'`.

            speed: Speed in knots. Required when `type` is `'ETA'` or `'ETD'`.

            avoid_zone: A list of zones to avoid in routing. Options: `'Panama Canal'`, `'Suez Canal'`.

            voyage_delay_factor: A factor between 0 and 1 to simulate increased voyage duration.
                For example, 0.2 means 120% of the original duration.

        # Returns
        `VoyageCalculatorResult`

        # Example

        _Calculate ETA for a VLCC travelling from Ras Tanura to Rotterdam at 12 knots._

        ```python
        >>> from vortexasdk import VoyageCalculator
        >>> ras_tanura = "539db1548407fd97024391d01a6a2be239b1100f070a137d54a79907d03db6c8"
        >>> rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
        >>> result = VoyageCalculator().search(
        ...     type="ETA",
        ...     vessel_status="vessel_status_laden_known",
        ...     origin=ras_tanura,
        ...     destination=rotterdam,
        ...     vessel_class="oil_vlcc",
        ...     ETD="2024-03-01T00:00:00.000Z",
        ...     speed=12,
        ... )
        >>> df = result.to_df()

        ```

        Returns a DataFrame with columns:

        |    | ETA                      | ETD                      |   duration |   speed |
        |---:|:-------------------------|:-------------------------|-----------:|--------:|
        |  0 | 2024-03-25T14:30:00.000Z | 2024-03-01T00:00:00.000Z |      590.5 |      12 |

        """
        api_params: Dict[str, Any] = {
            "type": type,
            "vessel_status": vessel_status,
            "origin": origin,
            "destination": destination,
            "vessel_id": vessel_id,
            "vessel_class": vessel_class,
            "waypoints": waypoints,
            "ETA": ETA,
            "ETD": ETD,
            "speed": speed,
            "avoid_zone": avoid_zone,
            "voyage_delay_factor": voyage_delay_factor,
        }

        response = super().search_with_client(
            response_type="breakdown", **api_params
        )

        return VoyageCalculatorResult(
            records=response["data"], reference=response.get("reference", {})
        )
