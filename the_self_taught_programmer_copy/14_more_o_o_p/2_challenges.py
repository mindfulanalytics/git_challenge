# 1. Add a square_list class variable to a class called Square so that every time you create a new Square object,
# the new object gets added to a list

# class Square():
#     square_list = []
#
#     def __init__(self, l):
#         self.length = l
#         self.square_list.append(self.length)
#
#     def calculate_perimeter(self):
#         return self.length * 4
#
#
# sq1 = Square(2)
# sq2 = Square(5)
# sq3 = Square(10)
#
# print(Square.square_list)

# 2. Change the Square class so that when you print a Square object, a message prints telling you the length
# of each of the fourse sides of the shape. For example, if you create a square with Square(29) and print it,
# Python should print 29 by 29 by 29 by 29.

# class Square():
#     square_list = []
#
#     def __init__(self, l):
#         self.length = l
#         self.square_list.append(self.length)
#
#     def calculate_perimeter(self):
#         return self.length * 4
#
#     def print_size(self):
#         print("{} by {} by {} by {}".format(self.length, self.length, self.length, self.length))
#
# Sq1 = Square(5)
# Sq1.print_size()

# 3. Write a function that takes two objects as parameters and returns True if they are the same object,
# and False if not.

def f(x,y):
    print(x is y)

f(1,1)