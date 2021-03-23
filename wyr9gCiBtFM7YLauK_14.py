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
​
  times = [times[i].split(':') for i in range(len(times))]
  new = []
  
  for i in range(3):
    new.append(sum(map(int,[time[i] for time in times])))
  
  return [(new[0] + (new[1] // 60)), (new[1] + (new[2] // 60)) % 60, new[2] % 60]

