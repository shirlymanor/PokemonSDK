import requests
'''
Create utils.py module to handle API requests and responses.
'''

BASE_URL = 'https://pokeapi.co/api/v2/'

def api_get(endpoint, params=None):
    url = BASE_URL + endpoint
    try:
        response = requests.get(url, params=params)  
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        raise
