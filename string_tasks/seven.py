"""
63 remove leading zeros from an IP address.

64 find maximum length of consecutive 0's in a given binary string.

65 find all the common characters in lexicographical order from two given lower
case strings. If there are no common letters print "No common characters".

66 make two given strings (lower case, may or may not be of the same length)
anagrams removing any characters from any of the strings.

67 remove all consecutive duplicates of a given string.

68 create two strings from a given string. Create the first string using those
character which occurs only once and create the second string which consists
of multi-time occurring characters in the said string.

69 find the longest common sub-string from two given strings.

70 create a string from two given strings concatenating uncommon characters
of the said strings.

71 move all spaces to the front of a given string in single traversal.

72 remove all characters except a specified character in a given string.
"""

from collections import Counter
from difflib import SequenceMatcher


# 63
def remove_zeros_from_ip(ip_add):
    new_ip_add = ".".join([str(int(i)) for i in ip_add.split(".")])
    return new_ip_add


print(remove_zeros_from_ip("255.024.01.01"))


# 64
def max_consecutive_0(input_str):
    return max(map(len, input_str.split("1")))


str1 = "111000010000110"
print("Original string:" + str1)
print("Maximum length of consecutive 0's:")
print(max_consecutive_0(str1))
str1 = "111000111"
print("Original string:" + str1)
print("Maximum length of consecutive 0's:")
print(max_consecutive_0(str1))


# 65
def common_chars(str1, str2):
    d1 = Counter(str1)
    d2 = Counter(str2)
    common_dict = d1 & d2
    if len(common_dict) == 0:
        return "No common characters."

    # list of common elements
    common_chars = list(common_dict.elements())
    common_chars = sorted(common_chars)

    return "".join(common_chars)


str1 = "Python"
str2 = "PHP"
print("Two strings: " + str1 + " : " + str2)
print(common_chars(str1, str2))
str1 = "Java"
str2 = "PHP"
print("Two strings: " + str1 + " : " + str2)
print(common_chars(str1, str2))


# 66
def make_map(s):
    temp_map = {}
    for char in s:
        if char not in temp_map:
            temp_map[char] = 1
        else:
            temp_map[char] += 1
    return temp_map


def make_anagram(str1, str2):
    str1_map1 = make_map(str1)
    str2_map2 = make_map(str2)

    ctr = 0
    for key in str2_map2.keys():
        if key not in str1_map1:
            ctr += str2_map2[key]
        else:
            ctr += max(0, str2_map2[key] - str1_map1[key])

    for key in str1_map1.keys():
        if key not in str2_map2:
            ctr += str1_map1[key]
        else:
            ctr += max(0, str1_map1[key] - str2_map2[key])
    return ctr


str1 = input("Input string1: ")
str2 = input("Input string2: ")
print(make_anagram(str1, str2))


# 67
def generateStrings(input):
    str_char_ctr = Counter(input)
    part1 = [key for (key, count) in str_char_ctr.items() if count == 1]
    part2 = [key for (key, count) in str_char_ctr.items() if count > 1]
    part1.sort()
    part2.sort()
    return part1, part2


input = "aabbcceffgh"
s1, s2 = generateStrings(input)
print("".join(s1))
print("".join(s2))


# 68
def generateStrings(input):
    str_char_ctr = Counter(input)
    part1 = [key for (key, count) in str_char_ctr.items() if count == 1]
    part2 = [key for (key, count) in str_char_ctr.items() if count > 1]
    part1.sort()
    part2.sort()
    return part1, part2


input = "aabbcceffgh"
s1, s2 = generateStrings(input)
print("".join(s1))
print("".join(s2))


# 69
def longest_Substring(s1, s2):
    seq_match = SequenceMatcher(None, s1, s2)

    match = seq_match.find_longest_match(0, len(s1), 0, len(s2))

    # return the longest substring
    if match.size != 0:
        return s1[match.a: match.a + match.size]
    else:
        return "Longest common sub-string not present"


s1 = "abcdefgh"
s2 = "xswerabcdwd"
print("Original Substrings:\n", s1 + "\n", s2)
print("\nCommon longest sub_string:")
print(longest_Substring(s1, s2))


# 70
def uncommon_chars_concat(s1, s2):
    set1 = set(s1)
    set2 = set(s2)

    common_chars = list(set1 & set2)
    result = [ch for ch in s1 if ch not in common_chars] + [
        ch for ch in s2 if ch not in common_chars
    ]
    return "".join(result)


s1 = "abcdpqr"
s2 = "xyzabcd"
print("Original Substrings:\n", s1 + "\n", s2)
print("\nAfter concatenating uncommon characters:")
print(uncommon_chars_concat(s1, s2))


# 71
def moveSpaces(str1):
    no_spaces = [char for char in str1 if char != " "]
    space = len(str1) - len(no_spaces)
    # Create string with spaces
    result = " " * space
    return result + "".join(no_spaces)


s1 = "Python Exercises"
print("Original String:\n", s1)

print("\nAfter moving all spaces to the front:")
print(moveSpaces(s1))


# 72
def remove_characters(str1, c):
    return "".join([el for el in str1 if el == c])


text = "Python Exercises"
print("Original string")
print(text)
except_char = "P"
print("Remove all characters except", except_char, "in the said string:")
print(remove_characters(text, except_char))
