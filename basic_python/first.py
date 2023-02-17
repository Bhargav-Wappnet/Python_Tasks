"""
Write a Python script below List Functions.
1) append 2) extend 3) insert 4) remove 5) pop
"""


# Adds an element to the end of the list.
def append_function(my_list, element):
    my_list.append(element)


# Adds elements from another list to the end of the list.
def extend_function(my_list, *elements):
    my_list.extend(elements)


# Inserts an element at a specified index in the list.
def insert_function(my_list, index, element):
    my_list.insert(index, element)


# Removes the first occurrence of an element from the list.
def remove_function(my_list, element):
    my_list.remove(element)


# Removes and returns the element at a specified index in the list.
def pop_function(my_list, index=None):
    return my_list.pop(index)


# Dictionary that maps function names to their corresponding function objects
function_dict = {
    "append": append_function,
    "extend": extend_function,
    "insert": insert_function,
    "remove": remove_function,
    "pop": pop_function,
}

# Making an list
list1 = []
total_input = int(input("Enter How many values want to add in list : "))

# Loop for adding the multiple values in list.
for i in range(total_input):
    nvalue = input("Enter the value : ")
    list1.append(nvalue)

# Show the list to the user.
print(list1)

# Get the user's choice of function
function_choice = input(
    """Choose a function to perform
(append, extend, insert, remove, pop): """
)
values = input("Enter any required values, separated by commas: ")
values = values.split(",")


# Call the chosen function
function_obj = function_dict.get(function_choice)
if function_obj is not None:
    function_obj(list1, *values)
    print(list1)
else:
    print("Invalid function choice.")
