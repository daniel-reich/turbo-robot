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
    # I hate seeing the solutions
    # because they are
    #always so fking simple :)
  return [len(i) for i in re.findall('1+',txt)] == [len(i) for i in re.findall('0+',txt)]

