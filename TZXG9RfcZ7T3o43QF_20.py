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
def same_length(txt):
  grp = [(k,sum(1 for _ in g)) for k,g in groupby(txt)]
  ones = [grp[i][1] for i in range(len(grp)) if grp[i][0]=='1']
  zeros = [grp[i][1] for i in range(len(grp)) if grp[i][0]=='0']
  return ones == zeros

