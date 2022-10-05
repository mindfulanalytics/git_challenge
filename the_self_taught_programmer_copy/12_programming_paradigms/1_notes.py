# A programming paradigm is a style of programming.
# To program professionally, you need to learn either the object-oriented or functional programming paradigms.

# One of the fundamental differences between the various programming paradigms is the handling of state.
# State is the value of a program's variable while it is running.
# Global state is the value of a program's global variables while it is running.

# The procedural proogramming paradigm: a programming style in which you write a sequence of steps moving towards a solution
# You write code to "do this, then that"

# When you program procedurally, you store data in global variables and manipulate it with functions:

# rock = []
# country = []
#
# def collect_songs():
#     song = "Enter a song."
#     ask = "Type r or c. q to quit."
#
#     while True:
#         genre = input(ask)
#         if genre == "q":
#             break
#
#         if genre == "r":
#             rk = input(song)
#             rock.append(rk)
#
#         elif genre == "c":
#             cy = input(song)
#             country.append(cy)
#
#         else:
#             print("Invalid.")
#         print(rock)
#         print(country)
#
# collect_songs()

# Procedural programming is fine when building small programs like this, however, because you store all of your
# program's state in global variables, you rin into problem when your program becomes larger.
# The problem with relying on global variables is that they cause unexpected errors.
# Furthermore, this approach to programming relies on SIDE EFFECTS. A side effec is changing the state of a global variable.
# This problem led to the development of object-oriented and functional programming paradigms.

# Functional programming relies on functions that do not use or change global state,
# the only state they use are the parameters you pass to the function.
# Eliminating global state removes side effects and the problems that come with them.

# "Functional code is characterized by one thing: the absence of side effects. It doesn't rely on data outside the current function,
# and it doesn't change data that exists outside the current function" - Mary Rose Cook

# Example: Code with side effects

# a = 0
#
# def increment():
#     global a
#     a += 1

# Example: Code without side effects

# def increment(a):
#     return a + 1
#
# print(increment(1))

# One advantage of functional programming is that it eliminates an entire category of errors caused by global state.
# A disadvantage of cuntional programmingn is certain problems are easier to conceptualize with state.

# Object-oriented programming paradigm also addresses side effects by eliminating global state,
# but instead of storing state in functions, it is stored in objects.
# CLASSES define a set of objects that can interact with each other. CLASSES are mechanisms for the programmer
# to classify and group together similar objects.
# Every object is an instance of a class. You can use the terms objects and instances interchangeably.

# In Python, a class is a compound statement with a header and suites.
# By convention, classes in python always start with a capital letter, and you write them in CamelCase, e.g. FruitOrange

# A suite in a class can be a simple statement or a compound statement called a method.
# Methods are like functions, but you define them inside of a class,
# and you can only call them on the object the class creates.
# Method names, like function names, should be all lowercase with words separated by underscores, e.g. weight_in_kgs

# You define methods with the same syntax as funtions, with two differences: you must define a method as a suite in a class,
# and it has to accept at least one parameter
# By convention, you always name the first parameter of a method SELF

# You can use SELF to define an instance variable: a variable that belongs to an object

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

# Any method surrounded by double underscores like __init__ is called a magic method:
# a method Python uses for special purposes like creating an object.

# You can create a new Orange object with the same syntax you use to call a function
# Creating a new object is called instantiating a class:

# class Orange:
#     def __init__(self, w, c):
#         self.weight = w
#         self.color = c
#         print("Created!")
#
# or1 = Orange(10,"dark orange")
# print(or1)

# Once you've created an object, you can get the value of its instance variables

# class Orange:
#     def __init__(self, w, c):
#         self.weight = w
#         self.color = c
#         print("Created!")
#
# or1 = Orange(10,"dark orange")
# print(or1.weight)
# print(or1.color)

# You can change the value of an instance variable with the syntax

# class Orange:
#     def __init__(self, w, c):
#         self.weight = w
#         self.color = c
#         print("Created!")
#
# or1 = Orange(10,"dark orange")
# or1.weight = 100
# or1.color = "light orange"
#
# print(or1.weight)
# print(or1.color)

# You can use the ORANGE class to create multiple oranges

# class Orange:
#     def __init__(self, w, c):
#         self.weight = w
#         self.color = c
#         print("Created!")
#
# or1 = Orange(4,"light orange")
# or1 = Orange(8,"dark orange")
# or1 = Orange(14,"yellow")

# You can model things ORANGES do, like rot, with methods

# class Orange:
#     def __init__(self, w, c):
#         """weights are in oz"""
#         self.weight = w
#         self.color = c
#         self.mold = 0
#         print("Created!")
#
#     def rot(self, days, temp):
#         self.mold = days * temp
#
# orange = Orange(6, "orange")
# print(orange.mold)
# orange.rot(10,98)
# print(orange.mold)