# --------------------------------------------------------------------
# ---------------**## Date Class **##---------------------------------

# # *-*-*---*-**-*-*-*-*- Example 1 ->>>> Geeting the curent date and time
# from datetime import datetime

# print(datetime.now())


# *-*-*---*-**-*-*-*-*- Example 2 ->>>> Geeting the curent date
# import datetime

# print(datetime.date.today())


# *-*-*---*-**-*-*-*-*- Example 3 ->>>> Geeting the datetime attributes
# import datetime

# print(dir(datetime))

# # *-*-*---*-**-*-*-*-*- Example 4 ->>>> creating a date object
# import datetime

# date = datetime.date(2021, 10, 8)
# print(date)
# print(type(date))

# # *-*-*---*-**-*-*-*-*- Example 5 ->>>> importing date class from datetime module
# from datetime import date

# print(date(2021, 10, 8))

# *-*-*---*-**-*-*-*-*- Example 6 ->>>> getting the date from a timestamp
# from datetime import date 

# time_stamp = date.fromtimestamp(1633685400)
# print(time_stamp)



# *-*-*---*-**-*-*-*-*- Example 7 ->>>> getting tuday's yaer, month and day
from datetime import date

today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)