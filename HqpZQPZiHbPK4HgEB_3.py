"""


Maxie is the largest number that can be obtained by **swapping two digits** ,
Minnie is the smallest. Write a function that takes a number and returns Maxie
and Minnie. Leading zeros are not permitted.

### Examples

    maxmin(12340) ➞ (42310, 10342)
    
    maxmin(98761) ➞ (98761, 18769)
    
    maxmin(9000) ➞ (9000, 9000)
    # Sometimes no swap needed.
    
    maxmin(11321) ➞ (31121, 11123)

### Notes

N/A

"""

def s(ls, func, total, i=0):
    while i+1 < total:
        if i == 0: value = func([a for a in ls if a != '0'])
        else: value = func(ls[i:])
        p = (total-1) - ls[::-1].index(value, 0,total-i)
        if p > i and ls[i] != ls[p]: ls[i], ls[p] = ls[p], ls[i]; break
        i += 1
    return ''.join(ls)
​
def maxmin(n):
    t = [i for i in str(n)]; m = t.copy(); u, d = s(m, max, len(m)), s(t, min, len(t))
    return int(u), int(d)

