"""
43 convert more than one list to nested dictionary.

44 filter the height and width of students, which are stored in a dictionary.

45 check all values are same in a dictionary.

46 create a dictionary grouping a sequence of key-value pairs
into a dictionary of lists.

47 split a given dictionary of lists into list of dictionaries.

48 remove a specified dictionary from a given list.

49 convert string values of a given dictionary, into integer/float datatypes.

50 Python Dictionary contains List as value.
clear the list values in the said dictionary.

51 A Python Dictionary contains List as value.
update the list values in the said dictionary.

52 extract a list of values from a given list of dictionaries.
"""


# 43
def nested_dictionary(l1, l2, l3):
    result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
    return result


student_id = ["S001", "S002", "S003", "S004"]
student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
student_grade = [85, 98, 89, 92]
print("Original strings:")
print(student_id)
print(student_name)
print(student_grade)
print("\nNested dictionary:")
ch = "a"
print(nested_dictionary(student_id, student_name, student_grade))


# 44
def filter_data(students):
    result = {k: s for k, s in students.items() if s[0] >= 6.0 and s[1] >= 70}
    return result


students = {
    "Cierra Vega": (6.2, 70),
    "Alden Cantrell": (5.9, 65),
    "Kierra Gentry": (6.0, 68),
    "Pierre Cox": (5.8, 66),
}
print("Original Dictionary:")
print(students)
print("\nHeight > 6ft and Weight> 70kg:")
print(filter_data(students))


# 45
def value_check(students, n):
    result = all(x == n for x in students.values())
    return result


students = {
    "Cierra Vega": 12,
    "Alden Cantrell": 12,
    "Kierra Gentry": 12,
    "Pierre Cox": 12,
}
print("Original Dictionary:")
print(students)
n = 12
print("\nCheck all are ", n, "in the dictionary.")
print(value_check(students, n))
n = 10
print("\nCheck all are ", n, "in the dictionary.")
print(value_check(students, n))


# 46
def grouping_dictionary(K):
    result = {}
    for k, v in K:
        result.setdefault(k, []).append(v)
    return result


colors = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
print("Original list:")
print(colors)
print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(grouping_dictionary(colors))


# 47
def list_of_dicts(marks):
    keys = marks.keys()
    vals = zip(*[marks[k] for k in keys])
    result = [dict(zip(keys, v)) for v in vals]
    return result


marks = {"Science": [88, 89, 62, 95], "Language": [77, 78, 84, 80]}
print("Original dictionary of lists:")
print(marks)
print("\nSplit said dictionary of lists into list of dictionaries:")
print(list_of_dicts(marks))


# 48
def remove_dictionary(colors, r_id):
    colors[:] = [d for d in colors if d.get("id") != r_id]
    return colors


colors = [
    {"id": "#FF0000", "color": "Red"},
    {"id": "#800000", "color": "Maroon"},
    {"id": "#FFFF00", "color": "Yellow"},
    {"id": "#808000", "color": "Olive"},
]
print("Original list of dictionary:")
print(colors)
r_id = "#FF0000"
print("\nRemove id", r_id, "from the said list of dictionary:")
print(remove_dictionary(colors, r_id))


# 49
def convert_to_int(lst):
    result = [dict([a, int(x)] for a, x in b.items()) for b in lst]
    return result


def convert_to_float(lst):
    result = [dict([a, float(x)] for a, x in b.items()) for b in lst]
    return result


nums = [{"x": "10", "y": "20", "z": "30"}, {"p": "40", "q": "50", "r": "60"}]
print("Original list:")
print(nums)
print("\nString values of a given dictionary, into integer types:")
print(convert_to_int(nums))
nums = [
    {"x": "10.12", "y": "20.23", "z": "30"},
    {"p": "40.00", "q": "50.19", "r": "60.99"},
]
print("\nOriginal list:")
print(nums)
print("\nString values of a given dictionary, into float types:")
print(convert_to_float(nums))


# 50
def test(dictionary):
    for key in dictionary:
        dictionary[key].clear()
    return dictionary


dictionary = {"C1": [10, 20, 30], "C2": [20, 30, 40], "C3": [12, 34]}
print("\nOriginal Dictionary:")
print(dictionary)
print("\nClear the list values in the said dictionary:")
print(test(dictionary))


# 51
def test(dictionary):
    dictionary["Math"] = [x + 1 for x in dictionary["Math"]]
    dictionary["Physics"] = [x - 2 for x in dictionary["Physics"]]
    return dictionary


dictionary = {"Math": [88, 89, 90], "Physics": [92, 94, 89], "Chemistry": [90, 87, 93]}
print("\nOriginal Dictionary:")
print(dictionary)
print("\nUpdate the list values of the said dictionary:")
print(test(dictionary))


# 52
def test(lst, marks):
    result = [d[marks] for d in lst if marks in d]

    return result


marks = [
    {"Math": 90, "Science": 92},
    {"Math": 89, "Science": 94},
    {"Math": 92, "Science": 88},
]

print("\nOriginal Dictionary:")
print(marks)
subj = "Science"
print("\nExtract a list of values from said list of dictionaries where subject =", subj)
print(test(marks, subj))

print("\nOriginal Dictionary:")
print(marks)
subj = "Math"
print("\nExtract a list of values from said list of dictionaries where subject =", subj)
print(test(marks, subj))
