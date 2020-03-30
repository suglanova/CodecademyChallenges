#Advanced Python Code Challenges: Lists
def every_three_nums(start):
    return list(range(start, 101, 3))
print(every_three_nums(91))


def remove_middle(lst, start, end):  
    lst = lst[:start] + lst[end+1:]
    return (lst)
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


def double_index(lst, index):
  if index >= 0 and index < len(lst):
    lst[index] *= 2
  return lst

print(double_index([3, 8, -10, 12], 2))


import math

def middle_element(lst):
  length = len(lst)
  halfLength = math.floor(length / 2)
  if length % 2 == 0:
    item1 = lst[halfLength - 1]
    item2 = lst[halfLength]
    return (item1 + item2) / 2
  else:
    return lst[length // 2]
print(middle_element([5, 2, -10, -4, 4, 5]))