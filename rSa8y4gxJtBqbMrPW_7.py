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
  largest = max(n1, n2)
  smallest = min(n1, n2)
  
  return largest if largest % smallest == 0 else largest * smallest

