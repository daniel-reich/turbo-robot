"""


In this challenge, you have to add a variable amount of hours, minutes and
seconds to a given time, obtaining, in turn, a new adjusted time.

Given a string `now` being a timestamp in the format `hh:mm:ss`, and three
integers `hrs`, `mins` and `sec` being the hours, minutes and seconds to add,
implement a function that returns a string being the newly adjusted timestamp
(maintaining the same format).

### Examples

    time_adjust("01:00:00", 1, 30, 10) ➞ "02:30:10"
    
    time_adjust("18:22:30", 4, 60, 30) ➞ "23:23:00"
    
    time_adjust("00:00:00", 72, 120, 120) ➞ "02:02:00"

### Notes

  * The amounts of `hrs`, `mins` and `sec` can be any positive integer, and you have to correctly add them to the corresponding unit if they exceed their scale. See example #2: sixty minutes is one hour, and sixty seconds (30 + 30) is one minute.
  * If the amount of time to add exceeds the 24 hours, then the time will start again from "00:00:00". See example #3: 72 hours are 3 exact days so that after three cycles of 24 hours, the hour will be again "00" (and becomes "02" because we are adding also 120 minutes or 2 hours).

"""

def time_adjust(now, hrs, mins, sec):
  now_time = list(map(int, now.split(':')))
  now_time = [now_time[0] + hrs, now_time[1] + mins, now_time[2] + sec]
  hrs_now, mins_now, sec_now = now_time[0], now_time[1], now_time[2]
  if sec_now - 60 >= 0:
    mins_now += sec_now // 60
    sec_now = sec_now % 60
  else:
    sec_now = sec_now
  if mins_now - 60 >= 0:
    hrs_now += mins_now // 60
    mins_now = mins_now % 60
  else:
    mins_now = mins_now
  if hrs_now - 24 >= 0:
    hrs_now = hrs_now % 24
  else:
    hrs_now = hrs_now
  return '{:02d}:{:02d}:{:02d}'.format(hrs_now, mins_now, sec_now)

