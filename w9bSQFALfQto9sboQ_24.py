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
  GCDArray = []
  if n1>n2:
    for GCD in range(n1):
      if GCD != 0 and n1 % GCD == 0 and n2 % GCD == 0:
        GCDArray.append(GCD)
  else:
    for GCD in range(n2):
      if GCD != 0 and n1 % GCD == 0 and n2 % GCD == 0:
        GCDArray.append(GCD)
  return GCDArray[len(GCDArray)-1]

