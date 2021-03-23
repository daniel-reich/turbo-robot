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
    l = [i for i in range(2, n+1)]
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                l[j] = int(l[j] / l[i])
    p = 1
    for i in l:
        p *= i
    return p

