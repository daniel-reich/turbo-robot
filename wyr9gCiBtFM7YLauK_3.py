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

from datetime import datetime
​
def time_sum(times):
    result = [0, 0, 0]
    hours = 0
    mins = 0
    secs = 0
    for i in times:
        i = i.split(':')
        hours += int(i[0])
        mins += int(i[1])
        secs += int(i[2])
​
    mins += int(secs / 60)
    secs = secs % 60
    hours += int(mins / 60)
    mins = mins % 60
    
    return [hours, mins, secs]

