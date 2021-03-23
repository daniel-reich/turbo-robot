"""


Create a function that takes a list of positive integers and returns a string
as:

  *  **p1** , **sum of all ij** of the list for which **p1** is a prime factor.
  *  **p2** , **sum of all ij** of the list for which **p2** is a prime factor, **...** .
  *  **pn** , **sum of all ij** of the list for which **pn** is a prime factor.

### Examples

    sum_prime([12, 15]) ➞ "(2 12)(3 27)(5 15)"
    # 2 is a prime factor of 12 results (2 12).
    # 3 is a prime factor of 12 and 15, add 15 + 12, results (3 27).
    # 5 is a prime factor of 15 results (5 15).
    # 7, 11 and 13 are prime numbers but not a factor of any of the number
    # in the given list.
    
    sum_prime([7, 13, 18, 23, 24]) ➞ "(2 42)(3 42)(7 7)(13 13)(23 23)"
    
    sum_prime([3, 5, 7, 9, 11, 13]) ➞ "(3 12)(5 5)(7 7)(11 11)(13 13)"

### Notes

N/A

"""

def sum_prime(lst):
  primes = sorted(set(sum((prime_facts(n) for n in lst),[])))
  return ''.join('({} {})'.format(str(p), str(sum(n for n in lst if n%p==0))) for p in primes)  
​
def prime_facts(n):
  ans = []
  p=2
  while n>1:
    while n%p==0:
      ans.append(p)
      n//=p
    p+=1
  return ans

