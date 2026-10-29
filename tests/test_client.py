from unittest import TestCase

from vortexasdk.client import (
    VortexaClient,
    verify_api_key_format,
    _handle_response,
)

from requests.models import Response


class TestClient(TestCase):
    def test__cleanse_payload(self):
        payload = {"a": [], "b": None, "d": 3, "c": [1, 2]}

        cleansed = VortexaClient._cleanse_payload(payload)

        assert cleansed == {"c": [1, 2], "d": 3}

    def test__cleanse_payload_removes_exclude_empties(self):
        payload = {
            "layer1_k1": [],
            "layer1_k2": None,
            "layer1_k3": 3,
            "exclude": {"layer2_k1": [], "layer2_k2": [1]},
        }

        cleansed = VortexaClient._cleanse_payload(payload)

        assert cleansed == {"layer1_k3": 3, "exclude": {"layer2_k2": [1]}}

    def test_raised_error_for_invalid_uuid(self):
        self.assertRaises(
            ValueError, lambda: verify_api_key_format("invalid_key")
        )

    def test_accepts_valid_uuid(self):
        sample_valid_key = "123e4567-e89b-12d3-a456-426614174000"
        verify_api_key_format(sample_valid_key)

    def test_raised_error_for_response_error(self):
        badResponse = Response()
        badResponse.code = "bad request"
        badResponse.reason = "bad request"
        badResponse.status_code = 400
        self.assertRaises(ValueError, lambda: _handle_response(badResponse))

    def test_401_error_tells_user_to_check_api_key(self):
        response = Response()
        response.reason = "Unauthorized"
        response.status_code = 401

        with self.assertRaises(ValueError) as context:
            _handle_response(response)

        assert "[401 Unauthorized]" in str(context.exception)
        assert "API key" in str(context.exception)

    def test_403_error_does_not_mention_api_key(self):
        response = Response()
        response.reason = "Forbidden"
        response.status_code = 403

        with self.assertRaises(ValueError) as context:
            _handle_response(response)

        assert "API key" not in str(context.exception)
