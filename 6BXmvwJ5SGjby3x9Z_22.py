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
  x = int(time1.split(':')[0]) + 12 if time1[-2] == 'P' else 0 if int(time1.split(':')[0]) == 12 else int(time1.split(':')[0])
  y = int(time2.split(':')[0]) + 12 if time2[-2] == 'P' else int(time2.split(':')[0])
  return str(y - x) + " hours" if y - x != 0 else "no time passed"

