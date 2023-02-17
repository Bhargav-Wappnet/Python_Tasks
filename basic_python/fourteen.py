"""
Write a python program to check whether two lists are circularly identical.
Write a Python program to find the second smallest number in a list.
Write a Python program to find the second largest number in a list.
Write a Python program to get unique values from a list.
Write a Python program to get the frequency of the elements in a list.
W.A.P.P to count the number of elements in a list within a specified range.
"""


def is_circular_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    if set(list1) != set(list2):
        return False
    for i in range(len(list1)):
        if list1 == list2[i:] + list2[:i]:
            return True
    return False


def find_second_smallest_largest(lst):
    lst.sort()
    return lst[1], lst[-1]


def get_unique_values(lst):
    return list(set(lst))


def get_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency


def count_elements_in_range(lst, lower, upper):
    count = 0
    for item in lst:
        if lower <= item <= upper:
            count += 1
    return count


list1 = [1, 2, 3, 4]
list2 = [3, 4, 1, 2]
print(is_circular_identical(list1, list2))

lst = [1, 2, 3, 4, 5, 6]
second_smallest, largest = find_second_smallest_largest(lst)
print(second_smallest, largest)

lst = [1, 2, 3, 1, 2, 4, 5, 6, 5]
unique_values = get_unique_values(lst)
print(unique_values)

lst = [1, 2, 3, 1, 2, 4, 5, 6, 5]
frequency = get_frequency(lst)
print(frequency)

lst = [1, 2, 3, 4, 5, 6]
count = count_elements_in_range(lst, 2, 5)
print(count)
