def reverse(lst):
    i = 0
    j = len(lst) - 1
    while i < j:
        t = lst[i]
        lst[i] = lst[j]
        lst[j] = t
        i += 1
        j -= 1

def reversed_list(lst1, lst2):
    reverse(lst2)
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))