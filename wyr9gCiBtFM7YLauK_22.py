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
  total = [0,0,0]
  for i in times:
    j=i.split(':')    
    for i in range(3):
      total[i]+=int(j[i])
  for i in reversed(range(2)):
    total[i]+=total[i+1]//60
    total[i+1]%=60
  return total

