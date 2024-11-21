import requests
from urllib3.exceptions import InsecureRequestWarning
# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

BASE_URL = 'https://pokeapi.co/api/v2/'

def api_get(endpoint, params=None):
    url = BASE_URL + endpoint
    try:
        response = requests.get(url, params=params, verify=False)  # Disable SSL verification
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        raise
