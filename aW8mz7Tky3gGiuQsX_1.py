"""


Given a positive number x:

    p = (p1, p2, …)
    # Set of *prime* factors of x

If the square of every item in p is also a factor of x, then x is said to be a
**_powerful_** number.

Create a function that takes a number and returns `True` if it's powerful,
`False` if it's not.

### Examples

    is_powerful(36) ➞ True
    # p = (2, 3) (prime factors of 36)
    # 2^2 = 4 (factor of 36)
    # 3^2 = 9 (factor of 36)
    
    is_powerful(27) ➞ True
    
    is_powerful(674) ➞ False

### Notes

N/A

"""

from math import sqrt
def is_powerful(n):
    while (n % 2 == 0):
        p = 0
        while (n % 2 == 0):
            n //= 2
            p += 1
        if (p == 1):
            return False
    for f in range(3, int(sqrt(n)) + 1, 2):
        p = 0
        while (n % f == 0):
            n //= f
            p = p + 1
        if (p == 1):
            return False
    return (n == 1)

