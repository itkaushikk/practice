import datetime

date_now = datetime.datetime.now()
print(date_now)
time_diff = datetime.timedelta(1,0,0,0,30,19,0)
print(time_diff)
date_diff = date_now + time_diff

print(date_now, time_diff, date_diff)