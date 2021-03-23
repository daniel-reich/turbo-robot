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

def same_length(txt):
  s = txt.replace('0',' ')
  d = [len(x) for x in  s.split()]
  return txt == ''.join('1'*x+'0'*x  for x in d)

