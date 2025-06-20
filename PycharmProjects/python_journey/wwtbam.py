from colorama import init, Fore
init(autoreset=True)

print("-" * 60)
print(Fore.GREEN + "🤑🤑🤑Welcome To Who Wants To Be A Millionaire🤑🤑🤑")
print("-" * 60)
question_1 = Fore.LIGHTWHITE_EX + f"{1}. What is the name of Manchester United captain as at 2025?"

dict_options = {

    "a":Fore.LIGHTWHITE_EX + "Bruno Fernades",
    "b":Fore.LIGHTWHITE_EX + "Michael Owen",
    "c":Fore.LIGHTWHITE_EX + "Gary Neville ",
    "d":Fore.LIGHTWHITE_EX + "Harry Maguire"
}

print(question_1)

display_option = dict_options.items()
for keys,items in display_option:
    print(f"{keys}.{items}")

print("-" * 60)
user_answer = input("Select your final answer: ")

def answer_check():
    """
    this validates the user preferred answer
    :return:
    """
    if user_answer == list(dict_options)[0]:
        print("You're Correct")
    elif user_answer == list(dict_options)[1]:
        print("Option B is Incorrect")
    elif user_answer == list(dict_options)[2]:
        print("Option C is Incorrect")
    elif user_answer == list(dict_options)[3]:
        print("Option D is Incorrect")
    else:
        print("Kindly select a valid option.")

answer_check()
