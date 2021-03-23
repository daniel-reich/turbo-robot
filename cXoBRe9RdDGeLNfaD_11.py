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

nbin = lambda x: bin(256+x if x<0 else x)[2:]
​
def eight_bit(exp):
    a, o, b = exp.split()
    a, b, s = map(int, (a, b, o+'1'))
    c = a + b*s
    if all(-129<i<128 for i in (a, b, c)):
        return (c, '{} {} {} = {}'.format(nbin(a), o, nbin(b), nbin(c)))
    return "Overflow"

