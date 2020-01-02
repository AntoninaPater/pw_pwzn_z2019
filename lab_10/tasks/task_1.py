from typing import Dict
from urllib.parse import urljoin
import requests

API_URL = 'https://www.metaweather.com/api/'


def get_cities_woeid(query: str, timeout: float = 5.) -> Dict[str, int]:
    location_url = urljoin(API_URL, 'location/search')
    params = {"query": query}
    try:
        response = requests.get(location_url, params=params, timeout=timeout)
    except requests.exceptions.Timeout as e:
        print('timeout error', e)
        raise requests.exceptions.Timeout
    else:
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print('communication error', e)
        cities_dict = {}
        try:
            cities_dict = {doc["title"]: doc["woeid"] for doc in response.json()}
        except RuntimeError as e:
            print('parsing error', e)

    finally:
        return cities_dict


if __name__ == '__main__':
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }
    try:
        get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)
