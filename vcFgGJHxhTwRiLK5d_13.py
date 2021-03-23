"""


Given a positive integer `n`, implement a function that finds the **smallest**
number that is evenly divisible by the integers `1` through `n` inclusive.

### Examples

    smallest(1) ➞ 1
    
    smallest(5) ➞ 60
    
    smallest(10) ➞ 2520
    
    smallest(20) ➞ 232792560

### Notes

N/A

"""

def smallest(n):
    if n == 1:
        return 1
    else:
        m=smallest(n-1)
        if m%n==0:
            return m
        else:
            off=m%n
            for i in range(m,(n*m)+1, m):
                if (i%n == 0) and (i%m == 0):
                    return i

