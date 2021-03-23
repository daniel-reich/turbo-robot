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

def hours_passed(start, end):
  convert = lambda r: [[int(k), 0][k == '12'] if k.isdigit()
            else [0, 12][k == 'PM'] for k in r.split(':00 ')]
  (s, x), (e, y) = convert(start), convert(end)
  return [str(e+y-s-x) + ' hours', 'no time passed'][start == end]

