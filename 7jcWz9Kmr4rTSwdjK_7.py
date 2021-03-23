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

def prime_factorize(n):
  if not n-1:
    return []
  q = n
  primes = [x for x in range(n) if prime(x)]
  no = []
  i = 0
  while n>1 and i < len(primes):
    if not n%primes[i]:
      n //=primes[i]
      no.append(primes[i])
    if n%primes[i]:
      i+=1
  return no if no else [q]
    
  
def prime(n):
  return n>1 and not bool([x for x in range(2,int(n**.5)) if not n%x])

