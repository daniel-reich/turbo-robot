"""


Write a function that returns the **least common multiple (LCM)** of two
integers.

### Examples

    lcm(9, 18) ➞ 18
    
    lcm(8, 5) ➞ 40
    
    lcm(17, 11) ➞ 187

### Notes

  * Both values will be positive.
  * The **LCM** is the smallest integer that is divisible by both numbers such that the remainder is zero.

"""

def lcm(n1, n2):
  a = []
  x = [n1, n2]
  y = max(x)
  z = min(x)
  for x in range(y, y*z+1, y):
    print(x)
    if x % n1 == 0 and x % n2 == 0:
      a.append(x)
  print(a)
  return a[0]

