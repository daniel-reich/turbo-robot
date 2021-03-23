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
​
    if time1 == time2:
        return "no time passed"
​
    time1_clock, time1_period = time1.split()
    time2_clock, time2_period = time2.split()
​
    hours1, minutes1 = time1_clock.split(':')
    hours2, minutes2 = time2_clock.split(':')
​
    if time1_period == time2_period:
        return str(int(hours2) - int(hours1)) + " hours"
    else:
        return str(12 - int(hours1) + int(hours2)) + " hours"
​
print(hours_passed("2:00 PM" , "4:00 PM"))

