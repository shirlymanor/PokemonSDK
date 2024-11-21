from pokemon_sdk import PokeSDK
'''
example of how to use the sdk'''
client = PokeSDK()
pokemon = client.get_pokemon('pikachu')
print(pokemon['name'])

# print ability name
pikachu = client.pokemon.get_pokemon('pikachu')
for ability in pikachu['abilities']:
    print(ability['ability']['name'])

generation_list = client.generation.get_generations_list(limit=3,offset=0)
for gen in generation_list['reslts']:
    print(gen['name'])

geneartion_i = client.generation.get_generation('generation-i')
for species in geneartion_i['species']:
    print(species['name'])