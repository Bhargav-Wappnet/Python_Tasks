"""
Write a Python program to get a list,
sorted in increasing order by the last element in each tuple
from a given list of non-empty tuples.
"""


def sort_tuples_by_last_element(lst):
    sorted_lst = sorted(lst, key=lambda x: x[-1])
    return sorted_lst


my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_tuples_by_last_element(my_list))
