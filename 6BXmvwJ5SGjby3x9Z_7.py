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
  
  class Time:
    
    def __init__(self, hours, mins, am_pm):
      self.h = hours
      self.m = mins
      self.ap = am_pm
    
    def hour_diff(self, other):
      if self.ap == 'AM' and other.ap == 'PM' or self.ap == 'PM' and other.ap == 'AM':
        if self.h == 12:
          return 12 + other.h
        else:
          return (12 - self.h) + other.h
      else:
        return abs(self.h - other.h)
  
  t1, ampm1 = time1.split()
  h1, m1 = [int(i) for i in t1.split(':')]
  
  t2, ampm2 = time2.split()
  h2, m2 = [int(i) for i in t2.split(':')]
  
  time1 = Time(h1, m1, ampm1)
  time2 = Time(h2, m2, ampm2)
  
  tr = time1.hour_diff(time2)
  
  if tr == 0:
    return "no time passed"
  elif tr == 1:
    return '1 hour'
  else:
    return '{} hours'.format(tr)

