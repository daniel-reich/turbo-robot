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
  for i in range(2,min(n1,n2)+1):
    if(n1%i==0 and n2%i==0):
      return i*lcm(int(n1/i),int(n2/i))       
  return n1*n2

