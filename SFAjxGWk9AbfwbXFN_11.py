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
  return [x for x in range(1, n+1) if x== 2 or 2**(x-1) % x == 1 ]

