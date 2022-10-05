# 1. Create Rectangle and Square classes with a method called calculate_perimeter
# that calculates the perimeter of the shapes they represent.
# Create Rectangle and Square objects and call the method on both of them.

# class Rectangle:
#     def __init__(self, w, l):
#         self.width = w
#         self.length = l
#         print("Created!")
#
#     def calculate_perimeter(self):
#         return (self.width * 2) + (self.length * 2)
#
# class Square:
#     def __init__(self,l):
#         self.length = l
#
#     def calculate_perimeter(self):
#         return self.length * 4
#
#
# rec_1 = Rectangle(5,5)
# print(rec_1.calculate_perimeter())
# sq_1 = Square(10)
# print(sq_1.calculate_perimeter())

# Define a method in Square class called change_size that allows you to pass in a number that increases or decreases
# (if the number is negative) each side of a Square object by that number

# class Square:
#     def __init__(self,l):
#         self.length = l
#
#     def calculate_perimeter(self):
#         return self.length * 4
#
#     def change_size(self, d):
#         self.difference = d
#         return self.length + self.difference
#
# sq_1 = Square(10)
# print(sq_1.change_size(10))

# 3. Create a class called Shape. Define a method in it called what_am_i that prints "I am a shape" when called.
# Change your Square and Rectangle classes from the previous challenges to inherit from Shape, create Square
# and Rectangle objects, and call the new method on both of them.

# class Shape():
#
#     def what_am_i(self):
#         print("I am a shape")
#
#
# class Rectangle(Shape):
#     def __init__(self, w, l):
#         self.width = w
#         self.length = l
#
#     def calculate_perimeter(self):
#         return (self.width * 2) + (self.length * 2)
#
#
# class Square(Shape):
#     def __init__(self, l):
#         self.length = l
#
#     def calculate_perimeter(self):
#         return self.length * 4
#
#
# a_rectangle = Rectangle(5,5)
# a_square = Square(10)
# print(a_rectangle.what_am_i())
# print(a_square.what_am_i())

# 4. Create a class called Horse and a class called Rider. Use composition to model a horse that has a rider.

class Horse():
    def __init__(self,name):
        self.name = name

class Rider():
    def __init__(self, name):
        self.name = name

the_rider = Rider("Jack Sparrow")
the_horse = Horse("Butter")

print("The name of the Horse is {}.".format(the_horse.name))
print("The name of the Rider is {}.".format(the_rider.name))
