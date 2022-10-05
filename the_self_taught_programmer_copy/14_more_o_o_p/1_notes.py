# In Python, classes are objects.
# Each class in Python is an object that is an instnce of class "type"

# class Square:
#     pass
#
# print(Square)

# The class Square is an object, and you printed it.

# Classes have two types of variables: class variables and instance variables.
# Instance variables belong to objects.

# class Rectangle():
#     def __init__(self, w, l):
#         self.width = w
#         self.len = l
#
#     def print_size(self):
#         print(""" {} by {}
#         """.format(self.width,self.len))
#
# my_rectangle = Rectangle(10, 24)
# my_rectangle.print_size()

# Class variables are useful. They allow you to share data between all of the instances of a class without relying on global variables.

class Rectangle():
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print(""" {} by {}
        """.format(self.width,self.len))

r1 = Rectangle(10, 24)
r1 = Rectangle(20, 40)
r1 = Rectangle(100, 200)

print(Rectangle.recs)