"""
1 create a set.
2 iteration over sets.
3 add member(s) in a set.
4 remove item(s) from a given set.
5 remove an item from a set if it is present in the set.
6 create an intersection of sets.
7 create a union of sets.
8 create set difference.
9 create a symmetric difference.
10 check if a set is a subset of another set.
"""
# 1
print("\nCreate a non empty set:")
n = set([0, 1, 2, 3, 4])
print(n)
print(type(n))
print("\nUsing a literal:")
a = {1, 2, 3, "foo", "bar"}
print(type(a))
print(a)

# 2
# Create a set
num_set = set([0, 1, 2, 3, 4, 5])
for n in num_set:
    print(n, end=" ")
print("\n\nCreating a set using string:")
char_set = set("w3resource")
# Iterating using for loop
for val in char_set:
    print(val, end=" ")

# 3
# A new empty set
color_set = set()
print(color_set)
print("\nAdd single element:")
color_set.add("Red")
print(color_set)
print("\nAdd multiple items:")
color_set.update(["Blue", "Green"])
print(color_set)

# 4
num_set = set([0, 1, 3, 4, 5])
print("Original set:")
print(num_set)
num_set.pop()
print("\nAfter removing the first element from the said set:")
print(num_set)

# 5
# Create a new set
num_set = set([0, 1, 2, 3, 4, 5])
print("Original set elements:")
print(num_set)
print("\nRemove 0 from the said set:")
num_set.discard(4)
print(num_set)
print("\nRemove 5 from the said set:")
num_set.discard(5)
print(num_set)
print("\nRemove 2 from the said set:")
num_set.discard(5)
print(num_set)
print("\nRemove 7 from the said set:")
num_set.discard(15)
print(num_set)

# 6
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx & sety
print(setz)

# 7
setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])
print("Original sets:")
print(setc1)
print(setc2)
setc = setc1.union(setc2)
print("\nUnion of above sets:")
print(setc)
setn1 = set([1, 1, 2, 3, 4, 5])
setn2 = set([1, 5, 6, 7, 8, 9])
print("\nOriginal sets:")
print(setn1)
print(setn2)
print("\nUnion of above sets:")
setn = setn1.union(setn2)
print(setn)

# 8
setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])
print("Original sets:")
print(setc1)
print(setc2)
r1 = setc1.difference(setc2)
print("\nDifference of setc1 - setc2:")
print(r1)
r2 = setc2.difference(setc1)
print("\nDifference of setc2 - setc1:")
print(r2)
setn1 = set([1, 1, 2, 3, 4, 5])
setn2 = set([1, 5, 6, 7, 8, 9])
print("\nOriginal sets:")
print(setn1)
print(setn2)
r1 = setn1.difference(setn2)
print("\nDifference of setn1 - setn2:")
print(r1)
r2 = setn2.difference(setn1)
print("\nDifference of setn2 - setn1:")
print(r2)


# 9
setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])
print("Original sets:")
print(setc1)
print(setc2)
r1 = setc1.symmetric_difference(setc2)
print("\nSymmetric difference of setc1 - setc2:")
print(r1)
r2 = setc2.symmetric_difference(setc1)
print("\nSymmetric difference of setc2 - setc1:")
print(r2)
setn1 = set([1, 1, 2, 3, 4, 5])
setn2 = set([1, 5, 6, 7, 8, 9])
print("\nOriginal sets:")
print(setn1)
print(setn2)
r1 = setn1.symmetric_difference(setn2)
print("\nSymmetric difference of setn1 - setn2:")
print(r1)
r2 = setn2.symmetric_difference(setn1)
print("\nSymmetric difference of setn2 - setn1:")
print(r2)

# 10
print(
    "Check if a set is a subset of another set, using comparison operators and issubset():\n"
)
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])
print("x: ", setx)
print("y: ", sety)
print("z: ", setz, "\n")
print("If x is subset of y")
print(setx <= sety)
print(setx.issubset(sety))
print("If y is subset of x")
print(sety <= setx)
print(sety.issubset(setx))
print("\nIf y is subset of z")
print(sety <= setz)
print(sety.issubset(setz))
print("If z is subset of y")
print(setz <= sety)
print(setz.issubset(sety))
