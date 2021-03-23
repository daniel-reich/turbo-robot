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
  time1 = time1.replace("12:00 AM", '00:00 AM')
  
  t1 = int(time1[:time1.index(':')]) + 12 if time1[-2:] == 'PM' else int(time1[:time1.index(':')])
  t2 = int(time2[:time2.index(':')]) + 12 if time2[-2:] == 'PM' else int(time2[:time2.index(':')])
  
  return '{} hours'.format(t2-t1) if t2 - t1 != 0 else "no time passed"

