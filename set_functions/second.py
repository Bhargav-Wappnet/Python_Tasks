"""
11 create a shallow copy of sets.

12 remove all elements from a given set.

13 use of frozensets.

14 find maximum and the minimum value in a set.

15 find the length of a set

16 check if a given value is present in a set or not

17 check if two given sets have no elements in common

18 check if a given set is superset of itself and superset of another given set

19 find the elements in a given set that are not in another set

20 remove the intersection of a 2nd set from the 1st set
"""
# 11
setp = set(["Red", "Green"])
setq = set(["Green", "Red"])
# A shallow copy
setr = setp.copy()
print(setr)

# 12
setp = set(["Red", "Green"])
setq = set(["Green", "Red"])
# A shallow copy
setr = setp.copy()
print(setr)

# 13
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
# use isdisjoint(). Return True if the set has no elements in common with other.
print(x.isdisjoint(y))
# use difference(). Return a new set with elements in the set that are not in the others.
print(x.difference(y))
# new set with elements from both x and y
print(x | y)

# 14
# Create a set
setn = {5, 10, 3, 15, 2, 20}
print("Original set elements:")
print(setn)
print(type(setn))
print("\nMaximum value of the said set:")
print(max(setn))
print("\nMinimum value of the said set:")
print(min(setn))

# 15
# Create a set
setn = {5, 10, 3, 15, 2, 20}
print("Original set elements:")
print(setn)
print(type(setn))
print("\nLength of the said set:")
print(len(setn))

setn = {5, 5, 5, 5, 5, 5}
print("Original set elements:")
print(setn)
print(type(setn))
print("\nLength of the said set:")
print(len(setn))

setn = {5, 5, 5, 5, 5, 5, 7}
print("Original set elements:")
print(setn)
print(type(setn))
print("\nLength of the said set:")
print(len(setn))

# 16
nums = {1, 3, 5, 7, 9, 11}
print("Original sets(nums): ", nums, "\n")
print("Test if 6 exists in nums:")
print(6 in nums)
print("Test if 7 exists in nums:")
print(7 in nums)
print("Test if 11 exists in nums:")
print(11 in nums)
print("Test if 0 exists in nums:")
print(0 in nums)
print("\nTest if 6 is not in nums")
print(6 not in nums)
print("Test if 7 is not in nums")
print(7 not in nums)
print("Test if 11 is not in nums")
print(11 not in nums)
print("Test if 0 is not in nums")
print(0 not in nums)

# 17
x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}
print("Original set elements:")
print(x)
print(y)
print(z)
print("\nConfirm two given sets have no element(s) in common:")
print("\nCompare x and y:")
print(x.isdisjoint(y))
print("\nCompare x and z:")
print(z.isdisjoint(x))
print("\nCompare y and z:")
print(y.isdisjoint(z))

# 18
nums = {10, 20, 30, 40, 50}
print("Original set: ", nums)
print("If nums is superset of itself?")
print(nums.issuperset(nums))
num1 = {1, 2, 3, 4, 5, 7}
num2 = {2, 4}
num3 = {2, 4}
print("\nnum1 = ", num1)
print("num2 = ", num2)
print("num3 = ", num3)
print("If mum1 is superset of num2:")
print(num1 > num2)
print("Compare mum2 and num3:")
print("If mum2 is superset of num3:")
print(num2 > num3)
print("If mum3 is superset of num2:")
print(num3 > num2)

# 19
sn1 = {1, 2, 3, 4, 5}
sn2 = {4, 5, 6, 7, 8}
print("Original sets:")
print(sn1)
print(sn2)
print("Difference of sn1 and sn2 using difference():")
print(sn1.difference(sn2))
print("Difference of sn2 and sn1 using difference():")
print(sn2.difference(sn1))
print("Difference of sn1 and sn2 using - operator:")
print(sn1 - sn2)
print("Difference of sn2 and sn1 using - operator:")
print(sn2 - sn1)

# 20
sn1 = {1, 2, 3, 4, 5}
sn2 = {4, 5, 6, 7, 8}
print("Original sets:")
print(sn1)
print(sn2)
print(
    "\nRemove the intersection of a 2nd set from the 1st set using difference_update():"
)
sn1.difference_update(sn2)
print("sn1: ", sn1)
print("sn2: ", sn2)
sn1 = {1, 2, 3, 4, 5}
sn2 = {4, 5, 6, 7, 8}
print("\nRemove the intersection of a 2nd set from the 1st set using -= operator:")
sn1 -= sn2
print("sn1: ", sn1)
print("sn2: ", sn2)
