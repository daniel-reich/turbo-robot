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

def is_powerful(number):
    factors, primes, prime_factors = [], [], []
    for i in range(1,number,1):
        if number % i == 0:
            factors.append(i)
    for i in range(2,number,1):
        flag = True
        for i1 in range(2,number,1):
            if i == i1:
                pass
            elif i % i1 == 0:
                flag = False
        if flag == True:
            primes.append(i)
    for i in primes:
        if i in factors:
            prime_factors.append(i)
    flag = True
    for i in prime_factors:
        if i**2 not in factors:
            flag = False
    if flag == True:
        return True
    return False

