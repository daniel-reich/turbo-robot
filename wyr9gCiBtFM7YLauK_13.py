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
  a = [x.split(':') for x in times]
  if len(times)==0: return [0, 0, 0]
  else: b = [[int(x) for x in y] for y in a ]
  i=0
  c=0
  d=0
  e=0
  while i<len(b):
    c+=b[i][0]
    d+=b[i][1]
    e+=b[i][2]
    i+=1
  c = c+(d//60)
  d = d%60+(e//60)
  e=e%60
  return [c, d, e]

