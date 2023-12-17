# ------------------------------------------------------------
# -------------**## Time Class **##---------------------------
from datetime import time

# *-*-*---*-**-*-*-*-*- Example 8 ->>>> Time object to represent time
time_1 = time()
print("Time A: ", time_1)

time_2 = time(11, 34, 00)
print("Time B: ", time_2)

time_3 = time(hour=11, minute=34, second=00)
print("Time C: ", time_3)

time_4 = time(hour=11, minute=34, second=00, microsecond=234566)
print("Time D: ", time_4)


# *-*-*---*-**-*-*-*-*- Example 9 ->>>> getting hour, minute, second and microsecond
timt_5 = time(11, 34, 00, 234566)
print("Hour: ", timt_5.hour)
print("Minute: ", timt_5.minute)
print("Second: ", timt_5.second)    
print("Microsecond: ", timt_5.microsecond)
