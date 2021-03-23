"""


Create a function that takes an array of three numbers and returns the **Least
Common Multiple** (LCM).

The LCM is the smallest positive number that is a multiple of two or more
numbers. In our case, we are dealing with three numbers.

  * Multiples of 3 are: 3, 6, 9, 12, and so on.
  * Multiples of 4 are: 4, 8,12, and so on.
  * Multiples of 12 are: 12, and so on.

Thus, the least common multiple of 3, 4, and 12 is 12.

### Examples

    lcm_three([5, 7, 13]) ➞ 455
    
    lcm_three([104, 105, 107]) ➞ 1168440
    
    lcm_three([19, 47, 43]) ➞ 38399

### Notes

N/A

"""

def prime_factors(n):
    factors = [1]
    while n > 1:
        for d in range(2, n+1):
            if n % d == 0:
                factors.append(d)
                n = int(n/d)
​
    return factors
​
def lcm_three(num):
    factors = {}
​
    for n in num:
        factor = prime_factors(n)
        for f in factor:
            if f not in factors.keys():
                factors[f] = factor.count(f)
            else:
                if factor.count(f) > factors[f]:
                    factors[f] = factor.count(f)
    lcm = 1
    for p in factors.keys():
        for _ in range(factors[p]):
            lcm *= p
    return lcm

