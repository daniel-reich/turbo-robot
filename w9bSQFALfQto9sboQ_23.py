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

def gcd(n1, n2):
  for i in range(max(n1,n2), 0, -1):
    if n1 % i == 0 and n2 % i == 0:
      return i
    else:
      erg = i
  return erg

