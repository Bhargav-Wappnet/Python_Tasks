"""
Write a Python program to get the difference between the two lists.
Write a Python program access the index of a list.
Write a Python program to convert a list of characters into a string.
Write a Python program to find the index of an item in a specified list.
Write a Python program to flatten a shallow list.
Write a Python program to select an item randomly from a list.

"""
import random


# For finding the diff between two list.
lst1 = [1, 2, 4, 5, 8]
lst2 = [3, 9, 7, 6, 8]

difference = list(set(lst1) - set(lst2))
print(f'difference is :{difference}')


# access the index of the list.
for i in range(len(lst1)):
    print(f"The index of {lst1[i]} is {i}")

# list charcter to string.
lst3 = ['B', 'h', 'a', 'r', 'g', 'a', 'v']
str_value = ''.join(lst3)
print(str_value)

# index of specific item.
index = lst3.index('B')
print(f'B index is {index}')

# flatten a shallow list.
shallow_list = [[1, 2], [3, 4], [5, 6]]
flat_list = []
for item in shallow_list:
    for val in item:
        flat_list.append(val)
print(flat_list)

# Select random item from list.
rand_item = random.choice(lst3)
print(rand_item)
