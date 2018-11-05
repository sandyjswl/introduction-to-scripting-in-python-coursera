"""
Demonstration of how to call functions.
"""

# Function that we can call
def useless(input1, input2, input3):
    """
    This function takes three arguments and always returns 3.
    """
    return 3

# Calling the function
useless(1, 2, 3)

# Calling the function and printing the result
print(useless(4, 5, 6))

# Calling the function and assigning the result to a variable
result = useless(7, 8, 9)
print(result)

# You must pass the right number of arguments
# useless()
# useless(1)
# useless(1, 2)
