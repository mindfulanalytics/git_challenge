# Imagine you wrote a program with 10,000 lines of code.
# If you put all of the code in one file, it would be difficult to navigate.
# Programmers solve this issue by dividing large programs into multiple pieces, called MODULES.
# Python allows you to use code from one module in another module.
# Python has built-in modules, modules that are built into Python and contain important functionality

# To use a module, you must first import it: which means writing code, so Python knows where to look for it

# The math module contains math-related functionality

# import math
#
# x = math.pow(2,3)
#
# print(x)

# The random module is another built-in module. You can use randit to generate a random integer between 2 integers

# import random
#
# x = random.randint(0,100)
#
# print(x)

# You can use the built-in statistics module to calculate the mean, median and mode in an iterable of numbers:

# import statistics
#
# nums = [1, 5, 33, 12, 46, 33, 2]
#
# # mean
# x = statistics.mean(nums)
# print(x)
# # median
# y = statistics.median(nums)
# print(y)
# # mode
# z = statistics.mode(nums)
# print(z)


# Use the built-in keyword module to check if a string is a python keyword:

import keyword

x = keyword.iskeyword("for")
print(x)

y = keyword.iskeyword("football")
print(y)