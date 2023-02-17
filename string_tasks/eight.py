"""
73 count Uppercase, Lowercase, special character and numeric values in string.

74 find the minimum window in a given string which will contain all
the characters of another given string.

75 find smallest window that contains all characters of a given string.

76 count number of substrings from a given string of lowercase alphabets
with exactly k distinct (given) characters.

77 count number of non-empty substrings of a given string.

78 count characters at same position in a given string
(lower and uppercase characters) as in English alphabet.

79 find smallest and largest word in a given string.

80 count number subtrings with same first & last characters of a given string.

81 find the index of a given string at which a given substring starts.
If the substring is not found in the given string return 'Not found'.

82 wrap a given string into a paragraph of given width.
"""
import textwrap
import collections
from collections import defaultdict


# 73
def count_chars(str):
    upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
    for i in range(len(str)):
        if str[i] >= "A" and str[i] <= "Z":
            upper_ctr += 1
        elif str[i] >= "a" and str[i] <= "z":
            lower_ctr += 1
        elif str[i] >= "0" and str[i] <= "9":
            number_ctr += 1
        else:
            special_ctr += 1
    return upper_ctr, lower_ctr, number_ctr, special_ctr


str = "@W3Resource.Com"
print("Original Substrings:", str)
u, l, n, s = count_chars(str)
print("\nUpper case characters: ", u)
print("Lower case characters: ", l)
print("Number case: ", n)
print("Special case characters: ", s)


# 74
def min_window(str1, str2):
    result_char, missing_char = collections.Counter(str2), len(str2)
    i = p = q = 0
    for j, c in enumerate(str1, 1):
        missing_char -= result_char[c] > 0
        result_char[c] -= 1
        if not missing_char:
            while i < q and result_char[str1[i]] < 0:
                result_char[str1[i]] += 1
                i += 1
            if not q or j - i <= q - p:
                p, q = i, j
    return str1[p:q]


str1 = "PRWSOERIUSFK"
str2 = "OSU"
print("Original Strings:\n", str1, "\n", str2)
print("Minimum window:")
print(min_window(str1, str2))


# 75
def find_sub_string(str):
    str_len = len(str)

    # Count all distinct characters.
    dist_count_char = len(set([x for x in str]))

    ctr, start_pos, start_pos_index, min_len = 0, 0, -1, 9999999999
    curr_count = defaultdict(lambda: 0)
    for i in range(str_len):
        curr_count[str[i]] += 1

        if curr_count[str[i]] == 1:
            ctr += 1

        if ctr == dist_count_char:
            while curr_count[str[start_pos]] > 1:
                if curr_count[str[start_pos]] > 1:
                    curr_count[str[start_pos]] -= 1
                start_pos += 1

            len_window = i - start_pos + 1
            if min_len > len_window:
                min_len = len_window
                start_pos_index = start_pos
    return str[start_pos_index: start_pos_index + min_len]


str1 = "asdaewsqgtwwsa"
print("Original Strings:\n", str1)
print("\nSmallest window that contains all characters of the said string:")
print(find_sub_string(str1))


# 76
def count_k_dist(str1, k):
    str_len = len(str1)

    result = 0

    ctr = [0] * 27

    for i in range(0, str_len):
        dist_ctr = 0

        ctr = [0] * 27

        for j in range(i, str_len):
            if ctr[ord(str1[j]) - 97] == 0:
                dist_ctr += 1

            ctr[ord(str1[j]) - 97] += 1

            if dist_ctr == k:
                result += 1
            if dist_ctr > k:
                break

    return result


str1 = input("Input a string (lowercase alphabets):")
k = int(input("Input k: "))
print("Number of substrings with exactly", k, "distinct characters : ", end="")
print(count_k_dist(str1, k))


# 77
def number_of_substrings(str):
    str_len = len(str)
    return int(str_len * (str_len + 1) / 2)


str1 = input("Input a string: ")
print("Number of substrings:")
print(number_of_substrings(str1))


# 78
def count_char_position(str1):
    count_chars = 0
    for i in range(len(str1)):
        if (i == ord(str1[i]) - ord("A")) or (i == ord(str1[i]) - ord("a")):
            count_chars += 1
    return count_chars


str1 = input("Input a string: ")
print(
    "Number of characters of the said string in English alphabet:"
)
print(count_char_position(str1))


# 79
def smallest_largest_words(str1):
    word = ""
    all_words = []
    str1 = str1 + " "
    for i in range(0, len(str1)):
        if str1[i] != " ":
            word = word + str1[i]
        else:
            all_words.append(word)
            word = ""

    small = large = all_words[0]

    # Find smallest and largest word in the str1
    for k in range(0, len(all_words)):
        if len(small) > len(all_words[k]):
            small = all_words[k]
        if len(large) < len(all_words[k]):
            large = all_words[k]
    return small, large


str1 = "Write a Java program to sort an array sort Algorithm."
print("Original Strings:\n", str1)
small, large = smallest_largest_words(str1)
print("Smallest word: " + small)
print("Largest word: " + large)


# 80
def smallest_largest_words(str1):
    word = ""
    all_words = []
    str1 = str1 + " "
    for i in range(0, len(str1)):
        if str1[i] != " ":
            word = word + str1[i]
        else:
            all_words.append(word)
            word = ""

    small = large = all_words[0]

    # Find smallest and largest word in the str1
    for k in range(0, len(all_words)):
        if len(small) > len(all_words[k]):
            small = all_words[k]
        if len(large) < len(all_words[k]):
            large = all_words[k]
    return small, large


str1 = "Write a Java program to sort an array sort Algorithm."
print("Original Strings:\n", str1)
small, large = smallest_largest_words(str1)
print("Smallest word: " + small)
print("Largest word: " + large)


# 81
def find_Index(str1, pos):
    if len(pos) > len(str1):
        return "Not found"

    for i in range(len(str1)):
        for j in range(len(pos)):
            if str1[i + j] == pos[j] and j == len(pos) - 1:
                return i

            elif str1[i + j] != pos[j]:
                break

    return "Not found"


print(find_Index("Python Exercises", "Ex"))
print(find_Index("Python Exercises", "yt"))
print(find_Index("Python Exercises", "PY"))

# 82
s = input("Input a string: ")
w = int(input("Input the width of the paragraph: ").strip())
print("Result:")
print(textwrap.fill(s, w))
