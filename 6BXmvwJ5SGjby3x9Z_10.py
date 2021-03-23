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
  time1AM = time1[-2:]
  time2AM = time2[-2:]
  colonIndx1 = time1.index(":")
  colonIndx2 = time2.index(":")
  hour1 = time1[:colonIndx1]
  hour2 = time2[:colonIndx2]
  hour1 = int(hour1)
  hour2 = int(hour2)
  #print(time1AM, time2AM)
  if time1AM == "AM":
    if hour1 == 12:
      hour1 = 0
    #print(hour1)
  else:
    if hour1 == 12:
      hour1 = 12
    else:
      hour1 += 12
  if time2AM == "AM":
    if hour2 == 12:
      hour2 = 0
    #print(hour1)
  else:
    if hour2 == 12:
      hour2 = 12
    else:
      hour2 += 12
  if hour2-hour1==0:
    return "no time passed"
  else:
    return str(hour2-hour1) + " hours"

