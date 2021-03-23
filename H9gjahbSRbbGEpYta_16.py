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
  final = 0
  for i in range(abs(n2)):
    final+=n1
  return abs(final) if n1<0 and n2<0 or n1>0 and n2>0 else -abs(final)

