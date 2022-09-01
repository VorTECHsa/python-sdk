from datetime import datetime
from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.api.freight_pricing import FreightPricing
from vortexasdk.endpoints.freight_pricing_result import FreightPricingResult
from vortexasdk.endpoints.freight_pricing_search import FreightPricingSearch

day = datetime(2021, 11, 1)


class TestFreightPricingReal(TestCaseUsingRealAPI):
    def test_deserialisation(self):
        dictionary = {
            "id": "abc123",
            "short_code": "a_route_code",
            "record_date": "2022-08-19T00:00:00.000Z",
            "rate": 100,
            "rate_precision": 2,
            "rate_unit": "WS",
            "cost": 100,
            "cost_precision": 2,
            "cost_unit": "$/ton",
            "tce": 100,
            "tce_precision": 0,
            "tce_unit": "$/day",
            "predictions": [
                {
                    "prediction": "firm",
                    "prediction_type": "outlook_4d",
                    "rating": "low",
                },
                {
                    "prediction": "firm",
                    "prediction_type": "outlook_2d",
                    "rating": "low",
                },
                {
                    "prediction": "soft",
                    "prediction_type": "outlook_1d",
                    "rating": "medium",
                },
            ],
        }

        p = FreightPricing(**dictionary)

        assert p.short_code == "a_route_code"

    def test_deserialisation_with_missing_keys(self):
        dictionary = {
            "id": "abc123",
            "short_code": "a_route_code",
            "record_date": "2022-08-19T00:00:00.000Z",
            "rate": 100,
            "tce_unit": "$/day",
            "predictions": [
                {
                    "prediction": "firm",
                    "rating": "low",
                },
                {
                    "prediction": "firm",
                    "prediction_type": "outlook_2d",
                },
                {
                    "prediction_type": "outlook_1d",
                    "rating": "medium",
                },
            ],
        }

        p = FreightPricing(**dictionary)

        assert p.id == "abc123"

    def test_default_search(self):
        results = FreightPricingSearch().search(routes=["TD3C"]).to_list()
        assert len(results) > 10

    def test_default_search_to_list(self):
        results_list = FreightPricingSearch().search(routes=["TD3C"]).to_list()
        assert results_list[0].short_code == "TD3C"

    def test_days(self):
        results = FreightPricingSearch().search(routes=["TD3C"], days=[day])
        assert len(results) == 1

    def test_route_as_string(self):
        results = FreightPricingSearch().search(routes="TD3C", days=[day])
        assert len(results) == 1

    def test_multiple_days(self):
        day2 = datetime(2021, 11, 2)
        results = FreightPricingSearch().search(
            routes=["TD3C"], days=[day, day2]
        )
        assert len(results) == 2

    def test_df(self):
        df = (
            FreightPricingSearch()
            .search(routes=["TD3C"])
            .to_df(
                columns=[
                    "short_code",
                    "rate",
                    "rate_unit",
                    "prediction.outlook_1d.prediction",
                ]
            )
            .head(2)
        )
        assert len(df) == 2
        assert list(df.columns) == [
            "short_code",
            "rate",
            "rate_unit",
            "prediction.outlook_1d.prediction",
        ]

    def test_format_prediction_outlooks(self):
        input = [
            {
                "predictions": [
                    {
                        "prediction_type": "outlook_1d",
                        "prediction": "firm",
                        "rating": "medium",
                    },
                    {
                        "prediction_type": "outlook_4d",
                        "prediction": "firm",
                        "rating": "low",
                    },
                ]
            }
        ]

        expected_result = [
            {
                "predictions": {
                    "outlook_1d": {
                        "prediction": "firm",
                        "rating": "medium",
                        "prediction_type": "outlook_1d",
                    },
                    "outlook_4d": {
                        "prediction": "firm",
                        "rating": "low",
                        "prediction_type": "outlook_4d",
                    },
                }
            }
        ]

        result = FreightPricingResult.format_prediction_outlooks(input)

        assert result == expected_result
