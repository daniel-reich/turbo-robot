"""


The function is given a non-negative integer `n`. Determine if there exist two
non-negative integers `a` and `b` such that `a**2 + b**2 == n`, return `True`
/ `False`.

### Examples

    squares_sum(0) ➞ True
    # 0^2 + 0^2 == 0
    
    squares_sum(1) ➞ True
    # 0^2 + 1^2 == 1
    
    squares_sum(2) ➞ True
    # 1^2 + 1^2 == 2
    
    squares_sum(3) ➞ False
    # Checking 0, 1 we can’t make the sum of squares equal to 3.
    
    squares_sum(5) ➞ True
    # 1^2 + 2^2 == 5

### Notes

The input range is `0 <= n < 2**31`.

"""

import math
import itertools
from collections import Counter
​
def get_factors(n):
    f = 2
    increments = itertools.chain([1,2,2], itertools.cycle([4,2,4,2,4,6,2,6]))
    for incr in increments:
        if f*f > n:
            break
        while n % f == 0:
            yield f
            n //= f
        f += incr
    if n > 1:
        yield n
​
def squares_sum(n):
    root = int(round(math.sqrt(n), 0))
    if n <= 2:
        return True
    if root**2 == n:
        # n is a perfect square, so it can be written as (sqrt(n))^2 + 0^2
        return True
    # n is a sum of squares iff each prime factor is of form 4k+1
    C = Counter(list(get_factors(n)))
    for f, c in C.items():
        if f != 2 and c % 2 == 1 and (f - 1) % 4 != 0:
            return False
    return True

