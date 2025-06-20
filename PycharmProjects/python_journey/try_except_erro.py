"""
In Python, try and except are used for exception handling,
which helps you deal with errors gracefully without crashing your program.

    try:
         # Code that might cause an error
    except SomeException:
        # Code that runs if there is an error

    try:
         # Code that might cause an error
    except Exception: #this is a general exception name without being specific of the particular error
        # Code that runs if there is an error

"""

"""
Here’s a list of some common exception errors in Python,
| **Exception**         | **Description**                                                                        |
| --------------------- | -------------------------------------------------------------------------------------- |
| `ZeroDivisionError`   | Raised when a number is divided by zero.                                               |
| `ValueError`          | Raised when a function receives an argument of the right type but inappropriate value. |
| `TypeError`           | Raised when an operation is performed on an inappropriate type.                        |
| `IndexError`          | Raised when a list index is out of range.                                              |
| `KeyError`            | Raised when a dictionary key is not found.                                             |
| `NameError`           | Raised when a variable is not defined.                                                 |
| `AttributeError`      | Raised when an invalid attribute reference is made.                                    |
| `FileNotFoundError`   | Raised when a file or directory is requested but doesn’t exist.                        |
| `ImportError`         | Raised when an import fails.                                                           |
| `ModuleNotFoundError` | Raised when a module can’t be found (a subclass of `ImportError`).                     |
| `IndentationError`    | Raised for incorrect indentation.                                                      |
| `SyntaxError`         | Raised when the parser encounters invalid syntax.                                      |
| `RuntimeError`        | Raised when an error doesn't fall into any other category.                             |
| `StopIteration`       | Raised when the `next()` function reaches the end of an iterator.                      |

"""

# try:
#     with open("you.txt","r") as no_file:
#         user_read = no_file.read()
#         var_1 = vars_var
#
# except FileNotFoundError:
#     print("The file does not exist")
#
# except Exception:
#     print("variable error")


#this is another use case
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That was not a valid number!")



try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError as error: #this is customized and assigned to a name called error,instead of specifying the error stated by the developer
    print(error)
except ValueError as error:
    print(error),


"""
Optional: else and finally
else: Runs if no error occurred in the try block.

finally: Always runs, whether or not an error occurred.
"""

try:
    print("Trying something risky...")
    result = 10 / 2
except ZeroDivisionError:
    print("Oops, division by zero!")
else:
    print("No error occurred, result is:", result)
finally:    #this will run irrespective of the error
    print("This will always run.")


