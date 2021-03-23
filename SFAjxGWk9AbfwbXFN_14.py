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

def findPrime(n):
  x = n-1
  while x > 1:
    if n % x == 0:
      return 0
    else:
      x -= 1
  return n
​
​
def primes_below_num(n):
  primesUnder = []
  while n > 1:
    if findPrime(n) > 0:
      primesUnder.append(n)
      n -= 1
    else:
      n -= 1
  return sorted(primesUnder)

