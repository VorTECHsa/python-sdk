from vortexasdk.endpoints.anywhere_freight_pricing_avoid_zone import (
    AFP_AVOID_ZONE_IDS,
    avoid_zone_ids,
    routes_with_avoid_zone_ids,
)


class TestAvoidZoneIds:
    def test_converts_names_to_ids(self):
        assert avoid_zone_ids(["Panama Canal", "Suez Canal"]) == [
            AFP_AVOID_ZONE_IDS["Panama Canal"],
            AFP_AVOID_ZONE_IDS["Suez Canal"],
        ]

    def test_keeps_ids_and_none(self):
        assert avoid_zone_ids(["abc"]) == ["abc"]
        assert avoid_zone_ids(None) is None

    def test_converts_the_avoid_zone_of_each_route(self):
        routes = [
            {"origin": "a", "avoid_zone": ["Suez Canal"]},
            {"origin": "b"},
        ]

        assert routes_with_avoid_zone_ids(routes) == [
            {"origin": "a", "avoid_zone": [AFP_AVOID_ZONE_IDS["Suez Canal"]]},
            {"origin": "b"},
        ]
        assert routes[0]["avoid_zone"] == ["Suez Canal"]
