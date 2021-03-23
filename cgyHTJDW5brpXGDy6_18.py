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
  if time1==time2:
    return "no time passed"
  time1_split = time1.split(':')
  time2_split = time2.split(':')
  if time1_split[1]==time2_split[1]:
    return str(int(time2_split[0])-int(time1_split[0]))+" hours"
  else:
    return str(int(time2_split[0])-int(time1_split[0])+12)+" hours"

