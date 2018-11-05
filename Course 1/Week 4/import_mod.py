"""
Demonstration of importing modules.
"""

# Import the math module (look in the Docs for help)
import math

# Import example module
import examples3_module as example

# Constants
print("Math constants")
print("==============")
print(math.pi)
print(math.e)
print("")

# Functions
print("Math functions")
print("==============")
print(math.sqrt(25))
print(math.trunc(14.83483))
print(math.sin(math.pi / 2.0))
print("")

# Dir
print("Dir")
print("===")
print(dir(math))
print(dir(example))
print("")

print(example.message)
print(math.__name__)
print(example.__name__)
