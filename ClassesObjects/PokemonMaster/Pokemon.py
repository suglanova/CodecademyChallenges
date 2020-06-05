class Pokemon:
    
    BASE_HEALTH = 10
    BASE_DAMAGE = 3
    DAMAGE_STRING = '{this_pokemon_name} did {damage} damage to {attacked_pokemon_name}'
    CURRENT_HP_STRING = '{pokemon_name} now has {HP} HP'
    KNOCKED_OUT_STRING = '{pokemon_name} is knocked out'
    REVIVE_STRING = '{pokemon_name} is revived'
    GAIN_HEALTH_STRING = '{pokemon_name}\'s been healed, current health is {health}'
    DAMAGE_TYPE_FACTORS = { 'FireGrass': 2.0, 'WaterFire': 2.0, 'GrassWater': 2.0,
                            'FireFire': 1.0, 'GrassGrass': 1.0, 'WaterWater': 1.0,
                            'FireWater': 0.5, 'WaterGrass': 0.5, 'GrassFire': 0.5 }
    
    def __init__(self, name, pokemon_type, level):
        self.name = name
        self.level = level
        self.pok_type = pokemon_type
        self.health = self.max_health = Pokemon.BASE_HEALTH * level
        self.knocked_out = False

    def attack(self, other_pokemon):
        if self.knocked_out: return
        damage_multiplier = Pokemon.DAMAGE_TYPE_FACTORS[self.pok_type + other_pokemon.pok_type]
        damage = Pokemon.BASE_DAMAGE * self.level * damage_multiplier
        print(Pokemon.DAMAGE_STRING.format(this_pokemon_name = self.name, damage = damage, attacked_pokemon_name = other_pokemon.name))
        other_pokemon.lose_health(damage)
                
#decreased Pokemon’s health
    def lose_health(self, lost_health):
        if self.knocked_out: return
        self.health = max(0, self.health - lost_health)
        print(Pokemon.CURRENT_HP_STRING.format(pokemon_name = self.name, HP = self.health))
        if self.health == 0:
            self.knock_out()
            
#regaining health
    def gain_health(self, gained_health):
        if self.knocked_out: return
        self.health = min(self.health + gained_health, self.max_health)
        print(Pokemon.GAIN_HEALTH_STRING.format(pokemon_name = self.name, health = self.health))
        
    def knock_out(self):
        self.knocked_out = True
        print(Pokemon.KNOCKED_OUT_STRING.format(pokemon_name = self.name))
        
    def is_knocked_out(self):
        return self.knocked_out
        
# to revive a knocked out Pokémon
    def revive(self):
        self.knocked_out = False
        self.health = self.max_health
        print(Pokemon.REVIVE_STRING.format(pokemon_name = self.name))

    def __repr__(self):
        return 'Pokemon {0} ({1}) - level {2}'.format(self.name, self.pok_type, self.level)

    def get_max_health(self):
        return self.max_health
        
    def get_health(self):
        return self.health
        
    def get_name(self):
        return self.name
        