# FUNCTIONS are compound statements that can take input, execute instructions and return an output.
# Functions allow you to define and reuse functionality in your program.

# CONVENTION is an agreed upon way of doing things

# CALLING a function means giving the function the input it needs to execute its instructions and return an output
# Each input to a function is a PARAMETER
# Functions in Python are similar to mathematical functions

# f(x) = x * 2

# The left hand side of the statement above defines a function f, that takes one parameter, x.
# You invoke a function with the following syntax [function_name]([parameters_separated_by_commas)], for example: f(x)

# To create a function in Python you choose a function name, define its parameters, define what it does, and define what values the function returns.

# The keyword def TELLS python your are defining a function.
# By convention, never use capital letters in a function name, and words should be separated by underscores like_this.
# After the parentheses put a colon and start a new line indeted by four spaces.
# The keyword RETURN defines the value a function outputs when you call it

# def f(x):
#     return x * 2
# result = f(2)
# print(result)

# Python comes with a library of functions built into the programming language called BUILT-IN FUNCTIONS
# PRINT is an example, LEN returns the legth (number of characters) of an object
# STR function take an object and returns a new object with a str data type
# The INT function takes an object and returns an integer object.
# The FLOAT function takes an object and returns a float.
# Python will raise an exception if you try to pass a parameter the function cannot convert.

# INPUT is a built-in function that collects information from the person using the program:
# It takes a string as a parameter and displays it to the user, the user can then type a response into the shell,
# and you can save their response in a variable

# age = input("Enter your age:")
# int_age = int(age)
# if int_age < 21:
#     print("You are young!")
# else:
#     print("Wow, you are old!")

# Functions can encapsulate functionality you want to reuse:

# def even_odd(x):
#     if x % 2 == 0:
#         print("even")
#     else:
#         print("odd")
#
# result = even_odd(2)
# print(result)

# Functions allow you to write less code because you can reuse functionality. Your program is shorter and easier to read.

# n = input("type a number:")
# n = int(n)
#
# if n % 2 == 0:
#     print("n is even.")
# else:
#     print("n is odd.")


# def even_odd():
#     n = input("type a number:")
#     n = int(n)
#     if n % 2 == 0:
#         print("n is even.")
#     else:
#         print("n is odd.")
#
# even_odd()
# even_odd()
# even_odd()

# There are two types of parameters a function can accept, either required parameters or optional parameters. The names are self-exaplanatory.
# Optional parameters are defined with the following syntax: [function_name]([parameter_name] = [parameter_value])

# def f(x=2):
#     return x**x
#
# print(f())
# print(f(4))

# You can define a function with both required and optional parameters, but you must define all the required parameters first.

# Variables have an important property called scope. It refers to what part of your program can read and write to it.
# Reading a variable means finding its value.
# Writing a variable means changing its value.
# A variable's scope is defined by where it is defined.

# Global scope means a variable can be read or written to from anywhere in your program. Such variables are called global variables.
# If you define a variable inside a function (or class), it has local scope. Your program can only read or write to it in the function.

# Here are variables with global scope

# x = 1
# y = 2
# z = 3
#
# print(x)
# print(y)
# print(z)

# If you define these same variables inside of a function, you can only read or write to them from inside of that function

# def f():
#     x = 1
#     y = 2
#     z = 3
#     print(x)
#     print(y)
#     print(z)
#
# f()

# EXCEPTION HANDLING
# Relying on user input from the input function means you do not control the input to your program - the user does,
# and that input could cause an error.

# a = input("type a number:")
# b = input("type another:")
# a = int(a)
# b = int(b)
# print(a/b)

# If you input 0 as the second number you will run into a problem "ZeroDivisionError: division by zero"

#One way to solve this is to use exception handling, which allows you to test for error conditions,
# "catch" exceptions if they occur, and decide how to proceed.

# If you are in a situation where you think your code may raise and exception, use a compound statement with the keywords try and except to catch it.
# The try clause contains the error that could occur.
# The except clause contains code that will execute if the exception in your try clause occurs.

# a = input("type a number:")
# b = input("type another:")
# a = int(a)
# b = int(b)
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("b cannot be zero.")

# You program will also break if the user enters a string that cannot be converted to an integer. You can fix this.

try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Invalid input.")

# DOCSTRINGS

# When you write a function, it is good practice to leave a comment called a docstring at the top of the function explaining
# what data type each parameter needs to be.
# Docstrings expkain what the function does, and document what kinds of parameters it needs.

# Docstrings will help you program faster because you can read a docstring to figure out what a function does,
# instead of reading all the code.

def add(x, y):
    """
    Returns x + y
    :param x: int.
    :param y: int.
    :return: int sum of x and y
    """
    return x + y

 # Only save data in a variable if you are going to use it later
