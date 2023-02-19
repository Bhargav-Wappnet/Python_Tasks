"""
23 combine values in python list of dictionaries.
24 create a dictionary from a string.
25 print a dictionary in table format.
26 count the values associated with key in a dictionary.
27 convert a list into a nested dictionary of keys.
28 sort a list alphabetically in a dictionary.
29 remove spaces from dictionary keys.
30 get the top three items in a shop.
31 get the key, value and item in a dictionary.
32 print a dictionary line by line.
"""
from heapq import nlargest
from operator import itemgetter
from collections import Counter

# 23
item_list = [
    {"item": "item1", "amount": 400},
    {"item": "item2", "amount": 300},
    {"item": "item1", "amount": 750},
]
result = Counter()
for d in item_list:
    result[d["item"]] += d["amount"]
print(result)

# 24
str1 = "w3resource"
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)

# 25
str1 = "w3resource"
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)

# 26
student = [
    {"id": 1, "success": True, "name": "Lary"},
    {"id": 2, "success": False, "name": "Rabi"},
    {"id": 3, "success": True, "name": "Alex"},
]
print(sum(d["id"] for d in student))
print(sum(d["success"] for d in student))

# 27
num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)

# 28
num = {"n1": [2, 3, 1], "n2": [5, 1, 2], "n3": [3, 2, 4]}
sorted_dict = {x: sorted(y) for x, y in num.items()}
print(sorted_dict)

# 29
student_list = {"S  001": ["Math", "Science"], "S    002": ["Math", "English"]}
print("Original dictionary: ", student_list)
student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
print("New dictionary: ", student_dict)

# 30
items = {"item1": 45.50, "item2": 35, "item3": 41.30, "item4": 55, "item5": 24}
for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    print(name, value)

# 31
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key  value  count")
for count, (key, value) in enumerate(dict_num.items(), 1):
    print(key, "   ", value, "    ", count)

# 32
students = {"Aex": {"class": "V", "rolld_id": 2}, "Puja": {"class": "V", "roll_id": 3}}
for a in students:
    print(a)
    for b in students[a]:
        print(b, ":", students[a][b])
