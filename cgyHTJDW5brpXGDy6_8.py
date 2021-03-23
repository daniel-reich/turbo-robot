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
  h1, p1 = time1.split(':')
  h2, p2 = time2.split(':')
  h1 = int(h1) + (12 if p1[-2:] == 'PM' else 0)
  h2 = int(h2) + (12 if p2[-2:] == 'PM' else 0)
  diff = abs(h2 - h1)
  return '{} hours'.format(diff) if diff != 0 else 'no time passed'

