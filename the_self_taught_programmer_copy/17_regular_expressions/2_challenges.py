# 1. Write a regular expression that matches the word Dutch in the Zen of Python

# import re
#
#
# zen = """The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!"""
#
# m = re.findall("Dutch",zen,re.MULTILINE)
#
# print(m)

# 2. Come up with a regular expression that matches all the digits in the string

# import re
# string = "Arizona 479, 479, 501, 870. California 209, 213, 650"
#
# m = re.findall("\d",string)
#
# print(m)

# 3. Create a regular expression that matches any word that start with any character and is followed by two o's.
# Then use Python's re module to match boo and loo in the sentence
# "The ghost that says boo haunts the loo."

import re

ghost = "The ghost that says boo haunts the loo."

m = re.findall(".oo",ghost)

print(m)