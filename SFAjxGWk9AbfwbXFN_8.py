"""


Create a function that will find all primes below a given number. Return the
result as a list.

### Examples

    primes_below_num(5) ➞ [2, 3, 5]
    
    primes_below_num(10) ➞ [2, 3, 5, 7]
    
    primes_below_num(20) ➞ [2, 3, 5, 7, 11, 13, 17, 19]

### Notes

If `n` is a prime, it is included in the list.

"""

import math
​
def primes_below_num(n):
    list = []
    i = 0
    for j in range(2,n+1):
        for k in range(2,math.floor(math.sqrt(j))+1):
            if j % k == 0:
                i += 1
        if i == 0:
            list += [j]
            i = 0
        else:
            i = 0
    return list

