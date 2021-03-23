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

from itertools import *
from operator import *
def time_sum(times):
  if not times: return 3*[0]
  h, m, s = list(map(sum, zip(*[(int(i) for i in t.split(':')) for t in times])))
  ds, z = divmod(0, 60)
  dm, s = divmod(s+ds, 60)
  dh, m = divmod(m+dm, 60)
  return [h+dh, m, s]

