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

from math import sqrt; from itertools import count, islice; import numpy
​
def check_prime(lst):
  return [n for n in lst if all(n % i for i in islice(count(2), int(sqrt(n)-1)))]
​
def prime_factorize(num):
  factors = [i for i in range(2, num+1) if num % i == 0]
  prime_factors = check_prime(factors)
  while num//numpy.prod(prime_factors) != 1:
    prime_factors.append(prime_factors[0])
  return sorted(prime_factors)

