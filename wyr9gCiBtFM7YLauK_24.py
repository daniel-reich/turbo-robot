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
  segundos=0
  for x in times:
    x=x.split(":")
    segundos=segundos+(int(x[0])*3600)
    segundos=segundos+(int(x[1])*60)
    segundos=segundos+(int(x[2]))
  hora=segundos//3600
  minuto=(segundos%3600)//60
  segundo=(segundos%3600)%60
  return [hora,minuto,segundo]

