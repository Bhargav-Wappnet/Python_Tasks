"""
W.A.P.P to remove duplicates from a list.
W.A.P.P to check a list is empty or not.
W.A.P.P to find list of words that are longer than n-
        from a given list of words.
W.A.P.F that takes two lists and returns True-
        if they have at least one common member.
"""

# Write a Python program to remove duplicates from a list.
my_list = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
unique_list = list(set(my_list))
print(unique_list)


# Write a Python program to check a list is empty or not.
my_list = []
if not my_list:
    print("The list is empty")
else:
    print("The list is not empty")


# list of words that are longer than n from a given list of words.
word_list = ['apple', 'banana', 'kiwi', 'orange', 'grapefruit', 'lemon']
n = 5
long_words = [word for word in word_list if len(word) > n]
print(long_words)


# takes two lists and returns True if they have at least one common member.
def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
list3 = [10, 11, 12, 13, 14]

print(has_common_member(list1, list2))
print(has_common_member(list1, list3))
