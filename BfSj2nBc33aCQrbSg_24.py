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

def truncatable(n):
  l = n
  r = n
  left = True
  right = True
  for i in range(2,n//2):
    if n % i == 0:
      return False
  for i in str(n):
    if i == "0":
      return False
      
      
  while len(str(l)) > 1:
    l = int(str(l)[1:])
    for i in range (2,l//2+1):
      if l%i == 0:
        left = False
  if l == 1:
    left = False
      
      
  while len(str(r)) > 1:
    r = int(str(r)[:-1])
    for i in range (2,r//2+1):
      if r%i == 0:
        right = False
  if r == 1:
    right = False
        
        
        
  if left and right:
    return "both"
  if left:
    return "left"
  if right:
    return "right"
  if not left and not right:
    return False

