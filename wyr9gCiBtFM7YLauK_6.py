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

import functools
def time_sum(times):
  sum_fnc=lambda ttt:(lambda a:'%02d:%02d:%02d' % (divmod(divmod(a,60)[0],60)+(divmod(a,60)[1],)))((lambda a:functools.reduce(lambda x,y:x+y[0]*3600+y[1]*60+y[2],a,0))((lambda a:[list(map(int,i.split()[-1].split(':'))) for i in a])(ttt)))
  x = sum_fnc(times)
  new = x.split(":")
  return list(map(int, new))

