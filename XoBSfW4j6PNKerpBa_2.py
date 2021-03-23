"""


Create a function that decomposes an integer into its prime factors, ordered
from smallest to largest.

For instance:

    complete_factorization(24) = [2, 2, 2, 3]
    # Since 24 = 8 x 3 = 2^3 x 3 = 2 x 2 x 2 x 3

### Examples

    complete_factorization(10) ➞ [2, 5]
    
    complete_factorization(9) ➞ [3, 3]
    
    complete_factorization(72) ➞ [2, 2, 2, 3, 3]

### Notes

`1` is not considered a prime number, so omit it in your final list of prime
factors.

"""

def complete_factorization(num):
  #find biggest prime number below half of num
  prime_numbers = []
  i = num // 2 + 1
  while i > 2:
    prm = True
    for n in range(2, i):
      if i % n == 0:
        prm = False
    if prm:
      prime_numbers.append(i)
    i -= 1
  prime_numbers.append(2)
  result = []
  for p in prime_numbers:
    while num % p == 0:
      result.append(p)
      num = num // p
  if result == []:
    result.append(num)
  return result[::-1]

