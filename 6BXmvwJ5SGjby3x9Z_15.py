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
    start = int(time1.split(':')[0])
    end = int(time2.split(':')[0])
    not_start = time1.split()[-1]
    not_end = time2.split()[-1]
    if time1 == '12:00 AM':
        start = 0
    if not_start == not_end and start == end:
        return 'no time passed'
    elif not_start == not_end and start != end:
        return str(abs(end - start)) + ' hours'
    elif not_start != not_end:
        if not_end == 'PM':
            return str(abs(end + 12 - start)) + ' hours'

