"""


You will be given a list of 32-bit unsigned integers. Flip all the bits 1 -> 0
and 0 -> 1 and return the result as an unsigned integer.

### Worked Example

    n = 4
    4 is 0100 in binary. We are working in 32 bits so:
    00000000000000000000000000000100 = 4
    11111111111111111111111111111011 = 4294967291
    return 4294967291

### Examples

    flipping_bits(2147483647) ➞ 2147483648
    
    flipping_bits(1) ➞ 4294967294
    
    flipping_bits(4) ➞ 4294967291

### Notes

N/A

"""

def flipping_bits(n):
    binary = '{0:b}'.format(n)
    flipped = ''.join(['1' if x == '0' else '0'
         for x in binary.zfill(32)])
    return int(flipped, 2)

