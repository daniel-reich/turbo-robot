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

def prime_factorize(num):
  factors, i = [], 2
  while num > 1:
    if num % i == 0:
      num /= i
      factors.append(i)
    else:
      i += 1
  return sum([[i] * factors.count(i) for i in sorted(set(factors))], [])

