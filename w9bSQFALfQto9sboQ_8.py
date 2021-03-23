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
  x=set([a for a in range(1,n1+1) if n1%a==0])
  y=set([a for a in range(1,n2+1) if n2%a==0])
  return max(x&y)

