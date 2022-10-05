# 1 .WRITE A FUNCTION THAT TAKES A NUMBER AS AN INPUT AND RETURNS THAT NUMBER SQUARED

# def squared(x):
#     """
#     Returns x**2
#     :param x: int.
#     :return: int x squared
#     """
#     return x**2
# print(squared(2))

# 2. CREATE A FUNCTION THAT ACCEPTS A STRING AS A PARAMETER AND PRINTS IT

# def print_string(x):
#     """
#     Returns print(x)
#     :param x: string.
#     :return: print string x
#     """
#     print(x)
# print_string("Testing 1, 2, and 3.")

# 3. WRITE A FUNCTION THAT TAKES THREE REQUIRED PARAMETERS AND TWO OPTIONAL PARAMETERS.

# def req_opt(x,y, z, a = 2, b = 4):
#     """
#     Returns x + y +z + a + b
#     :param x: int.
#     :param y: int.
#     :param z: int.
#     :param a: int.
#     :param b: int.
#     :return: int sum of x, y, z, a, and b
#     """
#     return x + y + z + a + b
#
# print(req_opt(1,2,3))

# 4. Write a program with two functions.
# The first should take an integer as a parameter and return the result of the integer divided by 2.
# The second function should take an integer as a parameter and return the result of the integer multiplied by 4.
# Call the first function the result of a variable, and pass it as a parameter to the second function.

# def divide(x):
#     """
#     Returns x / 2
#     :param x: int.
#     :return: int x divided by 2.
#     """
#     return x / 2
#
# def multiply(x):
#     """
#     Returns x * 4
#     :param x: int.
#     :return: int x multiplied by 4.
#     """
#     return x * 4
#
# y = divide(4)
# z = multiply(y)
#
# print(z)

# 5. WRITE A FUNCTION THAT CONVERTS A STRING TO A FLOAT AND RETURNS THE RESULT,
# USE EXCEPTION HANDLING TO CATCH THE EXCEPTION THAT COULD OCCUR.

# x = input("Type a string:")
# def string_to_float(x):
#     """
#     Returns float(x)
#     :param x: int.
#     :return: converts integer inputs into floats
#     """
#     return float(x)
# try:
#     print(string_to_float(x))
# except ValueError:
#     print("The string must be an integer.")

# 6. ADD A DOCSTRING TO ALL OF THE FUNCTIONS YOU WROTE IN CHALLENGES 1-5
# DONE