# -----------------------------------------------------------------------------
# ----------------**## strftime() method ##**---------------------------------

# US ->>>> MM/DD/YYYY
# UK ->>>> DD/MM/YYYY
from datetime import datetime

# *-*-*-*-*--*- Example 16 ->>> firmatting date using strftime() method
# current date and time
# now = datetime.now()

# t = now.strftime("%H:%M:%S")
# print(t)

# s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# # mm/dd/YY H:M:S format
# print(s1)
# print(type(s1))

# *-*-*-*-*--*- Example 17 ->>> datetime to string using strftime() method
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

# *-*-*-*-*--*- Example 18 ->>> create a string from a timestamp
timestamp = 1455454547
date_time = datetime.fromtimestamp(timestamp)
print(date_time)
print(type(date_time))

date = date_time.strftime("%d/%m/%Y, %H:%M:%S")
print("Date =", date)
print(type(date))

# https://dics.python.org/3/library/datetime.html
# https://www.w3schools.com/python/python_datetime.asp
# https://www.programiz.com/python-programming/datetime/strftime

date2 = date_time.strftime("%d %b, %Y")
print(date2)

date3 = date_time.strftime("%d %B, %Y")
print(date3)

date4 = date_time.strftime("%d %m, %Y")
print(date4)

time2 = date_time.strftime("%H:%M:%S")  
print(time2)
# *-*-*-*-*--*- Example 19 ->>> locale's appropriate date and time
timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

d1 = date_time.strftime("%c")
print(d1)

d2 = date_time.strftime("%x")
print(d2)

# hh:mm:ss format
d3 = date_time.strftime("%X")
print(d3)

# *-*-*-*-*--*- Example 20 ->>> Python datetime to timestamp
now = datetime.now()

# convert to timestamp and print it

timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)

# convert timestamp to datetime object
date_time = datetime.fromtimestamp(timestamp)
print("date and time =", date_time)