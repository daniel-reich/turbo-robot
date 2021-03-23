"""


A left-truncatable prime is a prime number that contains no 0 digits and, when
the first digit is successively removed, the result is always prime.

A right-truncatable prime is a prime number that contains no 0 digits and,
when the last digit is successively removed, the result is always prime.

Create a function that takes an integer as an argument and:

  * If the integer is only a left-truncatable prime, return `"left"`.
  * If the integer is only a right-truncatable prime, return `"right"`.
  * If the integer is both, return `"both"`.
  * Otherwise, return `False`.

### Examples

    truncatable(9137) ➞ "left"
    # Because 9137, 137, 37 and 7 are all prime.
    
    truncatable(5939) ➞ "right"
    # Because 5939, 593, 59 and 5 are all prime.
    
    truncatable(317) ➞ "both"
    # Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.
    
    truncatable(5) ➞ "both"
    # The trivial case of single-digit primes is treated as truncatable from both directions.
    
    truncatable(139) ➞ False
    # 1 and 9 are non-prime, so 139 cannot be truncatable from either direction.
    
    truncatable(103) ➞ False
    # Because it contains a 0 digit (even though 103 and 3 are primes).

### Notes

The input integers will not exceed 10^6.

"""

import numpy
from math import floor
def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n//2, dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1
  
def pruneNum(num):
  if (len(str(num))==1): return ''
  numb = list(str(num))
  numb.remove(numb[0])
  return int(''.join(numb))
  
def checkRL(num, rl, primes):
  if (rl=="r"):
    while len(list(str(num)))!=1:
      num = floor(num/10)
      if (num not in primes and num!=2): return False
    return True
  else:
    while len(list(str(num)))!=1:
      num = pruneNum(num)
      if (num not in primes and num!=2): return False
    return True
  
def truncatable(n):
  answer, primes = [], primesfrom3to(n+1)
  checkedR, checkedL = checkRL(n, "r", primes), checkRL(n, "l", primes)
  if ('0' in list(str(n))): return False
  elif (n not in primes): return False
  if (checkedR==True): answer.append("right")
  if (checkedL==True): answer.append("left")
  if ("right" in answer and "left" in answer): answer = ["both"]
  if (answer == []): answer=[False]
  return answer[0]

