import requests


def send_get_request(url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response
