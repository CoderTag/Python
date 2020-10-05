import os
import time
#from datetime import datetime, timedelta

# print(dir(os))
print(os.getcwd())
os.chdir('/var/log')
print(os.getcwd())
files = os.listdir()

# today = datetime.today()
# day_5_old = timedelta(days=5)
# print(today)
# print(day_5_old)

days_old = 5
DAY = 86400  # POSIX day in seconds

old_time = time.time() - days_old * DAY

for file in files:

    if os.path.isfile(file):
        t = os.path.getctime(file)
        if t > old_time:
            print(file, time.ctime(t))
