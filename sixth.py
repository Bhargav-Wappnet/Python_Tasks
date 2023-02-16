"""
Write a Python program to generate all sublists of a list.
"""


def sublists(lst):
    subs = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            subs.append(lst[i:j+1])
    return subs


# Example usage
my_list = [1, 2, 3, 4]
print(sublists(my_list))
