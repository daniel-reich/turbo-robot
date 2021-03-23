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
  if time1 == time2:
    return "no time passed"
  time1 = time1 if time1 != "12:00 AM" else "0:00 AM"
  time2 = time2 if time2 != "12:00 AM" else "0:00 AM"
  hour1 = int(time1.split(":")[0]) if time1[len(time1) - 2] == "A" else int(time1.split(":")[0]) + 12
  hour2 = int(time2.split(":")[0]) if time2[len(time2) - 2] == "A" else int(time2.split(":")[0]) + 12
  return str(hour2 - hour1) + " hours"

