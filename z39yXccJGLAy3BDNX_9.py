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

class Base:
  class Number:
​
    def __init__(self, val, base):
      self.v = val
      self.b = base
​
    def flip(self):
      nv = ''
      for n in range(len(self.v)):
        if self.v[n] == '0':
          nv += '1'
        else:
          nv += '0'
      return Base.Number(nv, self.b)
​
  def __init__(self, base):
    self.b = base
  
  def convert_from_int(self, integer):
​
    lst = [1]
    expon = 1
​
    while max(lst) < integer:
      lst.append(self.b ** expon)
      expon += 1
    
    vals = list(reversed(lst))
​
    nv = []
​
    for val in vals:
      nv.append(str(integer//val))
      integer = integer%val
    
    while len(nv) < 32:
      nv = ['0'] + nv
    
    return Base.Number(''.join(nv), self)
​
  def convert_to_int(self, number):
​
    nv = number.v
    
    vals = [1]
    expon = 1
​
    while len(vals) < len(nv):
      vals.append(self.b ** expon)
      expon += 1
    
    vals = list(reversed(vals))
​
    integer = 0
​
    for n in range(len(vals)):
      val = vals[n]
      nvv = int(nv[n])
​
      integer += (val * nvv)
    
    return integer
​
def flipping_bits(n):
​
  b2 = Base(2)
​
  n = b2.convert_from_int(n)
  new_n = n.flip()
​
  return b2.convert_to_int(new_n)

