gamers = []
def add_gamer(gamer, gamers_list):
    if "name" and "availability" in gamer.keys():
        gamers_list.append(gamer)
    return gamers_list

kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
def build_daily_frequency_table():
    ft = {}
    for day in week_days:
        ft[day] = 0
    return ft

count_availability = build_daily_frequency_table()
print(count_availability)

#The function should iterate through each gamer in gamers_list and iterate through each day
#in the gamer's availability. For each day in the gamer's availability, add one
#to that date on the frequency table.
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            available_frequency[day] += 1
calculate_availability(gamers, count_availability)
print(count_availability)

def find_best_night(availability_table):
    max = 0
    maxDay = ''
    for day in availability_table:
        availability = availability_table[day]
        if availability > max:
            max = availability
            maxDay = day
    return maxDay
game_night = find_best_night(count_availability)
print(game_night)

def available_on_night(gamers_list, day):
    people_list = []
    for gamer in gamers_list:
        if day in gamer["availability"]:
            people_list.append(gamer["name"]) 
    return people_list
attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)

form_email = "Dear {name}, come on {day_of_week} to play \"{game}\""

def send_email(gamers_who_can_attend, day, game):
    for person in gamers_who_can_attend:
        print(form_email.format(name = person, day_of_week = day, game = game))
send_email(attending_game_night, game_night, "Abruptly Goblins!")
     
unable_to_attend_best_night = []
for user in gamers:
    if user["name"] not in attending_game_night:
        unable_to_attend_best_night.append(user)

second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)
print(second_night_availability)

available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")   
