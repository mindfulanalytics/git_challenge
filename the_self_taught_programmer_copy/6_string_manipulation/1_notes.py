# Python has built-in functionality for manipulating strings
# Strings, like lists and tuples, are iterable.
# You can look up each character in a string with an index.

# author = "Kafka"
# print(author[0])
# print(author[1])
# print(author[2])
# print(author[3])
# print(author[4])

# If you try to look up a character past the last index in your string, Python raises an exception.

# print(author[5])

# Python also allows you to look up each item in a list with a negative index.
# You can use is to look up ites in an iterable from right to left instead of left to right.

# print(author[-1])

# Strings, like tuples, are immutable. You cannot change the characters in a string.
# If you want to change the characters in a string, you have to create a new string.

# ff = "F. Fitzgerald"
# ff = "F. Scott Fitzgerald"
# print(ff)

# You can add two (or more) strings together using the addition operator

# a = "cat" + "in" + "hat"
#
# b = "cat " + "in " + "the " + "hat"
# print(b)

# You can multiply a string by a number with the multiplication operator.

# c = "Sawyer" * 3
# print(c)

# You can change every character in a string to uppercase by calling the UPPER method.

# d = "We hold these truths...".upper()
# print(d)

# Similarily, you can change every character in a string to lowercase by calling LOWER.

# e = "SO IT GOES.".lower()
# print(e)

# You can capitalize the first letter of a sentence by calling the CAPITALIZE method.

# f = "four score and...".capitalize()
# print(f)

# You can create a new string using the FORMAT method,
# which looks for occurences of curly brackets {} in the string,
# and replaces them with the parameters you pass in.

# g = "William {}".format("Faulkner")
# print(g)

# You can also pass in a variable as a parameter.

# last = "Faulkner"
# h = "William {}".format(last)
# print(h)

# The FORMAT method is useful if you are creating a string from user input

# n1 = input("Enter a noun:")
# v = input("Enter a verb:")
# adj = input("Enter an adj:")
# n2 = input("Enter a noun:")
#
# r = """ The {} {} the {} {}
#     """.format(n1,
#                v,
#                adj,
#                n2)
# print(r)

# Strings have a method called SPLIT,
# which you can use to separate one string into two or more strings.

# i = "Hello.Yes!".split(".")
# print(i)

# The result is a list with two items in it:

# The JOIN method lets you add new characters between every character in a string:

# first_three = "abc"
# result = "+".join(first_three)
# print(result)

# You can turn a list of strings into a single string by calling the JOIN method on an
# empty string, and passing in the list as a parameter.

# words = ["The",
#          "fox",
#          "jumped",
#          "over",
#          "the",
#          "fence",
#          "."]
# one = "".join(words)
# print(one)

# You can create a string with each word separated by a space by calling the JOIN
# method on a string with a space in it:

# words = ["The",
#          "fox",
#          "jumped",
#          "over",
#          "the",
#          "fence",
#          "."]
# one = " ".join(words)
# print(one)

# You can use the STRIP method to remove leading and trailing whitespace from a string.

# s = "    The    "
# s = s.strip()
# print(s)

# The REPLACE method replaces every occurrence of a string with another string

# equ = "All animals are equal."
# equ = equ.replace("a", "@")
# print(equ)

# You can get the index of the first ocurrence of a character in a string with the INDEX method.

# j = "animals".index("m")
# print(j)

# Python raises an exception if the index method does not find a match:

# k = "animals".index("z")
# print(k)

# If you're not sure if you will find a match, you can use exception handling:

# try:
#     "animals".index("z")
# except:
#     print("Not found.")

# The IN keyword checks if a string is in another string, and returns either TRUE or FALSE.

# print("Cat" in "Cat in the hat.")
#
# print("Bat" in "Cat in the hat.")

# Put the keyword NOT in front of the IN to check if one string is not in another string.

# print("Potter" not in "Harry")
