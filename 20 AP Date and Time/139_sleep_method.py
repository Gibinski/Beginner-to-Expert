# -------------------------------------------------------------
# ---------------**## sleep() method ##**---------------------- 
import time

# *-*-*-*-*--*- Example 24 ->>> sleep() method
print("Imediate print")
time.sleep(5)

print("After 5 seconds print")
time.sleep(5)

# *-*-*-*-*--*- Example 25 ->>> creating a simple low level  digital clock
while True:
    local_time = time.localtime()
    result = time.strftime("%I:%M:%S %p", local_time)
    print(result)
    time.sleep(1)
    if result == "10:17:00 AM":
        break
print("Alarm is running")   
time.sleep(5)
