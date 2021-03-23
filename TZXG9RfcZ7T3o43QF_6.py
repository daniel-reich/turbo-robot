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

from itertools import groupby
​
def same_length(txt):
  if len(txt) % 2:
    return False
  groups = [len(list(g)) for k, g in groupby(txt)]
  return all(a == b for a, b in zip(groups[::2], groups[1::2]))

