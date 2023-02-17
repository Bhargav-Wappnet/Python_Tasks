"""
create a list by concatenating a given list which range goes from 1 to n.
get variable unique identification number or string.
find common items from two lists
change the position of every n-th value with the (n+1)th in a list.
convert a list of multiple integers into a single integer.
split a list based on first character of word.

"""


# create a list by concatenating a given list which range goes from 1 to n.
def concat_list_with_range(lst, n):
    new_lst = lst + [i for i in range(1, n + 1)]
    return new_lst


# example usage
my_list1 = [10, 20, 30]
new_list = concat_list_with_range(my_list1, 5)
print(new_list)


# get variable unique identification number or string.
x = 42
print(id(x))


# find common items from two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_items = list(set(list1).intersection(list2))

print(common_items)


# change the position of every n-th value with the (n+1)th in a list.
def swap_n_values(lst, n):
    lst_len = len(lst)
    if n > lst_len:
        return lst
    else:
        # Swap every n-th value with the (n+1)th
        for i in range(0, lst_len - 1, n):
            lst[i:i + 2] = lst[i + 1: i - 1: -1]
        return lst


# Example usage
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = swap_n_values(my_list2, 2)
print(new_list)


# convert a list of multiple integers into a single integer.
def list_to_int(lst):
    # Join the integers as a string
    joined_str = "".join(map(str, lst))
    # Convert the string to an integer
    result = int(joined_str)
    return result


my_list3 = [2, 3, 1, 8, 4, 2]
my_int = list_to_int(my_list3)
print(my_int)


# split a list based on first character of word.
def split_list_by_first_character(lst):
    result = {}
    for item in lst:
        first_char = item[0]
        if first_char not in result:
            result[first_char] = [item]
        else:
            result[first_char].append(item)
    return result


my_list4 = ["apple", "banana", "cherry", "date", "kiwi", "orange", "fig"]
result = split_list_by_first_character(my_list4)
print(result)
