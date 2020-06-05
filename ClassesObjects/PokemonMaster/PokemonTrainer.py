import random
from PokemonMaker import PokemonMaker

class PokemonTrainer:
    POKEMONS_AMOUNT = 6
    HEALING_POTIONS_AMOUNT = 10
    REVIVE_POTIONS_AMOUNT = 5
    CRITICAL_HP_PERCENT = 0.2  #20%
    HEALING_AMOUNT_PERCENT = 0.1
    HEAL_DECISION_CHANCE = 0.5
    REVIVE_DECISION_CHANCE = 0.5
    POKEMON_SWITCH_DECISION_CHANCE = 0.2
    
    def __init__(self, name):
        self.name = name
        self.healing_potions = PokemonTrainer.HEALING_POTIONS_AMOUNT
        self.revive_potions = PokemonTrainer.REVIVE_POTIONS_AMOUNT
        self.pokemons_list = []
        
        for i in range(PokemonTrainer.POKEMONS_AMOUNT):
            self.pokemons_list.append(PokemonMaker.make())
            
        self.choose_random_pokemon()
        
    def get_name(self): # it's "getter"
        return self.name
        
    def decide(self): #main logic
        print(self.name + ' plans his actions...')
        
        p = self.current_pokemon
            
        if p.is_knocked_out():
            if self.revive_potions > 0 and random.random() <= PokemonTrainer.REVIVE_DECISION_CHANCE:
                print('50%-chance revive!')
                p.revive()
                self.revive_potions -= 1
                self.current_pokemon = p #save chosen as current
            else:
                print('50%-chance to switch but revive')
                self.choose_random_pokemon()
                
        elif p.get_health() <= p.get_max_health() * PokemonTrainer.CRITICAL_HP_PERCENT:
            if self.healing_potions > 0 and random.random() <= PokemonTrainer.HEAL_DECISION_CHANCE:
                print('50%-chance heal!')
                p.gain_health(p.get_max_health() * PokemonTrainer.HEALING_AMOUNT_PERCENT)
                self.healing_potions -= 1
            else:
                print('50%-chance to switch but heal')
                self.choose_random_pokemon()
                
        elif random.random() <= PokemonTrainer.POKEMON_SWITCH_DECISION_CHANCE:
            print('Chance to try a new one!')
            self.choose_random_pokemon()
           
    def choose_random_pokemon(self):
        alive_pokemons = [] #local variable useful only for this method
        for pokemon in self.pokemons_list:
            if not pokemon.is_knocked_out():
                alive_pokemons.append(pokemon)
        
        if len(alive_pokemons) > 0:
            p = random.choice(alive_pokemons)
            if p.get_health() <= p.get_max_health() * PokemonTrainer.CRITICAL_HP_PERCENT and \
               self.healing_potions > 0:
                p.gain_health(p.get_max_health() * PokemonTrainer.HEALING_AMOUNT_PERCENT)
                self.healing_potions -= 1
                
            self.current_pokemon = p #save chosen as current
            print(self.get_name() + ' chose new current pokemon from alive', len(alive_pokemons))
        else:
            if self.revive_potions > 0:
                p = random.choice(self.pokemons_list)
                p.revive()
                self.revive_potions -= 1
                self.current_pokemon = p #save chosen as current
            else:
                print('No alive pokemons!')
                self.current_pokemon = None
                
    def can_fight(self):
        return self.current_pokemon != None
        
    def get_current_pokemon(self):
        return self.current_pokemon
    