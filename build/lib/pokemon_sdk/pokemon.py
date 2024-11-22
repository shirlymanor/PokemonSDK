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

    def get_pokemon_list(self,limit=20,offset=0):
        '''
        Get a list of pokemons with paginton support
        '''
        endpoint = 'pokemon'
        params = {'limit':limit,'offset':offset}
        data = api_get(endpoint,params)
        return data

    def get_all_pokemon(self):
        all_pokemons = []
        limit = 20
        offset = 0
        while True:
            data = self.get_all_pokemons(limit=limit,offset=offset)
            all_pokemons.extend(data['results'])
            if data['next'] is None:
                break
            offset += limit
        return all_pokemons
