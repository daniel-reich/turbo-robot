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

def base_conv(n, b):
    if type(n) is int:
        res = ''
        while n:
            res += chr(97 + n % b)
            n = n // b
        return res[::-1]
    else:
        res = 0
        for i in range(1, len(n) + 1):
            if 96 < ord(n[-i]) < 97 + b:
                res += (ord(n[-i]) - 97) * b ** (i - 1)
            else:
                return '{} is not a base {} number.'.format(n, b)
        return res

