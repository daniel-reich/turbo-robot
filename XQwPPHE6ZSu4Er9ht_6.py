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

def is_economical(n):
  def primes(n):
    factors, current, do = [n], [0,2], True
    while do:
      if current[1] >= factors[0]:
        do = False
      elif not factors[0] % current[1]:
        current[0] += 1
        factors.append([0,current[1]])
        while not factors[0] % current[1]:
          factors[0] /= current[1]
          factors[current[0]][0] += 1
      current[1] += 1
    if factors[0] != 1.0: factors.append([1,int(factors[0])])
    return factors[1:]
  pf = primes(n)
  digs = lambda a: len(str(a))
  digpf = sum([digs(pf[i][0])+digs(pf[i][1]) if pf[i][0] != 1 else digs(pf[i][1]) for i in range(len(pf))])
  if digs(n) == digpf: return "Equidigital"
  elif digs(n) > digpf: return "Frugal"
  else: return "Wasteful"

