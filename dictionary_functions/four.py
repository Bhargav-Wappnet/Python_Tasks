"""
33 check multiple keys exists in a dictionary.

34 count number of items in a dictionary value that is a list.

35 sort Counter by value.

36 create a dictionary from two lists without losing duplicate values.

37 replace dictionary values with their average.

38 match key values in two dictionaries.

39 store a given dictionary in a json file.

40 create a dictionary of keys x, y, and z
where each key has as value a list from 11-20, 21-30, and 31-40 respectively.
Access the fifth value of each key from the dictionary.

41 drop empty Items from a given Dictionary.

42 filter a dictionary based on values.
"""
from collections import Counter, defaultdict
import json
from pprint import pprint


# 33
student = {"name": "Alex", "class": "V", "roll_id": "2"}
print(student.keys() >= {"class", "name"})
print(student.keys() >= {"name", "Alex"})
print(student.keys() >= {"roll_id", "name"})

# 34
dict = {"Alex": ["subj1", "subj2", "subj3"], "David": ["subj1", "subj2"]}
ctr = sum(map(len, dict.values()))
print(ctr)

# 35
x = Counter({"Math": 81, "Physics": 83, "Chemistry": 87})
print(x.most_common())

# 36
class_list = ["Class-V", "Class-VI", "Class-VII", "Class-VIII"]
id_list = [1, 2, 2, 3]
temp = defaultdict(set)
for c, i in zip(class_list, id_list):
    temp[c].add(i)
print(temp)


# 37
def sum_math_v_vi_average(list_of_dicts):
    for d in list_of_dicts:
        n1 = d.pop("V")
        n2 = d.pop("VI")
        d["V+VI"] = (n1 + n2) / 2
    return list_of_dicts


student_details = [
    {"id": 1, "subject": "math", "V": 70, "VI": 82},
    {"id": 2, "subject": "math", "V": 73, "VI": 74},
    {"id": 3, "subject": "math", "V": 75, "VI": 86},
]
print(sum_math_v_vi_average(student_details))

# 38
x = {"key1": 1, "key2": 3, "key3": 2}
y = {"key1": 1, "key2": 2}
for key, value in set(x.items()) & set(y.items()):
    print("%s: %s is present in both x and y" % (key, value))

# 39
d = {
    "students": [
        {"firstName": "Nikki", "lastName": "Roysden"},
        {"firstName": "Mervin", "lastName": "Friedland"},
        {"firstName": "Aron ", "lastName": "Wilkins"},
    ],
    "teachers": [
        {"firstName": "Amberly", "lastName": "Calico"},
        {"firstName": "Regine", "lastName": "Agtarap"},
    ],
}
print("Original dictionary:")
print(d)
print(type(d))

with open("dictionary", "w") as f:
    json.dump(d, f, indent=4, sort_keys=True)

print("\nJson file to dictionary:")
with open("dictionary") as f:
    data = json.load(f)
print(data)

# 40
dict_nums = dict(x=list(range(11, 20)), y=list(range(21, 30)), z=list(range(31, 40)))
pprint(dict_nums)
print(dict_nums["x"][4])
print(dict_nums["y"][4])
print(dict_nums["z"][4])
for k, v in dict_nums.items():
    print(k, "has value", v)

# 41
dict1 = {"c1": "Red", "c2": "Green", "c3": None}
print("Original Dictionary:")
print(dict1)
print("New Dictionary after dropping empty items:")
dict1 = {key: value for (key, value) in dict1.items() if value is not None}
print(dict1)

# 42
marks = {
    "Cierra Vega": 175,
    "Alden Cantrell": 180,
    "Kierra Gentry": 165,
    "Pierre Cox": 190,
}
print("Original Dictionary:")
print(marks)
print("Marks greater than 170:")
result = {key: value for (key, value) in marks.items() if value >= 170}
print(result)
