from datetime import date
from datetime import time
from datetime import datetime

today = date.today()
print(today)
print("{}.{}.{}".format(today.day, today.month, today.year))

current_time = time()
print(current_time)

deadline = datetime(2017, 5, 10, 4, 30)
print(deadline)
