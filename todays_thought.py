import thoughts

import datetime
from threading import Timer

secs1 = 0
t1 = Timer(secs1, thoughts.daily_thought)
# t = Timer(time, func_name, [arguments])

t1.start()
