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

def smith_type(number):
    
    def fac(n):
        import math
        step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
        maxq = int(math.sqrt(n)) + 1
        d = 1
        q = 2 if n % 2 == 0 else 3
        while q <= maxq and n % q != 0:
            q = step(d)
            d += 1
        return [q] + fac(n // q) if q <= maxq else [n] if n > 1 else []
    
    def dsum(n):
        while n > 9:
            n = sum(map(int, list(str(n))))
        return n
    
    lw = fac(number)
    df = dsum(sum(lw))
    # digital sum n
    ds = dsum(number)
    if ds != df:
        return "Not a Smith"
    # Youngest Smith
    lyw = fac(number + 1)
    dyf = dsum(sum(lyw))
    dys = dsum(number + 1)
    if dyf == dys and len(lyw) > 1:
        return "Youngest Smith"
    # Oldest Smith
    low = fac(number - 1)
    dof = dsum(sum(low))
    dos = dsum(number - 1)
    while dys > 9:
        dys = sum(map(int, list(str(ds))))
    if dof == dos and len(low) > 1:
        return "Oldest Smith"
    # simple smith
    if len(lw) == 1:
        return "Trivial Smith"
    if df == ds:
        return "Single Smith"
def smith_type(number):
    
    def fac(n):
        import math
        step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
        maxq = int(math.sqrt(n)) + 1
        d = 1
        q = 2 if n % 2 == 0 else 3
        while q <= maxq and n % q != 0:
            q = step(d)
            d += 1
        return [q] + fac(n // q) if q <= maxq else [n] if n > 1 else []
    
    def dsum(n):
        while n > 9:
            n = sum(map(int, list(str(n))))
        return n
    
    lw = fac(number)
    df = dsum(sum(lw))
    # digital sum n
    ds = dsum(number)
    if ds != df:
        return "Not a Smith"
    # simple smith
    if len(lw) == 1:
        return "Trivial Smith"
    # Oldest Smith
    low = fac(number - 1)
    dof = dsum(sum(low))
    dos = dsum(number - 1)
    if dof == dos and len(low) > 1:
        return "Oldest Smith"
    # Youngest Smith
    lyw = fac(number + 1)
    dyf = dsum(sum(lyw))
    dys = dsum(number + 1)
    if dyf == dys and len(lyw) > 1:
        return "Youngest Smith"
    if df == ds:
        return "Single Smith"

