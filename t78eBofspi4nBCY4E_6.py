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

from math import log
def base_conv(n,b):
    if str(n).isnumeric():
        r=''
        p=int(log(n)/log(b))
        for d in range(p,-1,-1):
            a=int(n/(b**d))
            r+=chr(a+97)
            n-=a*(b**d)
    else:
        r=0 
        for p in range(len(n)):
            c=ord(n[p])-97
            if c>b-1 or c<0:
                return '{} is not a base {} number.'.format(n,b)
            r+=c*b**(len(n)-p-1)
    return r

