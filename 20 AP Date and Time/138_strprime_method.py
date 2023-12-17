# --------------------------------------------------
# --------------**## strprime() Method ##**---------
from datetime import datetime

# *-*-*-*-*--*- Example 21 ->>> strptime() method
date_str = "21 June, 2018"
print(type(date_str))

date_obj = datetime.strptime(date_str, "%d %B, %Y")
print(date_obj)
print(type(date_obj))

# *-*-*-*-*--*- Example 22 ->>> string to datetime object
date_str = "11 June, 2034"
print(type(date_str))

date_obj = datetime.strptime(date_str, "%d %B, %Y")
print(date_obj)
print(type(date_obj))

# *-*-*-*-*--*- Example 23 ->>> string to datetime object
date_str1 = "31/01/2019" # 31 January, 2019
date_str2 = "31/01/2019 12:20:30" # 31 January, 2019 12:20:30

# considering date is in dd/mm/yyyy format
date_obj1 = datetime.strptime(date_str1, "%d/%m/%Y")

print("The type of the date object1:", type(date_obj1))
print("The type of the date object2:", type(date_obj2))

# considering date is in mm/dd/yyyy format
date_obj2 = datetime.strptime(date_str2, "%d/%m/%Y %H:%M:%S")
print("Date Object 1:", date_obj1)
print("Date Object 2:", date_obj2)
