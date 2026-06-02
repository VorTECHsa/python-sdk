"""Type definitions for Anywhere Freight Pricing endpoints."""

from typing import List
from typing_extensions import Literal, TypedDict


# Literal type aliases for AFP parameters
AfpVesselClass = Literal[
    "oil_coastal",
    "oil_specialised",
    "oil_handysize_mr1",
    "oil_handymax_mr2",
    "oil_panamax_lr1",
    "oil_aframax_lr2",
    "oil_suezmax_lr3",
    "oil_vlcc",
]

AfpProduct = Literal["clean", "dirty", "crude"]

AfpUnit = Literal["usd_per_tonne", "usd_per_barrel"]

AfpFrequency = Literal["day", "week", "doe_week", "month", "quarter", "year"]

AfpAvoidZone = Literal["Panama Canal", "Suez Canal"]

AfpExplanationFrequency = Literal["day", "week", "month", "month_fixed"]

AfpForecastVesselClass = Literal[
    "oil_coastal",
    "oil_specialised",
    "oil_handysize_mr1",
    "oil_handymax_mr2",
    "oil_panamax_lr1",
    "oil_aframax_lr2",
    "oil_suezmax_lr3",
    "oil_vlcc",
    "lpg_sgc",
    "lpg_mgc",
    "lpg_lgc",
    "lpg_vlgc_vlec",
    "lng_small_scale_lng",
    "lng_mid_scale_lng",
    "lng_conventional_lng",
    "lng_q_fleet",
]


class AfpRoute(TypedDict, total=False):
    """
    Route specification for AFP POST endpoints.

    Required keys: origin_port, destination_port, product, vessel_class.
    Optional keys: avoid_zone, suggested_tonnage.
    """

    origin_port: str
    destination_port: str
    product: AfpProduct
    vessel_class: AfpVesselClass
    avoid_zone: List[AfpAvoidZone]
    suggested_tonnage: float


class AfpRouteRequired(TypedDict):
    """Required fields for AfpRoute."""

    origin_port: str
    destination_port: str
    product: AfpProduct
    vessel_class: AfpVesselClass


class AfpForecastRoute(TypedDict, total=False):
    """
    Route specification for AFP Forecast endpoints.

    Required keys: origin_port, destination_port, product, vessel_class.
    Optional keys: avoid_zone, suggested_tonnage.
    """

    origin_port: str
    destination_port: str
    product: AfpProduct
    vessel_class: AfpForecastVesselClass
    avoid_zone: List[AfpAvoidZone]
    suggested_tonnage: float
