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
  if time1 == time2: return "no time passed" 
  
  h1 = int(time1[:time1.index(':')])
  h2 = int(time2[:time2.index(':')])
  
  if 'PM' in time1: 
    h1+=12
  if 'PM' in time2:
    h2+=12
  
  if h1 == 12: h1 = 0
  if h2 == 12: h2 = 0
​
  return str(h2-h1) + ' hours'

