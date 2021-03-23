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
  sign = lambda x: (x>0) - (x<0)
  v = sum(abs(n1) for _ in range(abs(n2)))
  return v if sign(n1)==sign(n2) else -v

