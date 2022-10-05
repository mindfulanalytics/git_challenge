# 1. Print each item in the following list:
# ["The Walking Deead", "Entourage", "The Sopranos", "The Vampire Diaries"]

# shows = ["The Walking Deead",
#          "Entourage",
#          "The Sopranos",
#          "The Vampire Diaries"]
# for show in shows:
#     print(show)

# 2. Print all the numbers from 25 to 50

# for i in range(25,51):
#     print(i)

# 3. Print each item in the list from the first challenge and their indexes

# shows = ["The Walking Deead",
#          "Entourage",
#          "The Sopranos",
#          "The Vampire Diaries"]
# for i, show in enumerate(shows):
#     print(i)
#     print(show)

# 4. Write a program with an infinite loop (with the option to type q to quit) and a list of numbers.
# Each item through the loop ask the user to guess a number on the list,
# and tell them whether or not they guessed correctly.

# numbers = [11, 32, 33, 15, 1]
#
# while True:
#     answer = input("Guess a number or type q to quit.")
#     if answer == "q":
#         break
#     try:
#         answer = int(answer)
#     except ValueError:
#         print("please type a number or q to quit.")
#     if answer in numbers:
#         print("You guessed correctly!")
#     else:
#         print("You guessed incorrectly!")

# Multiply all the numbers in the list [8, 19, 148, 4] with all the numbers in the list [9, 1, 33, 83],
# and append each result to a third list.

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
multiplied = []

for i in list_a:
    for j in list_b:
        multiplied.append( i * j)

print(multiplied)

