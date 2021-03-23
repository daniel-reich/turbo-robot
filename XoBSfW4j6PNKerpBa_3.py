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
  div, lst = 2, []
  while not is_prime(num):
    if is_prime(div) and num % div == 0:
      lst.append(div)
      num = num//div
    else: div += 1
  lst.append(num)
  return lst
​
def is_prime(n):
  for i in range(2,n):
    if n % i==0: return False
  return True

