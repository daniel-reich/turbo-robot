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

def get_prime_factors(n):
​
    i = 2
    prime_factors = []
​
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
​
    if n > 1:
        prime_factors.append(n)
​
    return prime_factors
​
​
def is_powerful(n):
​
    prime_factors = get_prime_factors(n)
​
    unique_prime_factors = tuple(dict.fromkeys(prime_factors))
​
    for p in unique_prime_factors:
        if n % p != 0 or n % (p * p) != 0:
            return False
    return True

