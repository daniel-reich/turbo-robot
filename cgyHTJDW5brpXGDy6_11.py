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
  
  class Time:
    
    def __init__(self, hours, mins, ap):
      self.h = hours
      self.m = mins
      self.ap = ap
    
    def hours_passed(self, other):
      if self.ap == 'AM' and other.ap == 'PM':
        return (12 - self.h) + other.h
      elif self.ap == 'PM' and other.ap == 'AM':
        return (12 - other.h) + self.h
      else:
        hours = [self.h, other.h]
        print(hours)
        return max(hours) - min(hours)
  
  t1, ap1 = time1.split()
  h1, m1 = [int(i) for i in t1.split(':')]
  
  t2, ap2 = time2.split()
  h2, m2 = [int(i) for i in t2.split(':')]
  
  time1 = Time(h1, m1, ap1)
  time2 = Time(h2, m2, ap2)
  
  hd = time1.hours_passed(time2)
  
  if hd == 0:
    return 'no time passed'
  elif hd == 1:
    return '1 hour'
  else:
    return '{} hours'.format(hd)

