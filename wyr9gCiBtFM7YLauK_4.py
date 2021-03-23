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
  hSum = 0
  mSum = 0
  sSum = 0
  tiempos = []
  for time in times:
    tiempos = time.split(':')
    sSum+=int(tiempos[2])
    if sSum>60:
      mSum+=1
      sSum=sSum%60
    mSum+=int(tiempos[1])
    if mSum>60:
      hSum+=1
      mSum=mSum%60
    hSum+=int(tiempos[0])
  return [hSum, mSum, sSum]

