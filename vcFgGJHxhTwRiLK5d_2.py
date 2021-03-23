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

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
​
​
def smallest(n):
    ans = 1
    for i in range(1, n + 1):
        ans = (ans * i) // gcd(ans, i)
    return ans

