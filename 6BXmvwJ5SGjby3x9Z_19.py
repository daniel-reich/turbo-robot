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

def hours_passed(t1, t2):
  if t1 == t2:
    return 'no time passed'
  a = halp(t1)
  b = halp(t2)
  if b < a:
    b += 24
  return '{} hours'.format((b-a))
  
def halp(time):
  a, b = time.split()
  a, _ = a.split(':')
  if a == '12' and b == 'AM':
    a = '0'
  return int(a) + 12*(b=='PM')

