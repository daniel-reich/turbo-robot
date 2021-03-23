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

import datetime
​
def time_sum(times):
  if times == []:
    return [0, 0, 0]
  hours = []
  mins = []
  secs = []
  for time in times:
    clock = time.split(":")
    hours.append(int(clock[0]))
    mins.append(int(clock[1]))
    secs.append(int(clock[2]))
  hours_pre = sum(hours)
  mins_hours = str(datetime.timedelta(minutes = sum(mins))).split(":")
  secs_mins = str(datetime.timedelta(seconds = sum(secs))).split(":")
  final_hours = hours_pre + int(mins_hours[0]) + int(secs_mins[0])
  final_mins = int(mins_hours[1]) + int(secs_mins[1])
  final_secs = int(mins_hours[2]) + int(secs_mins[2])
  return [final_hours, final_mins, final_secs]

