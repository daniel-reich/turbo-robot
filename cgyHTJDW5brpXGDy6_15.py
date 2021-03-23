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
  if time1 == time2: 
    return "no time passed"
  t1, ampm1 = time1.split()
  t1 = int(t1.split(':')[0])
  if ampm1 == "PM":
    t1 += 12
  t2, ampm2 = time2.split()
  t2 = int(t2.split(':')[0])
  if ampm2 == "PM":
    t2 += 12
  return str(t2 - t1) + " hours"

