A Python SDK for interacting with the [PokéAPI](https://pokeapi.co/docs/v2#pokemon), allowing developers to easily retrieve information about Pokémon, generations, and more, with built-in support for pagination.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Fetching Pokémon Data](#fetching-pokémon-data)
  - [Pagination Support](#pagination-support)
  - [Fetching Generation Data](#fetching-generation-data)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Retrieve detailed information about Pokémon.
- Access data on different Pokémon generations.
- Built-in support for pagination to navigate through large datasets.
- Easy-to-use interface with clear methods and responses.
- Asynchronous support (if applicable).

## Installation

Install the package via pip:

```bash
pip install pokemon-sdk
```

Or clone the repository:

```bash
git clone https://github.com/shirlymanor/pokemon-sdk.git
cd pokemon-sdk
pip install .
```

## Usage

### Importing the SDK

```python
from pokemon_sdk import PokeAPI
```

### Initializing the Client

```python
sdk = PokeSDK()
```

### Fetching Pokémon Data

Retrieve data for a specific Pokémon by name or ID:

```python
pokemon = sdk.get_pokemon('pikachu')
print(pokemon)
```

**Sample Output:**

```json
{
  "id": 25,
  "name": "pikachu",
  "base_experience": 112,
  "height": 4,
  "weight": 60,
  "abilities": [
    {
      "ability": {
        "name": "static",
        "url": "https://pokeapi.co/api/v2/ability/9/"
      },
      "is_hidden": false,
      "slot": 1
    },
    ...
  ],
  ...
}
```

### Pagination Support

List all Pokémon with pagination support:

```python
pokemon_list = sdk.list_pokemon(limit=20, offset=0)
for pokemon in pokemon_list['results']:
    print(pokemon['name'])
```

Navigate through pages:

```python
next_page = pokemon_list['next']
previous_page = pokemon_list['previous']
```

### Fetching Generation Data

Retrieve data for a specific generation:

```python
generation = sdk.get_generation(1)
print(generation['name'])  # Output: "generation-i"
```

List all generations:

```python
generations = sdk.list_generations()
for gen in generations['results']:
    print(gen['name'])
```

## Documentation

For documentation, I used docstrings within the code.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Developed by [Shirly Manor](https://github.com/shirlymanor). Feel free to reach out for any questions or suggestions.

- Email: shirly.manor@gmail.com
- GitHub: [@shirlymanor](https://github.com/shirlymanor)