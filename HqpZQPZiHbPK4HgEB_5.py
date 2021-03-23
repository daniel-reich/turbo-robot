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

def exchange(n, i, j):
    nl = list(n)
    nl[i], nl[j] = nl[j], nl[i]
    return ''.join(nl)
​
def maxmin(num):
    n = m = str(num)
    for i, ch in enumerate(n[:-1]):
        if ch < max(n[i+1:]):
            j = n.rindex(max(n[i+1:]))
            n = exchange(n, i, j)
            break
    if num > 9:
        minch = min(m[1:], key=lambda c: '9' if c=='0' else c)
        if m[0] > minch:
            j = m.rindex(minch)
            m = exchange(m, 0, j)
        else:
            for i, ch in enumerate(m[1:-1], 1):
                if ch > min(m[i+1:]):
                    j = m.rindex(min(m[i+1:]))
                    m = exchange(m, i, j)
                    break
​
    return int(n), int(m)

