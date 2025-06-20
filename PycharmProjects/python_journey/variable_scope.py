"""
    LEGB
        Local variable
            Enclosing variable
                Global variable
                    Built-in variable

"""

x = "global var"

def test():
    global x #a variable can be make global within or outside by stating a keyword global

    y = "local var"

    print(y)
    print(x)
test()