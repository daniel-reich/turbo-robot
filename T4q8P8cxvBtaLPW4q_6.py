"""


Create a function that takes an integer argument and returns a list of prime
numbers found in the decimal representation of that number (not factors).

For example, `extract_primes(1717)` returns `[7, 7, 17, 17, 71]`.

The list should be in acending order. If a prime number appears more than
once, every occurance should be listed. If no prime numbers are found, return
an empty list.

### Examples

    extract_primes(1) ➞ []
    
    extract_primes(7) ➞ [7]
    
    extract_primes(73) ➞ [3, 7, 73]
    
    extract_primes(103) ➞ [3]
    
    extract_primes(1313) ➞ [3, 3, 13, 13, 31, 131, 313]

### Notes

  * All test cases are positive real integers.
  * Some numbers will have leading zeros. For example, the number `103` contains the prime number `3`, but also contains `03`. These should be treated as the same number, so the result would simply be `[3]`.

"""

def is_prime(n):
  if n == 2 or n == 3:
    return True
  if n < 2 or n%2 == 0:
    return False
  if n < 9:
    return True
  if n%3 == 0:
    return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0:
      return False
    if n % (f+2) == 0:
      return False
    f += 6
  return True 
    
​
 
def extract_primes(num):
  r = list(str(num))
  res = []
  for n in range(1, len(r)+1):
    for i, digit in enumerate(r):
      if i+n <= len(r) and r[i] != '0':
        res.append(
        int(''.join(r[i: i+n]))
        )
        
  return sorted(filter(is_prime, res))

