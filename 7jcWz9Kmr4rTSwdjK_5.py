"""


Write a function to find all the prime factors of a given integer. The
function must return a list containing all the prime factors, sorted in
ascending order. Remember that _1 is neither prime nor composite_ and should
not be included in your output list.

### Examples

    prime_factorize(25) ➞ [5, 5]
    
    prime_factorize(19) ➞ [19]
    
    prime_factorize(77) ➞ [7, 11]

### Notes

  * Output list must be sorted in ascending order.
  * The only positive integer which is neither prime nor composite is 1. Return an empty list if 1 is the input.

"""

import math
def prime_factorize(num):
  primeFactors = []
  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
      primeFactors.append(i)
      primeFactors.extend(prime_factorize(int(num / i)))
      break
  if primeFactors == []:
    if num != 1:
      primeFactors.append(num)
  sortedPrimeFactors = sorted(primeFactors)
  return sortedPrimeFactors

