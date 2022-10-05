# A LOOP is a piece of code tha6 continually executes instructions until a condition defined in the code is satisfied.
# A FOR-LOOP is used to iterate through an iterable. This process is called iterating.
# You can define a FOR-LOOP using the syntax for [variable_name] in [iterable_name]:[instructions] where [variable_name]

# name = "Ted"
# for character in name:
#     print(character)

# Example of a FOR-LOOP to iterate though the items in a list:

# shows = ["GOT",
#          "Narcos",
#          "Vice"]
# for show in shows:
#     print(show)

# Example using a FOR-LOOP to iterate through the items in a tuple:

# coms = ("A. Development",
#         "Friends",
#         "Always Sunny")
# for show in coms:
#     print(show)

# You can use FOR-LOOPS to change the items in a mutable iterable, like a list:

# tv = ["GOT",
#       "Narcos",
#       "Vice"]
# i = 0
# for show in tv:
#     new = tv[i]
#     new = new.upper()
#     tv[i] = new
#     i +=1
#
# print(tv)

# Because accessing each item and its index in an iterable is so common; Python has another syntax

# tv = ["GOT",
#       "Narcos",
#       "Vice"]
# for i, show in enumerate(tv):
#     new = tv[i]
#     new = new.upper()
#     tv[i] = new
#
# print(tv)

# You can use the built-in range function to create a sequence of integers

# for i in range(1, 11):
#     print(i)

# WHILE-LOOPS are loops that executes code as long as an expression evaluates to TRUE

# x = 10
# while x > 0:
#     print('{}'.format(x))
#     x -= 1
# print("Happy New Year!")

# A loop that never ends is called an INFINITE LOOP. Be ready to press control-c in the python sheel to quit

# while True:
#     print("Hello, World!")

# You can use a BREAK-STATEMENT, a statement with the keyword break to terminate a loop

# for i in range(0,100):
#     print(i)
#     break

# You can use a WHILE-LOOP and the BREAK statement to write a program that keeps asking the user for input
# until they type q to quit


# qs = ["What is your name?",
#       "What is your fav color?",
#       "What is your quest?"]
# n = 0
# while True:
#     print("Type q to quit")
#     a = input(qs[n])
#     if a == "q":
#         break
#     n = (n+1) % 3 # Whenever the first number in an expression using modulo is smaller than the second,
#     # the answer is the first number

# You can use a CONTINUE-STATEMENT a statement with the keyword continue,
# to stop the current iteration of a loop and move on to the next iteration of it.

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# You can combine loops in various ways. For example, you can have one loop inside of a loop
# The loop with another loop inside it is called an outer loop, and the nested loop is called an inner loop

for i in range(1, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)