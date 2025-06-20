import csv

with open("random_users.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    next(csv_reader)

    for line in csv_reader:
        print(line)


"""
A dictreader method can also be used
"""

with open("random_users.csv","r") as new_file:
    dict_reader = csv.DictReader(new_file)
    for rows in dict_reader:
        print(rows) #the key can also be used to access each items in the csv file, you can also set up a fieldname
                            #while writing to a new file
