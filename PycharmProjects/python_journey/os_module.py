import os

print(dir(os)) #this shows all the available modules to use with the os module

cur_list = os.getcwd() #getcwd- get current working directory

change_dir = os.chdir('/Users/ADMIN/PycharmProjects/')

walk_var = os.walk('C:/Users/ADMIN/PycharmProjects/') #os.walk works like a tree diagram,
                        # it print all directories and files inside a directory recursively, it takes three arguments

for dirpath,dirnames,filenames in walk_var:
    print("Current path:", dirpath)
    print("Directories:", dirnames)
    print("Filenames:", filenames)
    print("-" * 40)


print(cur_list)
print(change_dir)

file_check = os.path.exists("C:/Users/ADMIN/PycharmProjects/") #os.path.exists method check if a file exist or not
if file_check == True:
    print("File Exist")
else:
    print("File does not Exist!")