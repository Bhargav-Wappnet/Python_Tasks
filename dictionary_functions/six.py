"""
53 find the length of a given dictionary values.

54 get the depth of a dictionary.

55 access dictionary key's element by index.

56 convert a given dictionary into a list of lists.

57 filter even numbers from a given dictionary values.

58 get all combinations of key-value pairs in a given dictionary.

59 find the specified number of maximum values in a given dictionary.

60 find shortest list of values with the keys in a given dictionary.

61 count the frequency in a given dictionary.

62 extract values from a given dictionaries and
create a list of lists from those values.

63 convert a given list of lists to a dictionary.

64 create a key-value list pairings in a given dictionary.

65 get the total length of all values of a given dictionary with string values.

66 check if a specific Key and a value exist in a dictionary.
"""
import itertools
from itertools import product
from collections import Counter


# 53
def test(dictt):
    result = {}
    for val in dictt.values():
        result[val] = len(val)
    return result


color_dict = {1: "red", 2: "green", 3: "black", 4: "white", 5: "black"}
print("\nOriginal Dictionary:")
print(color_dict)
print("Length of dictionary values:")
print(test(color_dict))

color_dict = {
    "1": "Austin Little",
    "2": "Natasha Howard",
    "3": "Alfred Mullins",
    "4": "Jamie Rowe",
}
print("\nOriginal Dictionary:")
print(color_dict)
print("Length of dictionary values:")
print(test(color_dict))


# 54
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0


dic = {"a": 1, "b": {"c": {"d": {}}}}
print(dict_depth(dic))

# 55
num = {"physics": 80, "math": 90, "chemistry": 86}
print(list(num)[0])
print(list(num)[1])
print(list(num)[2])


# 56
def test(dictt):
    result = list(map(list, dictt.items()))
    return result


color_dict = {1: "red", 2: "green", 3: "black", 4: "white", 5: "black"}
print("\nOriginal Dictionary:")
print(color_dict)
print("Convert the said dictionary into a list of lists:")
print(test(color_dict))

color_dict = {
    "1": "Austin Little",
    "2": "Natasha Howard",
    "3": "Alfred Mullins",
    "4": "Jamie Rowe",
}
print("\nOriginal Dictionary:")
print(color_dict)
print("Convert the said dictionary into a list of lists:")
print(test(color_dict))


# 57
def test(dictt):
    result = {key: [idx for idx in val if not idx % 2] for key, val in dictt.items()}
    return result


students = {"V": [1, 4, 6, 10], "VI": [1, 4, 12], "VII": [1, 3, 8]}
print("\nOriginal Dictionary:")
print(students)
print("Filter even numbers from said dictionary values:")
print(test(students))

students = {"V": [1, 3, 5], "VI": [1, 5], "VII": [2, 7, 9]}
print("\nOriginal Dictionary:")
print(students)
print("Filter even numbers from said dictionary values:")
print(test(students))


# 58
def test(dictt):
    result = list(map(dict, itertools.combinations(dictt.items(), 2)))
    return result


students = {"V": [1, 4, 6, 10], "VI": [1, 4, 12], "VII": [1, 3, 8]}
print("\nOriginal Dictionary:")
print(students)
print("\nCombinations of key-value pairs of the said dictionary:")
print(test(students))

students = {"V": [1, 3, 5], "VI": [1, 5]}
print("\nOriginal Dictionary:")
print(students)
print("\nCombinations of key-value pairs of the said dictionary:")
print(test(students))


# 59
def test(dictt, N):
    result = sorted(dictt, key=dictt.get, reverse=True)[:N]
    return result


dictt = {
    "a": 5,
    "b": 14,
    "c": 32,
    "d": 35,
    "e": 24,
    "f": 100,
    "g": 57,
    "h": 8,
    "i": 100,
}
print("\nOriginal Dictionary:")
print(dictt)
N = 1
print("\n", N, "maximum value(s) in the said dictionary:")
print(test(dictt, N))
N = 2
print("\n", N, "maximum value(s) in the said dictionary:")
print(test(dictt, N))
N = 5
print("\n", N, "maximum value(s) in the said dictionary:")
print(test(dictt, N))


