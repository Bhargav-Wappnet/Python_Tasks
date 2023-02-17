"""
Print the numbers of a specified list after removing even numbers from it.
Write a Python program to shuffle and print a specified list.
"""
import random
import itertools


def remove_even_numbers(numbers):
    # Create an empty list to store the odd numbers
    odd_numbers = []

    # Iterate over each number in the input list
    for number in numbers:
        # If the number is odd, add it to the odd_numbers list
        if number % 2 != 0:
            odd_numbers.append(number)

    # Return the list of odd numbers
    return odd_numbers


my_list = [12, 25, 36, 48, 3, 5, 7, 2, 4, 13, 22, 19]
print(my_list)
random.shuffle(my_list)
print(my_list)
odd_numbers = remove_even_numbers(my_list)
print(odd_numbers)

new_list = [1, 3, 4]
# Generate all permutations of the list
permutations_list = list(itertools.permutations(new_list))

# Print the permutations
print(permutations_list)
