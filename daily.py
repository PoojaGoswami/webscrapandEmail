import thoughts
import sendmail1

# from datetime import datetime
import datetime
from threading import Timer
#
# x = datetime.datetime.today()
#
# print(x.day,x.hour)
# y = x.replace(day=x.day, hour=21, minute=52, second=0, microsecond=0)
# delta_t = y-x
# secs1 = delta_t.seconds + 1
# secs2 = delta_t.seconds + 50
# print(secs1,secs2)
#
# # r =  datetime.datetime.now() + datetime.timedelta(minutes=15)
# # print(r)
#
secs1 = 0
secs2 = 50
t1 = Timer(secs1, thoughts.daily_thought)
t2 = Timer(secs2, sendmail1.main)
# t = Timer(time, func_name, [arguments])

t1.start()
t2.start()
print('good morning pooja, Read todays thought', datetime.datetime.now())
