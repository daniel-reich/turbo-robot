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
  prime = True
  if n>1:
    for i in range(2, n):
      if n%i == 0:
        prime = False
        break
  else:
    prime = False
  return prime
​
def truncatable(n):
  # left truncatable prime
  left = True
  for i in range(len(str(n))):
      if not isprime(int(str(n)[i:])):
          left = False
          break
          
  #right truncatable prime
  right = True
  for i in range(len(str(n))):
      if not isprime(int(str(n)[0:len(str(n))-i])):
          right = False
          break
          
  if "0" in str(n):
    right = False
    left = False
  
  if right == True and left == False:
    return "right"
  if right == False and left == True:
    return "left"
  if right == True and left == True:
    return "both"
  if right == False and left == False:
    return False

