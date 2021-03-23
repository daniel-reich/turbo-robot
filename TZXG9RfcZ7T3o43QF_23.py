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
  one = []
  
  lst = [(label, sum(1 for _ in group)) for label, group in groupby(txt)]
  for i in lst:
    if i[0] == '1':
      one.append(i[1])
    elif one[0] != i[1] or len(lst) % 2 == 1:
      return False
    else:
      one = []
  return True

