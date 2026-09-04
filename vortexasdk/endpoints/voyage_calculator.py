from typing import Any, Dict, List, Optional, Union

from typing_extensions import Literal, Required, TypedDict

from vortexasdk.client import _handle_response, default_client
from vortexasdk.endpoints.endpoints import VOYAGE_CALCULATOR
from vortexasdk.endpoints.voyage_calculator_result import (
    VoyageCalculatorBatchResult,
    VoyageCalculatorResult,
)
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search
from vortexasdk.retry_session import _HEADERS as default_headers
from vortexasdk.retry_session import retry_post
from vortexasdk.utils import filter_empty_values

VoyageCalculatorType = Literal["speed", "ETA", "ETD"]
VoyageCalculatorVesselStatus = Literal[
    "vessel_status_ballast",
    "vessel_status_laden_known",
    "vessel_status_laden_unknown",
]
VoyageCalculatorAvoidZone = Literal["Panama Canal", "Suez Canal"]

LatLong = Dict[str, float]

logger = get_logger(__name__)


class VoyageCalculatorRoute(TypedDict, total=False):
    """
    Route specification for batch voyage calculations.

    Required keys: type, vessel_status, origin, destination.
    Optional keys: vessel_id, vessel_class, waypoints, ETA, ETD, speed, avoid_zone, voyage_delay_factor.
    """

    type: Required[VoyageCalculatorType]
    vessel_status: Required[VoyageCalculatorVesselStatus]
    origin: Required[Union[str, LatLong]]
    destination: Required[Union[str, LatLong]]
    vessel_id: str
    vessel_class: str
    waypoints: List[str]
    ETA: str
    ETD: str
    speed: float
    avoid_zone: List[VoyageCalculatorAvoidZone]
    voyage_delay_factor: float


class VoyageCalculator(Search):
    """
    Voyage Calculator endpoint.

    Calculates voyage routes, ETAs, ETDs, or speeds between an origin and destination.
    The calculator accounts for vessel class, laden/ballast status, canal avoidance
    zones, and optional waypoints.
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

    def batch_search(
        self,
        routes: List[VoyageCalculatorRoute],
    ) -> "VoyageCalculatorBatchResult":
        """
        Calculate voyage routes for multiple origin-destination pairs in a single request.

        Accepts up to 5 route specifications and returns results with correlation fields
        (origin, destination, vessel_class, avoid_zone) alongside the calculation results.

        # Arguments
            routes: A list of route dictionaries (max 5). Each route must contain:
                - `type` (str, required): One of `'speed'`, `'ETA'`, `'ETD'`.
                - `vessel_status` (str, required): One of `'vessel_status_ballast'`,
                  `'vessel_status_laden_known'`, `'vessel_status_laden_unknown'`.
                - `origin` (str or dict, required): Geography ID string or `{"lat": float, "long": float}`.
                - `destination` (str or dict, required): Geography ID string or `{"lat": float, "long": float}`.
                - `vessel_id` (str, optional): Vessel identifier (IMO, MMSI, vessel name, or Vortexa ID).
                - `vessel_class` (str, optional): E.g. `'oil_vlcc'`, `'oil_suezmax_lr3'`.
                - `waypoints` (list, optional): List of geography IDs for intermediate waypoints.
                - `ETA` (str, optional): ISO 8601 date string. Required when type is `'speed'` or `'ETD'`.
                - `ETD` (str, optional): ISO 8601 date string. Required when type is `'speed'` or `'ETA'`.
                - `speed` (float, optional): Speed in knots. Required when type is `'ETA'` or `'ETD'`.
                - `avoid_zone` (list, optional): Zones to avoid: `'Panama Canal'`, `'Suez Canal'`.
                - `voyage_delay_factor` (float, optional): Factor between 0 and 1 for increased duration.

        # Returns
        `VoyageCalculatorBatchResult`

        # Example

        _Calculate ETA and speed for two routes in a single batch request._

        ```python
        >>> from vortexasdk import VoyageCalculator
        >>> ras_tanura = "539db1548407fd97024391d01a6a2be239b1100f070a137d54a79907d03db6c8"
        >>> rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"
        >>> routes = [
        ...     {
        ...         "type": "ETA",
        ...         "vessel_status": "vessel_status_laden_known",
        ...         "origin": ras_tanura,
        ...         "destination": rotterdam,
        ...         "vessel_class": "oil_vlcc",
        ...         "ETD": "2024-03-01T00:00:00.000Z",
        ...         "speed": 12,
        ...     },
        ...     {
        ...         "type": "speed",
        ...         "vessel_status": "vessel_status_ballast",
        ...         "origin": rotterdam,
        ...         "destination": ras_tanura,
        ...         "vessel_class": "oil_suezmax_lr3",
        ...         "ETD": "2024-03-01T00:00:00.000Z",
        ...         "ETA": "2024-04-01T00:00:00.000Z",
        ...     },
        ... ]
        >>> result = VoyageCalculator().batch_search(routes=routes)
        >>> df = result.to_df()

        ```

        Returns a DataFrame with columns including correlation and calculation fields:

        |    | origin   | destination | vessel_class     | ETA                      |   speed |   duration |
        |---:|:---------|:------------|:-----------------|:-------------------------|--------:|-----------:|
        |  0 | 539db1.. | 68faf6..    | oil_vlcc         | 2024-03-25T14:30:00.000Z |      12 |      590.5 |
        |  1 | 68faf6.. | 539db1..    | oil_suezmax_lr3  |                          |    10.5 |      744.0 |

        """
        if not routes:
            raise ValueError("batch_search requires at least 1 route")
        if len(routes) > 5:
            raise ValueError(
                f"batch_search accepts a maximum of 5 routes, got {len(routes)}"
            )

        cleaned_routes = [filter_empty_values(dict(route)) for route in routes]

        client = default_client()
        url = client._create_url(VOYAGE_CALCULATOR)

        logger.info(f"Batch payload: {cleaned_routes}")
        response = retry_post(
            url, json=cleaned_routes, headers=default_headers
        )

        result = _handle_response(response)

        return VoyageCalculatorBatchResult(
            records=result["data"],
            reference=result.get("reference", {}),
            metadata=result.get("metadata", []),
        )
