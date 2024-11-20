from .utils import api_get

class PokemonClient:
    def __init__(self):
        pass

    def get_pokemon(self,):
       endpoint='pokemon'
       data = api_get(endpoint)
       return data