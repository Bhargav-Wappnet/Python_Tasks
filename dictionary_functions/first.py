"""
3 concatenate the following dictionaries to create a new one.

4 check whether a given key already exists in a dictionary.

5 iterate over dictionaries using for loops. Go to the editor

6 generate and print a dictionary that contains a number
(between 1 and n) in the form (x, x*x). Go to the editor
Sample Dictionary ( n = 5)

7 print a dictionary where the keys are numbers between 1 and 15 (included)
and the values are square of keys. Go to the editor

8 merge two Python dictionaries.

9 iterate over dictionaries using for loops.

10 sum all the items in a dictionary.

11 multiply all the items in a dictionary.

12 remove a key from a dictionary.
"""
# 3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)

# 4
d = {"x": 10, "y": 20, "z": 30}
for dict_key, dict_value in d.items():
    print(dict_key, "->", dict_value)

# 5
d = {"x": 10, "y": 20, "z": 30}
for dict_key, dict_value in d.items():
    print(dict_key, "->", dict_value)

# 6
n = int(input("Input a number "))
d = dict()

for x in range(1, n + 1):
    d[x] = x * x

print(d)

# 7
d = dict()
for x in range(1, 16):
    d[x] = x**2
print(d)

# 8
d = {"Red": 1, "Green": 2, "Blue": 3}
for color_key, value in d.items():
    print(color_key, "corresponds to ", d[color_key])

# 9
d = {"Red": 1, "Green": 2, "Blue": 3}
for color_key, value in d.items():
    print(color_key, "corresponds to ", d[color_key])

# 10

my_dict = {"data1": 100, "data2": -54, "data3": 247}
print(sum(my_dict.values()))

# 11
my_dict = {"data1": 100, "data2": -54, "data3": 247}
result = 1
for key in my_dict:
    result = result * my_dict[key]

print(result)

# 12
myDict = {"a": 1, "b": 2, "c": 3, "d": 4}
print(myDict)
if "a" in myDict:
    del myDict["a"]
print(myDict)
