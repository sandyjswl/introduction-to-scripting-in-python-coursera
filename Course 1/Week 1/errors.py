"""
Examples of common errors in Python
"""

# Remember you can use ctrl+k to comment a block of code and
# ctrl+shift+k to uncomment a block of code



# Syntax errors correspond to problems where your code doesn't follow the rules
# for writing valid Python programs.  Note that these errors arise
# before Python tries to run your code



print "To error is human, to forgive is divine"

# In Python 2, print was a statement and didn't need parentheses
# In Python 3, print is a function and its arguments should be enclosed in parentheses
# For those moving from Python 2 to Python 3, this syntax error will be extrememly common



#print("To error is human, to forgive is divine")

# As you enter expressions in Python, you will sometimes forget to include
# matching parentheses, quotations, brackets, etc.
      
# When you get a syntax error, always check whether you have matched up pairs correctly.
# Note that CodeSkulptor tries to help you with this task via coloring.  
# The right parenthesis is colored red to indicate an issue.



#print_quote = True
#if print_quote:
#    print("To error is human, to forgive is divine")
#else:
#    pass
#print_quote = False      
      
      
# Note that sometimes Python doesn't detect a syntax error until it's moved on to 
# processing the next line in your program.  If the line marked as having an error looks OK,
# be sure to check your previous line of code for problems.

# Here the previous else clause is missing its body.  Since Python requires each if-else 
# clause to have a body, we can insert a "pass" statement that does nothing.



# Syntax errors happen while Python is trying to parse your program into a recognizable form.
# A second class of errors happen while Python is running your code. Here are a few examples.

      
      
#pope_quote = "To error is human, to forgive is divine"
#print(pope_quote)

# Name errors corresponds to issues where Python is trying to find a value for one
# of the variables in your code and doesn' have one.  In that case, Python tells
# you that your variable is not defined.

# The most common cause of this error is misspelling a variable name.


#joe_ranking = 1
#print("Joe is number " + str(joe_ranking) + " coder.")

# Python loves to use the same operator on as many different types of data as possible.
# The + operator can be used to add numbers as well as add string (via concatenation)
# However, Python does know how to add a number and a string.  
# Here, Python threw a Type error to indicate this fact. 

# To fix this error, you can convert joe_ranking to a string using str().








