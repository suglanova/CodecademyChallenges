def delete_starting_evens(lst):
    while lst[0] % 2 == 0:
        lst = lst[1:]
    return lst           
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))


def delete_starting_evens(lst):
    while len(lst) > 0 and lst[0] % 2 == 0:
        lst.pop(0)
    return lst           
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))



def delete_starting_evens(lst):
    i = 0
    while lst[0] % 2 == 0:
        lst = lst[1:]
    i += 1
    return lst
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))


#The function should create a new empty list and add every element from lst
#that has an odd index.
#The function should then return this new list.
def odd_indices(lst):
    new_lst = []
    for i in range(len(lst)):
        if i % 2 == 1:
            new_lst.append(lst[i])
    return new_lst
print(odd_indices([4, 3, 7, 10, 11, -2]))


#comprehention
def odd_indices(lst):
    result = [lst[i] for i in range(len(lst)) if i % 2 == 1]
    return(result)
print(odd_indices([4, 3, 7, 10, 11, -2]))


def exponents(bases, powers):
    new_lst = []
    for m in bases:
        for n in powers:
            new_lst.append(m**n)
    return new_lst
print(exponents([2, 3, 4], [1, 2, 3]))


# function should return the list whose elements sum to the greater number.
#If the sum of the elements of each list are equal, return lst1.
def larger_sum(lst1, lst2):
  if sum(lst1) >= sum(lst2):
    return lst1
  else:
    return lst2
print(larger_sum([1, 9, 5], [2, 3, 7]))



#sum the elements of the list until the sum is greater than 9000.
#When this happens, the function should return the sum.
#If the sum of all of the elements is never greater than 9000,
#the function should return total sum of all the elements.
#If the list is empty, the function should return 0.
def func(lst):
    sum = 0
    for x in lst:
        sum += x
        if sum > 9000:
            break
    return sum
print(func([8000, 900, 120, 5000]))


#The function should return the largest number in nums
def max_num(nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max
print(max_num([50, -10, 0, 75, 20]))



def same_values(lst1, lst2):
    lst3 = []
    for i in range(len(lst1)):
            if lst1[i] == lst2[i]:
                lst3.append(i)
    return lst3
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))



def reversed_list(lst1, lst2):
    l = len(lst1)
    i = 0
    j = l - 1
    while i < l:
        if lst1[i] != lst2[j]:
            return False
        i += 1
        j -= 1
    return True
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))