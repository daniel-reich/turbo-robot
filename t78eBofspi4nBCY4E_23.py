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

base=list("abcdefghijklmnopqrstuvwxyz")
​
def base_conv(n, b):
  if type(n)==int:
    out=[]
    while n>0:
      out.append(base[n%b])
      n=(n-n%b)//b
    return ''.join(out[::-1])
​
  if ord(max(list(n)))-ord('a')>=b or min(list(n))<'a': return n+" is not a base "+str(b)+" number."
  return sum([(ord(x)-ord('a'))*(b**idx) for idx,x in enumerate(n[::-1])])

