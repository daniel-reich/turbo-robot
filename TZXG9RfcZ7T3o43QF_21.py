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
  m = re.findall("1+0+",txt)  
  return False if not m else all(i.count('1')==i.count('0') for i in m)  and len("".join(i for i in m))==len(txt)

