import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pokemon_sdk import PokeSDK
'''
example of how to use the sdk'''
client = PokeSDK()
pokemon = client.pokemon.get_pokemon('pikachu')
print(pokemon['name'])

# print ability name
pikachu = client.pokemon.get_pokemon('pikachu')
for ability in pikachu['abilities']:
    print(ability['ability']['name'])

generation_list = client.generation.get_generations_list(limit=3,offset=0)
for gen in generation_list['results']:
    print(gen['name'])
# print name
geneartion_i = client.generation.get_generation('generation-i')
for species in geneartion_i['pokemon_species']:
    print(species['name'])
