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
  a,b=','.join(i[:-6] if i[-2:]=='AM' else str(eval(i[:-6])+12) for i in (time1,time2)).split(',')
  if time1=='12:00 AM':
    return b+' hours'
  elif a==b:
    return "no time passed"
  else:
    return str(eval(b)-eval(a))+' hours'

