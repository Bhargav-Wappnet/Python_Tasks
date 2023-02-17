"""
43 print square & cube symbol in area of a rectangle and volume of a cylinder.

44 print the index of the character in a string.

45 check if a string contains all letters of the alphabet.

46 convert a string in a list.

47 lowercase first n characters in a string.

48 swap comma and dot in a string.

49 count and display the vowels of a given text.

50 split a string on the last occurrence of the delimiter.

51 find the first non-repeating character in given string.

52 print all permutation with given repetition number of chars of given string.
"""
import string
from itertools import product

# 43
area = 1256.66
volume = 1254.725
decimals = 2
print("The area of rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))
decimals = 3
print("The volume of cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))

# 44
my_string = "hello world"
char = "w"
index = my_string.index(char)
print(f"The index of {char} is {index}")

# 45
alphabet = set(string.ascii_lowercase)
input_string = "sun meri sahejadi me hu tera divan."
print(set(input_string.lower()) >= alphabet)

# 46
str_first = "KYA bolti PUblic"
print(str_first.split(" "))

# 47
print(str_first[:5].lower() + str_first[6:])

# 48
amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(",.", ".,"))
print(amount)


# 49
def vowel(text):
    vowels = "aeiuoAEIOU"
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])


vowel("bhagavBOR")

# 50
str1 = "b, h, a, r, g, a, v"
print(str1.rsplit(",", 1))
print(str1.rsplit(",", 2))
print(str1.rsplit(",", 5))


# 51
def first_non_repeating_character(str1):
    char_order = []
    ctr = {}
    for c in str1:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1
            char_order.append(c)
    for c in char_order:
        if ctr[c] == 1:
            return c
    return None


print(first_non_repeating_character("abcdef"))


# 52
def all_repeat(str1, rno):
    chars = list(str1)
    results = []
    for c in product(chars, repeat=rno):
        results.append(c)
    return results


print(all_repeat("bha", 3))
