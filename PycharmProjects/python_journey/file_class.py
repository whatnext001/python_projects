"""
A file can be open using a context manager
different methods can be used with the file variable e.g readlines,readline etc
"""

with open("fake_names.csv","r") as file:
    file_content = file.read(100)    #it takes a parameter of size i.e,  to specify the size or amount of data i want
                                     #to read at a go as in file.read(100)

    mult_content = file.readline()

    print(file_content)
    print(mult_content)

with open("new_csv_file","w") as w_file:
    writer_var = w_file.write("this is a new text")
    print(writer_var)

with open("fake_names.csv","r") as file:
    with open("fake_names.csv","w") as w_file:
        for items in file:
            w_file.write(items)
