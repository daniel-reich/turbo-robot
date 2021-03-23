"""


Create a function that returns a list containing the prime factors of whatever
integer is passed to it.

### Examples

    prime_factors(20) ➞ [2, 2, 5]
    
    prime_factors(100) ➞ [2, 2, 5, 5]
    
    prime_factors(8912234) ➞ [2, 47, 94811]

### Notes

  * Implement your solution using trial division.
  * Your solution should not require recursion.

"""

def factorization(x):
    for i in range (2, int(x) + 1, 1):
        if x % i == 0:
            return i
    return 1
​
def prime_factors(x):
    factors = []
    factor = factorization(x)
    while factor != 1:
        factors.append(factor)
        x = x / factor
        factor = factorization(x)
    return factors

