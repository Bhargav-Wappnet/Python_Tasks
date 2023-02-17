"""
1 Write a Python program to calculate the length of a string.
count the number of characters (character frequency) in a string.

2 get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string.

3 Write a Python program to get a string from a given string
where all occurrences of its first char have been changed to '$',
except the first char itself.

4 Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.

5 add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.

6 find the first appearance of the substring 'not' and 'poor' from string,
if 'not' follows the 'poor',replace the whole 'not'.'poor'substring with'good'.

7 function that takes a list of words and returns the longest word and
the length of the longest one.

8 remove the nth index character from a nonempty string.

9 change a string to a new string where first and last chars have been exch.
"""


import collections

# 1
test_str = "jay siya-ram"
print(len(test_str))

# 2
char_freq = collections.Counter(test_str)
print(char_freq)

# 3
new_str = test_str[:2] + test_str[-2:]
if len(new_str) < 2:
    print(new_str)

# 4
test1_str = "hakakulahula"
print(test1_str[0] + test1_str[1:].replace(test1_str[0], "$"))


# 5
def swap_strings(str1, str2):
    # swap the first two characters of str1
    str1_swapped = str2[:2] + str1[2:]

    # swap the first two characters of str2
    str2_swapped = str1[:2] + str2[2:]

    # combine the swapped strings into a single string separated by a space
    result = str1_swapped + " " + str2_swapped

    return result


string1 = "hello"
string2 = "world"
result = swap_strings(string1, string2)
print(result)


# 6
def add_ing_ly(string):
    if len(string) < 3:
        # If the string length is less than 3, leave it unchanged
        result = string
    elif string[-3:] == "ing":
        # If the string already ends with 'ing', add 'ly' instead
        result = string + "ly"
    else:
        # Otherwise, add 'ing' at the end of the string
        result = string + "ing"
    return result


string3 = "run"
string4 = "swimming"
result3 = add_ing_ly(string3)
result4 = add_ing_ly(string4)
print(result3)
print(result4)


# 7
def replace_not_poor(string):
    not_index = string.find("not")
    poor_index = string.find("poor")
    if poor_index > not_index and not_index != -1 and poor_index != -1:
        # If 'not' follows 'poor', replace the substring with 'good'
        result = string[:not_index] + "good" + string[poor_index + 4:]
    else:
        # Otherwise, leave the string unchanged
        result = string
    return result


string5 = "The lyrics are not that poor!"
result5 = replace_not_poor(string5)
print(result5)


# 8
def find_longest_word(words):
    max_length = 0
    longest_word = ""
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    return (longest_word, max_length)


words = ["apple", "banana", "pear", "grapefruit", "watermelon"]
result = find_longest_word(words)
print("Longest word:", result[0])
print("Length of longest word:", result[1])


# 9
def remove_char(string, n):
    if n < 0 or n >= len(string):
        return string
    else:
        return string[:n] + string[n + 1:]


string6 = "jadduuu"
new3_string = remove_char(string6, 6)
print(new3_string)


# 10
def exchange_first_last_chars(string):
    # Check if the string is empty or has only one character
    if len(string) <= 1:
        return string
    else:
        # Extract the first and last characters of the string
        first_char = string[0]
        last_char = string[-1]
        # Replace the first and last characters
        new_string = last_char + string[1:-1] + first_char
        return new_string


original_string = "hello world"
new_string = exchange_first_last_chars(original_string)
print(new_string)
