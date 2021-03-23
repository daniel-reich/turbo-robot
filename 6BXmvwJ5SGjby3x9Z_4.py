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
  if time1==time2: return "no time passed"
  a, b = time1.split()
  c, d = time2.split()
  h1 = int(a[:-3])
  h2 = int(c[:-3])
  e = (h1+12)%24 if (b=="PM" and h1!=12) or (b=="AM" and h1==12)\
      else h1
  f = (h2+12)%24 if (d=="PM" and h2!=12) or (d=="AM" and h2==12)\
      else h2
  return '{} hours'.format(f - e)

