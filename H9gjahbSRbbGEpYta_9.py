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
  i=0
  n=0
  while i<abs(n2):
    n+=n1
    i+=1
  if n2>0:
    return n
  else:
    return -n

