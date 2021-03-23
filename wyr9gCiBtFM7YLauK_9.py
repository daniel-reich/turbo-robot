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
    times = [[int(n) for n in t.split(':')] for t in times]
    seconds = sum(t[2] for t in times)
    minutes = sum(t[1] for t in times) + seconds // 60
    hours = sum(t[0] for t in times) + minutes // 60
    return [hours, minutes%60, seconds%60]

