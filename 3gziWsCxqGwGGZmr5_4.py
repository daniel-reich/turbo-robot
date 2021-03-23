"""


Given two integers as arguments, create a function that finds the largest
prime within the range of the two integers.

### Examples

    fat_prime(2, 10) ➞ 7
    # range [2, 3, 4, 5, 6, 7, 8, 9, 10] and the largest prime is 7.
    
    fat_prime(10, 2) ➞ 7
    # [10, 9, 8, 7, 6, 5, 4, 3, 2] and the largest prime is 7.
    
    fat_prime(4, 24) ➞ 23
    # range [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] the largest prime is 23.

### Notes

All numbers will be positive integers.

"""

def primes2(n):
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3:: 2 * k] = [False] * ((n // 6 - k * k // 6 - 1)
                                                   // k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) // 3:: 2 * k] = \
                ([False] * ((n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) //
                            k + 1))
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction)
                     if sieve[i]]
​
set_primes = set(primes2(400000))
​
def fat_prime(a, b):
    a, b = (a, b) if a < b else (b, a)
    b = b if b % 2 else b - 1
    for k in range(b, a - 1, -2):
        if k in set_primes:
            return k

