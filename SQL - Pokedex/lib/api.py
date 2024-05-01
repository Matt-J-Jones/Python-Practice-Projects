import requests, json
from requests.exceptions import Timeout
import pokemon

def get_pokemon(pokemon_id, timeout = 5):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/', timeout=timeout)
        response.raise_for_status()
        data = response.json()
        new_pokemon = pokemon.Pokemon(
            data['id'],
            data['name'],
            data['height'],
            data['weight'],
            data['types'],
            data['sprites']['other']['dream_world']['front_default'])
        return new_pokemon
    except Timeout:
        return "The request timed out"

# def main():
#     returned_pokemon = get_pokemon(150, timeout=10)
#     if returned_pokemon:
#         returned_pokemon.printAll()
#         print(returned_pokemon.getPic())

# if __name__ == "__main__":
#     main()
