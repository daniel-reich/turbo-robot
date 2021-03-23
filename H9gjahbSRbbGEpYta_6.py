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
  num1 = n1 + multiply(n1, n2 - 1) if n2 > 1 else n1
  num2 = -n1 + multiply(n1, n2 + 1) if n2 < -1 else -n1
  return num2 if (n1 < 0 or n1 > 0) and n2 < 0 else num1

