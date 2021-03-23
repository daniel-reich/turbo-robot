"""


Jake is a very habitual person. He eats breakfast at 7:00 a.m. each morning,
lunch at 12:00 p.m. and dinner at 7:00 p.m. in the evening.

Create a function that takes in the current time as a string and determines
the duration of time before Jake's next meal. Represent this as a list with
the first and second elements representing hours and minutes, respectively.

### Examples

    time_to_eat("2:00 p.m.") ➞ [5, 0]
    // 5 hours until the next meal, dinner
    
    time_to_eat("5:50 a.m.") ➞ [1, 10]
    // 1 hour and 10 minutes until the next meal, breakfast

### Notes

N/A

"""

from datetime import datetime, timedelta
import re
​
BREAKFAST = datetime(2000,1,2,7)
LUNCH = datetime(2000,1,2,12)
DINNER = datetime(2000,1,2,19)
​
def time_to_eat(current_time):
  match = re.search(r"(\d\d?):(\d\d?) ([ap])\.m\.", current_time)
​
  if match:
    if match.group(3)=="a":
      if match.group(1) != "12":
        dt_current = datetime(2000,1,2,int(match.group(1)),
                        int(match.group(2)))
      else:
        dt_current = datetime(2000,1,2,0, int(match.group(2)))
    else:
      dt_current = datetime(2000,1,2,int(match.group(1)) + 12,
                      int(match.group(2)))
    
    if bool(dt_current > DINNER) != bool(dt_current <= BREAKFAST):
      if dt_current > DINNER:
        dt_current = datetime(2000,1,1, dt_current.hour, dt_current.minute)
      time_diff = BREAKFAST - dt_current
    elif dt_current > BREAKFAST and dt_current <= LUNCH:
      time_diff = LUNCH - dt_current
    else:
      time_diff = DINNER - dt_current
​
    hours = divmod(time_diff.seconds, 3600)
    seconds = hours[1] / 60
    return [hours[0], seconds]

