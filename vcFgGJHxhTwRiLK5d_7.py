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

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
​
def lcm(x, y):
    return abs(x * y) // gcd(x, y)
​
def smallest(n):
    res = 1
    for i in range(1, n + 1):
        res = lcm(res, i)
    return (res)

