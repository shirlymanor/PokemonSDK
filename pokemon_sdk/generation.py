generation.py
from utils import api_get

class GenerationClient:
    def __init__(self):
        pass

    def get_generations_list(self,limit=20,offset=0):
        endpoint = 'generation'
        params = {'limit': limit,'offset':offset}
        data=api_get(endpoint, params)
        return data
    
    def get_generation(self, identifier):
        endpoint = f'generation/{identifier}'
        data = api_get(endpoint)
        return data