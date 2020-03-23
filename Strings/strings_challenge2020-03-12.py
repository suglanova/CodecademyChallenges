#1
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
    unique_count = 0
    for letter in letters:
        if letter in word:
            unique_count += 1
    return unique_count

def unique_letters1(word):
    encountered_letters = ''
    unique_count = 0
    for letter in word:
        if letter not in encountered_letters:
            unique_count += 1
            encountered_letters += letter
    return unique_count

def unique_letters2(word):
    encountered_letters = [False] * 256
    unique_count = 0
    for letter in word:
        letter_index = ord(letter)
        if not encountered_letters[letter_index]:
            unique_count += 1
            encountered_letters[letter_index] = True
    return unique_count

def unique_letters3(word):
    encountered_letters = {}
    for letter in word:
        if letter not in encountered_letters:
            encountered_letters[letter] = True
    print(encountered_letters)
    return len(encountered_letters)

print(unique_letters3("mississippi"))

#2
def count_char_x(word, x):
  print(word.count(x))
count_char_x("mississippi", "s")
count_char_x("mississippi", "m")

#3
def count_multi_char_x(word, x):
  new_word = word.split(x)
  return(len(new_word) - 1)
print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))

#4
#This function should return the substring between the first
#occurrence of start and end in word. If start or end are 
#not in word, the function should return word.
def substring_between_letters(word, start, end):
    substring = ()
    if start and end in word:
        i = word.find(start)
        j = word.find(end)
        substring = word[(i+1):j]
        return substring
    else:
            return word
print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))

