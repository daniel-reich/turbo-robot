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
  primes = []
  
  for i in range(1, limit):
    no_prime = False
    for p in primes:
      if p != 1 and i % p == 0:
        no_prime = True
        break
    
    if no_prime:
      continue
    else:
      primes.append(i)
  matches = []
  additions = 6 * (n -1) + 1
  
  for i in range(0, len(primes)):
    p = primes[i]
    if p == 1:
      continue
    current = []
    for i in range(p, (p + additions), 6):
      if i in primes:
        current.append(i)
  
    if len(current) == n:
      matches.append(current)
  result = []   
  for m in matches:
    result.append(tuple(m))
  return result

