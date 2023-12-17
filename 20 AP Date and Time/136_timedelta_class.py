# --------------------------------------------
# -------------**## Timedelta class ##**-------------
from datetime import timedelta, date, datetime


# *-*-*-*-*-*-* Example 12 ->>> Difference between two dates and times
# time_1 = datetime(2024, 12, 15)
# time_2 = datetime(2024, 1, 25)

# print(time_1 - time_2)  # 324 days, 0:00:00

# t1 = date(2024, 12, 15)
# t2 = date(2024, 1, 25)

# print(t1 - t2)  # 324 days, 0:00:00
# print(type(t1 - t2)) # <class 'datetime.timedelta'>

# *-*-*-*-*-*-* Example 13 ->>> Difference between two timedelta objects
# t1 = timedelta(days=14, hours=10)
# t2 = timedelta(days=7, hours=5)

# t3 = t1 - t2
# print(t3)  # 7 days, 5:00:00    
# print(type(t3)) # <class 'datetime.timedelta'>

# *-*-*-*-*-*-* Example 14 ->>> gettin negative timedelta object

t1 = timedelta(days=14, hours=10)
t2 = timedelta(days=7, hours=5)

t3 = t2 - t1
print(t3)  # -8 days, 19:00:00

# *-*-*-*-*-*-* Example 15 ->>> timr duration in seconds

t1 = timedelta(days=14, hours=10)
t2 = timedelta(days=7, hours=5)

t3 = t2 - t1
print(t3.total_seconds())  # -732000.0  
