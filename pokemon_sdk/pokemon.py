from .utils import api_get

class PokemonClient:
    def __init__(self):
        pass

    def get_pokemon(self,identifier):
       '''
       Get the details of the pokemon by ID or Name'''
       endpoint=f'pokemon/{identifier}'
       data = api_get(endpoint)
       return data