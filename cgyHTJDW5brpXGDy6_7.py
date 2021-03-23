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
  hours = ""
  if time1 == time2:
    hours = "no time passed"
​
  elif time1[5:7] == "AM" and time2[5:7] == "AM":
    passTime = int(time2[:time2.index(":")]) - int(time1[:time1.index(":")])
    hours = "{0} hours".format(passTime)
  
  elif time1[5:7] == "PM" and time2[5:7] == "PM":
    passTime = int(time2[:time2.index(":")]) - int(time1[:time1.index(":")])
    hours = "{0} hours".format(passTime)
  
  elif time1[5:7] == "AM" and time2[5:7] == "PM":
    passTime = int(time2[:time2.index(":")]) + 12 - int(time1[:time1.index(":")])
    hours = "{0} hours".format(passTime)
​
  elif time1[5:7] == "PM" and time2[5:7] == "AM":
    passTime = int(time2[:time2.index(":")]) + 12 - (int(time1[:time1.index(":")]))
    hours = "{0} hours".format(passTime)
      
  return hours

