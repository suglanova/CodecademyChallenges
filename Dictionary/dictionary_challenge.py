def sum_even_keys(my_dictionary):
    summa = 0
    for key, value in my_dictionary.items():
        if int(key) % 2 == 0:
            summa += value
    return summa  
#print(sum_even_keys({1:5, 2:2, 3:3}))

#print(sum_even_keys({10:1, 100:2, 1000:3}))

def add_ten(my_dictionary):
    for key, value in my_dictionary.items():
        value +=10
        my_dictionary.update({key: value})
    return my_dictionary
#print(add_ten({1:5, 2:2, 3:3}))
#print(add_ten({10:1, 100:2, 1000:3}))

def values_that_are_keys(my_dictionary):
    values_list = []
    for value in my_dictionary.values():
        if value in list(my_dictionary):
            values_list.append(value)
    return values_list
#print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
#print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))

def max_key(my_dictionary):
    max_value = max(my_dictionary.values())
    for key, value in my_dictionary.items():
        if value == max_value:
            return key
#print(max_key({1:100, 2:1, 3:4, 4:10}))
#print(max_key({"a":100, "b":10, "c":1000}))

#return a dictionary of key/value pairs where every key is
#a word in words and every value is the length of that word.
def word_length_dictionary(words):
    new_dic = {}
    for word in words:
        new_dic.update({word: len(word)})
    return new_dic
#print(word_length_dictionary(["apple", "dog", "cat"]))
#print(word_length_dictionary(["a", ""]))

def frequency_dictionary(words):
    return {word: words.count(word) for word in words}
#print(frequency_dictionary(["apple", "apple", "cat", 1]))

#dictionary where each key is the first letter of a last name, and the value is
#the number of people whose last name begins with that letter.
#names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
def count_first_letter(names):
    letters = {}
    for last in list(names):
        if last[0] not in letters:
            letters.update({last[0]: len(names[last])})
        else:
            letters[last[0]]+= len(names[last])
    return letters
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
    

        