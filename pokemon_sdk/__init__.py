from pokemon import PokemonClient
from generation import GenerationClient

class PokeSDK:
    '''
    PokeSDK is the main class for the PokeAPI SDK.
    '''
    def __init__(self):
        self.pokemon = PokemonClient()
        self.generation = GenerationClient()