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
    def dec_to_base(n, b):
        if n == 0: return 'a'
        s = ''
        while n:
            n, r = divmod(n, b)
            s = chr(97+r) + s
        return s
​
    def base_to_dec(s, b):
        if max(s) > chr(96 + b) or not all(c.isalpha() for c in s):
            return '{} is not a base {} number.'.format(s, b)
        n = 0
        for c in s:
            n = n * b + ord(c) - 97
        return n
​
    return dec_to_base(n, b) if isinstance(n, int) else base_to_dec(n, b)

