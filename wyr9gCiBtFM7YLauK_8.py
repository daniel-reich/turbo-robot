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
  from functools import reduce
  times_list = [list(map(int,one_time.split(':'))) for one_time in times]
  return reduce(lambda t1,t2:
    [(t1[0]+t2[0]+(t1[1]+t2[1])//60),\
    (t1[1]+t2[1]+(t1[2]+t2[2])//60) % 60,\
    (t1[2]+t2[2]) % 60],times_list) if times_list else [0,0,0]

