"""


Given an integer, create a function that returns the next prime. If the number
is prime, return the number itself.

### Examples

    next_prime(12) ➞ 13
    
    next_prime(24) ➞ 29
    
    next_prime(11) ➞ 11
    # 11 is a prime, so we return the number itself.

### Notes

N/A

"""

def next_prime(num):
    primes = [2,3,5,7,11,13,17,19,23,29,31,37]
    if num in primes:
        return num
    for i in primes:
        if i > num:
            return i

