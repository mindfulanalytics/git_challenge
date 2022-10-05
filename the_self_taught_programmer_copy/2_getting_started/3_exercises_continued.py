# A COMMENT is a line in plain english that explains what a line of code does

# This is a comment
# print("Hello, World!")

# print Hello, World
# print("Hello, World!")
#
# import math
#
# # length of a diagonal
# l = 4
# w = 10
# d = math.sqrt(l**2 + w**2)
# print(d)

# for i in range(100):
#     print("Hello, World!")

# In the code above, print is indented four spaces. It let's python know when blocks of code begin and end. More readable.

#pythong groups data into different categories, called DATE TYPES.

# Each data value is called an OBJECT. Think of an object as a data value in Python with three properties: identity, data type and value.

# An object's identity its location in your computer's memory.
# The data type is the category of data the object belongs to.
# The value of an object is the data it represents.

# A STR, short for STRING, is a sequence of one or more characters surrounded by quotes "string"
# A CHARACTER is a single symbol, like a or 1.
# Whole numbers have the data type INT, short for INTEGER
# Decimal numbers have a data type called FLOAT, they are FLOATING-POINT NUMBERS
# Objects with a bool data type are called BOOLEANS
# Objects with a data type NONETYPE always have the value NONE, they represent the abscence of value

# You can use python to do math, just like you would in a calculator

# A CONSTANT is a value that never changes
# A VARIABLE referes to a value that can change. A variable consists of a name made up of one or more characters.
# The name is assigned a value using the ASSIGNMENT OPERATOR (the = sign)

# Python has a special syntax for when you want to INCREMENT (increase) or DECREMENT (decrease) the value of a variable


# Instead of:
# x = 10
# x = x + 1
# print(x)

# Use the increment operator

# x = 10
# x += 1
# print(x)
#
# # Instead of:
# x = 10
# x = x - 1
# print(x)
# Use the decrement operator
# x = 10
# x -= 1
# print(x)

# Variables are not limited to storing integer values. They can refer to any data type:

# hi = "Hello, World!"
# print(hi)

# When naming variables follow these 4 rules:
# 1. Variables can't have spaces.
# 2. Variable names can only contain letters, numbers and the underscore symbols.
# 3. You cannot start a variable name with a number.
# 4. You cannot use python keywords for variable names.

# SYNTAX is the set of rules, principles, and processes that govern the structure of sentences in a given language, specially word order.
# The English language has syntax, and so does python

# If you write a Python program and disregard Python's syntax, you will get one or more errors when you run your program.

# SYNTAX ERRORS are fatal. A program cannot run with a syntax error.
# Although errors look intimidating, they happen all the time.

# Python has two kinds of errors: SYNTAX ERRORS and EXCEPTIONS
# Any error that is not a syntax error is an exception.
# ZERODIVISIONERROR is an exception that occurs if you try dividing by zero.

# In order to do simple arithmetic operations, you use symbols and they are called OPERATORS
# One category of operators is ARITHMETIC OPERATORS, see page 27 for a list of them
# The values on either side of an operator are called OPERANDS.
# Together, two operands and an operator form an EXPRESSION.
# When your program runs, Python evaluates each expression and returns a single value.

# The ORDER OF OPERATIONS is a set of rules used in mathematical calcuations to evaluate an expression.
# Remember Please Excuse My Dear Aunt Sally? PEMDAS, is an acronym to help you remember the order of operations in math equations.
# Paraantheses, exponents, multiplication, division, addition and subtraction. Parentheses outrank exponents.

# COMPARISON OPERATORS are another category of operators in Python, and they evaluate expressions to either TRUE or FALSE.
# See page 30 for a detailed list of COMPARISON OPERATORS
# >, <, >=, <=, == equal, != not equal

# LOGICAL OPERATORS are another category. They also evaluate to TRUE or FALSE.
# AND, OR, NOT
# You can use multiple AND or OR keywords in one statement

# The keywords IF, ELIF and ELSE are used in CONDITIONAL STATEMENTS.
# Conditional statements are type of CONTROL STRUCTURE: a block of code that makes decisions by analyzing the values of variables.
# A conditional statement is code that can execute additional code conditionally

# There are IF-STATEMENTS, ELSE-STATEMENTS and together they form IF-ELSE STATEMENTS

home = "America"
if home == "America":
    print("Hello, America!")
else:
    print("Hello, World!")

# You can have multiple if-statements in a row
# You cannot use else-statement on its own

# You can use the ELIF keyword to create ELIF-STATEMENTS.
# ELIF stands for else if, and they can indefinitely be added to if-else statements to allow it to make additional decisions.

# A STATEMENT is a technical term that describes various parts of the Python language.
# You can think of a Python statement as a command or calculation.

# Python has two kinds of statements: SIMPLE STATEMENTS and COMPOUND STATEMENTS
# Simple statements generally span one line of code, whereas compound statements generally span multiple lines.

# Compound statements are made up of one or more CLAUSES.
# A clause consists of two or more lines of code: a HEADER followed by a SUITE(S)
# A HEADER is a line of code in a claise that contains a keyword, followed by a colon and a sequence of one or more lines of indented code.
# A SUITE is just a line of code in a clause. The header controls the suites.

# Spaces between statements do not affect the code
