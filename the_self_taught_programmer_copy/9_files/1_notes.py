# You can use python to read data from files and write data to a file.
# Reading data from a file means accessing the file's data.
# Writing data from a file means adding or changing data in the file.

# The first step to working with a file is to open it with Python's built-in OPEN function.
# The path to a file, or file path, represents the location on your computer where a file resides.
# You should always create file paths using Python's built-in OS MODULE
# The path function in it take each folder in a file path as a parameter and builds the file path for you:
# The path function ensures file paths will work on any operating system

# import os
# x = os.path.join("Users",
#              "bob",
#              "st.txt")
#
# print(x)

# The mode you pass to the open function determines the actions you will be able to perform on the file you open.
# "r" opens a file for reading only
# "w" opens a file for writing only
# "w+" opens a file for reading and writing

# The opne function returns an object, called a file object
# The open function create a new file if it doesn't already exist in the directory your program is running in
# You can use the write method to write to the file, and the close method to close it

# st = open("st.txt", "w")
# st.write("Hi from Python!")
# st.close()

# There is a preferred syntax to open file that prevents you from having to remember to close them.
# You put all your code that needs access to the file object inside a WITH-STATEMENT


# with open("st.txt", "w") as f:
#     f.write("Hello from Python!")

# If you want to read the file, you pass in "r" as the second parameter to open.
# Then you call the READ method on your file object

# with open("st.txt", "r") as f:
#     print(f.read())

# You can only read on a file once, without closing and reopening it to get its contents,
# so you should save the file contents in a variable or cntainer if you need to use them later in your program

# my_list = list()
#
# with open("st.txt", "r") as f:
#     my_list.append(f.read())
#
# print(my_list)

# Python comes with a built-in module that allows you to work with CSV files.
# CSV stands for Comma separated Values
# A delimeter is a symbol, like a comma or a vertical bar |, use dto reparate data in a CSV file

# You can use a with-STATEMENT to open a CSV file,
# and within you need to use the CSV modeule to convert the file object into a csv object
# The csv module has a method called writer that accepts a file object and a delimeter.
# The WRITERROW method accepts a list as a parameter, and you can use it to write to a CSV file.
# WRITERROW only creates one row, so you have to call it twice to create two rows

# import csv
#
# with open("st.csv", "w", newline='') as f:
#     w = csv.writer(f,
#                    delimiter=",")
#     w.writerow(["one",
#                 "two",
#                 "three"])
#     w.writerow(["four",
#                "five",
#                "six"])

import csv

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
