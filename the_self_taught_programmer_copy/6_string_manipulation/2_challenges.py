# 1. PRINT EVERY CHARACTER IN THE STRING "CAMUS"

# author = "Camus"
# print(author[0])
# print(author[1])
# print(author[2])
# print(author[3])
# print(author[4])

# 2. WRITE A PROGRAM THAT COLLECTS TWO STRINGS FROM A USER, INSERTS THEM INTO THE STRING
# "Yesterday I wrote a [response_one]. I sent it to [response_two]!" and prints a new string

# r1 = input("Enter a response:")
#
# r2 = input("Enter a response:")
#
# r = """Yesterday I wrote a {}. I sent it to {}!
#     """.format(r1, r2)
#
# new_string = "Let's hope for the best!"
# print(r)
# print(new_string)

# 3. Use a method to make the string "aldous Huxley was born in 1894."
# gramatically correct by capitalizing the first letter in the sentence.

# capitalize = "aldous Huxley was born in 1894.".capitalize()
#
# print(capitalize)

# 4. Take the string "Where now? Who now? When now?" and call a method that returns a list that looks like:
# ["Where now?", "Who now?", "When now?"]

# x = "Where now? Who now? When now?".split("? ")
#
# print(x)

# 5. Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn it into a grammatically correct string.
# There should be a space between each word, but no space between the word fence and the period that follows it.
# Don't forget, you learned a method that turns a list of strings into a single string.)

# words = ["The",
#          "fox",
#          "jumped",
#          "over",
#          "the",
#          "fence",
#          "."]
#
# words = " ".join(words)
#
# words = words.replace(" .", ".")
#
# print(words)

# 6. REPLACE EVERY INSTANCE OF "s" in "A screaming comes across the sky." with a $ dollar sign

# sentence = "A screaming comes across the sky."
# sentence = sentence.replace("a", "$")
# print(sentence)

# 7. Use a method to find the first index of the character "m" in the string "Hemingway"

# x = "Hemingway".index("m")
# print(x)

# 8. Find dialogue in your favorite book (containing quotes" and turn into into a string

# x = """\"You know, don't you, Sheena took the Van Gogh paiting from... your sleeping chamber\"
# Why does that hurt?
# \"I notice it was missing.\"
# \"She said she was borrowing it for her room in the ship.\"
# Murbella's lips went thin."""
# print(x)

# 9. Create the string "three three three" using concatenation, and then again using multiplication.

# string = "three " + "three " + "three"
# print(string)
# string2 = "three "*3
# string2 = string2.strip()
# print(string2)

# 10. Slice the string "It was bright cold day in April, and the clocks were striking thirteen"

x = "It was bright cold day in April, and the clocks were striking thirteen"
print(x[:31])
