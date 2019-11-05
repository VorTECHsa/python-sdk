import os

import requests
from requests import Response

from python_sdk.constants import API_URL


class VortexaClient:
    """
    The API client responsible for calling Vortexa's Public API
    """

    _DEFAULT_PAGE_LOAD_SIZE = 10000

    def __init__(self, **kwargs):
        self.api_key = kwargs["api_key"]

    def get_reference(self, resource, id):
        url = f'{API_URL}{resource}/{id}?apikey={self.api_key}'

        response = requests.get(url)

        return self._handle_response(response)['data']

    def search(self, resource, **data):
        url = f'{API_URL}{resource}?apikey={self.api_key}'
        payload = {k: v for k, v in data.items() if v is not None}

        offset = 0
        more = True
        responses = []

        while more:
            response = self._sent_post_request(url, payload, offset)
            offset += payload.get(['size'], self._DEFAULT_PAGE_LOAD_SIZE)
            responses += response['data']
            print(f'Adding {len(response["data"])} records to responses. len(all_responses): {len(responses)}')

            if offset > response['total']:
                print(f'Finishing. offset: {offset}, total_records: {response["total"]}')
                more = False

        return responses

    def _sent_post_request(self, url, payload, offset):
        print(f'Sending post request, offset: {offset}')
        payload["offset"] = offset
        payload["cm_offset"] = offset

        response = requests.post(url, json=payload)

        return self._handle_response(response)

    @staticmethod
    def _handle_response(response: Response):
        if response.ok:
            return response.json()
        else:
            print(response.reason)
            print(response.json())
            raise Exception(response)


__client__ = None


def default_client():
    global __client__

    if __client__ is None:
        __client__ = VortexaClient(api_key=os.environ["VORTEXA_API_KEY"])

    return __client__
