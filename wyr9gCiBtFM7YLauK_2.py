"""


Create a function that takes a list of strings representing times
(`'hours:minutes:seconds'`) and returns their sum as a list of integers
(`[hours, minutes, seconds]`).

### Examples

    time_sum(["1:23:45"]) ➞ [1, 23, 45]
    
    time_sum(["1:03:45", "1:23:05"]) ➞ [2, 26, 50]
    
    time_sum(["5:39:42", "10:02:08", "8:26:33"]) ➞ [24, 8, 23]

### Notes

If the input is an empty list, return `[0, 0, 0]`

"""

def time_sum(times):
  timelist = [ x.split(":") for x in times ]
  seconds = sum([ int(x[2]) for x in timelist ])
  minutes = sum([ int(x[1]) for x in timelist ]) + int(seconds/60)
  hours = sum([ int(x[0]) for x in timelist ]) + int(minutes/60)
  
  return [ hours , minutes % 60 , seconds % 60]

