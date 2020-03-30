def divisible_by_ten(nums):
    num_10 = []
    for num in nums:
        if num % 10 == 0:
            num_10.append(num)
    return len(num_10)
print(divisible_by_ten([20, 25, 30, 35, 40]))

def add_greetings(names):
    greetings = []
    for name in names:
        greetings.append("Hello, " + name)
    return greetings
print(add_greetings(["Owen", "Max", "Sophie"]))

def add_greetings(names):
    return ["Hello, " + names[i] for i in range(len(names))]
print(add_greetings(["Owen", "Max", "Sophie"]))

def delete_starting_evens(lst):
    i = 0
    while i % 2 == 1:
        lst = lst.append(lst.pop(i)) 
        i += 1
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))