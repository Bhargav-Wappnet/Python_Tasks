"""
Program to print a specified list after removing the 0th, 4th and 5th elements.
"""

my_list = ["Bhargav", "Bhautik", "Aniket", "Raju", "Harsh", "MyMan"]

for index, _ in enumerate(my_list, start=0):
    if index == 0 or 4 or 5:
        my_list.pop(index)

print(my_list)
