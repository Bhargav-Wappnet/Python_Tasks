"""
53 find the first repeated character in a given string.

54 find the first repeated character of a given string
where the index of first occurrence is smallest.

55 find the first repeated word in a given string.

56 find the second most repeated word in a given string.

57 remove spaces from a given string.

58 move spaces to the front of a given string.

59 find the maximum occurring character in a given string.

60 capitalize first and last letters of each word of a given string.

61 remove duplicate characters of a given string.

62 compute sum of digits of a given string.
"""
from collections import OrderedDict


# 53
def first_repeated_char(str1):
    for index, c in enumerate(str1):
        if str1[: index + 1].count(c) > 1:
            return c
    return "None"


print(first_repeated_char("abcdabcd"))


# 54
def first_repeated_char_smallest_distance(str1):
    temp = {}
    for ch in str1:
        if ch in temp:
            return ch, str1.index(ch)
        else:
            temp[ch] = 0
    return "None"


print(first_repeated_char_smallest_distance("abcabc"))


# 55
def first_repeated_char_smallest_distance(str1):
    temp = {}
    for ch in str1:
        if ch in temp:
            return ch, str1.index(ch)
        else:
            temp[ch] = 0
    return "None"


print(first_repeated_char_smallest_distance("abcabc"))


# 56
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    counts_x = sorted(counts.items(), key=lambda kv: kv[1])
    # print(counts_x)
    return counts_x[-2]


print(
    word_count(
        '''rajan tu aa buliya shunle pukar buliya tu hi to yar buliya,
        mursat mera.'''
    )
)


# 57
def remove_spaces(str1):
    str1 = str1.replace(" ", "")
    return str1


print(remove_spaces("w 3 res ou r ce"))
print(remove_spaces("a b c"))


# 58
def move_Spaces_front(str1):
    noSpaces_char = [ch for ch in str1 if ch != " "]
    spaces_char = len(str1) - len(noSpaces_char)
    result = " " * spaces_char
    result = '"' + result + "".join(noSpaces_char) + '"'
    return result


print(move_Spaces_front("w3resource .  com  "))
print(move_Spaces_front("   w3resource.com  "))


# 59
def get_max_occuring_char(str1):
    ASCII_SIZE = 256
    ctr = [0] * ASCII_SIZE
    max = -1
    ch = ""
    for i in str1:
        ctr[ord(i)] += 1

    for i in str1:
        if max < ctr[ord(i)]:
            max = ctr[ord(i)]
            ch = i
    return ch


print(get_max_occuring_char("Py: Get file creation and modify date/times"))
print(get_max_occuring_char("abcdefghijkb"))


# 60
def get_max_occuring_char(str1):
    ASCII_SIZE = 256
    ctr = [0] * ASCII_SIZE
    max = -1
    ch = ""
    for i in str1:
        ctr[ord(i)] += 1

    for i in str1:
        if max < ctr[ord(i)]:
            max = ctr[ord(i)]
            ch = i
    return ch


print(get_max_occuring_char("Py: Get file creation & modification date/times"))
print(get_max_occuring_char("abcdefghijkb"))


# 61
def remove_duplicate(str1):
    return "".join(OrderedDict.fromkeys(str1))


print(remove_duplicate("python exercises practice solution"))
print(remove_duplicate("w3resource"))


# 62
def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() is True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit


print(sum_digits_string("123abcd45"))
