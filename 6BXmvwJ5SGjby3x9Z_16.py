"""


Create a function that takes `time1` and `time2` and return how many hours
have passed between the two times.

### Examples

    hours_passed("3:00 AM", "9:00 AM") ➞ "6 hours"
    
    hours_passed("2:00 PM", "4:00 PM") ➞ "2 hours"
    
    hours_passed("1:00 AM", "3:00 PM") ➞ "14 hours"

### Notes

  * `time1` will always be the starting time and `time2` the ending time.
  * Return `"no time passed"` if `time1` is equal to `time2`.

"""

def conv(time):
  return int(time.split(':')[0]) + (12 if time[-2]=='P' or time[:2]=='12' else 0)
​
def hours_passed(time1, time2):
  delta = (conv(time2) - conv(time1))%24
  return '{} hours'.format(delta) if delta else 'no time passed'

