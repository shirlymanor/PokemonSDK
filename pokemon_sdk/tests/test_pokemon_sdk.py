import unittest
import os
import sys
# Add the project root to sys.path
#sys.path.append(os.path.dirname(__file__) + '/..')

# Add the project root to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

print(f"Current working directory: {os.getcwd()}")
print(f"Project root added to sys.path: {project_root}")
print("Python path:")
for path in sys.path:
    print(path)

try:
    from pokemon_sdk import PokeSDK
    print("Successfully imported PokeSDK")
except ImportError as e:
    print(f"Error importing: {e}")
    import traceback
    traceback.print_exc()


from pokemon_sdk import PokeSDK



class TestPokemonSDK(unittest.TestCase):
    def setUp(self):
        self.sdk = PokeSDK()
    
    def test_get_pokemon_by_name(self):
        pokemon = self.sdk.pokemon.get_pokemon("pikachu")
        self.assertEqual(pokemon['name'], "pikachu")

    def test_get_generation(self):
        generation = self.sdk.generation.get_generation("generation-i")
        self.assertEqual(generation['name'], "generation-i")

    def test_get_all_generations(self):
        generations = self.sdk.generation.get_generations_list()
        self.assertGreater(len(generations['results']), 0)


if __name__ == '__main__':
    unittest.main()
