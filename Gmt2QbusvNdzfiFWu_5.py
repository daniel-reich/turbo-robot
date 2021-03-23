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

primes = []
def sum_prime(lst):
  def is_prime(num):
    if num >= 2:
      for n in range(2, num):
        if num%n==0:
          return False
      return True
    return False
  
  if len(primes) != 0:
    mp = max(primes)
  else:
    mp = 0
  
  if max(lst) > mp:
    for n in range(mp+1, max(lst)):
      if is_prime(n) == True:
        primes.append(n)
  
  prime_factors = {}
  
  for prime in primes:
    
    for num in lst:
      if prime > num:
        continue
      if num % prime == 0:
        if prime not in prime_factors.keys():
          prime_factors[prime] = [num]
        else:
          prime_factors[prime].append(num)
  
  tr = []
  print(primes)
  for prime in sorted(list(prime_factors.keys())):
    tr.append('({} {})'.format(prime, sum(prime_factors[prime])))
  
  return ''.join(tr)

