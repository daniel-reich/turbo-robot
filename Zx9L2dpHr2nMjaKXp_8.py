"""


In this challenge, you have to create functions to encode and decode variable-
length quantities. A variable-length quantity (VLQ) is a universal code that
uses an arbitrary number of binary octets (eight-bit bytes) to represent an
arbitrarily large integer. A VLQ is essentially a base-128 representation of
an unsigned integer with the addition of the eighth bit to mark a continuation
of bytes.

The way it works is fairly simple. As a big-endian series of bytes, the most
significant bit (MSB) of each byte is a 1 to indicate that another VLQ byte
follows. The remaining 7 bits of each byte make up the decoded value.

### Examples

    # ENCODE:
    int_to_vlq(127) ➞ [127]
    # numbers between 0 and 127 are unchanged
    # binary: [01111111]
    
    int_to_vlq(128) ➞ [129, 0]
    # 1st byte = 1 + 128 equivalent to 1 * 128 with MSB set to 1 indicating byte follows
    # 2nd byte = 0 
    # 128 + 0 ➞ 128
    # binary: [10000001, 00000000]
    
    int_to_vlq(106903) ➞ [134, 195, 23]
    # 1st byte = 128 + 6 ➞ 6 * 128^2 ➞ 98304
    # 2nd byte = 128 + 67 ➞ 67 * 128 ➞ 8576
    # 3rd byte = 23 ➞ 23
    # 98304 + 8576 + 23 = 106903
    # binary: [10000110, 11000011, 00010111]
    
    # DECODE:
    vlq_to_int([229, 145, 63]) ➞ 1657023
    # (229 - 128)*128^2 + (145 - 128)*128 + 63 = 1657023

### Notes

Integer values for encoding will be in the range 0 <= n <= 2^63

"""

def int_to_vlq(n):
    if n == 0:
        return [0]
    byte = []
    while n > 0:
        value_bits = n & 0b1111111
        if len(byte) == 0:
            byte.append(value_bits)
        else:
            byte.append((0b1 << 7) | value_bits)
        n >>= 7
    return list(reversed(byte))
def vlq_to_int(lst):
    if lst[-1] >> 7 == 1:
        raise ValueError(
            "Incomplete sequence.  Last byte has continuation bit set.")
​
    result = []
    current_result = 0
    for byt in lst:
        current_result = (current_result << 7) | (byt & 0b1111111)
        if byt >> 7 == 0:
            result.append(current_result)
            current_result = 0
    return result[0]

