from .utils import api_get

class PokemonClient:
    def __init__(self):
        pass

    def get_pokemon(self,):
       '''
       Get the details of the pokemon by ID or Name'''
       endpoint='pokemon'
       data = api_get(endpoint)
       return data