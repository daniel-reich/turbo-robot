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
  pattern = r''
  for i in range(1,int(len(txt)/2)+1):
    c = r'1'*i+r'0'*i+r'|'
    pattern+=c
  pattern+=r'1'*(int(len(txt)/2)+1)+r'0'*(int(len(txt)/2)+1)
  return list(set(re.sub(pattern,'*',txt))) == ['*']

