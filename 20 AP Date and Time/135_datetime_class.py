# ---------------------------------------------------------
# ----------**## Datetime Class ##**------------------------
from datetime import datetime, timedelta

# *-*-*-*-*-*-* Example 10 ->>> Python datetime object 
time_1 = datetime(2024, 1, 1)
print(time_1)

time_2 = datetime(2040, 1, 1, 12, 30, 45)
print(time_2)

# *-*-*-*-*-*-* Example 11 ->>> getting yaer, month, day, hour, minute and timestamp from datetime object
time_3 = datetime(2024, 10, 11, 12, 30, 45)
print("Year: ", time_3.year)
print("Month: ", time_3.month)
print("Day: ", time_3.day)
print("Hour: ", time_3.hour)
print("Minute: ", time_3.minute)
print("Timestamp: ", time_3.timestamp())
