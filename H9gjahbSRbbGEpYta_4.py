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
  a=0
  neg=False
  if (n1<0 or n2<0) and not (n1<0 and n2<0):
    neg=True
  n1=abs(n1)
  n2=abs(n2)
  for i in range(n2):
    a+=n1
  
  return a if not neg else a-a-a

