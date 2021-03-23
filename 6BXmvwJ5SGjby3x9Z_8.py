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
  
  Text_A = time1.replace(" ",":")
  Text_B = time2.replace(" ",":")
  
  Blocks_A = Text_A.split(":")
  Blocks_B = Text_B.split(":")
  
  if (Blocks_A[-1] == "PM"):
    Hours_A = int(Blocks_A[0]) + 12
  elif (Blocks_A[0] == "12") and (Blocks_A[-1] == "AM"):
    Hours_A = 0
  else:
    Hours_A = int(Blocks_A[0])
  
  if (Blocks_B[-1] == "PM"):
    Hours_B = int(Blocks_B[0]) + 12
  else:
    Hours_B = int(Blocks_B[0])
  
  Elapsed = abs(Hours_A - Hours_B)
  
  if (Elapsed == 0):
    return "no time passed"
  else:
    return "{} hours".format(Elapsed)

