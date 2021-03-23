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
  lst=[]
  for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
      lst.append(i)
  return max(lst)

