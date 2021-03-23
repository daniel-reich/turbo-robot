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

from fractions import gcd
​
def smallest(n):
    l = 1
    for x in range(1, n+1):
        l = lcm(l, x)
    return l
​
def lcm(a, b):
    return a * b // gcd(a, b)

