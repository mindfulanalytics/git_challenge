# In this chapter, you will find out how to store objects in containers.
# Containers are like filling cabinets, they keep your data organized.
# You will learn three commonly used contaners: lists, tuples, and dictionaries.

# Methods are functions closely associated with a given type of data.
# Unlike a function, you call a method on an onject.

# print("Hello".upper())
#
# print("Hello".replace("o", "@"))

# A list is a container that sorts objects in a specific order
# You can create a list with the LIST function, or with brackets []

# fruit = ["Apple", "Orange", "Pear"]
# print(fruit)

# Add a new item to a list using the append method:


# fruit = ["Apple", "Orange", "Pear"]
# fruit.append("Banana")
# fruit.append("Peach")
# print(fruit)

#Lists can store any data type

# random = []
# random.append(True)
# random.append(100)
# random.append(1.1)
# random.append("Hello")
# print(random)

# Strings, lists and tuples are ITERABLE. An object is ITERABLE when you can access each item using a loop.
# Each item in an iterable has an INDEX, a number representing the item's position in the iterable.

# fruit = ["Apple", "Orange", "Pear"]
# print(fruit[0])

# Lists are MUTABLE. When a container is mutable, you can add or remove objects from the container.

# colors = ["blue", "green", "yellow"]
# print(colors)
# colors[2] = "red"
# print(colors)

# You can remove the last item from a list using the method POP:

# colors = ["blue", "green", "yellow"]
# print(colors)
# item = colors.pop()
# print(item)
# print(colors)

# YOU CAN CHECK IF AN ITEM IS IN A LIST WITH THE KEYWORD IN:

# colors = ["blue", "green", "yellow"]
# print("green" in colors)

# Use the keyword NOT to cjeck if an item is not in a list:

# colors = ["blue", "green", "yellow"]
# print("black" not in colors)
#
# # You can get the size of a list (the number of items in it) with the LEN function
#
# print(len(colors))

# Example of a list being used in practice

# colors = ["purple",
#           "orange",
#           "green"]
#
# guess = input("Guess a color:")
#
# if guess in colors:
#     print("You guessed correctly!")
# else:
#     print("Wrong! Try again.")

# A TUPLE is a container that stores objects in a specific order. Unlike lists, tuples are IMMUTABLE,
# which means their contents cannot change. Once you create a tuple,
# you cannot modify the value of any of the items in it, add new items to it, or remove items from it.

# my_tuple = tuple()
# print(my_tuple)
#
# # OR
#
# my_tuple = ()
# print(my_tuple)
#
# rndm = ("M. Jackson", 1958, True)
# print(rndm)

# Even if a tuple has on item in it, you need to put a comma after it.
# To differentiate between number inside a parentheses.

# If you try to change an object in a tuple after you've created it, Python will raise an exception.

# dys = ("1984",
#        "Brave New World",
#        "Farenheit 451")
#
# dys[1] = "Handmaid's Tale"

# You can get items froom a tuple by referencing an index:

# dys = ("1984",
#        "Brave New World",
#        "Farenheit 451")
# print(dys[2])

# You can check if an item is in a tuple using the keyword in:

# dys = ("1984",
#        "Brave New World",
#        "Farenheit 451")
# print("1984" in dys)

# Put the keyword NOT before IN to check if an item is not in a tuple:

# dys = ("1984",
#        "Brave New World",
#        "Farenheit 451")
# print("Handmaid's Tale" not in dys)

# TUPLES are useful when you are dealing with values you know will never change,
# and you want to ensure other parts of your program won't change them.

# Tuples - unlike lists - can be used as keys in dictionaries.

# DICTIONARIES are another built-in container for storing objects. They are useful to link one object,
# called a KEY, to another object, called the VALUE.
# Linking one object to another is called MAPPING. The result is a KEY-VALUE PAIR.
# Dictionaries are mutable, you can add new key-value pairs to them

# Dictionaries are represented with curly brackets. There are two syntaxes for creating dictionaries:

# my_dict = dict()
# print(my_dict)

# OR

# my_dict = {}
# print(my_dict)

# fruits = {"Apple":
#           "Red",
#           "Banana":
#           "Yellow"}
# print(fruits)

# Dictionaries do not sotre they keys in order, and python prints the items in an arbitrary order

# Dictionaries are mutable. Once you've created a dictionary, you can add key-value pairs to it with the syntax
# [dictionary_name][[key]] = [value], and look up a value using a key with the syntax [dictionary_name][key]:

# facts = dict()

# add a value
# facts["code"] = "fun"
# look up a key
# print(facts["code"])

# add a value
# facts["Bill"] = "Gates"
# look up a key
# print(facts["Bill"])

# add a value
# facts["founded"] = 1776
# look up a key
# print( facts["founded"] )

# Any object can be a dictionary value. Unlike a value, a dictionary key must be immutable
# Usr the IN keyword to check if a key is in a dictionary. You cannot use the IN keyword to check values in a dictionary.
# Add the keyword NOT to In to check if a key is not in a dictionary

# You can delete a key-value pair from a dictionary with the keyword del:

books = {"Dracula": "Stoker",
         "1984": "Orwell",
         "The Trial": "Kafka"}

del books["The Trial"]
print(books)

# You can store container in other containers

lists = []

rap = ["Kanye West",
       "Jay Z",
       "Eminem",
       "Nas"]

rock = ["Bob Dylan",
        "The Beatles",
        "Led Zeppelin"]

djs = ["Zeds Dead",
       "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

# In the above example, lists has three indexes. Each index is a list. You can access these lists using their index.

# You can sotre a tuple inside a list, a list inside a tuple, and a dictionary inside of a list or a tuple: