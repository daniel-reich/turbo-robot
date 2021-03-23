"""


Write a function that returns the **greatest common divisor (GCD)** of two
integers.

### Examples

    gcd(32, 8) ➞ 8
    
    gcd(8, 12) ➞ 4
    
    gcd(17, 13) ➞ 1

### Notes

  * Both values will be positive.
  * The **GCD** is the largest factor that divides both numbers.

"""

def gcd(a, b):
  if   a == 0: return b
  elif b == 0: return a
  x = max(a, b)
  y = min(a, b)
  return gcd(y, x % y)

