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

def hours_passed(time1, time2):
  if time1 == time2: return "no time passed"
  
  h1 = int(time1.split(':')[0])
  h2 = int(time2.split(':')[0])
  
  if time1 == '12:00 AM': h1=0
  if 'PM' in time1:
    if h1 == 12: h1=12
    else: h1+=12
  
  if time2 == '12:00 AM': h2=0
  if 'PM' in time2:
    if h2 == 12: h2=12
    else: h2+=12
  
  return str(h2-h1) + ' hours'

