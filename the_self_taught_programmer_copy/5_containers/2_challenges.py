# 1. CREATE A LIST OF YOUR FAVORITE MUSICIANS

# fav_musicians = ["Bad Bunny", "Maluma", "Residente"]
# print(fav_musicians)

# 2. CREATE A LIST OF TUPLES, WITH EACH TUPLE CONTAINING THE LONGITUDE AND LATITUDE OF SOMEWHERE YOU'VE LIVED OR VISITED

# locations = []
#
# tijuana = (32.5149, 117.0382)
# san_diego = (32.7157, 117.1611)
#
# locations.append(tijuana)
# locations.append(san_diego)
#
# print(locations)

# 3. CREATE A DICTIONARY THAT CONTAINS DIFFERENT ATTRIBUTES ABOUT YOU: HEIGHT, FAVORITE COLOR, FAVORITE AUTHOR, ETC.

# my_dictionary = {"birth_day":
#                  "1993-04-06",
#                  "born_in":
#                  "Tijuana, B.C. Mexico",
#                  "height":
#                  "5'9",
#                  "fav_color":
#                  "blue",
#                  "fav_author":
#                  "Frank Herbert"}
#
# print(my_dictionary)

# 4. WRITE A PROGRAM THAT LETS THE USER ASK YOUR HEIGHT, FAV COLO, OR FAV AUTHOR, AND RETURNS THE RESULT FROM THE
# DICTIONARY YOU CREATED IN THE PREVIOUS CHALLENGE.

# question = input("What about me do you want to know? Type: height, fav_color or fav_author? ")
#
# question = str(question)
#
# if question == "height":
#     print(my_dictionary["height"])
# elif question == "fav_color":
#     print(my_dictionary["fav_color"])
# elif question == "fav_author":
#     print(my_dictionary["fav_author"])
# else:
#     print("Please try again.")

# 5. CREATE A DICTIONARY MAPPING YOUR FAVORITE MUSICIANS TO A LIST OF YOUR FAVORITE SONGS BY THEM

my_fav_artist_songs = {"Bad Bunny":
                       ["Titi me pregunto",
                        "Efecto",
                        "Callaita"],

                       "Maluma":
                       ["Felices los 4",
                        "Hawai",
                        "Madrid"],

                       "Residente":
                       ["Atrevete-te-te",
                        "Un beso de desayuno",
                        "Rene"]
                       }
print(my_fav_artist_songs)

# LISTS, TUPLES AND DICTIONARIES ARE JUST A FEW OF THE CONTAINERS BUILT INTO PYTHON.
# RESEARCH PYTHON SETS (A TYPE OF CONTAINER). WHEN WOULD YOU USE A SET?

# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable, unindexed, and do not allow for duplicate values.
# Once created, you cannot change its items, but you can remove and add new items.
# They are written with curly brackets, like dictionaries, but there are no pairings.

# You can use a set when you need uniqueness of elements, don't care for order, and you don't want to allow for updates.
# Use when all that matters is whether something is in the collection or not.

# You can use it to find the unique elements in a collection of elements.
# Also, to find the interesection of two collections of elements