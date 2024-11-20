from pokemon import PokeSDK

client = PokeSDK()
pokemon = client.get_pokemon('pikachu')
print(pokemon['name'])

# print ability name
pikachu = client.pokemon.get_pokemon('pikachu')
for ability in pikachu['abilities']:
    print(ability['ability']['name'])

