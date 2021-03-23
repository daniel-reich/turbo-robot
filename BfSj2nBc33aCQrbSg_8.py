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

def isprime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return n > 1
​
def truncatable(n):
  x = str(n)
  direction = {0:False, 1:"right", 2:"left", 3:"both"}
  d_in = 0
  if isprime(n) and "0" not in x:
    #right
    for i in range(1, len(x)):
      if isprime(int(x[:i])):
        continue
      else:
        break
    else:d_in += 1
    #left
    for i in range(1, (len(x))):
      if isprime(int(x[i:])):
        continue
      else:
        break
    else:d_in += 2
  
  return direction[d_in]
