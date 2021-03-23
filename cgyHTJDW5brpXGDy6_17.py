"""


Create a function that takes `time1` and `time2` and return how many hours
have passed between the two times.

### Examples

    hours_passed("3:00 AM", "9:00 AM") ➞ "6 hours"
    
    hours_passed("2:00 PM", "4:00 PM") ➞ "2 hours"
    
    hours_passed("1:00 AM", "3:00 PM") ➞ "14 hours"

### Notes

`time1` will always be the starting time and `time2` the ending time. Return
"no time passed" if `time1` is equal to `time2`.

"""

import re
def hours_passed(time1, time2):
  t1=re.split('[:\s]', time1)
  t2=re.split('[:\s]', time2)
  delta=int(t2[0])-int(t1[0]) if t1[-1]==t2[-1] else int(t2[0])-int(t1[0])+12
  if delta:
    return "{} hours".format(delta)
  return  "no time passed"

