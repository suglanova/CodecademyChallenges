letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {letters: points for letters, points in zip(letters, points)}
letter_to_points.update({" ": 0})
def score_word(player, word):
    score = 0
    for letter in word:
        for key, value in letter_to_points.items():
            if letter == key:
                score += value
    return score
#print(score_word("BROWNIE"))

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        b = score_word(word)
        player_points += b
        player_to_points.update({player: player_points})
#After the inner loop ends, set the current player value to be a key of
#player_to_points, with a value of player_points
print(player_to_points)


#play_word() — a function that would take in a player and a word,
#and add that word to the list of words they’ve played update_point_totals()
#— turn your nested loops into a function that you can
#call any time a word is played make your letter_to_points dictionary able
#to handle lowercase inputs as well

