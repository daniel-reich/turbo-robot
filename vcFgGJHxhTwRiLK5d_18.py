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
    if n == 1:
        return 1
    else:
        lcm = (n*(n-1))//gcd(n, n-1)
        while n != 1:
            n -= 1
            lcm = (lcm*n)//gcd(lcm, n)
        return lcm

