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

def multiply(n1,n2):
  if n1 == 0 or n2 == 0:
    return 0
  prod = 0 
  
  if n2 > 0:
    for i in range(1,n2+1):
      prod += n1
    return prod
  if n2 < 0:
    for i in range(n2,0):
      prod -= n1
  return prod

