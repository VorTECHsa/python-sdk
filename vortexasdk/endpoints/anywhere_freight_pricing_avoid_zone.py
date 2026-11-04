"""Conversion of AFP avoid zone names to the IDs that the AFP API takes."""

from typing import Any, Dict, List, Optional, Sequence

# IDs of the routing zones that the AFP API can avoid
AFP_AVOID_ZONE_IDS: Dict[str, str] = {
    "Panama Canal": "bd1594fc2d1404fa06f9406139c7620bb4d9f495bc33bb44cc153a327b0b40d8",
    "Suez Canal": "f5634597081459985237dc54fcbe518d4b0a4f4af618b7719abda334b95538d1",
}


def avoid_zone_ids(zones: Optional[Sequence[str]]) -> Optional[List[str]]:
    """Convert zone names to zone IDs. A value that is not a known name is kept as it is."""
    if zones is None:
        return None
    return [AFP_AVOID_ZONE_IDS.get(zone, zone) for zone in zones]


def routes_with_avoid_zone_ids(routes: Sequence[Any]) -> List[Dict[str, Any]]:
    """Convert the `avoid_zone` of each route to zone IDs."""
    converted: List[Dict[str, Any]] = []
    for route in routes:
        new_route: Dict[str, Any] = dict(route)
        if "avoid_zone" in new_route:
            new_route["avoid_zone"] = avoid_zone_ids(new_route["avoid_zone"])
        converted.append(new_route)
    return converted
