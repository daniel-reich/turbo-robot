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

def is_prime(n):
  for f in range( 2, int(n**0.5) + 1 ):
    if n % f == 0:
      return False
  return True
​
prime_factors = []
​
def prime_factorize(num):
  global prime_factors
  
  for f in range(2, num+1):
    if num % f == 0:     # f is a factor
      if is_prime(f):
        prime_factors.append(f)     # f is a factor and prime
        return prime_factorize( int(num / f) )
      else:
        return prime_factorize( int(num / f) )    # f is a factor but not prime
  pf = prime_factors
  prime_factors = []
  return sorted(pf)

