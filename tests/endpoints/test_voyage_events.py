from vortexasdk.api.voyages import (
    VoyageCargoEvent,
    VoyageStatusEvent,
    VoyageVesselEvent,
)


class TestVoyageEvents:
    def test_serialize_voyage_vessel_event(self):
        event = {
            "event_id": "9fd5917dc61b15d4d3aa758ac6c5f75d6ddb7238ff71440eced4a8a1141346f7",
            "start_timestamp": "2022-07-13T00:00:00.000Z",
            "end_timestamp": "2022-07-29T00:00:00.000Z",
            "event_group": "vessel",
            "event_type": "fixture",
            "activity": None,
            "odometer_start": 476662685,
            "odometer_end": 476662685,
            "location_id": "0011001100110011",
            "location_layer": ["root"],
            "location_details": [],
            "cargo_movement_id": [],
            "sts_event_counterparty_vessel_id": None,
            "waiting_event_target_geography_id": None,
            "waiting_event_target_geography_details": [],
            "fixture_event_fixing_timestamp": "2022-07-13T00:00:00.000Z",
            "tags": [],
            "probability": 1,
        }

        VoyageVesselEvent.parse_obj(event)

    def test_serialize_voyage_status_event(self):
        event = {
            "event_id": "7bbf5ab36d93c995",
            "event_group": "derived",
            "event_type": "status",
            "activity": "commitment",
            "start_timestamp": "2022-07-13T00:00:00.000Z",
            "end_timestamp": "2022-07-29T00:00:00.000Z",
            "is_open_event": False,
            "value": "committed",
            "source_event_id": "9fd5917dc61b15d4",
        }

        VoyageStatusEvent.parse_obj(event)

    def test_serialize_voyage_cargo_event(self):
        event = {
            "event_id": "283307fa86429bac",
            "start_timestamp": "2022-07-13T20:55:57.000Z",
            "end_timestamp": "2022-08-24T02:25:27.000Z",
            "event_group": "derived",
            "event_type": "cargo",
            "odometer_start": 469280788,
            "odometer_end": 483840141,
            "cargo_movement_id": "add7c1abff0d7d61",
            "cargo_origin_id": "01dac2bfd53f05ef",
            "cargo_origin_details": [
                {"layer": "berth", "id": "01dac2bfd53f05ef"},
                {
                    "id": "ac2b49d2e52fb31b",
                    "layer": "terminal",
                    "label": "Transneft - Port Primorsk (Crude) (Ex-Baltic Pipeline System)",
                },
                {
                    "id": "4534ce5267a46804",
                    "layer": "port",
                    "label": "Primorsk (Koivisto) [RU]",
                },
                {
                    "id": "b996521be9c996db",
                    "layer": "country",
                    "label": "Russia",
                },
                {
                    "id": "082a8900f310fa09",
                    "layer": "shipping_region",
                    "label": "Baltic",
                },
                {
                    "id": "b996521be9c996db",
                    "layer": "region",
                    "label": "Russia",
                },
                {
                    "id": "a7536c48714140c7",
                    "layer": "trading_block",
                    "label": "OPEC + Russia",
                },
                {
                    "id": "1c47e09ebf73cbb0",
                    "layer": "trading_block",
                    "label": "OPEC+",
                },
                {
                    "id": "ce4978a70f57396f",
                    "layer": "trading_block",
                    "label": "FSU",
                },
                {
                    "id": "956b03529510459d",
                    "layer": "trading_block",
                    "label": "Non-OPEC",
                },
                {
                    "id": "6478105a82fd32e1",
                    "layer": "trading_block",
                    "label": "West of Suez",
                },
                {
                    "id": "8caa32ab75a70f29",
                    "layer": "trading_region",
                    "label": "Baltics",
                },
                {
                    "id": "c48ec599431027d6",
                    "layer": "trading_subregion",
                    "label": "Russia Baltics",
                },
                {
                    "id": "4534ce5267a46804",
                    "layer": "storage",
                    "label": "Primorsk (Koivisto) [RU]",
                },
                {
                    "id": "5a418e0457c5c4fc",
                    "layer": "fragment",
                    "label": "Russia Baltics (Baltic) 0",
                },
            ],
            "cargo_destination_id": "470ac6a8077e1480",
            "cargo_destination_details": [
                {"layer": "berth", "id": "470ac6a8077e1480"},
                {
                    "id": "3108e11eb618dd53",
                    "layer": "terminal",
                    "label": "Jamnagar Reliance Spms",
                },
                {
                    "id": "a07eaa030bfe925e",
                    "layer": "port",
                    "label": "Sikka [IN]",
                },
                {
                    "id": "70425373a1836d6d",
                    "layer": "country",
                    "label": "India",
                },
                {
                    "id": "2f23421545dabf17",
                    "layer": "shipping_region",
                    "label": "West Coast India",
                },
                {"id": "e6955a2c59dc9083", "layer": "region", "label": "Asia"},
                {
                    "id": "956b03529510459d",
                    "layer": "trading_block",
                    "label": "Non-OPEC",
                },
                {
                    "id": "fc6694742ebce49f",
                    "layer": "trading_block",
                    "label": "East of Suez",
                },
                {
                    "id": "043b3b0acb039514",
                    "layer": "trading_region",
                    "label": "Indian Sub-Continent",
                },
                {
                    "id": "4e74c1d252e3921b",
                    "layer": "trading_subregion",
                    "label": "West Coast India",
                },
                {
                    "id": "a07eaa030bfe925e",
                    "layer": "storage",
                    "label": "Sikka [IN]",
                },
                {
                    "id": "c7feba5c88113a4c",
                    "layer": "fragment",
                    "label": "West Coast India (West Coast India) 2",
                },
            ],
            "product_id": "c8803c073c2980d9",
            "product_details": [
                {
                    "id": "a7e26956fbb91d78",
                    "layer": "category",
                    "label": "Medium-Sour",
                },
                {
                    "id": "6f11b0724c9a4e85",
                    "layer": "group_product",
                    "label": "Crude",
                },
                {
                    "id": "54af755a090118dc",
                    "layer": "group",
                    "label": "Crude/Condensates",
                },
                {"id": "c8803c073c2980d9", "layer": "grade", "label": "Urals"},
            ],
            "quantity_tonnes": 110910,
            "quantity_barrels": 796251,
            "quantity_cubic_metres": 126594,
            "tonne_miles": 871910281.4416846,
        }

        VoyageCargoEvent.parse_obj(event)
