"""


Create a function that takes two numbers `n1` `n2` and multiplies them
**without using** `*`.

### Examples

    multiply(3, 2) ➞ 6
    
    multiply(4, 10) ➞ 40
    
    multiply(-2, 4) ➞ -8

### Notes

Do not use `*` for this challenge.

"""

def multiply(n1, n2):
  
  Total = 0
  
  Added = 0
  Required = abs(n2)
  
  while (Added < Required):
    Total += n1
    Added += 1
    
  if (n2 < 0):
    return Total * -1
  else:
    return Total

