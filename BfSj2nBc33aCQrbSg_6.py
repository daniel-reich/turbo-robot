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
  def isprime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    f = 5
    m = int(n**0.5)
    while f <= m:
      if n%f == 0: return False
      if n%(f+2) == 0: return False
      f += 6
    return True
  
  if '0' in list(str(n)): return False
  left_n,right_n = str(n),str(n)
  for side in ['left','right']:
    while len(eval(side+'_n')) > 0:
      if isprime(int(eval(side+'_n'))):
        if side == 'left': left_n = left_n[1:]
        if side == 'right': right_n= right_n[:-1]
      else:
        break
  
  if (len(left_n) == 0) and (len(right_n) == 0):
    return 'both'
  elif len(left_n) == 0:
    return 'left'
  elif len(right_n) == 0:
    return 'right'
  else:
    return False

