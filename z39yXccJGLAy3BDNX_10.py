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
    return int(''.join('0' if i=='1' else '1' for i in str(bin(n)[2:]).zfill(32)),2)

