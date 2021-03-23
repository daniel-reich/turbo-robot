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

from datetime import datetime
​
def hour(time):
  return datetime.strptime(time, '%I:%M %p').hour
​
def hours_passed(time1, time2):
  hours = hour(time2) - hour(time1)
  return ('{} hours'.format(hours) if hours else 
    'no time passed')

