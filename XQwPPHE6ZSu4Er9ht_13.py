"""


A number is Economical if the quantity of digits of its prime factorization
(including exponents greater than 1) is equal to or lower than the digit
quantity of the number itself.

Given an integer `n`, implement a function that returns a string:

  * `"Equidigital"` if the quantity of digits of the prime factorization (including exponents greater than 1) is equal to the quantity of digits of `n`;
  * `"Frugal"` if the quantity of digits of the prime factorization (including exponents greater than 1) is lower than the quantity of digits of `n`;
  * `"Wasteful"` if none of the two above conditions is true.

### Examples

    is_economical(14) ➞ "Equidigital"
    # The prime factorization of 14 (2 digits) is [2, 7] (2 digits)
    # Exponents equal to 1 are not counted
    
    is_economical(125) ➞ "Frugal"
    # The prime factorization of 125 (3 digits) is [5^3] (2 digits)
    # Notice how exponents greater than 1 are counted
    
    is_economical(1024) ➞ "Frugal"
    # The prime factorization of 1024 (4 digits) is [2^10] (3 digits)
    
    is_economical(30) ➞ "Wasteful"
    # The prime factorization of 30 (2 digits) is [2, 3, 5] (3 digits)

### Notes

  * Any given `n` will be a positive integer greater than 1.
  * Remember to count also the exponents greater than 1 into the prime factorization: 2¹ = 2 (one digit), 2² = 22 (two digits), 2¹° = 210 (three digits)...

"""

def prime_factors(n):
  """ Return a list with the prime factors of n """
  ### Function needed for simplify_root()
  ### Function needed for is_economical()
  i = 2
  while n>1:
    while not n%i:
      n//=i
      yield i
    i+=1
​
def is_economical(n):                   # Economical numbers
  """ View rules on edabit """
  prime_fac = list(prime_factors(n))
  prime_fac = list(set([(x, prime_fac.count(x)) for x in prime_fac]))
  sum_prime = sum(len(str(x[0])) if x[1]==1 else len(str(x[0])) + len(str(x[1])) for x in prime_fac)
  return "Equidigital" if sum_prime == len(str(n)) else "Frugal" if sum_prime < len(str(n)) else "Wasteful"

