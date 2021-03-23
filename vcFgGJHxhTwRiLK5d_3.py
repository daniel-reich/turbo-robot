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

from functools import reduce
​
def get_gcd(a, b):
    while b:
        a, b = b, a%b
    return a
​
def get_lcm(a, b):
    return a*b // get_gcd(a, b)
​
def smallest(n):
    return reduce(get_lcm, range(1, n+1))

