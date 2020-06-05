import random
from Pokemon import Pokemon

class PokemonMaker:
    
    PRESETS = [('Sunflora', 'Grass'),
               ('Rapidash', 'Fire'),
               ('Krabby', 'Water'),
               ('Charmander', 'Fire'),
               ('Grovyle', 'Grass'),
               ('Wartortle', 'Water')]
    MIN_LEVEL = 1
    MAX_LEVEL = 5
    
    def make():
        preset = random.choice(PokemonMaker.PRESETS)
        level = random.randint(PokemonMaker.MIN_LEVEL, PokemonMaker.MAX_LEVEL)
        return Pokemon(preset[0], preset[1], level)