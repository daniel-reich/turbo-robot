"""


You will be given a simple string expression representing an addition or
subtraction in 8-bit 2's complement arithmetic. Write a function that returns
the result in base 10 followed by a binary representation. If any of the
values are outside the range of 8-bit 2's complement, return `"Overflow"`.

### Examples

    eight_bit("3 + 12") ➞ (15, "11 + 1100 = 1111")
    
    eight_bit("3 - 12") ➞ (-9, "11 - 1100 = 11110111")
    
    eight_bit(-18 - 6) ➞ (-24, "11101110 - 110 = 11101000")
    
    eight_bit(65 + 70) ➞ "Overflow"
    
    eight_bit(-127 + 127) ➞ (0, "10000001 + 1111111 = 0")

### Notes

Numbers in 8-bit 2's complement notation can range from -128 to 127. The
eighth (leftmost) bit signifies a negative number. See **Resources** for
details.

"""

import re
def eight_bit(exp):
    res = eval(exp)
    a, operator, b = re.findall(r"(-?\d*) ([+-]) (\d*)", exp)[0]
    a, b = int(a), int(b)
    if -128 > res or res > 127 or -128 > a or a > 127 or -128 > b or b > 127:
        return 'Overflow'
​
    def convert(n):
        return (bin(n)[2:] if n >= 0 else '1'
                + ''.join('0' if c == '1' else '1' for c in '{:0>7}'
                          .format(bin(~n)[2:])))
​
    return res, '{} {} {} = {}'.format(convert(a), operator, convert(b),
                                       convert(res))

