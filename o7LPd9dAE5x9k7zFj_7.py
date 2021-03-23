"""


A logarithm is kind of like reverse exponents. There is a base and a number in
a logarithm. The point of a logarithm is to find out what power you have to
raise the base to get the number next to the base. For example:

    log base 5 of 25 = x

This is the same thing as saying 5 to the `x`th power is 25, which is 2 (so
`x` would be 2). Using this example, your function must take the 5 and 25 and
somehow get 2.

### Examples

    logarithm(5, 25) ➞ 2
    
    logarithm(2, 64) ➞ 6
    
    logarithm(2, 4) ➞ 2

### Notes

  * All inputs and their associated outputs are integers.
  * Return `"Invalid"` for inputs outside of domain.

"""

def logarithm(base, num):
  x=0
  if num==1:
    return 0
  if base<=1 or num<1:
    return "Invalid"
  while base<=num:
    x+=1
    num=num/base
  return x

