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
    if not times: return [0,0,0]
    h_l, m_l, s_l = zip(*[t.split(":") for t in times])
    s = sum(int(si) for si in s_l)
    m = sum(int(mi) for mi in m_l) + s//60
    h = sum(int(hi) for hi in h_l) + m//60
​
    return [h,m%60,s%60]

