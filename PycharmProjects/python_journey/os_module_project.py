
import os

def list_items():
    items = os.listdir()
    print(f"\nFiles and Directories in '{os.getcwd()}':")
    for item in items:
        print("-", item)

def create_directory():
    name = input("Enter new directory name: ")
    if not os.path.exists(name):
        os.mkdir(name)
        print(f"Directory '{name}' created.")
    else:
        print(f"Directory '{name}' already exists.")


def rename_item():
    old_name = input("Enter current file/folder name: ")
    new_name = input("Enter new name: ")
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed '{old_name}' to '{new_name}'.")
    else:
        print(f"'{old_name}' does not exist.")


def delete_item():
    name = input("Enter file/folder name to delete: ")
    if os.path.exists(name):
        if os.path.isfile(name):
            os.remove(name)
        else:
            os.rmdir(name)
        print(f"'{name}' has been deleted.")
    else:
        print(f"'{name}' does not exist.")


def change_directory():
    path = input("Enter directory name to move into: ")
    if os.path.isdir(path):
        os.chdir(path)
        print(f"Moved into directory '{path}'.")
    else:
        print(f"'{path}' is not a directory.")


def main():
    while True:
        print("\n========== File Manager ==========")
        print("1. List files and folders")
        print("2. Create new folder")
        print("3. Rename file/folder")
        print("4. Delete file/folder")
        print("5. Change directory")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            list_items()
        elif choice == '2':
            create_directory()
        elif choice == '3':
            rename_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            change_directory()
        elif choice == '6':
            print("Exiting File Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()


