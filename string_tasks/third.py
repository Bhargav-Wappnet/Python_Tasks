"""
21 Write a Python function to convert a given string to all uppercase if
it contains at least 2 uppercase characters in the first 4 characters.

22 Write a Python program to sort a string lexicographically.

23 Write a Python program to remove a newline in Python.

24 check whether a string starts with specified characters.

25 Write a Python program to create a Caesar encryption. Go to the editor

26 Write a Python program to display formatted text (width=50) as output.

27 remove existing indentation from all of the lines in a given text.

28 Write a Python program to add a prefix text to all of the lines in a string.

29 Write a Python program to set the indentation of the first line.

30 print the following floating numbers upto 2 decimal places.
"""
import textwrap  # used in 21 program.


# 21
def convert_to_uppercase(string):
    # Check if the first 4 characters contain at least 2 uppercase characters
    uppercase_count = 0
    for char in string[:4]:
        if char.isupper():
            uppercase_count += 1
    if uppercase_count >= 2:
        # Convert the string to all uppercase
        new_string = string.upper()
    else:
        new_string = string
    return new_string


original_string = "HeLLo, WorLD!"
new_string = convert_to_uppercase(original_string)
print(new_string)


# 22
def sort_lexicographically(string):
    sorted_string = ''.join(sorted(string))
    return sorted_string


string = "HellO world"
sorted_string = sort_lexicographically(string)
print(sorted_string)


# 23
def remove_newline(string):
    new_string = string.replace('\n', '')
    return new_string


string1 = '''hello
world'''
new_string = remove_newline(string1)
print(new_string)


# 24
def starts_with(string, prefix):
    if string.startswith(prefix):
        return True
    else:
        return False


string2 = "Hello, world!"
prefix = "Hello"
result = starts_with(string2, prefix)
print(result)


# 25
def caesar_encrypt(string, shift):
    result = ""
    for char in string:
        if char.isalpha():
            char_code = ord(char) + shift
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            result += chr(char_code)
        else:
            result += char
    return result


string3 = "Hello, world!"
shift = 3
encrypted = caesar_encrypt(string3, shift)
print(encrypted)

# 26

text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Duis pretium auctor mi, id tempus ex laoreet sit amet.
Maecenas luctus ex sed neque bibendum blandit.
Morbi ornare justo sit amet lobortis tempor.
Nulla facilisi. Cras eget nisi non enim consectetur lacinia.
Donec euismod, massa eget efficitur gravida,
sapien nisl aliquam quam, nec bibendum ipsum risus vitae risus.'''
print()
print(textwrap.fill(text, width=50))
print()


# 27
def remove_indentation(text):
    lines = text.split("\n")
    # Find the minimum indentation length
    min_indent = float('inf')
    for line in lines:
        if line.strip():
            indent_len = len(line) - len(line.lstrip())
            if indent_len < min_indent:
                min_indent = indent_len
    # Remove the minimum indentation from each line
    new_lines = []
    for line in lines:
        if len(line) >= min_indent:
            new_lines.append(line[min_indent:])
    return "\n".join(new_lines)


text1 = "   Hello, world!\n   How are you?\n   I'm doing well."
new_text = remove_indentation(text1)
print(new_text)


# 28
def add_prefix(text, prefix):
    lines = text.split("\n")
    new_lines = [f"{prefix}{line}" for line in lines]
    return "\n".join(new_lines)


text2 = "Hello\nWorld\n!"
prefixed_text = add_prefix(text2, "Prefix: ")
print(prefixed_text)


# 29
def set_indentation(text, indent):
    lines = text.split("\n")
    lines[0] = f"{indent}{lines[0].lstrip()}"
    return "\n".join(lines)


text = "Hello\n   World\n!"
indented_text = set_indentation(text, "\t")
print(indented_text)


# 30
x = 3.14159
y = 2.71828
print("x = {:.2f}, y = {:.2f}".format(x, y))
