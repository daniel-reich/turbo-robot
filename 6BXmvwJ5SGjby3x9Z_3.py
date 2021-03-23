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

def hours_passed(a,b):
  if a==b: return 'no time passed'
  c,d=int(a.split(':')[0]),int(b.split(':')[0]) 
  e,f=a[-2],b[-2]
  if c==12 and e=='A': c=0
  if e=='P': c+=12
  if d==12 and f=='A': d=0
  if f=='P': d+=12
  return str(d-c)+' hours'

