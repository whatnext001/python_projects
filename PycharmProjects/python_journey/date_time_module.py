import datetime
# from datetime import timedelta  #timedelta is part of the datetime module, which can be use to add, subtract date and time
# import pytz #pytz is another time zone you can use
#
#
# mod_date = datetime.date(2024,4,27)
# cur_date = datetime.date.today()
# t_delta = datetime.timedelta(days=7)
# next_week = cur_date + t_delta
#
#
# print(cur_date)
# print(mod_date)
# print(t_delta)
# print(next_week)

user_in = input("Kindly enter your birthdate in this format YYYY-MM-DD:")

t_date = datetime.datetime.today()
t_diff = t_date - user_in

print(t_diff)