# 60
def test(dictt):
    min_value = 1
    result = [k for k, v in dictt.items() if len(v) == (min_value)]
    return result


dictt = {
    "V": [10, 12],
    "VI": [10],
    "VII": [10, 20, 30, 40],
    "VIII": [20],
    "IX": [10, 30, 50, 70],
    "X": [80],
}

print("\nOriginal Dictionary:")
print(dictt)
print("\nShortest list of values with the keys of the said dictionary:")
print(test(dictt))


# 61
def test(dictt):
    result = Counter(dictt.values())
    return result


dictt = {
    "V": 10,
    "VI": 10,
    "VII": 40,
    "VIII": 20,
    "IX": 70,
    "X": 80,
    "XI": 40,
    "XII": 20,
}

print("\nOriginal Dictionary:")
print(dictt)
print("\nCount the frequency of the said dictionary:")
print(test(dictt))


# 62
def test(dictt, keys):
    return [list(d[k] for k in keys) for d in dictt]


students = [
    {"student_id": 1, "name": "Jean Castro", "class": "V"},
    {"student_id": 2, "name": "Lula Powell", "class": "V"},
    {"student_id": 3, "name": "Brian Howell", "class": "VI"},
    {"student_id": 4, "name": "Lynne Foster", "class": "VI"},
    {"student_id": 5, "name": "Zachary Simon", "class": "VII"},
]

print("\nOriginal Dictionary:")
print(students)
print(
    "\nExtract values from the said dictionarie and create a list of lists using those values:"
)
print("\n", test(students, ("student_id", "name", "class")))
print("\n", test(students, ("student_id", "name")))
print("\n", test(students, ("name", "class")))


# 63
def test(lst):
    result = {item[0]: item[1:] for item in lst}
    return result


students = [
    [1, "Jean Castro", "V"],
    [2, "Lula Powell", "V"],
    [3, "Brian Howell", "VI"],
    [4, "Lynne Foster", "VI"],
    [5, "Zachary Simon", "VII"],
]

print("\nOriginal list of lists:")
print(students)
print("\nConvert the said list of lists to a dictionary:")
print(test(students))


# 64
def test(dictt):
    result = [dict(zip(dictt, sub)) for sub in product(*dictt.values())]
    return result


students = {
    1: ["Jean Castro"],
    2: ["Lula Powell"],
    3: ["Brian Howell"],
    4: ["Lynne Foster"],
    5: ["Zachary Simon"],
}

print("\nOriginal dictionary:")
print(students)
print("\nA key-value list pairings of the said dictionary:")
print(test(students))


# 65
def test(dictt):
    result = sum((len(values) for values in dictt.values()))
    return result


color = {"#FF0000": "Red", "#800000": "Maroon", "#FFFF00": "Yellow", "#808000": "Olive"}
print("\nOriginal dictionary:")
print(color)
print("\nTotal length of all values of the said dictionary with string values:")
print(test(color))


# 66
def test(dictt, key, value):
    if any(sub[key] == value for sub in dictt):
        return True
    return False


students = [
    {"student_id": 1, "name": "Jean Castro", "class": "V"},
    {"student_id": 2, "name": "Lula Powell", "class": "V"},
    {"student_id": 3, "name": "Brian Howell", "class": "VI"},
    {"student_id": 4, "name": "Lynne Foster", "class": "VI"},
    {"student_id": 5, "name": "Zachary Simon", "class": "VII"},
]


print("\nOriginal dictionary:")
print(students)
print("\nCheck if a specific Key and a value exist in the said dictionary:")
print(test(students, "student_id", 1))
print(test(students, "name", "Brian Howell"))
print(test(students, "class", "VII"))
print(test(students, "class", "I"))
print(test(students, "name", "Brian Howelll"))
print(test(students, "student_id", 11))
