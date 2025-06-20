# temperatures_f = [32.0, 64.0, 72.0, 79.8, 100.0, 130.5, 212.0]

# temp_f = []
#
# for a_temperature in range (len(temperatures_f)):
#     a_temperature = 5/9*(a_temperature - 32)
#
# print(temperatures_f)

from colorama import Fore


from colorama import Fore

print(Fore.RED + "This is red text")
print(Fore.GREEN + "This is green text")
print(Fore.YELLOW + "This is yellow text")


print(__name__)


def upper(*args):
    user_in = input("kindly enter your string")

    to_upper = user_in.upper()
    print(to_upper)

upper()


new = ord("a")
huun = chr(65)
print(huun)


# def count_up_to():
#     for nums in range(1,4):
#         print (nums)
#
# count_up_to()

count_up_to = (nums for nums in range(1,4))


print(next(count_up_to))
print(next(count_up_to))
print(next(count_up_to))



for char in "string":
    print(char.title())


