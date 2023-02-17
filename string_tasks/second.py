"""
11 remove the characters which have odd index values of a given string.

12 count the occurrences of each word in a given sentence.

13 takes input from the user and displays that
input back in upper and lower cases.

14 accepts a comma separated sequence of words as input and
prints the unique words in sorted form (alphanumerically).

15 Python function to create the HTML string with tags around the word(s).

16 Python function to insert a string in the middle of a string.

17 Python function to get a string made of 4 copies of last two characters of
a specified string (length must be at least 2).

18 Python function to get a string made of its first three characters of
specify string. If length of string is less than 3 then return original string.

19 get the last part of a string before a specified character.

20 Python function to reverses a string if it's length is a multiple of 4.
"""


# 11
def remove_odd_index_chars(string):
    # Use string slicing to remove characters with odd index values
    new_string = string[::2]
    return new_string


original_string = "hello world"
new_string = remove_odd_index_chars(original_string)
print(new_string)


# 12
def count_word_occurrences(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Create a dictionary to store the word occurrences
    word_occurrences = {}
    # Count the occurrences of each word and update the dictionary
    for word in words:
        if word in word_occurrences:
            word_occurrences[word] += 1
        else:
            word_occurrences[word] = 1
    return word_occurrences


sentence = "the quick brown fox jumps over the lazy dog"
word_occurrences = count_word_occurrences(sentence)
print(word_occurrences)


# 13
user_input = input("Enter a string: ")
print("Uppercase:", user_input.upper())
print("Lowercase:", user_input.lower())


# 14
user_input1 = input("Enter a comma-separated sequence of words: ")
# Split the input into a list of words
words = user_input1.split(",")
# Convert the list to a set to remove duplicates and then back to a list
unique_words = list(set(words))
# Sort the list in alphabetical order
unique_words.sort()
# Print the sorted list
print("Sorted unique words:", ", ".join(unique_words))


# 15
def wrap_html_tag(word, tag="strong"):
    return f"<{tag}>{word}</{tag}>"


wrapped_word = wrap_html_tag("Python", "code")
print(wrapped_word)


# 16
def insert_string_in_middle(original_string, string_to_insert):
    mid_index = len(ostring) // 2
    return ostring[:mid_index] + string_to_insert + ostring[mid_index:]


ostring = "Hello World"
string_to_insert = "Python"
new_string1 = insert_string_in_middle(ostring, string_to_insert)
print(new_string1)


# 17
def four_copies_of_last_two_chars(string):
    if len(string) < 2:
        return "String must be at least 2 characters long"
    last_two_chars = string[-2:]
    return last_two_chars * 4


string = "hello"
new_string2 = four_copies_of_last_two_chars(string)
print(new_string2)


# 18
def get_first_three_chars(string):
    if len(string) < 3:
        return string
    else:
        return string[:3]


string1 = "hello"
new_string3 = get_first_three_chars(string1)
print(new_string3)


# 19
def get_last_part_before_character(string, character):
    index = string.rfind(character)
    if index == -1:
        return string
    else:
        return string[:index]


string2 = "Hello World!"
character = " "
last_part = get_last_part_before_character(string2, character)
print(last_part)


# 20
def reverse_if_multiple_of_four(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string


string3 = "abcdefg"
new_string4 = reverse_if_multiple_of_four(string3)
print(new_string4)
