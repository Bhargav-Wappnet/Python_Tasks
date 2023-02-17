"""
Write a Python script for below List Functions.
1) clear 2) index 3) count 4) sort 5) reverse 6) copy
"""
# initialize a list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(my_list)

# remove all elements from the list
my_list.clear()
print(f'\nclear function result is :\n{my_list}')

# initialize a new list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# get the index of the first occurrence of an element
index = my_list.index(5)
print(f'\nindex function result is :\n{index}')

# get the number of occurrences of an element
count = my_list.count(5)
print(f'\ncount function result is :\n{count}')

# sort the elements of the list in ascending order
my_list.sort()
print(f'\nsort function result is :\n{my_list}')

# reverse the order of the elements in the list
my_list.reverse()
print(f'\nreverse function result is :\n{my_list}')

# create a shallow copy of the list
my_list_copy = my_list.copy()
print(f'\ncopy of mylist :\n{my_list_copy}')

# get a slice of the list from index 2 to index 7 (exclusive)
slice_list = my_list[2:7]
print(f'\nslice list result :\n{slice_list}\n')
