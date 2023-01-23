"""Vortexa endpoints."""
from vortexasdk.endpoints.asset_tanks import AssetTanks
from vortexasdk.endpoints.attributes import Attributes
from vortexasdk.endpoints.cargo_movements import CargoMovements
from vortexasdk.endpoints.cargo_timeseries import CargoTimeSeries
from vortexasdk.endpoints.vessel_movements import VesselMovements
from vortexasdk.endpoints.corporations import Corporations
from vortexasdk.endpoints.geographies import Geographies
from vortexasdk.endpoints.products import Products
from vortexasdk.endpoints.vessels import Vessels
from vortexasdk.endpoints.storage_terminals import StorageTerminals
from vortexasdk.endpoints.tonne_miles_breakdown import TonneMilesBreakdown
from vortexasdk.endpoints.vessel_availability_breakdown import (
    VesselAvailabilityBreakdown,
)
from vortexasdk.endpoints.vessel_availability_timeseries import (
    VesselAvailabilityTimeseries,
)
from vortexasdk.endpoints.vessel_availability_search import (
    VesselAvailabilitySearch,
)
from vortexasdk.endpoints.fleet_utilisation_avg_distance_timeseries import (
    FleetUtilisationAvgDistanceTimeseries,
)
from vortexasdk.endpoints.fleet_utilisation_capacity_timeseries import (
    FleetUtilisationCapacityTimeseries,
)
from vortexasdk.endpoints.fleet_utilisation_quantity_timeseries import (
    FleetUtilisationQuantityTimeseries,
)
from vortexasdk.endpoints.fleet_utilisation_speed_breakdown import (
    FleetUtilisationSpeedBreakdown,
)
from vortexasdk.endpoints.fleet_utilisation_origin_breakdown import (
    FleetUtilisationOriginBreakdown,
)
from vortexasdk.endpoints.fleet_utilisation_destination_breakdown import (
    FleetUtilisationDestinationBreakdown,
)
from vortexasdk.endpoints.fleet_utilisation_timeseries import (
    FleetUtilisationTimeseries,
)
from vortexasdk.endpoints.eia_forecasts import EIAForecasts
from vortexasdk.endpoints.origin_breakdown import OriginBreakdown
from vortexasdk.endpoints.destination_breakdown import DestinationBreakdown
from vortexasdk.endpoints.movement_status_breakdown import (
    MovementStatusBreakdown,
)
from vortexasdk.endpoints.vessel_class_breakdown import VesselClassBreakdown
from vortexasdk.endpoints.product_breakdown import ProductBreakdown
from vortexasdk.endpoints.parent_product_breakdown import (
    ParentProductBreakdown,
)
from vortexasdk.endpoints.onshore_inventories_timeseries import (
    OnshoreInventoriesTimeseries,
)
from vortexasdk.endpoints.onshore_inventories_search import (
    OnshoreInventoriesSearch,
)
from vortexasdk.endpoints.freight_pricing_search import FreightPricingSearch
from vortexasdk.endpoints.freight_pricing_timeseries import (
    FreightPricingTimeseries,
)
from vortexasdk.endpoints.voyages_timeseries import VoyagesTimeseries
from vortexasdk.endpoints.voyages_congestion_breakdown import (
    VoyagesCongestionBreakdown,
)
from vortexasdk.endpoints.voyages_top_hits import VoyagesTopHits
from vortexasdk.endpoints.voyages_search_enriched import VoyagesSearchEnriched
