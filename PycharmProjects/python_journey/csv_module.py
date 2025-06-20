import csv

#this will import the csv file and name it as csv_file
with open('random_users.csv','r') as csv_file:
    #csv_reader = csv.reader(csv_file)
    csv_reader = csv.DictReader(csv_file) #this will print out the csv in a dictionary format
    next(csv_reader) #the next will start the index from the first email and exclude the header

    with open('new_csv_file','w') as write_csv:
        csv_write = csv.writer(write_csv,delimiter="\t")#delimeter e.g ,.-\t can be specified


#iterating the csv_reader variable
        for line in csv_reader:
             print(line)
             print(line['First Name'])#passing the email will print out the list of email
            #csv_write.writerow(line) #this line will write into the new csv file that is created
            #print(line[2]) #to print out a row or index from the list