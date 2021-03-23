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
  seconds = 0
  for t in times:
    tParts = [int(i) for i in t.split(':')]
    seconds += tParts[0]*60*60 + tParts[1]*60 + tParts[2]
  
  min, sec = divmod(seconds, 60)
  hours, min = divmod(min, 60)
  return [hours, min, sec]

