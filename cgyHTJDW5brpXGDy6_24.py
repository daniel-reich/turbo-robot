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

def parse_time(time):
  c1 = time.find(':')
  c2 = time.rfind(' ')
  hours = int(time[:c1])
  minutes = int(time[c1+1:c2])
  modifier = time[c2+1:]
  if modifier == 'PM':
    hours += 12
  return hours
​
def hours_passed(time1, time2):
  if time1 == time2:
    return 'no time passed'
  return str(parse_time(time2) - parse_time(time1))+' hours'

