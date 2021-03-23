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

def hours_passed(time1, time2):
  if time1[-2:] == 'PM':
    t1 = int(time1[0]) + 12
  else:
    t1 = int(time1[0])
  if time2[-2:] == 'PM':
    t2 = int(time2[0]) + 12
  else:
    t2 = int(time2[0])
  if t2 == t1:
    return "no time passed"
  return str(t2-t1) + ' hours'

