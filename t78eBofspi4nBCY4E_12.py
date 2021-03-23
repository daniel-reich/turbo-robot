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
    def base_10_to_base_b(n, b):
        w = 1
        while True:
            if n // (b ** w) == 0:
                break
            else:
                w += 1
        if w == 1:
            return chr(n % b + 97)
        o = []
        for ix in range(0, w):
            o[0:0] = chr(n % (b ** (ix + 1)) // (b ** ix) + 97)
            n -= n % (b ** (ix + 1))
        return ''.join(o)
​
    def base_b_to_base_10(n, b):
​
        is_not_alpha = [True if not ele.isalpha() else False for ele in n]
        is_out_of_range = [True if ord(ele) - ord('a') >= b else False for ele in n]
        if any(is_not_alpha) or any(is_out_of_range):
            return n + ' is not a base ' + str(b) + ' number.'
        d = [ord(ele) - ord('a') for ele in n]
        p = [b ** ix for ix in range(len(n) - 1, -1, -1)]
        s = [d[ix] * p[ix] for ix in range(len(d))]
        return sum(s)
​
    if type(n) is int:
        return base_10_to_base_b(n, b)
    else:
        return base_b_to_base_10(n, b)

