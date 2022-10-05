# You can use regular expressions in Python with its built-in library, re (regular expressions)

# import re
#
# l = "Beautiful is better than ugly."
#
# matches = re.findall("Beautiful",l)
#
# print(matches)

# You can ignore case in the findall method by passing in re.IGNORECASE to the findall method as the third parameter

# You can use regular expressions in Python with its built-in library, re (regular expressions)
# import re
#
# l = "Beautiful is better than ugly."
#
# matches = re.findall("beautiful",l,re.IGNORECASE)
#
# print(matches)

# You can define a pattern that matches multiple characters by putting them iside of brackets in a regular expression.

# import re
#
# string = "Two too."
#
# m = re.findall("t[wo]o",
#                string,
#                re.IGNORECASE)
#
# print(m)

# You can match digits in a string with [[:digit:]]

# import re
#
# line = "123?34 hello?"
#
# m = re.findall("\d",
#                line,
#                re.IGNORECASE)
#
# print(m)

# An asterisk is greedy, which means that it will try to match as much text as it can.
# You can follow an asterisk with a question mark to make the regex non-greedy.

# import re
#
# t = "__one__two__three__"
#
# found = re.findall("__.*__", t)
#
# for match in found:
#     print(match)

# You can create the game Mad Libs, paragraph of text with various words missing that the players are prompted to fill in.

import re


text = """Giraffes have aroused
 the curiosity of __PLURAL_NOUN__
 since earliest times. The
 giraffe is the tallest of all
 living __PLURAL_NOUN__, but
 scientists are unable to
 explain how it got its long
 __PART_OF_THE_BODY__. The
 giraffe's tremendous height,
 which might reach __NUMBER__
 __PLURAL_NOUN__, comes from
 it legs and __BODYPART__.
"""


def mad_libs(mls):
    """
    :param mls: String
    with parts the user
    should fill out surrounded
    by double underscores.
    Underscores cannot
    be inside hint e.g., no
    __hint_hint__ only
    __hint__.
    """
    hints = re.findall("__.*?__",
                      mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {}"\
                   .format(word)
            new = input(q)
            mls = mls.replace(word,
                              new,
                              1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("invalid mls")

mad_libs(text)