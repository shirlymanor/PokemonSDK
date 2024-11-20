import requests

BASE_URL='https://pokemonapi.co/api/v2/'

def api_get(endpoint,params=None):
    url = BASE_URL + endpoint
    try:
        response = requests.get(url,params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error {err}")
        