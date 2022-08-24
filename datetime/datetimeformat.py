from datetime import datetime
from datetime import timedelta

# Фоматирование дат и времени
now = datetime.now()
print(now.strftime("%Y-%m-%d"))  # 2017-05-03
print(now.strftime("%d/%m/%Y"))  # 03/05/2017
print(now.strftime("%d/%m/%y"))  # 03/05/17
print(now.strftime("%d %B %Y (%A)"))  # 03 May 2017 (Wednesday)
print(now.strftime("%d/%m/%y %I:%M"))  # 03/05/17 01:36

# Сложение и вычитание дат и времени
now = datetime.now()
print(now)  # 2017-05-03 17:46:44.558754
two_days = timedelta(2)
in_two_days = now + two_days
print(in_two_days)  # 2017-05-05 17:46:44.558754
