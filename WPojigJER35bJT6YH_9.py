"""


Write a function that takes an integer `n`, reverses the binary representation
of that integer, and returns the new integer from the reversed binary.

### Examples

    reversed_binary_integer(10) ➞ 5
    # 10 = 1010 -> 0101 = 5
    
    reversed_binary_integer(12) ➞ 3
    # 12 = 1100 -> 0011 = 3
    
    reversed_binary_integer(25) ➞ 19
    # 25 = 11001 -> 10011 = 19
    
    reversed_binary_integer(45) ➞ 45
    # 45 = 101101 -> 101101 = 45

### Notes

All values of `n` will be positive.

"""

import numpy as np
def reversed_binary_integer(num):
  s = bin(num)[2:][::-1]
  n = 0
  for i in s:
    i = int(i)
    n = n*2+i
  return n

