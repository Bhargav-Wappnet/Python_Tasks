"""
Write a Python program to sum all the items and mul all the items in a list.
Write a Python program to get the largest and smallest number from a list.
"""
my_list = [2, 4, 6, 8, 10]

# sum all items in the list
list_sum = sum(my_list)

# multiply all items in the list
list_product = 1
for item in my_list:
    list_product *= item

# find the largest number in the list
largest = max(my_list)

# find the smallest number in the list
smallest = min(my_list)

print("The sum of all items in the list is:", list_sum)
print("The product of all items in the list is:", list_product)

print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)
