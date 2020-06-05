from PokemonTrainer import PokemonTrainer
       
trainer_1 = PokemonTrainer('Sveta')
trainer_2 = PokemonTrainer('Dima')

i = 1
while True:
    print('=====\nRound #' + str(i) + '\n=====')
    i += 1
    
    trainer_1.decide()
    if not trainer_1.can_fight():
        print(trainer_2.get_name() + ' is the winner!')
        break
    print(trainer_1.get_name() + ' attacks:')
    trainer_1.get_current_pokemon().attack(trainer_2.get_current_pokemon())
    
    trainer_2.decide()
    if not trainer_2.can_fight():
        print(trainer_1.get_name() + ' is the winner!')
        break
    print(trainer_2.get_name() + ' attacks:')
    trainer_2.get_current_pokemon().attack(trainer_1.get_current_pokemon())
    