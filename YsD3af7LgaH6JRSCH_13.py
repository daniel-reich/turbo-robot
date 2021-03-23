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
    hours,minutes,seconds = now.split(':')
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    seconds += sec
    minutes_carry = seconds // 60
    seconds = seconds % 60
    minutes = minutes + minutes_carry + mins
    hours_carry = minutes // 60
    minutes = minutes % 60
    hours = hours + hrs + hours_carry
    hours = hours % 24
    return '{:0>2d}:{:0>2d}:{:0>2d}'.format(hours,minutes,seconds)

