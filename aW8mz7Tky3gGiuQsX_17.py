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

def is_powerful(n):
    factors = [i for i in range(2,n+1) if n % i == 0]
    i = 2
    p_factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            p_factors.append(i)
    if n > 1:
        p_factors.append(n)
    p_factors = [x**2 for x in set(p_factors)]
 
    return set(p_factors).issubset(set(factors))

