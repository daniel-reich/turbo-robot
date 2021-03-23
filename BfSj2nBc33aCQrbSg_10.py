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
  str_n = str(n)
  if "0" in str_n:
    return False
  lr_n = [prime_factors(n)]
  rl_n = [prime_factors(n)]
  for i in range(1, len(str_n)):
    lr_n.append(prime_factors(int(str_n[i:])))
    rl_n.append(prime_factors(int(str_n[:-i])))
​
  if all(len(x) == 1 for x in lr_n) and all(len(x) == 1 for x in rl_n):
    return "both"
  elif all(len(x) == 1 for x in lr_n):
    return "left"
  elif all(len(x) == 1 for x in rl_n):
    return "right"
  else:
    return False
  
def prime_factors(num):
  f = 2
  prime_list = []
  while num!=1:
    if (num % f) == 0:
      prime_list.append(f)
      num //= f
    else:
      f += 1
  return prime_list

