import os

import requests

from python_sdk.constants import API_URL


class VortexaClient(object):

    def __init__(self, **kwargs):
        self.api_key = kwargs["api_key"]

    def get_reference(self, resource, id):
        url = f'{API_URL}{resource}/{id}?apikey={self.api_key}'

        response = requests.get(url).json()
        return response['data']

    def search(self, resource, **data):
        url = f'{API_URL}{resource}?apikey={self.api_key}'

        non_null_payload = {k: v for k, v in data.items() if v is not None}

        request = requests.post(url, json=non_null_payload)
        response = request.json()
        try:
            return response['data']
        except Exception as e:
            print(response)
            raise e


__client__ = None


def default_client():
    global __client__

    if __client__ is None:
        __client__ = VortexaClient(api_key=os.environ["VORTEXA_API_KEY"])

    return __client__
