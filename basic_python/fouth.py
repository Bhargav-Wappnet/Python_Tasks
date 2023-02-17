"""
Write a Python program to create a tuple and impliment all the tuple methods.
Write a Python script to slice a tuple.
"""

# create a tuple
my_tuple = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

# count the number of occurrences of an element in the tuple
count = my_tuple.count(8)
print("Number of occurrences of 8:", count)

# get the index of the first occurrence of an element in the tuple
index = my_tuple.index(10)
print("Index of the first occurrence of 10:", index)

# get a slice of the tuple from index 2 to index 6 (exclusive)
slice_tuple = my_tuple[2:6]
print("Slice of the tuple:", slice_tuple)

# convert the tuple to a list
my_list = list(my_tuple)
print("Tuple as a list:", my_list)

# concatenate two tuples
new_tuple = (22, 24, 26)
concatenated_tuple = my_tuple + new_tuple
print("Concatenated tuple:", concatenated_tuple)

# get the length of the tuple
length = len(my_tuple)
print("Length of the tuple:", length)
