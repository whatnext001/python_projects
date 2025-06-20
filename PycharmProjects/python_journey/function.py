def none_function():
    pass #the pass keyword indicates that we are not using this function for now, just pass it as the name implies



def onloan(team,player):

    print(f"this current players are loaned {team}, {player}")

#onloan("barca","madrid")


def calc(a,b):
    result = a + b
    return result
calc(3,5)

#print(result)

def min(d,c):
    return d*c
result = min(5,6)
print(result)


def square(num):
    return num ** 2
root = square(4)
print(root)

def sum(u,i):
    return u + i
summ = sum(6,8)
print(summ)

sum(4,5)

def name(fir,sec):
    return f"{fir} {sec}"
namem = name("jk","kl")
print(namem)

# *args is called positional argument, which allows functions to accept any number of positional arguments.
def greet(*args):
    """checks for how to use positional arguments"""
    for name in args:
        print(f"Welcome {name}")
greet("bobby","chris","evans")


# **kwargs is called keyword arguments, lets function accepts any number of keyword arguments.
def show_info(**kwargs):
    """This shows student info using kwargs"""
    for key,value in kwargs.items():
        print(f"{key}:{value}")
show_info(name="alice", age=25, city="oyo" )

#example to show both usage by unpacking a list
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

courses = ["math","biology","literature"]
info = {"name":"john","age":25,"class":"2021/2025"}

student_info(*courses,**info)