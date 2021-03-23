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
  result = [0,0,0]
  for time in times:
    temp = time.split(":")
    for i in range(3):
      result[i] += int(temp[i]) 
  print (result)
  extra_minutes = int(result[2] / 60)
  result[2] = int(result[2] % 60)
  extra_hours = int((result[1] + extra_minutes) / 60)
  result[1] = (result[1] + extra_minutes) % 60
  result[0] += extra_hours
  return result

