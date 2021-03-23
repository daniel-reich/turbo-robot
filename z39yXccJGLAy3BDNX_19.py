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
  str_bin = bin(n).replace('0b','')
  arr_bin = []
  for item in str_bin:
    if item == '0':
      arr_bin.append('1')
    else:
      arr_bin.append('0')
  arr_bin_32 = ['1'] * (32-len(arr_bin)) + arr_bin
  str_bin_32 = ''.join(arr_bin_32)
  return int(str_bin_32,2)

