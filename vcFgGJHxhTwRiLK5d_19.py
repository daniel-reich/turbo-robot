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

from collections import Counter
​
def smallest(n):
    count_max = Counter()
    for i in range(2, n + 1):
        count_current = factorize(i)
        for key in count_current.keys():
            count_max[key] = max(count_max[key], count_current[key])
    prod = 1
    for key in count_max:
        prod *= key**count_max[key]
    return prod
​
def factorize(n):
    count_current = Counter()
    i = 2
    while i < n + 1:
        if n%i == 0:
            count_current[i] += 1
            n = n//i
            i = 2
        else:
            i += 1
    return count_current

