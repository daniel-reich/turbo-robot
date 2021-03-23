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

def is_economical ( n ) :
    prm , pow = [ ] , [ ]
    prm = prime_fact(n)
    pow = power(prm ,pow, n).copy()
    return "Equidigital"*(sum([len(str(i)) for i in pow+prm if i!=1])==len(str(n)))\
           or"Wasteful"*(sum([len(str(i)) for i in pow+prm if i!=1]) > len(str(n)))\
           or"Frugal"
​
def prime_fact(n):
    return [i for i in get_primes(n) if not n%i]
​
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers-=set(range(p * 2 , n + 1 , p))
    return primes
​
​
def power(prm,pow,num):
    count=0
    for i in prm :
        while (not num % i) :
            num /= i
            count += 1
        pow.append(count)
        count = 0
    return pow

