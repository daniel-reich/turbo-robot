"""


In numbers theory, a positive composite integer is a Smith number if its
digital root is equal to the digital root of the sum of its prime factors,
with factors being counted by multiplicity. Trivially, every prime is also a
Smith number, having just one prime factor that is equal to itself. If two
Smith numbers are consecutive in the integer series, then they are Smith
brothers. Any other number will not be a Smith.

Given a positive integer `number`, implement a function that returns:

  * `"Youngest Smith"` if the given number is the lower element of a couple of Smith brothers.
  * `"Oldest Smith"` if the given number is the higher element of a couple of Smith brothers.
  * `"Single Smith"` if the given number is a Smith number without another Smith number adjacent, lower or higher.
  * `"Trivial Smith"` if the given number is a prime.
  * `"Not a Smith"` if the given number is not a Smith number.

### Examples

    smith_type(22) ➞ "Single Smith"
    # Digital root of 22 = 2 + 2 = 4
    # Sum of prime factors of 22 = 2 + 11 = 13
    # Digital root of 13 = 1 + 3 = 4
    # Is a Smith  number without a brother
    
    smith_type(7) ➞ "Trivial Smith"
    # The given number is a prime
    
    smith_type(728) ➞ "Youngest Smith"
    # Digital root of 728 = 7 + 2 + 8 = 17 = 1 + 7 = 8
    # Sum of prime factors of 728 = 2 + 2 + 2 + 7 + 13 = 26
    # Digital root of 26 = 2 + 6 = 8
    # The number 729 is a Smith number, so 728 is the youngest brother
    
    smith_type(6) ➞ "Not a Smith"
    # Digital root of 6 = 6
    # Sum of prime factors of 6 = 2 + 3 = 5
    # Digital root of 5 = 5

### Notes

  * The prime factors are counted by multiplicity, they don't have to be unique (see example #3).
  * Two Smith numbers are brothers if they are adjacent and if they are **composite** , a Trivial Smith (a prime) can't be the brother of a Smith number! Look at example #1: 22 is a Single Smith, despite the next one, 23 (a prime), being a Trivial Smith.
  * The digital root is the reiterated sum of the digits of a number until a single digit is reached. You can find more info in the **Resources** tab.
  * All given integers will be greater than zero.

"""

def isPrime(n):
  if n < 2:
    return False
  else:
    for i in range(2, n):
      if n % i == 0:
        return False
    return True
​
def factors(n):
  return [i for i in range(2, n+1) if n % i == 0]
  
def primeFactors(n):
  p_facts = []
  while n != 1:
    for factor in factors(n)[::-1]:
      if isPrime(factor):
        p_facts.append(factor)
        n = int(n/factor)
  return p_facts
  
def digitalRoot(n):
  dR = 0
  while n != 0:
    dR += (n % 10)
    n //= 10
  return dR
  
def isSmith(n):
  sum = 0
  for prime in primeFactors(n):
    sum += digitalRoot(prime)
  return sum == digitalRoot(n) and not isPrime(n)
​
def smith_type(n):
  if isPrime(n):
    return "Trivial Smith"
  elif isSmith(n) and isSmith(n-1):
    return "Oldest Smith"
  elif isSmith(n) and isSmith(n+1):
    return "Youngest Smith"
  elif isSmith(n):
    return "Single Smith"
  else:
    return "Not a Smith"

