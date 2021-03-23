"""


Write a function that returns `True` if every consecutive sequence of **ones**
is followed by a consecutive sequence of **zeroes** of the same length.

### Examples

    same_length("110011100010") ➞ True
    
    same_length("101010110") ➞ False
    
    same_length("111100001100") ➞ True
    
    same_length("111") ➞ False

### Notes

N/A

"""

import re
def same_length(txt):
  one = re.findall(r'[1]+', txt)
  zero = re.findall(r'[0]+', txt)
  return len(one)==len(zero) and all(len(i)==len(j) for i,j in zip(one, zero))

