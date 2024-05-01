# lib/pokedex.py

import api

class Pokedex:
    def __init__(self):
        self.pokemon_caught = []
    
    def returnCaught(self):
        return self.pokemon_caught

    def add_pokemon(self, pokemon_id):
        self.pokemon_caught.append(api.get_pokemon(pokemon_id))
        return True

    def printAll(self):
        if self.pokemon_caught:
            for p in self.pokemon_caught:
                p.printAll()

    def printNames(self):
        names = []
        for p in self.pokemon_caught:
            names.append(p.getName())

        for n in names:
            print(n)

# pokedex = Pokedex()
# pokedex.add_pokemon(150)
# pokedex.printAll()
