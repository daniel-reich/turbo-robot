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
  res = 0
  for _ in range(abs(n2)):
    res += n1
  return -res if n2<0 else res

