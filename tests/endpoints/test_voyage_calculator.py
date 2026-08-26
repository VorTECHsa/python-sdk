from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import VoyageCalculator

ras_tanura = "539db1548407fd97024391d01a6a2be239b1100f070a137d54a79907d03db6c8"
rotterdam = "68faf65af1345067f11dc6723b8da32f00e304a6f33c000118fccd81947deb4e"


class TestVoyageCalculator(TestCaseUsingRealAPI):
    def test_calculate_eta(self):
        result = VoyageCalculator().search(
            type="ETA",
            vessel_status="vessel_status_laden_known",
            origin=ras_tanura,
            destination=rotterdam,
            vessel_class="oil_vlcc",
            ETD="2024-03-01T00:00:00.000Z",
            speed=12,
        )

        result_list = result.to_list()
        assert len(result_list) == 1
        assert "ETA" in result_list[0]
        assert "ETD" in result_list[0]
        assert "speed" in result_list[0]
        assert "duration" in result_list[0]

    def test_calculate_etd(self):
        result = VoyageCalculator().search(
            type="ETD",
            vessel_status="vessel_status_ballast",
            origin=ras_tanura,
            destination=rotterdam,
            vessel_class="oil_vlcc",
            ETA="2024-04-01T00:00:00.000Z",
            speed=12,
        )

        result_list = result.to_list()
        assert len(result_list) == 1
        assert "ETD" in result_list[0]

    def test_calculate_speed(self):
        result = VoyageCalculator().search(
            type="speed",
            vessel_status="vessel_status_laden_known",
            origin=ras_tanura,
            destination=rotterdam,
            vessel_class="oil_vlcc",
            ETD="2024-03-01T00:00:00.000Z",
            ETA="2024-04-01T00:00:00.000Z",
        )

        result_list = result.to_list()
        assert len(result_list) == 1
        assert "speed" in result_list[0]
        assert result_list[0]["speed"] > 0

    def test_calculate_with_latlong_origin(self):
        result = VoyageCalculator().search(
            type="ETA",
            vessel_status="vessel_status_laden_known",
            origin={"lat": 26.6, "long": 50.1},
            destination=rotterdam,
            vessel_class="oil_vlcc",
            ETD="2024-03-01T00:00:00.000Z",
            speed=12,
        )

        result_list = result.to_list()
        assert len(result_list) == 1

    def test_calculate_with_avoid_zone(self):
        result = VoyageCalculator().search(
            type="ETA",
            vessel_status="vessel_status_laden_known",
            origin=ras_tanura,
            destination=rotterdam,
            vessel_class="oil_vlcc",
            ETD="2024-03-01T00:00:00.000Z",
            speed=12,
            avoid_zone=["Suez Canal"],
        )

        result_list = result.to_list()
        assert len(result_list) == 1

    def test_to_df(self):
        result = VoyageCalculator().search(
            type="ETA",
            vessel_status="vessel_status_laden_known",
            origin=ras_tanura,
            destination=rotterdam,
            vessel_class="oil_vlcc",
            ETD="2024-03-01T00:00:00.000Z",
            speed=12,
        )

        df = result.to_df()
        assert len(df) == 1
        assert "ETA" in df.columns
        assert "ETD" in df.columns
        assert "speed" in df.columns
        assert "duration" in df.columns

    def test_to_df_with_columns(self):
        result = VoyageCalculator().search(
            type="ETA",
            vessel_status="vessel_status_laden_known",
            origin=ras_tanura,
            destination=rotterdam,
            vessel_class="oil_vlcc",
            ETD="2024-03-01T00:00:00.000Z",
            speed=12,
        )

        df = result.to_df(columns=["ETA", "speed"])
        assert len(df.columns) == 2

    def test_calculate_with_delay_factor(self):
        result = VoyageCalculator().search(
            type="ETA",
            vessel_status="vessel_status_laden_known",
            origin=ras_tanura,
            destination=rotterdam,
            vessel_class="oil_vlcc",
            ETD="2024-03-01T00:00:00.000Z",
            speed=12,
            voyage_delay_factor=0.2,
        )

        result_list = result.to_list()
        assert len(result_list) == 1
