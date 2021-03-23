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
    time1 = eval(time1.replace(' AM','').replace(' PM','+12').replace(':00',''))
    time2 = eval(time2.replace(' AM','').replace(' PM','+12').replace(':00',''))
    if time1==12:time1=0
    return str(abs(time2-time1)) + ' hours' if time1!=time2 else 'no time passed'

