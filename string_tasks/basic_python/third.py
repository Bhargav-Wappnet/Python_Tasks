"""
Write a Python program to generate and print a list of
first and last 5 elements where the values are square of
numbers between 1 and 30 (both included),

Write a Python program to generate and print a list
except for the first 5 elements,
where the values are square of numbers between 1 and 30 (both included)

Write a Python program to generate all permutations of a list in Python.

"""

# generate a list of the square of numbers between 1 and 30 (both included)
squares = [i**2 for i in range(1, 31)]

# get the all after first 5 elements
except_five = squares[5:]

# get the first and last 5 elements of the list
first_five = squares[:5]
last_five = squares[-5:]

# print the first and last 5 elements of the list
print("First 5 elements:", first_five)
print("Last 5 elements:", last_five)

# print the except first five.
print("except first five : ", except_five)
