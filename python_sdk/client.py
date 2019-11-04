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
        response = requests.post(url, data=data).json()
        return response['data']


__client__ = None


def default_client():
    global __client__

    if __client__ is None:
        __client__ = VortexaClient(api_key=os.environ["VORTEXA_API_KEY"])

    return __client__
