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

def primes_below_num(n):
​
    return [number for number in range(1, n+1) if is_prime(number)]
​
​
def is_prime(n):
​
    if n <= 1:
        return False
​
    if n <= 3 or n == 5:
        return True
​
    if not (n % 2) or not (n % 5):
        return False
​
    for i in range(3, int(n**0.5)+1, 2):
        if not (n % i):
            return False
​
    return True

