import requests

poke = requests.get('https://pokeapi.co/api/v2/pokemon/ditto').json()
print(poke['id'], poke['name'], poke['weight'], poke['height'])




class BasePokemon:
    def __init__(self, name)
        self.name == 'ditto'


class Pokemon(BasePokemon):
    def __init__(self, ID, name, height, weight)
        self.id == 132
        self.name == 'ditto'
        self.weight == 40
        self.height == 3
    def __str__(self, id, name, height, weight):




class PokeIp:
    def  get.pokemon(self, pokemon)
