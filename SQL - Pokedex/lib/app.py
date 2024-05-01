from database_connection import DatabaseConnection
from pokedex import Pokedex
import random

# Connect to the database
connection = DatabaseConnection()
connection.connect()

pokedex = Pokedex()

# def catchPokemon(id_n):
#     pokedex.add_pokemon(id_n)

# x = 150

# for i in range(1, x+1):
#     catchPokemon(i)

# pokemonInComputer = pokedex.returnCaught()

# for pokemon in pokemonInComputer:
#     sql = f"INSERT INTO pokemon (name, height, weight, type, pic) VALUES ('{pokemon.getName()}', '{pokemon.getHeight()}', '{pokemon.getWeight()}', '{pokemon.getTypes()}', '{pokemon.getPic()}');"
#     connection.execute(sql)
# print("Pokemon added to the database!")

random_number = random.randint(1, 150)
sql = f"SELECT * FROM pokemon WHERE id = {random_number};"
randomPokemon = connection.execute(sql)
print(randomPokemon[0]['name'].capitalize())