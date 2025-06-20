import loops
"""
    I imported an already existing python file into my current working file by calling using the import keyword
        followed by the name of the file, this can also be called by doing (import loops as mini_import), 
            mini_import is just any random name you can use
     """

from loops import teams
"""
    I can also call a specific value e.g function from an existing module e.g (from loops import function_name)
        where "teams" is  a variable defined in the loops.py
        *Note* if you want to import everything...from loops import * (the asterik sign indicates import all)
        """

print(teams)
print(loops) #I was able to print the content of the loops.py file

import random
"""
    random is another library that can be use
"""
import math
import datetime
import calendar
"""
    using the datetime and calendar modules
"""

courses = ["math","physics","english","yoruba","arabic"]
random_courses = random.choice(courses)


math_calc = math.radians(90)


current_date = datetime.date.today()
calendar_chk = calendar.isleap(2023)


import os
"""
    This is another standard library you can use os(operating system)
    """

working_dir = os.getcwd()
dunder_file = os.__file__   #double underscore is called dunder


print(dunder_file)
print(working_dir)
print(calendar_chk)
print(current_date)
print(random_courses)
print(math_calc)