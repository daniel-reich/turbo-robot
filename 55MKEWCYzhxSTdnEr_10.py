"""


Create a function that takes two numbers as arguments and returns the Greatest
Common Divisor (GCD) of the two numbers.

### Examples

    gcd(3, 5) ➞ 1
    
    gcd(14, 28) ➞ 14
    
    gcd(4, 18) ➞ 2

### Notes

The GCD is the highest number that can divide both arguments without a
remainder.

"""

def gcd(a, b):
  small = a if a < b else b
  large = b if b > a else a
  i = small
  while i > 0:
    if small % i == 0 and large % i == 0:
      return i
    i -= 1
  return 1

