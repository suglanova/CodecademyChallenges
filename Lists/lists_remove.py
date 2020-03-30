def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return lst.count(item) > n
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


def more_than_n(lst, item, n):
  count = 0
  for i in lst:
    if i == item:
	    count = count + 1
  return count > n
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))



#If there are an odd number of elements in lst, the function should return the middle element.
#If there are an even number of elements, the function should return the average of the middle two elements.

import math

def middle_element(lst):
  length = len(lst)
  halfLength = math.floor(length / 2)
  if length % 2 == 0:
    item1 = lst[halfLength - 1]
    item2 = lst[halfLength]
    return (item1 + item2) / 2
  else:
    return lst[length / 2]
print(middle_element([5, 2, -10, -4, 4, 5]))


def middle_element(lst):
    length = len(lst)
    halfLength = length // 2
    if length % 2 == 0:
        item1 = lst[halfLength - 1]
        item2 = lst[halfLength]
        return (item1 + item2) / 2
    else:
        return lst[length / 2]
print(middle_element([5, 2, -10, -4, 4, 5]))


def append_sum(lst):
  length = len(lst)
  for i in range(3):
    sum = lst[-2] + lst[-1]
    lst.append(sum)
  return lst
print(append_sum([1, 1, 2]))


def append_sum(lst):
    i = 0
    while i < 3:
        lst.append(lst[-2] + lst[-1])
        i += 1
    return(lst)
print(append_sum([1, 1, 2]))


def every_three_nums(start):
    return list(range(start, 101, 3))
print(every_three_nums(91))

#The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed
def remove_middle(lst, start, end):  
    lst = lst[:start] + lst[end+1:]
    return (lst)
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
	