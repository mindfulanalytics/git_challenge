# 1. Define a class called Apple with four instance variables that represent four attributes of an apple.

# class Apple:
#     def __init__(self, w, c, t, s):
#         self.weight = w
#         self.color = c
#         self.type = t
#         self.shape = s
#         print("Created!")
#
# ap1 = Apple(10, "Dark red", "Fuji", "Sphere")
# print(ap1)

# 2. Create a Circle class with a method called area that calculates and returns its area.
# Then create a Circle object, call area on it, and print the result.
# Use Python's pi function in the built-in math module.

# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius  # radius in centimeters
#         print("Created!")
#
#     def calculated_area(self):
#         return (self.radius ** 2) * math.pi
#
#
# a_circle = Circle(10)
# print(a_circle.calculated_area())

# 3. Create a TRIANGLE class with a method called AREA that calculates and returns its areas.
# Then create a TRIANGLE object, call AREA on it, and print the result

# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#         print("Created!")
#
#     def calculated_area(self):
#         return (self.base * self.height) / 2
#
# a_triangle = Triangle(10,10)
# print(a_triangle.calculated_area())

# 4. Make a hexagon class with a method called calculated_perimeter that calculates and returns its perimeter.
# Then create a hexagon object, call calculated_perimeter on it, and print the result.

class Hexagon:
    def __init__(self, side):
        self.side = side
        print("Created!")

    def calculated_perimeter(self):
        return self.side*6

a_hexagon = Hexagon(10)
print(a_hexagon.calculated_perimeter())


