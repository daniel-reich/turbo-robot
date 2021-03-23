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

def prime_factors(num):
    p = 2
    lst = []
    while num >= p*p:
        if num % p == 0:
            lst.append(p)
            num /= p
        else:
            p += 1
    lst.append(int(num))
    return lst
​
def smallest(n):
    if n == 1:
        return 1
    lst = []
    for x in range(2, n + 1):
        lst.append(prime_factors(x))
    d = {}
    for i in range(2, n + 1):
        cnt = 0
        d[i] = 0
        for x in lst:
            if x.count(i) > cnt:
                cnt = x.count(i)
                d[i] = cnt
    prod = 1
    for i, c in d.items():
        if c > 0:
            prod *= i**c
    return prod

