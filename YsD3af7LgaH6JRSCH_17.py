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
  now = [int(i) for i in now.split(":")]
  now[2] += sec % 60
  mins += sec // 60
  now[1] += mins % 60
  hrs += mins // 60
  if now[2] > 59:
    now[1] += 1
    now[2] = now[2] % 60
  if now[1] > 59:
    now[0] += 1
    now[1] = now[1] % 60
  now[0] = (now[0] + hrs) % 24
  now = ["0" + str(i) if i < 10 else str(i) for i in now ]
  return "{}:{}:{}".format(now[0], now[1], now[2])

