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
  if time1 == time2: return 'no time passed'
  t1, m1 = int(time1.split(':')[0]), time1[-2:]
  t2, m2 = int(time2.split(':')[0]), time2[-2:]
  if t1 < 12 and m1 == 'PM':
    t1 += 12
  if t2 < 12 and m2 == 'PM':
    t2 += 12
  return '{} hours'.format(abs(t1-t2))

