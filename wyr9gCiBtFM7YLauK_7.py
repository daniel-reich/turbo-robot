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
    if not times:
        return [0, 0, 0]
    secs = sum([get_secs(x) for x in times])
    h = secs // 3600
    secs = secs% 3600
    m = secs // 60
    s = secs % 60
    return [h, m, s]
    print(secs)
​
def get_secs(x):
    h, m, s = x.split(':')
    return 3600*int(h) + 60*int(m) + int(s)

