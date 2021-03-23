"""


Sexy primes are primes that differ by 6.

For example, (5, 11) comprise a sexy prime pair, while (5, 11, 17) comprise a
set of sexy prime triplets.

Create a function that takes two numbers as argument, the set length `n` (2
for pairs, 3 for triplets), and the `limit`. Return a list of sorted tuples of
sexy primes up to (but excluding) the `limit`.

### Examples

    sexy_primes(2, 100) ➞ [(5, 11), (7, 13), (11, 17), (13, 19), (17, 23), (23, 29), (31, 37), (37, 43), (41, 47), (47, 53), (53, 59), (61, 67), (67, 73), (73, 79), (83, 89)]
    
    sexy_primes(3, 100) ➞ [(5, 11, 17), (7, 13, 19), (11, 17, 23), (17, 23, 29), (31, 37, 43), (41, 47, 53), (47, 53, 59), (61, 67, 73), (67, 73, 79)]
    
    sexy_primes(3, 250) ➞ [(5, 11, 17), (7, 13, 19), (11, 17, 23), (17, 23, 29), (31, 37, 43), (41, 47, 53), (47, 53, 59), (61, 67, 73), (67, 73, 79), (97, 103, 109), (101, 107, 113), (151, 157, 163), (167, 173, 179), (227, 233, 239)]

### Notes

N/A

"""

def sexy_primes(n, limit):
  pairs = []
  for i in range(2, limit-((n-1)*6)):
    num_is_prime = True
    next_is_prime = True
    for y in range(2, int(round(i**(0.5)))+1):
      if i/y == i//y:
        num_is_prime = False
        break
    if num_is_prime:
      nex = i+6
      for y in range(2, int(round(nex**(0.5)))+1):
        if nex/y == nex//y:
          next_is_prime = False
          break
    if next_is_prime and n == 3:
      nexy = i+12
      for y in range(2, int(round(nexy**(0.5)))+1):
        if nexy/y == nexy//y:
          next_is_prime = False
          break
    if next_is_prime and num_is_prime:
      if n == 2:
        pairs.append((i, nex))
      if n == 3:
        pairs.append((i, nex, nexy))
  return pairs

