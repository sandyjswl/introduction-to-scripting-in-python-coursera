"""
Demonstration of logical expressions.
"""

# Boolean values are True and False
value1 = True
value2 = False
print(value1, value2)

print("")

# Logical NOT
print("Logical NOT")
print("===========")
print(not value1)
print(not value2)

print("")

# Logical AND
print("Logical AND")
print("===========")
print(value1 and value1)
print(value1 and value2)
print(value2 and value2)

print("")

# Logical OR
print("Logical OR")
print("==========")
print(value1 or value1)
print(value1 or value2)
print(value2 or value2)

print("")

value3 = True
value4 = True

print(value2 or ((value1 and value4) or value3))
