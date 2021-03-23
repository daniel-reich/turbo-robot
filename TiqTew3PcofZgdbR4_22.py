"""


A decimal number can be represented as a sequence of bits. To illustrate:

    6 = 00000110
    23 = 00010111

From the bitwise representation of numbers, we can calculate the **bitwise
AND** , **bitwise OR** and **bitwise XOR**. Using the example above:

    bitwise_and(6, 23) ➞ 00000110
    
    bitwise_or(6, 23) ➞ 00010111
    
    bitwise_xor(6, 23) ➞ 00010001

Write three functions to calculate the **bitwise AND** , **bitwise OR** and
**bitwise XOR** of two numbers.

### Examples

    bitwise_and(7, 12) ➞ 4
    
    bitwise_or(7, 12) ➞ 15
    
    bitwise_xor(7, 12) ➞ 11

### Notes

N/A

"""

def bitwise_and(n1, n2):
  s1='{0:08b}'.format(n1)
  s2='{0:08b}'.format(n2)
  r=''.join(['1' if x=='1' and v=='1' else'0' for x,v in zip(s1,s2)])
  return int(r,2)
​
def bitwise_or(n1, n2):
  s1='{0:08b}'.format(n1)
  s2='{0:08b}'.format(n2)
  r=''.join(['1' if x=='1' or v=='1' else'0' for x,v in zip(s1,s2)])
  return int(r,2)
​
def bitwise_xor(n1, n2):
  s1='{0:08b}'.format(n1)
  s2='{0:08b}'.format(n2)
  r=''.join(['1' if (x=='1' or v=='1') and not (x=='1' and v=='1') 
  else'0' for x,v in zip(s1,s2)])
  return int(r,2)

