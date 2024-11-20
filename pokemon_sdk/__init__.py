from pokemon import PokemonClient
from generation import GenerationClient

class PokeSDK:
    def __init__(self):
        self.pokemon = PokemonClient()
        self.generation = GenerationClient()