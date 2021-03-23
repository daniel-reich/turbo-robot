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
  lst = [x.split(':') for x in times]
  hrs = 0
  mn = 0
  sec = 0
  for l in lst:
    sec += int(l[2])
    mn += int(l[1])
    hrs += int(l[0]) 
  return [hrs+(mn+sec//60)//60, (mn+sec//60)%60, sec%60]

