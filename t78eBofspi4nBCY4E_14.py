"""


Create a function that allows you to convert from a positive base 10 integer
to any other base from 2 to 26, and also does the reverse, converts from base
2 to 26 back to base 10. The digits in the new base will be the lower case
letters a-z with a=0 and z=25. If the number is out of range for the base
specified, return the error message shown in the examples.

### Examples

    base_conv(15, 2) ➞ "bbbb"
    # 1111
    
    base_conv(16, 2) ➞ "baaaa"
    # converts 16 (base 10) to base 2
    
    base_conv(1234, 10) ➞ "bcde"
    
    base_conv("bac", 3) ➞ 11
    # converts "bac" (base 3) to base 10
    # 1*3**2 + 0*3 + 2 = 11
    
    base_conv("dac", 3) ➞ "dac is not a base 3 number."

### Notes

N/A

"""

def base_conv(n,b):
  base = { i: chr(ord('a')+i) for i in range(26)}
  rev = {v:k for k,v in base.items()}
  if type(n) == int:
    ret = []
    while n > 0:
      ret.append(base[n % b])
      n = n // b
    return "".join(ret[::-1])
  else:
    for c in n:
      if c not in rev or rev[c] >= b:
        return "{} is not a base {} number.".format(n, b)
    return sum(rev[c]*b**i for i,c in enumerate(n[::-1]))

