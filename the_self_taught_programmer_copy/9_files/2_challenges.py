# 1. Find a file on your computer and print its contents using Python.

# import csv
# with open("/Users/diegogalanhoffman/Documents/Sample data.csv", "r") as f:
#     r = csv.reader(f,delimiter=",")
#     for row in r:
#         print(",".join(row))

# 2. Write a program that asks a user a question, and saves their answer to a file.

# with open("answer.txt", "w") as f:
#     f.write(input("What day is it?"))

# 3. Take the items in this list of lists: [["Top Gun", "Risky Business", "Minority Report"],
# ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
# and write them to a CSV file. The data from each list should be a row in the file,
# with each item in the list separated by comma.

import csv

with open("movies.csv", "w", newline='') as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(["Top Gun",
                "Risky Business",
                "Minority Report"])
    w.writerow(["Titanic",
                "The Revenant",
                "Inception"])
    w.writerow(["Training Day",
                "Man on Fire",
                "Flight"])

