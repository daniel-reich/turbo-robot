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

from math import sqrt
def factors(n):
    pfs = []
    while n%2 == 0:
        pfs.append(2)
        n //= 2
    lim = int(sqrt(n)) + 1
    for i in range(3, lim, 2):
        while n%i == 0:
            pfs.append(i)
            n //= i
    return pfs + [n] if n > 2 else pfs
​
​
def is_economical(n):
    numlen = lambda n: len(str(n))
    pfs = factors(n)
    eco = 0
    for d in set(pfs):
        exp = pfs.count(d)
        eco += numlen(d) + (numlen(exp) if exp > 1 else 0)
    return 'Frugal' if eco < numlen(n) else 'Equidigital' if eco == numlen(n) else 'Wasteful'

