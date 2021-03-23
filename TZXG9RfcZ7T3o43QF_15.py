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
  lst = []
  if txt.count('0') == txt.count('1'):
    for n in range(1, int(txt.count('1')/2)):
      chk = re.compile(r'(1{'+str(n)+ '})(?=0{' +str(n)+ '})')
      if re.search(chk, txt):
        lst.append(True)
      else:
        lst.append(False)
    return all(lst)
  else:
    return False

