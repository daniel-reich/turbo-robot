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
  b = d_to_b(n)
  b = [1 if i==0 else 0 for i in b]
  return b_to_d(b)
  
def d_to_b(n):
  ret = []
  while n>0:
    ret.append(n%2)
    n//=2
  ret+=[0]*(32-len(ret))
  return ret
  
def b_to_d(b):
  ret = 0
  for i in range(len(b)):
    ret+=(2**i)*b[i]
  return ret

