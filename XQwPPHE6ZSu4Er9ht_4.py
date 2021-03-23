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
  lst = pf(n)
  lst = list(set([str(i)+str(lst.count(i)) if lst.count(i)>1 else str(i) for i in lst]))
  length = sum([len(i) for i in lst])
  return 'Equidigital' if len(str(n))==length else 'Frugal' if len(str(n))>length else 'Wasteful'
  
def pf(n):
  it = 2
  lst = []
  while n>1:
    while n%it==0:
      lst.append(it)
      n=n//it
    it+=1
    while not prime(it):
      it+=1
  return lst
​
def prime(n):
  for i in range(2,n):
    if n%i==0:
      return False
  return True

