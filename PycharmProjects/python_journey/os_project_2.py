from colorama import Fore,init
init(autoreset=True)

import os

print("--"*20)
print(Fore.GREEN + "A Mini Project On File Traversal.")
print("--"*20)

def current_location():
    cur_loc = os.getcwd()
    print(f"You're currently located in the {Fore.LIGHTCYAN_EX}{cur_loc}:")
current_location()

def list_files():
    lis_f = os.listdir()
    print(Fore.LIGHTCYAN_EX + "The list of files and directory are:")
    for items in lis_f:
        print(items)


def create_folder():
    user_in = input("Kindly enter the name of the folder you want to create: " )
    if not os.path.exists(user_in):
        os.mkdir(user_in)
        print(f"Directory {user_in} created successfully! ✅")
    else:
        print("Folder already exits. ❌")


print("--"*20)
def rename_item():
    old_f = input("Enter the old folder name: ")
    new_f = input("Enter the new folder name: ")
    if os.path.exists(old_f):
        ren_f = os.rename(old_f,new_f)
        print(f"{old_f} has been renamed to {new_f}. ✅✅ ")
    else:
        print("Old folder does not exist ❌❌")

def delete_item():
    del_in = input("Enter the folder/file to delete: ")
    if os.path.exists(del_in):
        if os.path.isfile(del_in):
            os.remove(del_in)
        else:
            os.rmdir(del_in)
            print(f"{del_in} has been removed. ✅✅✅")
    else:
        print(f"{del_in} does not exist. ❌❌❌")

def change_dir():
    change_in = input("Enter the directory to switch into:")
    if os.path.isdir(change_in):
        os.chdir(change_in)
        print(f"You are now in {change_in} directory.👌")
    else:
        print(f"{change_in} is not a directory.")


def main():
    while True:
        print(f"{Fore.GREEN} \n========== File Manager ==========")
        print("1. List files and folders")
        print("2. Create new folder")
        print("3. Rename file/folder")
        print("4. Delete file/folder")
        print("5. Change directory")
        print("6. Exit")

        choice = input(f"{Fore.CYAN}Enter your choice (1-6): ")

        if choice == '1':
            list_files()
        elif choice == '2':
            create_folder()
        elif choice == '3':
            rename_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            change_dir()
        elif choice == '6':
            print("Exiting File Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


main( )