import datetime



now = datetime.datetime.now()

print(now.time())
print(now.date())

f = datetime.datetime(2025,6,7)
print("who's birthday is at ",f)

print(f.strftime("so the birthday is in the month %m and i think the time will be %h"))

from datetime import timedelta

s = f + timedelta(days=53)
print(s.strftime("%d %m %y"))

import math
x = math.sqrt(16)
print(int(x))

f = math.sqrt(80)
f = math.ceil(f)  # it rounds upwards so be careful
print(f)



