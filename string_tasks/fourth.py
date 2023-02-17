"""
31 print the following floating numbers upto 2 decimal places with a sign.

32 print the following floating numbers with no decimal places.

33 print the following integers with zeros on the left of specified width.

34 print the following integers with '*' on the right of specified width.

35 display a number with a comma separator.

36 format a number with a percentage.

37 display a number in left, right and center aligned of width 10.

38 count occurrences of a substring in a string.

39 reverse a string.

40 reverse words in a string.

41 strip a set of characters from a string.

42 count repeated characters in a string.
"""
import collections

# 31
x = 3.1415926
print("\nOriginal Number: ", x)
print("Formatted Number with sign: "+"{:+.2f}".format(x))


# 32
x = 3.1415926
print("\nOriginal Number: ", x)
print("Formatted Number with sign: "+"{:.0f}".format(x))

# 33
z = 3
print("\nOriginal Number: ", z)
print("Formatted Number with sign: "+"{:0>3d}".format(z))

# 34
a = 32511510
print("\nOriginal Number: ", a)
print("Formatted Number with sign: "+"{:,}".format(a))

# 35
b = 3
print("\nOriginal Number: ", b)
print("Formatted Number with sign: "+"{:*<3d}".format(b))

# 36
b = 3
print("\nOriginal Number: ", b)
print("Formatted Number with sign: "+"{:*<3d}".format(b))

# 37
c = .34
print("\nOriginal Number: ", c)
print("Formatted Number with sign: "+"{:.2%}".format(c))

# 38
new_str = 'jay siya-ram, jay shree krishna'
print(new_str.count("jay"))


# 39
def reverse_string(new1str):
    return ''.join(reversed(new1str))


print(reverse_string("hello"))


# 40
def reverse_string_words(text):
    for line in text.split('\n'):
        return (' '.join(line.split()[::-1]))


print(reverse_string_words("hello world guys."))


# 41
def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)


jadu = "kya bolu bhai, lagi padi he"
print(f"\nOriginal String: {jadu}")
print(strip_chars(jadu, "aeiou"))


# 42
jadu1 = "csdc eeccsdc sd"
repeater = collections.Counter(jadu1)
print(repeater)
