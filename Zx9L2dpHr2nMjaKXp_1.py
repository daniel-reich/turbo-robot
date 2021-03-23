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

class Base:
​
  def __init__(self, base):
    self.b = base
  
  def convert_from_b10(self, b10_val):
​
    values = [1]
    expon = 1
​
    while max(values) < b10_val:
      values.append(self.b ** expon)
      expon += 1
    #print(values)
    values = list(reversed(values))
    
    tr_vals = []
​
    for value in values:
      if value <= b10_val:
        tr_vals.append(b10_val//value)
        b10_val = b10_val % value
      else:
        tr_vals.append(0)
    
    while tr_vals[0] == 0:
      tr_vals.pop(0)
​
    return tr_vals
​
  def convert_to_b10(self, base_value):
​
    values = [1]
    expon = 1
​
    while len(values) < len(base_value):
      values.append(self.b ** expon)
      expon += 1
    
    values = list(reversed(values))
​
    return sum([values[n] * base_value[n] for n in range(len(values))])
​
b128 = Base(128)
​
​
def int_to_vlq(n):
  try:
    converted = b128.convert_from_b10(n)
  except IndexError:
    return [0]
  return [converted[n] + 128 for n in range(len(converted) - 1)] + [converted[-1]]
def vlq_to_int(lst):
​
  converted = b128.convert_to_b10([lst[n] - 128 for n in range(len(lst) - 1)] + [lst[-1]])
​
  return converted

