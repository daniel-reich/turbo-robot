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
    retval = [0, 0, 0]
    for time in times:
        parts = time.split(':')
        if(len(parts) == 3):
            retval[0] += int(parts[0])
            retval[1] += int(parts[1])
            retval[2] += int(parts[2])
        else:
            retval.append([0, 0, 0])
​
    retval[1] += retval[2] // 60
    retval[0] += retval[1] // 60
    retval[2] = retval[2] % 60
    retval[1] = retval[1] % 60
​
    return retval

