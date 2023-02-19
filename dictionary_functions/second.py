"""
13 map two lists into a dictionary.

14 sort a dictionary by key.

15 get the maximum and minimum value in a dictionary.

16 get a dictionary from an object's fields.

17 remove duplicates from Dictionary.

18 check a dictionary is empty or not.

19 combine two dictionary adding values for common keys.

20 print all unique values in a dictionary.

21 create and display all combinations of letters,
selecting each letter from a different key in a dictionary.

22 find the highest 3 values of corresponding keys in a dictionary.
"""
from collections import Counter
import itertools
from heapq import nlargest


# 13
keys = ["red", "green", "blue"]
values = ["#FF0000", "#008000", "#0000FF"]
color_dictionary = dict(zip(keys, values))
print(color_dictionary)

# 14
color_dict = {
    "red": "#FF0000",
    "green": "#008000",
    "black": "#000000",
    "white": "#FFFFFF",
}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))

# 15
my_dict = {"x": 500, "y": 5874, "z": 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print("Maximum Value: ", my_dict[key_max])
print("Minimum Value: ", my_dict[key_min])


# 16
class dictObj(object):
    def __init__(self):
        self.x = "red"
        self.y = "Yellow"
        self.z = "Green"

    def do_nothing(self):
        pass


test = dictObj()
print(test.__dict__)

# 17
student_data = {
    "id1": {
        "name": ["Sara"],
        "class": ["V"],
        "subject_integration": ["english, math, science"],
    },
    "id2": {
        "name": ["David"],
        "class": ["V"],
        "subject_integration": ["english, math, science"],
    },
    "id3": {
        "name": ["Sara"],
        "class": ["V"],
        "subject_integration": ["english, math, science"],
    },
    "id4": {
        "name": ["Surya"],
        "class": ["V"],
        "subject_integration": ["english, math, science"],
    },
}

result = {}

for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)

# 18
my_dict = {}

if not bool(my_dict):
    print("Dictionary is empty")

# 19
d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
d = Counter(d1) + Counter(d2)
print(d)

# 20
L = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"},
]
print("Original List: ", L)
u_value = set(val for dic in L for val in dic.values())
print("Unique Values: ", u_value)

# 21
d = {"1": ["a", "b"], "2": ["c", "d"]}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print("".join(combo))

# 22
my_dict = {"a": 500, "b": 5874, "c": 560, "d": 400, "e": 5874, "f": 20}
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest)
